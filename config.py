from pyrogram import emoji


class Messages:
    START_MSG = "**Hi there {}.**\n__I'm Google Drive Uploader Bot.You can use me to upload any file / video to Google Drive from direct link or Telegram Files.__\n__You can know more from /help.__"
    start_msg = "**์๋ํ๊ฐ ๐จ๐ผโ๐ {} ํ์...**\n์ง์ ๋ ์๊ฐ์ **๊ธ์**์ ์๋ ค์ฃผ๋ **๊ธ์๋ด**์ด๋ผ๊ณ  ํ๋ค...\n/help ๋ช๋ น์ด๋ก ์ฌ์ฉ ๋ฐฉ๋ฒ์ ๋ฐฐ์๋ณด๊ฑฐ๋ผ..."
    help_msg = f"""/start - โ **์ธ๋ชจ ์๋ ๋ช๋ น์ด**
/help - โน๏ธ **ํ์ฌ ์ด ๋ฉ์ธ์ง ๋ณด๊ธฐ**
/set - โ๏ธ **๊ธ์ ์ ๋ณด๋ฅผ ๋ฐ์ผ๋ ค๋ ํ๊ต ์ ๋ณด ๋ฑ๋ก** ์) /set ํ๊ตญ์คํ๊ต
/launch - {emoji.BELL} **๊ธ์ ์๋ฆผ ์ผ๊ธฐ**
/stop - {emoji.BELL_WITH_SLASH} **๊ธ์ ์๋ฆผ ๋๊ธฐ**
/delete - {emoji.PROHIBITED} **์ ์  ์ ๋ณด ์ญ์ **
/today - {emoji.POT_OF_FOOD} **์ค๋ ๊ธ์ ํ ๋ฒ์ ๋ณด๊ธฐ**
"""
    set_msg = "โ๏ธ **๊ธ์ ์ ๋ณด**๋ฅผ ๋ฐ์ผ๋ ค๋ **ํ๊ต**๋ฅผ ๋ฑ๋กํ๊ฒ ๋ธ๋ผ...\n์์๋ฅผ ๋ณด๊ณ  **์ ํํ** ์๋ ฅํ๊ฑฐ๋ผ...\n**์) /set ๋ํ๊ณ ๋ฑํ๊ต, /set ๋ฏผ๊ตญ์คํ๊ต**"
    launch_msg = f"{emoji.BELL} **์๋ฆผ์ด ์ผ์ก๋ธ๋ผ...**\n์์ผ๋ก **์กฐ/์ค/์์(์๋ ๊ฒฝ์ฐ๋ง)**์ ์๋ ค์ฃผ๊ฒ ๋ธ๋ผ...\n**์๋ฆผ ์ผ์ ์ค์ง๋** /stop **๋ฅผ ์๋ ฅํ๊ฑฐ๋ผ~**"
    stop_msg = f"{emoji.BELL_WITH_SLASH} **์๋ฆผ์ด ์ค์ง๋์๋ธ๋ผ...\n์๋ฆผ์ ๋ค์ ์ผ ๋ค๋ฉด** /launch **๋ฅผ ์๋ ฅํ๊ฑฐ๋ผ~**"
    alarm_msg = "๐ฝ๏ธ๐ฅฃ **์ค๋ {}** ๐ฝ๏ธ๐ฅฃ\n-----\n**{}**\n-----\nโ **์นผ๋ก๋ฆฌ :** ```{}```"
    alarm_error_msg = f"{emoji.CROSS_MARK_BUTTON} **์ค๋์ ๊ธ์์ด ์์ต๋๋ค!**"
    delete_msg = f"{emoji.WARNING} **์ ๋ง๋ก ์ ์  ์ ๋ณด๋ฅผ ์ญ์ ํ์๊ฒ ์ต๋๊น?** {emoji.WARNING}"
    delete_complete_msg = f"{emoji.CROSS_MARK_BUTTON} ** ์ ์  ์ ๋ณด๊ฐ ์ฑ๊ณต์ ์ผ๋ก ์ญ์ ๋์์ต๋๋ค.**"
    status_msg = "๐ค **ํ์ฌ ์ ์ , ๋ด ์ํฉ** ๐ค\n๐จ **์ด ์ ์  :** ```{}``` **๋ช**\n๐ **์๋ฆผ ํ์ฑํ ์ ์  :** ```{}``` **๋ช**\n๐ฝ๏ธ **๊ธ์ ์ด ์(์กฐ, ์ค, ์์ ์์) :** ```{}, {}, {}``` **๊ฐ**"
    help_msg_2 = f"""๐ฝ๏ธ๐ฅฃ **๊ธ์ ์๋ฆผ ๋ฐ๋ ๋ฐฉ๋ฒ** ๐ฝ๏ธ๐ฅฃ
{emoji.KEYCAP_DIGIT_ONE} /set **๋ช๋ น์ด๋ก ํ๊ต๋ฅผ ๋ฑ๋กํ๋ค.**
{emoji.KEYCAP_DIGIT_TWO} **๊ธ์ ์๊ฐ์  ์๋ฆผ์ ๊ธฐ๋ค๋ฆฐ๋ค. ๋~**
{emoji.KEYCAP_DIGIT_THREE} /stop **๋ช๋ น์ด๋ก ์๋ฆผ์ ์ผ์ ์ค์งํ๊ฑฐ๋,** /launch **๋ช๋ น์ด๋ก ์ผ์ ์ค์งํ ์๋ฆผ์ ๋ค์ ์ผค ์ ์๋ค.**
{emoji.KEYCAP_DIGIT_FOUR} /delete **๋ช๋ น์ด๋ก ์ ์  ์ ๋ณด๋ฅผ ์ญ์ ํ๋ค. ํ๊ต๋ฅผ ๋ฐ๊พธ๊ฑฐ๋ ๋ ์ด์ ๋ด์ ์ฌ์ฉํ์ง ์์ ๋ ์ด ๋ช๋ น์ด๋ฅผ ์๋ ฅํ๋๋ก!**
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
    #     # Dont remove this โ if you respect developer.
    #     "**Developed by @viperadnan**"
    # ]

    RATE_LIMIT_EXCEEDED_MESSAGE = "โ **Rate Limit Exceeded.**\n__User rate limit exceeded try after 24 hours.__"

    FILE_NOT_FOUND_MESSAGE = "โ **File/Folder not found.**\n__File id - {} Not found. Make sure it\'s exists and accessible by the logged account.__"

    INVALID_GDRIVE_URL = "โ **Invalid Google Drive URL**\nMake sure the Google Drive URL is in valid format."

    COPIED_SUCCESSFULLY = "โ **Copied successfully.**\n[{}]({}) __({})__"

    # NOT_AUTH = f"๐ **You have not authenticated me to upload to any account.**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"

    DOWNLOADED_SUCCESSFULLY = "๐ค **Uploading File...**\n**Filename:** ```{}```\n**Size:** ```{}```"

    UPLOADED_SUCCESSFULLY = "โ **Uploaded Successfully.**\n[{}]({}) __({})__"

    DOWNLOAD_ERROR = "โ**Downloader Failed**\n{}\n__Link - {}__"

    DOWNLOADING = "๐ฅ **Downloading File...\nLink:** ```{}```"

    ALREADY_AUTH = "๐ **Already authorized your Google Drive Account.**\n__Use /revoke to revoke the current account.__\n__Send me a direct link or File to Upload on Google Drive__"

    # FLOW_IS_NONE = f"โ **Invalid Code**\n__Run {BotCommands.Authorize[0]} first.__"

    AUTH_SUCCESSFULLY = '๐ **Authorized Google Drive account Successfully.**'

    INVALID_AUTH_CODE = 'โ **Invalid Code**\n__The code you have sent is invalid or already used before. Generate new one by the Authorization URL__'

    AUTH_TEXT = "โ๏ธ **To Authorize your Google Drive account visit this [URL]({}) and send the generated code here.**\n__Visit the URL > Allow permissions > you will get a code > copy it > Send it here__"

    DOWNLOAD_TG_FILE = "๐ฅ **Downloading File...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"

    PARENT_SET_SUCCESS = '๐โ **Custom Folder link set successfully.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'

    # PARENT_CLEAR_SUCCESS = f'๐๐ฎ **Custom Folder ID Cleared Successfuly.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'

    CURRENT_PARENT = "๐ **Your Current Custom Folder ID - {}**\n__Use__ ```/{} (Folder link)``` __to change it.__"

    # REVOKED = f"๐ **Revoked current logged account successfully.**\n__Use /{BotCommands.Authorize[0]} to authenticate again and use this bot.__"

    NOT_FOLDER_LINK = "โ **Invalid folder link.**\n__The link you send its not belong to a folder.__"

    CLONING = "๐๏ธ **Cloning into Google Drive...**\n__G-Drive Link - {}__"

    PROVIDE_GDRIVE_URL = "**โ Provide a valid Google Drive URL along with commmand.**\n__Usage - /{} (GDrive Link)__"

    INSUFFICIENT_PERMISSONS = "โ **You have insufficient permissions for this file.**\n__File id - {}__"

    DELETED_SUCCESSFULLY = "๐๏ธโ **File Deleted Successfully.**\n__File deleted permanently !\nFile id - {}__"

    WENT_WRONG = "โ๏ธ **ERROR: SOMETHING WENT WRONG**\n__Please try again later.__"

    EMPTY_TRASH = "๐๏ธ๐ฎ**Trash Emptied Successfully !**"

    PROVIDE_YTDL_LINK = "โ**Provide a valid YouTube-DL supported link.**"
