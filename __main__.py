import os
from os import environ
from pyrogram import Client, idle
from info import API_ID, API_HASH, BOT_TOKEN

BOT_TOKEN2 = os.environ.get("BOT_TOKEN2", "5229561897:AAHCZD5-U7iyN57G8fPDNyyYlFIRST1TUpo")

if __name__ == "__main__" :
    plugins = dict(root="CYNITE")
    app1 = Client(
        "Client1",
        bot_token=BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app2 = Client( # This is 2nd client. add much as you wish. but remember to edit starting process
        "Client2",
        bot_token=BOT_TOKEN2,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    print("Waking Up Client 1")
    app1.start() # Starting Client 1
    print("Waking Up Client 2")
    app2.start() # Starting Client 2
    print("Everything Ok! Enjoy Multi Client! Lol!") # Remove this shit if you like lmao
    idle()
