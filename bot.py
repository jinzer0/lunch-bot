from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import Messages
import requests as r
import logging
import urllib.parse
import schedule as s
import csv
import datetime
import time
from pymongo import MongoClient

api_id = 8515288
api_hash = "da9c7ef954fc0212589870cb079bdd21"
token = "1890496399:AAGVRWGm3q0FnysKMBSzr9AvwUI4OguwPfM"

school_code = {}
with open("source/highschool.csv") as file:
    lines = csv.reader(file)
    lines.__next__()
    for line in lines:
        school_code[line[2]] = [line[0], line[3]]

    print("School code is prepared...")

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

mongo = MongoClient("localhost", 27017)
db = mongo["student"]
col = db.members

def user_info(message):
    epochtime = message.date
    user_id = message.chat.id
    message_id = message.message_id
    username_first = message.chat.first_name
    username_last = message.chat.last_name
    user_message = message.text

    realtime = time.localtime(epochtime + 32400)

    text = f"""
--------------------------------------------
USER : {username_first} {username_last}
ID : {user_id}
MESSAGE : {user_message}
ID_MESSAGE : {message_id}
DATE : {realtime.tm_year}-{realtime.tm_mon}-{realtime.tm_mday} {realtime.tm_hour}:{realtime.tm_min}:{realtime.tm_sec}
--------------------------------------------"""
    print(text)


def set_code(school):
    edu_code = {'7800000': 'K10', '7530000': 'J10', '9010000': 'S10', '8750000': 'R10', '7380000': 'F10',
                '7240000': 'D10',
                '7430000': 'G10', '7150000': 'C10', '7010000': 'B10', '9300000': 'I10', '7480000': 'H10',
                '7310000': 'E10',
                '8490000': 'Q10', '8320000': 'P10', '9290000': 'T10', '8140000': 'N10', '8000000': 'N10'}
    info = school_code[school]
    sch_number = info[0]
    edu_number = edu_code[info[1]]

    return sch_number, edu_number


def set_meal(meal):
    if meal["mealServiceDietInfo"][0]["head"][0]["list_total_count"] == 1:
        morning = meal["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"].strip().replace("<br/>", "\n").replace(".",
                                                                                                              "\.").replace(
            "*", "\*").replace("-", "\-")
        return morning
    elif meal["mealServiceDietInfo"][0]["head"][0]["list_total_count"] == 2:
        morning = meal["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"].strip().replace("<br/>", "\n").replace(".",
                                                                                                              "\.").replace(
            "*", "\*").replace("-", "\-")
        noon = meal["mealServiceDietInfo"][1]["row"][1]["DDISH_NM"].strip().replace("<br/>", "\n").replace(".",
                                                                                                           "\.").replace(
            "*", "\*").replace("-", "\-")
        return morning, noon
    elif meal["mealServiceDietInfo"][0]["head"][0]["list_total_count"] == 3:
        morning = meal["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"].strip().replace("<br/>", "\n").replace(".",
                                                                                                              "\.").replace(
            "*", "\*").replace("-", "\-")
        noon = meal["mealServiceDietInfo"][1]["row"][1]["DDISH_NM"].strip().replace("<br/>", "\n").replace(".",
                                                                                                           "\.").replace(
            "*", "\*").replace("-", "\-")
        evening = meal["mealServiceDietInfo"][1]["row"][2]["DDISH_NM"].strip().replace("<br/>", "\n").replace(".",
                                                                                                              "\.").replace(
            "*", "\*").replace("-", "\-")
        return morning, noon, evening
    else:
        return


def get_info():
    target = "https://open.neis.go.kr/hub/mealServiceDietInfo?"
    apikey = "3157754f46dc4aafbc8f52dc0f257b77"

    with open("setup.txt", "r") as setup:
        name = setup.readline()

    numbers = set_code(name)

    KEY = apikey
    Type = "json"
    pIndex = 1
    pSize = 100
    school = numbers[0]
    education = numbers[1]

    KST = datetime.timezone(datetime.timedelta(hours=9))
    year = datetime.datetime.now(tz=KST).year
    mon = datetime.datetime.now(tz=KST).month
    day = datetime.datetime.now(tz=KST).day

    if mon < 10:
        today = str(year) + "0" + str(mon)
    else:
        today = str(year) + str(mon)

    if day < 10:
        today = today + "0" + str(day)
    else:
        today = today + str(day)

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
    res = r.get(url)
    result = res.json()
    output = set_meal(result)

    print("Got information...\n\n")

    return output


def send_meal(message):
    meal = get_info()
    print(meal)

    if meal == None:
        bot.send_message(message.chat.id, "오늘은 급식이 없습니다\.")

    if len(meal) == 1:
        if datetime.datetime.now().hour == 22:
            msg = meal[0]
            text = "*_조식_*\n" + msg
            bot.send_message(message.chat.id, text)
        return

    elif len(meal) == 2:
        if datetime.datetime.now().hour == 22:
            msg = meal[0]
            text = "*_조식_*\n" + msg
            bot.send_message(message.chat.id, text)
        elif datetime.datetime.now().hour == 2:
            msg = meal[1]
            text = "*_중식_*\n" + msg
            bot.send_message(message.chat.id, text)
        else:
            return
    elif len(meal) == 3:
        if datetime.datetime.now().hour == 22:
            msg = meal[0]
            text = "*_조식_*\n" + msg
            bot.send_message(message.chat.id, text)

        elif datetime.datetime.now().hour == 2:
            msg = meal[1]
            text = "*_중식_*\n" + msg
            bot.send_message(message.chat.id, text)

        elif datetime.datetime.now().hour == 8:
            msg = meal[2]
            text = "*_석식_*\n" + msg
            bot.send_message(message.chat.id, text)


breakfast = s.Scheduler()
lunch = s.Scheduler()
dinner = s.Scheduler()


def alarm(message):
    breakfast.every().day.at("22:00").do(send_meal, message)
    lunch.every().day.at("02:10").do(send_meal, message)
    dinner.every().day.at("08:25").do(send_meal, message)

    while True:
        breakfast.run_pending()
        lunch.run_pending()
        dinner.run_pending()
        time.sleep(1)


def halt_schedule():
    breakfast.clear()
    lunch.clear()
    dinner.clear()


def set_school(message):
    user_info(message)
    msg = message.text
    with open("setup.txt", "w") as sch:
        sch.write(msg)

    bot.send_message(message.chat.id, "학교 설정이 완료되었습니다\.")
    bot.send_message(message.chat.id, "알림을 켜기 위해 *_/begin_*을 입력하세요\.")



app = Client("lunch", api_id, api_hash, parse_mode="markdown")

@app.on_message(filters=filters.command(["start"]))
def start(client: Client, message: Message):
    app.send_message(chat_id=message.chat.id, text=Messages.start_msg)

@app.on_message(filters=filters.command(["help"]))
def help(client: Client, message: Message):
    app.send_message(chat_id=message.chat.id, text=Messages.help_msg)

@app.on_message(filters=filters.command(["set"]))
def start(client: Client, message: Message):
    app.send_message(chat_id=message.chat.id, text=Messages.set_msg)

@app.on_message(filters=filters.command(["launch"]))
def launch(client: Client, message: Message):
    alarm(message)
    app.send_message(chat_id=message.chat.id, text=Messages.launch_msg)

@app.on_message(filters=filters.command(["stop"]))
def stop(client: Client, message: Message):
    halt_schedule()
    app.send_message(chat_id=message.chat.id, text=Messages.stop_msg)


app.run()