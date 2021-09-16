from config import Config 
from pyrogram import Client, Filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from translation import Translation

UPDATE_CHANNEL=Config.UPDATE_CHANNEL
PASS_TEXT=Config.PASS_TEXT

LINK = "https://telegram.dog/Mo_Tech_YT"



@Client.on_message(filters.private & filters.command("password"))
async def password(motech, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await motech.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 😜**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{Channel User Name} To Use Me") From Motech.py
            await update.reply_text(
                text="First Join My Update Channel Then Will Get Password",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="🔔 Join My Update Channel 🔔", url=f"t.me/{UPDATE_CHANNEL}")],
                    ])
            )
            return
        except Exception:
            await update.reply_text(f"@{UPDATE_CHANNEL}")
            return  
    reply_markup =  PASS_BUTTON
    await update.reply_text(
        text=Translation.PASSWORD.format(update.from_user.mention, PASS_TEXT),
        disable_web_page_preview=True,
        reply_markup=reply_markup
  )

PASS_BUTTON = InlineKeyboardMarkup([[
         InlineKeyboardButton("How To Own", url=f"{LINK}")
         ]]
         )
