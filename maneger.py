import tkinter.messagebox
import time, threading

from base.config import Config_do
from base.windows import totop


class drink_notify(totop, Config_do):
    def __init__(self, p: str) -> None:
        totop.__init__(self)
        Config_do.read_config(p)
        r = False

    def show_notify(self):
        _w = threading.Thread(target=self.__show_notify)
        _w.start()

        self.__read_hwnd()

        _t = threading.Thread(target=self.force_focus, args=(self.hwnd))
        _t.start()

        _w.join()
        # 返回布尔值参数，除了确定，其他都是false
        return self.r

    def __show_notify(self):
        self.r = tkinter.messagebox.askokcancel(
            Config_do.get_self(["title"], "喝水啦!"),
            Config_do.get_self(["msg"], " 你该喝水啦, 记得起来走走哇! "),
        )
        time.sleep(1)

    def __read_hwnd(self):
        while True:
            self.hwnd = self.get_jb_id(Config_do.get_self(["title"], "喝水啦!"))
            if self.hwnd:
                break


def main(p: str):
    d = drink_notify(p)
    while True:
        _r = d.show_notify()
        if _r:
            print("暂停 {} 分钟".format(Config_do.get_self(["interval"], 20)))
            time.sleep(Config_do.get_self(["interval"], 30) * 60)


if __name__ == "__main__":
    main("config.json")
