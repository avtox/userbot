from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from time import sleep
 
app = Client("my_account")
 
# Команда type
@app.on_message(filters.command("е", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".е ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.04) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.04)
 
        except FloodWait as e:
            sleep(e.x)
 
app.run()