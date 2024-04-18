from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("✨ ᴄᴏᴍᴍᴀɴᴅs ✨", data="help_back")
    ],
    [
        Button.url("⚜️ ᴅᴇᴠᴇʟᴏᴘᴇʀ ⚜️", "https://t.me/llxHKxll"),
        Button.url("🍁 ᴏᴡɴᴇʀ 🍁", "https://t.me/H4SS4NP4P4")
    ],
    [
        Button.url("✨ ғᴏʀ ᴜᴘᴅᴀᴛᴇs ✨", "https://t.me/XovaAssociation")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n"
        await event.client.send_file(
            event.chat_id,
            "https://telegra.ph/file/f098d4e87cd29f185ea26.jpg",
            caption=TEXT,
            buttons=START_BUTTON
        )
