import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6361480431:AAF7g8BRquOXyBeVu8_f_kpp9gDwXDBVDSY")
SUDO = int(os.environ.get("SUDO", "6653027663"))
HEROKU = os.environ.get("HEROKU", "")
APP_URL = "https://"+ HEROKU +".herokuapp.com/" + BOT_TOKEN
