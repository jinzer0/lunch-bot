# Lunch-bot

텔레그램을 이용한 급식알림봇입니다.   
A lunch alarm bot with Telegram.  

# Installation
On terminal:   
1. Clone this repository
`git clone https://github.com/jinzer0/lunch-bot.git`
2. Install packages   
`pip install -r requirements.txt`
3. Create .env   
```dotenv
API_ID = your API_id
API_HASH = "your API_hash"
TOKEN = "your Bot Token"
```

# Run
On terminal:   
`python bot.py`

# Bot Commands
/help, /start - **설명 메세지 보기**   
/set - **급식 정보를 받으려는 학교 정보 등록** 예) /set 한국중학교   
/launch - **급식 알림 켜기**   
/stop - **급식 알림 끄기**   
/delete - **유저 정보 삭제**   
/today - **오늘 급식 한 번에 보기**   

## Admin Commands
/fetch - 모든 학교 급식 정보 업데이트   
/st - 현재 급식 정보, 유저 정보
