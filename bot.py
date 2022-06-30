from pyrogram import Client, filters, emoji
from config import Messages
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, \
    CallbackQuery, ReplyKeyboardRemove
import time, sqlite3, datetime, urllib
import requests as r
import urllib.parse
from errors import WeekendError, NoInfoError
from apscheduler.schedulers.background import BackgroundScheduler
import os
from dotenv import load_dotenv

load_dotenv()
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
token = os.getenv("TOKEN")

app = Client("lunch", api_id, api_hash, bot_token=token, parse_mode="markdown")
admin = [1899480287, 1516844869, 1751382310, 1707277448]

"""
현재 해야 할 코드 리팩토링
1. 유저 table 생성 및 db 저장 - DONE
2. 명령어 세팅 (학교 설정, 시간 설정#필요없을 수 있음, 도움말help, start, 알람시작, 알람중지) - 학교 설정, start, help - DONE
3. 명언 보내기 기능 - doing...
4. NEIS API fetch - DONE
5. 지정된 시간에 보내기 - DONE
6. user table - alarm column 추가하여 true일시 알람 전송, false일시 비전송. 명령어로 true, false update하기 - DONE
"""


def search_school(school_name):
    school_db = sqlite3.connect("highschool.db")
    cur = school_db.cursor()
    sql = "SELECT * FROM highschool WHERE school_name = ?"
    cur.execute(sql, [school_name])
    result = cur.fetchall()  # list
    school_db.close()
    if len(result) == 0:
        return False
    else:
        return result


def search_school_fullname(school_fullname):
    school_db = sqlite3.connect("highschool.db")
    cur = school_db.cursor()
    sql = "SELECT * FROM highschool WHERE school_fullname = ?"
    cur.execute(sql, [school_fullname])
    result = cur.fetchone()
    return result


def insert_user(message: Message, result: tuple):
    school_db = sqlite3.connect("highschool.db")
    cur = school_db.cursor()
    sql = "INSERT INTO user(user_id, username, school_fullname, school_code, edu_tag, alarm) values (?, ?, ?, ?, ?, ?)"
    cur.execute(sql, (message.from_user.id, message.from_user.username, result[2], result[1], result[5], 'true'))
    school_db.commit()
    school_db.close()


def fetch_info():  # get information from NEIS Service
    school_db = sqlite3.connect("highschool.db")
    cur = school_db.cursor()

    target = "https://open.neis.go.kr/hub/mealServiceDietInfo?"
    apikey = "3157754f46dc4aafbc8f52dc0f257b77"
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}

    KST = datetime.timezone(datetime.timedelta(hours=9))
    year = datetime.datetime.now(tz=KST).year
    mon = datetime.datetime.now(tz=KST).month
    day = datetime.datetime.now(tz=KST).day
    week = datetime.datetime.now().weekday()

    if week in [5, 6]:  # if Saturday or Sunday, returns None
        raise WeekendError

    if mon < 10:  # Make month better
        today = str(year) + "0" + str(mon)
    else:
        today = str(year) + str(mon)

    if day < 10:  # Make day better
        today = today + "0" + str(day)
    else:
        today = today + str(day)

    KEY = apikey
    Type = "json"
    pIndex = 1
    pSize = 100
    school = 7010170
    education = "B10"

    sql = "DROP TABLE cafeteria"
    cur.execute(sql)
    school_db.commit()

    sql = "CREATE TABLE cafeteria (school_code INTEGER, meal TEXT, calorie TEXT, meal_code INTEGER, meal_tag TEXT)"
    cur.execute(sql)
    school_db.commit()

    sql = "SELECT school_code, edu_tag FROM highschool"
    cur.execute(sql)
    result = cur.fetchall()

    # today = 20211020

    print(f"Today : {today}")

    for school_code, edu_tag in result:
        school = school_code
        education = edu_tag

        parameter = {
            "KEY": KEY,
            "Type": Type,
            "SD_SCHUL_CODE": school,
            "ATPT_OFCDC_SC_CODE": education,
            "MLSV_YMD": today,
            "pIndex": pIndex,
            "pSize": pSize

        }

        url = target + urllib.parse.urlencode(parameter, doseq=True)

        res = r.get(url, headers=headers, verify=False)
        result: dict = res.json()
        # Check result whether has info
        if result.get("RESULT", False):
            continue

        list_total_count = result.get("mealServiceDietInfo").__getitem__(0).get("head").__getitem__(0).get(
            "list_total_count")

        for count in range(list_total_count):
            calorie = result.get("mealServiceDietInfo").__getitem__(1).get("row").__getitem__(count).get("CAL_INFO")
            meal = result.get("mealServiceDietInfo").__getitem__(1).get("row").__getitem__(count).get("DDISH_NM")
            meal_code = result.get("mealServiceDietInfo").__getitem__(1).get("row").__getitem__(count).get(
                "MMEAL_SC_CODE")
            meal_tag = result.get("mealServiceDietInfo").__getitem__(1).get("row").__getitem__(count).get(
                "MMEAL_SC_NM")
            sql = "INSERT INTO cafeteria values (?, ?, ?, ?, ?)"
            cur.execute(sql, (school_code, meal, calorie, meal_code, meal_tag))
            print(f"sql executed\n")

        school_db.commit()
        time.sleep(2)

    school_db.close()
    return


def alarm(meal_code: int):
    school_db = sqlite3.connect("highschool.db")
    cur = school_db.cursor()
    sql_user = "SELECT user_id, school_code FROM user WHERE alarm = 'true'"
    cur.execute(sql_user)
    user_list = cur.fetchall()
    for user_id, school_code in user_list:
        sql = "SELECT meal, calorie, meal_tag FROM cafeteria WHERE school_code = ? and meal_code = ?"
        cur.execute(sql, (school_code, meal_code))
        result = cur.fetchone()
        user = app.get_users(user_ids=user_id)
        if user.is_deleted:
            print(f"Deleted user - {user_id}")
            continue

        if result is None:
            print(f"Sent Alarm - {user_id}")
            app.send_message(chat_id=int(user_id), text=Messages.alarm_error_msg)
            time.sleep(0.1)
            continue

        meal: str = result[0].replace("<br/>", "\n")
        calorie = result[1]
        meal_tag = result[2]
        app.send_message(chat_id=int(user_id), text=Messages.alarm_msg.format(meal_tag, meal, calorie))
        print(f"Sent Alarm - {user_id}")
        time.sleep(0.1)


@app.on_message(filters=filters.command("start"))
def help(client: Client, message: Message):
    app.send_message(chat_id=message.chat.id, text=Messages.start_msg.format(message.from_user.mention),
                     parse_mode="markdown")


@app.on_message(filters=filters.command("help"))
def help(client: Client, message: Message):
    message.reply_text(text=Messages.help_msg, quote=True)
    message.reply_text(text=Messages.help_msg_2, quote=True)


@app.on_message(filters=filters.command("set"))
def start(client: Client, message: Message):
    if message.text == "/set":
        app.send_message(chat_id=message.chat.id, text=Messages.set_msg)
    else:
        school_db = sqlite3.connect("highschool.db")
        cur = school_db.cursor()
        sql = "SELECT * FROM user WHERE user_id = ?"
        cur.execute(sql, [message.chat.id])

        if cur.fetchone() is None:
            school_name = message.text.split()[-1]
            result = search_school(school_name=school_name)
            if result == False:
                app.send_message(chat_id=message.chat.id,
                                 text=f"{emoji.CROSS_MARK_BUTTON} **학교 검색 결과**가 없습니다! **유효한 학교 이름**을 입력해주세요!")
            elif len(result) == 1:
                app.send_message(chat_id=message.chat.id, text=f"{emoji.INFORMATION} **알맞은 학교를 선택해주세요!**",
                                 reply_markup=ReplyKeyboardMarkup([[KeyboardButton(text=".school - " + result[0][2])]],
                                                                  one_time_keyboard=True, resize_keyboard=True))
            else:
                keyboards = list()
                for school in result:
                    keyboards.append([KeyboardButton(text=".school - " + school[2])])
                app.send_message(chat_id=message.chat.id, text=f"{emoji.INFORMATION} **알맞은 학교를 선택해주세요!**",
                                 reply_markup=ReplyKeyboardMarkup(keyboard=keyboards, one_time_keyboard=True,
                                                                  resize_keyboard=True))
        else:
            message.reply_text(f"{emoji.MAN_STUDENT} **이미 등록된 유저입니다!** /delete **명령어로 정보를 삭제하고 다시 등록하세요.**", quote=True)


@app.on_message(filters=filters.command("school", prefixes="."))
def check_school(clinet: Client, message: Message):
    if message.text == ".school":
        return
    school_fullname = message.text.split(" - ")[1]
    result = search_school_fullname(school_fullname)
    if result is None:
        return
    insert_user(message, result)
    message.reply_text(f"{emoji.CHECK_MARK_BUTTON} **학교 정보가 저장 되었습니다.**", quote=True, reply_markup=ReplyKeyboardRemove())
    message.reply_text(f"{emoji.BELL} **알림이 켜졌습니다. 알림을 일시 중지 하려면** /stop **명령어를 입력하세요.**", quote=True)


@app.on_message(filters=filters.command(["launch"]))
def launch(client: Client, message: Message):
    school_db = sqlite3.connect("highschool.db")
    cur = school_db.cursor()
    sql = "SELECT user_id, alarm FROM user WHERE user_id = ?"
    cur.execute(sql, [message.chat.id])
    result = cur.fetchone()
    if result is not None:
        if result[1] == "false":
            sql = "UPDATE user SET alarm = ? WHERE user_id = ?"
            cur.execute(sql, ("true", message.chat.id))
            school_db.commit()
            school_db.close()
            message.reply_text(text=Messages.launch_msg, quote=True)
        else:
            message.reply_text(text=f"{emoji.BELL} **이미 알림이 켜져 있습니다!**", quote=True)
    else:
        message.reply_text(text=f"{emoji.BELL} **유저 정보가 없습니다!** /set **명령어로 학교를 먼저 등록하세요!**", quote=True)


@app.on_message(filters=filters.command(["stop"]))
def stop(client: Client, message: Message):
    school_db = sqlite3.connect("highschool.db")
    cur = school_db.cursor()
    sql = "SELECT user_id, alarm FROM user WHERE user_id = ?"
    cur.execute(sql, [message.chat.id])
    result = cur.fetchone()
    if result is not None:
        if result[1] == "true":
            sql = "UPDATE user SET alarm = ? WHERE user_id = ?"
            cur.execute(sql, ("false", message.chat.id))
            school_db.commit()
            school_db.close()
            message.reply_text(text=Messages.stop_msg, quote=True)
        else:
            message.reply_text(text=f"{emoji.BELL_WITH_SLASH} **이미 알림이 꺼져 있습니다!**", quote=True)
    else:
        message.reply_text(text=f"{emoji.BELL_WITH_SLASH} **유저 정보가 없습니다!** /set **명령어로 학교를 먼저 등록하세요!**", quote=True)


@app.on_message(filters=filters.command("delete"))
def delete_callback(client: Client, message: Message):
    message.delete()
    school_db = sqlite3.connect("highschool.db")
    cur = school_db.cursor()
    sql = "SELECT * FROM user WHERE user_id = ?"
    cur.execute(sql, [message.chat.id])
    if cur.fetchone() is not None:
        app.send_message(message.chat.id, text=Messages.delete_msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="아니요, 전혀요.", callback_data="delete_false")],
            [InlineKeyboardButton(text="아니요.", callback_data="delete_false")],
            [InlineKeyboardButton(text="네. 삭제할게요.", callback_data="delete_true")]
        ]))
    else:
        message.reply_text(text=f"{emoji.MAN_STUDENT} **이미 유저 정보가 없습니다!**")


@app.on_callback_query(group=0)
def delete(client: Client, callback: CallbackQuery):
    school_db = sqlite3.connect("highschool.db")
    cur = school_db.cursor()
    if callback.data.split("_")[0] == "delete":
        if callback.data.split("_")[1] == "true":
            sql = "DELETE FROM user WHERE user_id = ?"
            user_id = callback.from_user.id
            cur.execute(sql, [user_id])
            school_db.commit()
            school_db.close()
            callback.message.delete()
            app.send_message(user_id, text=Messages.delete_complete_msg)

        else:
            callback.message.delete()


@app.on_message(filters=(filters.command("st") & filters.chat(admin)))
def status_admin(client: Client, message: Message):
    school_db = sqlite3.connect("highschool.db")
    cur = school_db.cursor()

    sql = "SELECT * FROM user"
    cur.execute(sql)
    result_user = cur.fetchall()
    user_count = len(result_user)

    sql = "SELECT * FROM user WHERE alarm = 'true'"
    cur.execute(sql)
    result_alarm = cur.fetchall()
    alarm_count = len(result_alarm)

    sql = "SELECT * FROM cafeteria WHERE meal_code = 1"
    cur.execute(sql)
    result_meal_1 = cur.fetchall()
    meal_1_count = len(result_meal_1)

    sql = "SELECT * FROM cafeteria WHERE meal_code = 2"
    cur.execute(sql)
    result_meal_2 = cur.fetchall()
    meal_2_count = len(result_meal_2)

    sql = "SELECT * FROM cafeteria WHERE meal_code = 3"
    cur.execute(sql)
    result_meal_3 = cur.fetchall()
    meal_3_count = len(result_meal_3)

    message.delete()
    app.send_message(message.chat.id,
                     text=Messages.status_msg.format(user_count, alarm_count, meal_1_count, meal_2_count, meal_3_count))


@app.on_message(filters=filters.command("fetch") & filters.chat(admin))
def fetch(client: Client, message: Message):
    msg = app.send_message(chat_id=message.chat.id, text=f"{emoji.BOWL_WITH_SPOON} **급식 정보 갱신 중...**")
    fetch_info()
    msg.edit(f"{emoji.CHECK_MARK_BUTTON}**급식 정보를 성공적으로 갱신했습니다!**\n")


@app.on_message(filters=filters.command("today"))
def today_meal(client: Client, message: Message):
    user_id = message.chat.id

    school_db = sqlite3.connect("highschool.db")
    cur = school_db.cursor()
    sql = "select school_code FROM user WHERE user_id = ?"
    cur.execute(sql, [user_id])

    school_code = cur.fetchone()[0]

    sql = "select * FROM cafeteria WHERE school_code = ?"
    cur.execute(sql, [school_code])

    meal_all = cur.fetchall()
    for result in meal_all:
        meal: str = result[1].replace("<br/>", "\n")
        calorie = result[2]
        meal_tag = result[4]
        app.send_message(chat_id=int(user_id), text=Messages.alarm_msg.format(meal_tag, meal, calorie))
        time.sleep(0.3)


advice_id = 1


def send_advice():
    global advice_id
    res = r.get(f"https://api.adviceslip.com/advice/{advice_id}")
    advice = res.json()["slip"]["advice"]

    school_db = sqlite3.connect("highschool.db")
    cur = school_db.cursor()
    sql = "select user_id FROM user"
    cur.execute(sql)
    user_ids = cur.fetchall()  # fetchall은 리스트로 나옴, 예시 : [(1707277448,)]

    for user_id_list in user_ids:
        user_id = user_id_list[0]
        user = app.get_users(user_ids=user_id)
        if user.is_deleted:
            print(f"Deleted user - {user_id}")
            continue

        app.send_message(chat_id=user_id, text=f"{emoji.THINKING_FACE}  **오늘의 명언** {emoji.THINKING_FACE}\n**{advice}**")
        time.sleep(0.2)

    advice_id += 1


scheduler = BackgroundScheduler(timezone="Asia/Tokyo")
scheduler.start()
scheduler.add_job(fetch_info, "cron", second=0, minute=0, hour=3)
scheduler.add_job(alarm, "cron", second=0, minute=55, hour=6, args=[1])
scheduler.add_job(alarm, "cron", second=0, minute=55, hour=11, args=[2])
scheduler.add_job(alarm, "cron", second=0, minute=25, hour=17, args=[3])
scheduler.add_job(send_advice, "cron", second=0, minute=0, hour=17)

app.run()
