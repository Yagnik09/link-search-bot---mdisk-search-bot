From configs import Config

From pyrogram import Client, filters, idle

From pyrogram.errors import QueryIdInvalid

From pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQuery, InlineQueryResultArticle, \
     InputTextMessageContent

From TeamTeleRoid.forcesub import ForceSub

Import asyncio



# Bot Client for Inline Search

Bot = Client(

    Session_name=Config.BOT_SESSION_NAME,

    Api_id=Config.API_ID,

    Api_hash=Config.API_HASH,

    Bot_token=Config.BOT_TOKEN

)



# User Client for Searching in Channel.

User = Client(

    Session_name=Config.USER_SESSION_STRING,

    Api_id=Config.API_ID,

    Api_hash=Config.API_HASH

)



@Bot.on_message(filters.private & filters.command(“start”))

Async def start_handler(_, event: Message):

	Await event.reply_photo(https://telegra.ph/file/19eeb26fa2ce58765917a.jpg,

                                Caption=Config.START_MSG.format(event.from_user.mention),

                                Reply_markup=InlineKeyboardMarkup([

					[InlineKeyboardButton(“Updates Channel”, url=https://t.me/ATM_Film_HD)],

					[InlineKeyboardButton(“How To Download”, url=https://t.me/how_to_download_movie_ka_video)],

                                        [InlineKeyboardButton(“About”, callback_data=”About_msg”)]

				]))



@Bot.on_message(filters.private & filters.command(“help”))

Async def help_handler(_, event: Message):



    Await event.reply_text(Config.ABOUT_HELP_TEXT.format(event.from_user.mention),

        Reply_markup=InlineKeyboardMarkup([

		[InlineKeyboardButton(“Updates Channel”, url=https://t.me/ATM_Film_HD), 

             InlineKeyboardButton(“About”, callback_data=”About_msg”)]

        ])

    )



@Bot.on_message(filters.incoming)

Async def inline_handlers(_, event: Message):

    If event.text == ‘/start’:

        Return

    Answers = f’**📂 Results For ➠ {event.text} \n\n➠ Type Only Movie Name With Correct Spelling.✍️\n➠ Add Year For Better Result.🗓️\n➠ Join @ATM_Film_HD\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n\n**’

    Async for message in User.search_messages(chat_id=Config.CHANNEL_ID, limit=50, query=event.text):

        If message.text:

            Thumb = None

            F_text = message.text

            Msg_text = message.text.html

            If “|||” in message.text:

                F_text = message.text.split(“|||”, 1)[0]

                Msg_text = message.text.html.split(“|||”, 1)[0]

            Answers += f’**🍿 Title ➠ ‘ + ‘’ + f_text.split(“\n”, 1)[0] + ‘’ + ‘\n\n📜 About ➠ ‘ + ‘’ + f_text.split(“\n”, 2)[-1] + ‘ \n\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱\nLink Will Auto Delete In 60Sec…⏰\n\n**’

    Try:

        Msg = await event.reply_text(answers)

        Await asyncio.sleep(65)

        Await event.delete()

        Await msg.delete()

    Except:

        Print(f”[{Config.BOT_SESSION_NAME}] – Failed to Answer – {event.from_user.first_name}”)





@Bot.on_callback_query()

Async def button(bot, cmd: CallbackQuery):

        Cb_data = cmd.data

        If “About_msg” in cb_data:

            Await cmd.message.edit(

			Text=Config.ABOUT_BOT_TEXT,

			Disable_web_page_preview=True,

			Reply_markup=InlineKeyboardMarkup(

				[

					[

						InlineKeyboardButton(“Updates Channel”, url=https://t.me/ATM_Film_HD)

					],

					[

						InlineKeyboardButton(“Home”, callback_data=”gohome”)

					]

				]

			),

			Parse_mode=”html”

		)

        Elif “Help_msg” in cb_data:

            Await cmd.message.edit(

			Text=Config.ABOUT_HELP_TEXT,

			Disable_web_page_preview=True,

			Reply_markup=InlineKeyboardMarkup(

				[

					[

					InlineKeyboardButton(“Updates Channel”, url=https://t.me/ATM_Film_HD)

					], 

                                        [

					InlineKeyboardButton(“Home”, callback_data=”gohome”),

					InlineKeyboardButton(“About”, callback_data=”About_msg”)

					]

				]

			),

			Parse_mode=”html”

		)

        Elif “gohome” in cb_data:

            Await cmd.message.edit(

			Text=Config.START_MSG.format(cmd.from_user.mention),

			Disable_web_page_preview=True,

			Reply_markup=InlineKeyboardMarkup(

				[

                                        [

					InlineKeyboardButton(“Updates Channel”, url=https://t.me/ATM_Film_HD)

					],

		           [

					InlineKeyboardButton(“How To Download”, url=”https://t.me/how_to_download_movie_ka_video”)

                                                                        ],

                                       [

					InlineKeyboardButton(“About”, callback_data=”About_msg”)

					]

				]

			),

			Parse_mode=”html”

		)



# Start Clients

Bot.start()

User.start()

# Loop Clients till Disconnects

Idle()

# After Disconnects,

# Stop Clients

Bot.stop()

User.stop()
