import tkinter.messagebox

from base.config import Config_do
from tkinter import Tk

tk = Tk()
tk.wm_attributes("-topmost", 1)
tk.withdraw()

Config_do.read_config("config.json")

a = tkinter.messagebox.askokcancel(
    Config_do.get_self(["title"], "喝水啦!"),
    Config_do.get_self(["msg"], " 你该喝水啦, 记得起来走走哇! "),
)
print(a)
