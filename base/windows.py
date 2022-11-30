import win32gui
import keyboard
import win32con


class totop:
    """
    hWndlnsertAfter: 用于标识 Z 顺序, 可设为以下值:
        HWND_BOTTOM: 值为 1, 置底
        HWND_TOP : 值为 0, 置顶
        HWND_NOTOPMOST: 值为 -2, 置于非置顶窗口之上
        HWND_TOPMOST: 值为 -1, 置顶 (在HWND_TOP之上)



    :prams hwnd 被修改的窗口的句柄
    """

    flag = False
    hw = ""

    def force_focus(self, hwnd):
        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_TOPMOST,
            0,
            0,
            0,
            0,
            win32con.SWP_NOOWNERZORDER | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE,
        )

    def cancel_focus(self, hwnd):
        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_NOTOPMOST,
            0,
            0,
            0,
            0,
            win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE,
        )

    def handler(self, op, hwnd):
        op(hwnd)

    def get_key(self):
        def fun():

            if not self.flag and win32gui.GetForegroundWindow() != "":
                self.hd = win32gui.GetForegroundWindow()
                self.handler(self.force_focus, self.hd)
                self.flag = True
            elif self.flag and win32gui.GetForegroundWindow() != "":
                if self.hd == win32gui.GetForegroundWindow():
                    self.handler(self.cancel_focus, win32gui.GetForegroundWindow())
                    self.flag = False

        keyboard.add_hotkey("alt+t", fun)

        while True:
            keyboard.wait()

    def get_all_windows(self):
        """
        获取窗口句柄
        """
        hWnd_list = []
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
        print(hWnd_list)
        return hWnd_list

    def get_jb_id(self, title):
        """
        根据标题找句柄
        :param title: 标题
        :return:返回句柄所对应的ID
        """
        jh = []
        hwnd_title = dict()

        def get_all_hwnd(hwnd, *args):
            if (
                win32gui.IsWindow(hwnd)
                and win32gui.IsWindowEnabled(hwnd)
                and win32gui.IsWindowVisible(hwnd)
            ):
                hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

        win32gui.EnumWindows(get_all_hwnd, 0)
        for h, t in hwnd_title.items():
            if t != "":
                if title in t:
                    jh.append(h)

        if len(jh) == 0:
            print("找不到相应的句柄")
        else:
            return jh
