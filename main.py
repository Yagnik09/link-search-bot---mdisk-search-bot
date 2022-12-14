from configs import Config
from pyrogram import Client, filters, idle
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent
from TeamTeleRoid.forcesub import ForceSub
import asyncio

# Bot Client for Inline Search
Bot = Client(
    session_name=Config.BOT_SESSION_NAME,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# User Client for Searching in Channel.
User = Client(
    session_name=Config.USER_SESSION_STRING,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

@Bot.on_message(filters.private & filters.command("start"))
async def start_handler(_, event: Message):
	await event.reply_photo("https://telegra.ph/file/19eeb26fa2ce58765917a.jpg",
                                caption=Config.START_MSG.format(event.from_user.mention),
                                reply_markup=InlineKeyboardMarkup([
					[InlineKeyboardButton('❤ Donation Link', url='https://p.paytm.me/xCTH/gbenmi6c')],
					[InlineKeyboardButton("Updates 𝙲𝚑𝚊𝚗𝚗𝚊𝚕", url="https://t.me/ATM_Film_HD")],
					[InlineKeyboardButton("Donation", callback_data="Help_msg"),
                                        InlineKeyboardButton("About", callback_data="About_msg")]
				]))

@Bot.on_message(filters.private & filters.command("help"))
async def help_handler(_, event: Message):

    await event.reply_text(Config.ABOUT_HELP_TEXT.format(event.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
		[InlineKeyboardButton('❤ Donation Link', url='https://p.paytm.me/xCTH/gbenmi6c')
	 ],[InlineKeyboardButton("Updates 𝙲𝚑𝚊𝚗𝚗𝚊𝚕", url="https://t.me/ATM_Film_HD"), 
             InlineKeyboardButton("𝙰𝚋𝚘𝚞𝚝", callback_data="About_msg")]
        ])
    )

@Bot.on_message(filters.incoming)
async def inline_handlers(_, event: Message):
    if event.text == '/start':
        return
    answers = f'**📂 Results For ➠ {event.text} \n\n➠ Type Only Movie Name.✍️\n➠ Use Google For Correct Spelling.🔍\n➠ Join @ATM_Film_HD\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n\n**'
    async for msg_list in AsyncIter(search):
        async for msg in msg_list:
            c += 1
            f_text = re.sub("__|\*", "", msg.text)
            
            f_text = await link_to_hyperlink(f_text)
            answers += f'**✅ PAGE {c}:\n🍿 Title ➠ ' + '' + f_text.split("\n", 1)[0] + '' + '\n\n🔊 Language ➠ ' + '' + f_text.split("\n", 2)[-1] + ' \n\n━━━━━━━━━━━━━━\n⬇️ HOW TO 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 MOVIE\n@how_to_download_movie_ka_video\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n\n**'
    try:
        msg = await event.reply_text(answers)
        await asyncio.sleep(65)
        await event.delete()
        await msg.delete()
    except:
        print(f"[{Config.BOT_SESSION_NAME}] - Failed to Answer - {event.from_user.first_name}")


@Bot.on_callback_query()
async def button(bot, cmd: CallbackQuery):
        cb_data = cmd.data
        if "About_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_BOT_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
						InlineKeyboardButton('❤ Donation Link', url='https://p.paytm.me/xCTH/gbenmi6c')
					],
					[
						InlineKeyboardButton("Updates 𝙲𝚑𝚊𝚗𝚗𝚊𝚕", url="https://t.me/ATM_Film_HD")
					],
					[
						InlineKeyboardButton("Home", callback_data="gohome")
					]
				]
			),
			parse_mode="html"
		)
        elif "Help_msg" in cb_data:
            await cmd.message.edit(
			text=Config.ABOUT_HELP_TEXT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
					[
					InlineKeyboardButton('❤ Donation Link', url='https://p.paytm.me/xCTH/gbenmi6c')
					],
					[
					InlineKeyboardButton("Updates 𝙲𝚑𝚊𝚗𝚗𝚊𝚕", url="https://t.me/ATM_Film_HD")
					], 
                                        [
					InlineKeyboardButton("Home", callback_data="gohome"),
					InlineKeyboardButton("About", callback_data="About_msg")
					]
				]
			),
			parse_mode="html"
		)
        elif "gohome" in cb_data:
            await cmd.message.edit(
			text=Config.START_MSG.format(cmd.from_user.mention),
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(
				[
                                        [
					InlineKeyboardButton('❤ Donation Link', url='https://p.paytm.me/xCTH/gbenmi6c')
					],
					[
					InlineKeyboardButton("Updates 𝙲𝚑𝚊𝚗𝚗𝚊𝚕", url="https://t.me/ATM_Film_HD")
					],
					[
					InlineKeyboardButton("Donation", callback_data="Help_msg"),
					InlineKeyboardButton("About", callback_data="About_msg")
					]
				]
			),
			parse_mode="html"
		)

# Start Clients
Bot.start()
User.start()
# Loop Clients till Disconnects
idle()
# After Disconnects,
# Stop Clients
Bot.stop()
User.stop()
