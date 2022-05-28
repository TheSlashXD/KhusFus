from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Namaskar {}

🌐 I'm the Whisper Bot.

💬 You can use me to send secret whispers in groups.

🔮 I work in the Inline mode that means you can use me even if I'm not in the group.

💌 It is very easy to use me, simply forward a message from a user to which you want to send a whisper and I'll do the rest for you.

There are other ways to use me too. If you are interested to learn more about me click on the Button below.
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Send a Whisper", switch_inline_query="")],
        [InlineKeyboardButton(text="Return Home", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("💬 Send a Whisper 💬", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help")
        ],
    ]

    # Help Message
    HELP = """
Just type the message in below format in any chat.

`@KhusFusBot your_message friend_username/id`
he other way to use me is to write the inline query by your self

the format should be in this arrangement

`@KhusFusBot your whisper @username`

now I'll split out the format in 3 parts and explain every part of it

1- `@KhusFusBot`
this is my username it should be at the beginning of the inline query so I'll know that you are using me and not another bot.

2-`whisper message`
it is the whisper that will be sent to the target user, you need to remove `your whisper` and insert your actual whisper.

3- `@username`
you should replace this with target's username so the bot will know that the user with this username can see your `whisper message`.

example:- 
`@KhusFusBot hello this is a test @xyusername`

📎 The bot works in groups and the target user should be in the same group with you
what you are waiting for?!
try me now 😉
    """