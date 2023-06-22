# structured-echo-bot
A training project within the course on the development of Telegram bots. Contains simple structured Telegram echo-bot.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green) 
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

## Installation 🛠️

1. Clone the repository: `git clone https://github.com/jiptwo553900/structured-echo-bot.git`
2. Rename `.env.example`: `mv .env.example .env`
3. In `.env` edit `BOT_TOKEN=<put your Telegram bot token here>`
4. Start `bot.py`

## Project structure 🗃️

made with my micro-project: [folder-tree-printer](https://github.com/jiptwo553900/folder-tree-printer)

```
├── 📁 structured-echo-bot
│   ├── 📄 .env                   # API token here
│   ├── 📄 .env.example
│   ├── 📄 .gitignore
│   ├── 📄 bot.py                    
│   ├── 📁 config_data            # classes and config load
│   │   ├── 📄 config.py
│   │   └── 📄 __init__.py
│   ├── 📁 handlers               # handlers
│   │   ├── 📄 other_handlers.py       
│   │   ├── 📄 user_handlers.py   # /start & /help handlers
│   │   └── 📄 __init__.py
│   ├── 📁 lexicon
│   │   ├── 📄 lexicon.py         # bot answers
│   │   └── 📄 __init__.py
│   └── 📄 README.md
```
