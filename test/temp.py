import csv
import os
import sqlite3
import datetime
import time
import urllib
import urllib.parse
import requests as r

from errors import WeekendError

"""
현재 해야 할 코드 리팩토링
1. 유저 table 생성 및 db 저장
2. 명령어 세팅 (학교 설정, 시간 설정#필요없을 수 있음, 도움말help, start, 알람시작, 알람중지)
3. 명언 보내기 기능
4. NEIS API fetch
5. 지정된 시간에 보내기
"""

# db = sqlite3.connect("highschool.db")
# cur = db.cursor()

# sql = "SELECT school_code, edu_tag FROM highschool"
# sql = "SELECT school_code FROM cafeteria where school_code = 12334"
# sql = "INSERT INTO cafeteria values (1234,'test','test','test')"
# cur.execute(sql)
# print(cur.fetchone())
# db.commit()
# db.close()
os.chdir("/Users/kjy/Desktop/Codes/python/lunch-bot")

# print(type(result[0]))
# print(dict(result[0]))
# print(type(result))

def fetch_info():  # get information from NEIS Service
    target = "https://open.neis.go.kr/hub/mealServiceDietInfo?"
    apikey = "3157754f46dc4aafbc8f52dc0f257b77"

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

    school_db = sqlite3.connect("./highschool.db")
    cur = school_db.cursor()
    sql = "SELECT school_code, edu_tag FROM highschool"
    cur.execute(sql)
    result = cur.fetchall()

    # today = 20211020

    print(f"Today : {today}")

    # for school_code, edu_tag in result:
    #     school = schoold_code
    #     education = edu_tag

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
    print(url)

    res = r.get(url)
    result: dict = res.json()
    # Check result whether has info
    if result.get("RESULT", False):
        print("false")

    list_total_count = result.get("mealServiceDietInfo").__getitem__(0).get("head").__getitem__(0).get(
        "list_total_count")

    print(f"Total meal {list_total_count}")
    for count in range(list_total_count):
        calorie = result.get("mealServiceDietInfo").__getitem__(1).get("row").__getitem__(count).get("CAL_INFO")
        meal = result.get("mealServiceDietInfo").__getitem__(1).get("row").__getitem__(count).get("DDISH_NM")
        meal_code = result.get("mealServiceDietInfo").__getitem__(1).get("row").__getitem__(count).get(
            "MMEAL_SC_CODE")
        meal_tag = result.get("mealServiceDietInfo").__getitem__(1).get("row").__getitem__(count).get(
            "MMEAL_SC_NM")
        sql = "INSERT INTO cafeteria values (?, ?, ?, ?,?)"
        cur.execute(sql, (school, meal, calorie, meal_code, meal_tag))
        print(f"sql executed\n")
    school_db.commit()
    time.sleep(3)

    school_db.close()
    return print("Done")

def alarm(meal_code: int):
    school_db = sqlite3.connect("./highschool.db")
    cur = school_db.cursor()
    sql_user = "SELECT user_id, school_code FROM user WHERE alarm = 'true'"
    cur.execute(sql_user)
    user_list = cur.fetchall()
    print(user_list)
    user_list = [(1707277448, 7010170)]
    for user_id, school_code in user_list:
        print(user_id, school_code)
        school_code = int(school_code)

        sql = "SELECT meal, calorie, meal_tag FROM cafeteria WHERE school_code = ? and meal_code = ?"
        cur.execute(sql, (school_code, meal_code))
        result = cur.fetchone()
        print(result)

        meal = result[0]
        calorie = result[1]
        meal_tag = result[2]
        # app.send_message(chat_id=int(user_id), text=Messages.alarm_msg.format(meal_tag, meal, calorie))
        time.sleep(0.1)

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

print(user_count, alarm_count)