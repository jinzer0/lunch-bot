import csv
import urllib.parse
import datetime
import requests as r
import schedule as s
import time

kangwon = "K10"
gyeonggi = "J10"
geongsangnam = "S10"
geongsangbuk = "R10"
gwangju = "F10"
daegu = "D10"
daejeon = "G10"
busan = "C10"
seoul = "B10"
sejong = "I10"
ulsan = "H10"
incheon = "E10"
jeollanam = "Q10"
jeollabuk = "P10"
jeju = "T10"
chungcheongnam = "N10"
chungcheongbuk = "N10"

numbers = [kangwon, gyeonggi, geongsangnam, geongsangbuk, gwangju, daegu, daejeon, busan, seoul, sejong, ulsan, incheon,
           jeollanam, jeollabuk, jeju, chungcheongnam, chungcheongbuk]

school_code = {}
with open("../highschool.csv") as file:
    lines = csv.reader(file)
    lines.__next__()
    for line in lines:
        school_code[line[2]] = [line[0], line[3]]


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
            "*", "\*")
        return morning
    elif meal["mealServiceDietInfo"][0]["head"][0]["list_total_count"] == 2:
        morning = meal["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"].strip().replace("<br/>", "\n").replace(".",
                                                                                                              "\.").replace(
            "*", "\*")
        noon = meal["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"].strip().replace("<br/>", "\n").replace(".",
                                                                                                           "\.").replace(
            "*", "\*")
        return morning, noon
    elif meal["mealServiceDietInfo"][0]["head"][0]["list_total_count"] == 3:
        morning = meal["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"].strip().replace("<br/>", "\n").replace(".",
                                                                                                              "\.").replace(
            "*", "\*")
        noon = meal["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"].strip().replace("<br/>", "\n").replace(".",
                                                                                                           "\.").replace(
            "*", "\*")
        evening = meal["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"].strip().replace("<br/>", "\n").replace(".",
                                                                                                              "\.").replace(
            "*", "\*")
        return morning, noon, evening
    else:
        return


def get_info():
    target = "https://open.neis.go.kr/hub/mealServiceDietInfo?"
    apikey = "3157754f46dc4aafbc8f52dc0f257b77"

    with open("../setup.txt", "r") as setup:
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
    week = datetime.datetime.now(tz=KST).weekday()

    if week in [5, 6]:
        return None

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
    print(url)
    res = r.get(url)
    result = res.json()
    print(result)
    output = set_meal(result)

    print("Got information...\n\n")

    return output


kangwon = "7800000"
gyeonggi = "7530000"
geongsangnam = "9010000"
geongsangbuk = "8750000"
gwangju = "7380000"
daegu = "7240000"
daejeon = "7430000"
busan = "7150000"
seoul = "7010000"
sejong = "9300000"
ulsan = "7480000"
incheon = "7310000"
jeollanam = "8490000"
jeollabuk = "8320000"
jeju = "9290000"
chungcheongnam = "8140000"
chungcheongbuk = "8000000"

code = [kangwon, gyeonggi, geongsangnam, geongsangbuk, gwangju, daegu, daejeon, busan, seoul, sejong, ulsan, incheon,
        jeollanam, jeollabuk, jeju, chungcheongnam, chungcheongbuk]

edu_code = {}

for i in range(17):
    edu_code[code[i]] = numbers[i]

print(school_code["배재고등학교"])
KST = datetime.timezone(datetime.timedelta(hours=9))
year = datetime.datetime.now(tz=KST).year
mon = datetime.datetime.now(tz=KST).month
day = datetime.datetime.now(tz=KST).day

breakfast = s.Scheduler()
lunch = s.Scheduler()
dinner = s.Scheduler()


def alarm():
    # breakfast.every().day.at("07:00").do(hello)
    # lunch.every().day.at("11:10").do(hello)
    # dinner.every().day.at("5:25").do(hello)
    breakfast.every(10).seconds.do(hello)
    lunch.every(3).seconds.do(hello)
    dinner.every(1).seconds.do(hello)
    while True:
        breakfast.run_pending()
        lunch.run_pending()
        dinner.run_pending()
        time.sleep(1)


if get_info() is None:
    print("None")


# sample = '칼슘찹쌀밥*<br/>쇠고기무국*13.16.<br/>청경채나물*<br/>소시지볶음*2.5.6.10.12.13.15.16.18.<br/>새우볼꼬치*1.5.6.9.10.13.16.18.<br/>데리야끼떡갈비*2.5.6.10.13.15.16.18.<br/>깍두기*9.13.<br/>쿨피스*13.<br/>바나나*13.'
#
# sample=sample.strip().replace("<br/>","\n").replace(".","\.").replace("*","\*")
# text="조식\n"+sample
# print(text)
# print(sample)
