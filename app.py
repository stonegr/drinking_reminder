import tkinter.messagebox
from tkinter import Tk
import time

from base.config import Config_do

# message的状态
message_status = False

tk = Tk()
tk.wm_attributes("-topmost", 1)
tk.withdraw()

Config_do.read_config("config.json")


def show_message():
    global message_status
    message_status = tkinter.messagebox.askokcancel(
        Config_do.get_self(["title"], "喝水啦!"),
        Config_do.get_self(["msg"], " 你该喝水啦, 记得起来走走哇! "),
    )


while True:
    if not message_status:
        show_message()
    else:
        sleep_time = Config_do.get_self(["interval"], 30)
        print("休眠: {} 分钟".format(sleep_time))
        time.sleep(sleep_time * 60)
        message_status = False
