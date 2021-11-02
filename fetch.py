import sqlite3
import time
import urllib.parse
import requests as r
import datetime
from errors import WeekendError


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
        print(f"School_code : {school_code} // List total : {list_total_count}")
        for count in range(list_total_count):
            calorie = result.get("mealServiceDietInfo").__getitem__(1).get("row").__getitem__(count).get("CAL_INFO")
            meal = result.get("mealServiceDietInfo").__getitem__(1).get("row").__getitem__(count).get("DDISH_NM")
            meal_code = result.get("mealServiceDietInfo").__getitem__(1).get("row").__getitem__(count).get(
                "MMEAL_SC_CODE")
            meal_tag = result.get("mealServiceDietInfo").__getitem__(1).get("row").__getitem__(count).get(
                "MMEAL_SC_NM")
            sql = "INSERT INTO cafeteria values (?, ?, ?, ?, ?)"
            cur.execute(sql, (school_code, meal, calorie, meal_code, meal_tag))
            print(f"sql executed")

        school_db.commit()
        time.sleep(2)

    school_db.close()


fetch_info()
