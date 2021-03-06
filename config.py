from pyrogram import emoji


class Messages:
    START_MSG = "**Hi there {}.**\n__I'm Google Drive Uploader Bot.You can use me to upload any file / video to Google Drive from direct link or Telegram Files.__\n__You can know more from /help.__"
    start_msg = "**안녕한가 👨🏼‍🎓 {} 학생...**\n지정된 시간에 **급식**을 알려주는 **급식봇**이라고 한다...\n/help 명령어로 사용 방법을 배워보거라..."
    help_msg = f"""/start - ✅ **쓸모 없는 명령어**
/help - ℹ️ **현재 이 메세지 보기**
/set - ⚙️ **급식 정보를 받으려는 학교 정보 등록** 예) /set 한국중학교
/launch - {emoji.BELL} **급식 알림 켜기**
/stop - {emoji.BELL_WITH_SLASH} **급식 알림 끄기**
/delete - {emoji.PROHIBITED} **유저 정보 삭제**
/today - {emoji.POT_OF_FOOD} **오늘 급식 한 번에 보기**
"""
    set_msg = "⚙️ **급식 정보**를 받으려는 **학교**를 등록하겠노라...\n예시를 보고 **정확히** 입력하거라...\n**예) /set 대한고등학교, /set 민국중학교**"
    launch_msg = f"{emoji.BELL} **알림이 켜졌노라...**\n앞으로 **조/중/석식(있는 경우만)**을 알려주겠노라...\n**알림 일시 중지는** /stop **를 입력하거라~**"
    stop_msg = f"{emoji.BELL_WITH_SLASH} **알림이 중지되었노라...\n알림을 다시 켠다면** /launch **를 입력하거라~**"
    alarm_msg = "🍽️🥣 **오늘 {}** 🍽️🥣\n-----\n**{}**\n-----\n✅ **칼로리 :** ```{}```"
    alarm_error_msg = f"{emoji.CROSS_MARK_BUTTON} **오늘은 급식이 없습니다!**"
    delete_msg = f"{emoji.WARNING} **정말로 유저 정보를 삭제하시겠습니까?** {emoji.WARNING}"
    delete_complete_msg = f"{emoji.CROSS_MARK_BUTTON} ** 유저 정보가 성공적으로 삭제되었습니다.**"
    status_msg = "🤖 **현재 유저, 봇 상황** 🤖\n👨 **총 유저 :** ```{}``` **명**\n🔔 **알림 활성화 유저 :** ```{}``` **명**\n🍽️ **급식 총 수(조, 중, 석식 순서) :** ```{}, {}, {}``` **개**"
    help_msg_2 = f"""🍽️🥣 **급식 알림 받는 방법** 🍽️🥣
{emoji.KEYCAP_DIGIT_ONE} /set **명령어로 학교를 등록한다.**
{emoji.KEYCAP_DIGIT_TWO} **급식 시간전 알림을 기다린다. 끝~**
{emoji.KEYCAP_DIGIT_THREE} /stop **명령어로 알림을 일시 중지하거나,** /launch **명령어로 일시 중지한 알림을 다시 켤 수 있다.**
{emoji.KEYCAP_DIGIT_FOUR} /delete **명령어로 유저 정보를 삭제한다. 학교를 바꾸거나 더 이상 봇을 사용하지 않을 때 이 명령어를 입력하도록!**
"""
    # HELP_MSG = [
    #     ".",
    #     "**Google Drive Uploader**\n__I can upload files from direct link or Telegram Files to your Google Drive. All i need is to authenticate me to your Google Drive Account and send a direct download link or Telegram File.__\n\nI have more features... ! Wanna know about it ? Just walkthrough this tutorial and read the messages carefully.",
    #
    #     f"**Authenticating Google Drive**\n__Send the /{BotCommands.Authorize[0]} commmand and you will receive a URL, visit URL and follow the steps and send the received code here. Use /{BotCommands.Revoke[0]} to revoke your currently logged Google Drive Account.__\n\n**Note: I will not listen to any command or message (except /{BotCommands.Authorize[0]} command) until you authorize me.\nSo, Authorization is mandatory !**",
    #
    #     f"**Direct Links**\n__Send me a direct download link for a file and i will download it on my server and Upload it to your Google Drive Account. You can rename files before uploading to GDrive Account. Just send me the URL and new filename separated by ' | '.__\n\n**__Examples:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```\n\n**Telegram Files**\n__To Upload telegram files in your Google drive Account just send me the file and i will download and upload it to your Google Drive Account. Note: Telegram Files Downloading are slow. it may take longer for big files.__\n\n**YouTube-DL Support**\n__Download files via youtube-dl.\nUse /{BotCommands.YtDl[0]} (YouTube Link/YouTube-DL Supported site link)__",
    #
    #     f"**Custom Folder for Upload**\n__Want to upload in custom folder or in__ **TeamDrive** __ ?\nUse /{BotCommands.SetFolder[0]} (Folder URL) to set custom upload folder.\nAll the files are uploaded in the custom folder you provide.__",
    #
    #     f"**Delete Google Drive Files**\n__Delete google drive files. Use /{BotCommands.Delete[0]} (File/Folder URL) to delete file or reply /{BotCommands.Delete[0]} to bot message.\nYou can also empty trash files use /{BotCommands.EmptyTrash[0]}\nNote: Files are deleted permanently. This process cannot be undone.\n\n**Copy Google Drive Files**\n__Yes, Clone or Copy Google Drive Files.\n__Use /{BotCommands.Clone[0]} (File id / Folder id or URL) to copy Google Drive Files in your Google Drive Account.__",
    #
    #     "**Rules & Precautions**\n__1. Don't copy BIG Google Drive Files/Folders. It may hang the bot and your files maybe damaged.\n2. Send One request at a time unless bot will stop all processes.\n3. Don't send slow links @transload it first.\n4. Don't misuse, overload or abuse this free service.__",
    #
    #     # Dont remove this ↓ if you respect developer.
    #     "**Developed by @viperadnan**"
    # ]

    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Rate Limit Exceeded.**\n__User rate limit exceeded try after 24 hours.__"

    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder not found.**\n__File id - {} Not found. Make sure it\'s exists and accessible by the logged account.__"

    INVALID_GDRIVE_URL = "❗ **Invalid Google Drive URL**\nMake sure the Google Drive URL is in valid format."

    COPIED_SUCCESSFULLY = "✅ **Copied successfully.**\n[{}]({}) __({})__"

    # NOT_AUTH = f"🔑 **You have not authenticated me to upload to any account.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"

    DOWNLOADED_SUCCESSFULLY = "📤 **Uploading File...**\n**Filename:** ```{}```\n**Size:** ```{}```"

    UPLOADED_SUCCESSFULLY = "✅ **Uploaded Successfully.**\n[{}]({}) __({})__"

    DOWNLOAD_ERROR = "❗**Downloader Failed**\n{}\n__Link - {}__"

    DOWNLOADING = "📥 **Downloading File...\nLink:** ```{}```"

    ALREADY_AUTH = "🔒 **Already authorized your Google Drive Account.**\n__Use /revoke to revoke the current account.__\n__Send me a direct link or File to Upload on Google Drive__"

    # FLOW_IS_NONE = f"❗ **Invalid Code**\n__Run {BotCommands.Authorize[0]} first.__"

    AUTH_SUCCESSFULLY = '🔐 **Authorized Google Drive account Successfully.**'

    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__The code you have sent is invalid or already used before. Generate new one by the Authorization URL__'

    AUTH_TEXT = "⛓️ **To Authorize your Google Drive account visit this [URL]({}) and send the generated code here.**\n__Visit the URL > Allow permissions > you will get a code > copy it > Send it here__"

    DOWNLOAD_TG_FILE = "📥 **Downloading File...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"

    PARENT_SET_SUCCESS = '🆔✅ **Custom Folder link set successfully.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'

    # PARENT_CLEAR_SUCCESS = f'🆔🚮 **Custom Folder ID Cleared Successfuly.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'

    CURRENT_PARENT = "🆔 **Your Current Custom Folder ID - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"

    # REVOKED = f"🔓 **Revoked current logged account successfully.**\n__Use /{BotCommands.Authorize[0]} to authenticate again and use this bot.__"

    NOT_FOLDER_LINK = "❗ **Invalid folder link.**\n__The link you send its not belong to a folder.__"

    CLONING = "🗂️ **Cloning into Google Drive...**\n__G-Drive Link - {}__"

    PROVIDE_GDRIVE_URL = "**❗ Provide a valid Google Drive URL along with commmand.**\n__Usage - /{} (GDrive Link)__"

    INSUFFICIENT_PERMISSONS = "❗ **You have insufficient permissions for this file.**\n__File id - {}__"

    DELETED_SUCCESSFULLY = "🗑️✅ **File Deleted Successfully.**\n__File deleted permanently !\nFile id - {}__"

    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n__Please try again later.__"

    EMPTY_TRASH = "🗑️🚮**Trash Emptied Successfully !**"

    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"
