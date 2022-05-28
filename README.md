# Whisper Bot

> A star ⭐ from you means a lot to us!

<p align="center"><a href="https://www.github.com/TheSlashXD/KhusFus"><img src="https://telegra.ph/file/6bced0abd8685486332a2.png" width="800"></a></p>

Telegram bot for Whisper Message.

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

## Usage

### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TheSlashXD/KhusFus)

1. Tap on above button and fill `API_ID`, `API_HASH`, `BOT_TOKEN`.
2. Then tap "Deploy App" below it. Wait till deploying is complete (will take atmost 2 minutes).
3. After deploying is complete, tap on "Manage App"
4. Check the logs to see if your bot is ready!
5) **IMPORTANT** : You need to do two things on [@BotFather](https://t.me/BotFather).
   1) Turn on Inline Mode in your bot settings.
   2) Now go back to settings, Tap on `Inline Feedback` and then on `100%` (without this your bot is nothing.)

### Local Deploying

1. Clone the repo
   ```markdown
   git clone https://github.com/TheSlashXD/KhusFus
   ```
   
2. Get a DATABASE_URL. If you don't know how, deploy using Heroku Button only.
   
3. Edit `Config.py` and fill the needed variables

4. Enter the directory
   ```markdown
   cd WhisperBot
   ```
5. Run the file
   ```markdown
   python3 whisper.py
   ```

## Environment Variables

#### Mandatory Vars

- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
- `DATABASE_URL` - Will be automatically added by Heroku.

## Stats

[![GitHub forks](https://img.shields.io/github/forks/TheSlashXD/KhusFus.svg?style=social&label=Fork&maxAge=25920000)](https://github.com/TheSlashXD/KhusFus/network/) [![GitHub stars](https://img.shields.io/github/stars/TheSlashXD/KhusFus.svg?style=social&label=Star&maxAge=25920000)](https://github.com/TheSlashXD/KhusFus/stargazers/) [![GitHub watchers](https://img.shields.io/github/watchers/TheSlashXD/KhusFus.svg?style=social&label=Watch&maxAge=25920000)](https://github.com/TheSlashXD/KhusFus/watchers/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/TheSlashXD/KhusFus/graphs/commit-activity)

## License

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

## Contributing

[![GitHub contributors](https://img.shields.io/github/contributors/TheSlashXD/KhusFus.svg)](https://github.com/TheSlashXD/KhusFus/graphs/contributors/)

> Contributions are heartily accepted.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Credits

- [Dan Tès](https://github.com/delivrance) for his [Pyrogram](https://docs.pyrogram.org) Library