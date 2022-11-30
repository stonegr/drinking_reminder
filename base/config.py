import json


class Config_do:
    @staticmethod
    def r_json(lj):
        """
        读取json到字典
        """
        try:
            f = open(f"{lj}", "r", encoding="utf-8", newline="")
            char_ = f.read()
            f.close()
            _c = json.loads(char_)
        except:
            _c = {}
        return _c

    @classmethod
    def read_config(cls, f_path: str):
        """
        读取json配置文件
        """
        cls.config = cls.r_json(f"{f_path}")

    # 获取配置并设置默认值
    @classmethod
    def get_self(cls, l: list = [], d="", c={}) -> str:
        """
        获取配置文件的默认值
        :param c,json格式的配置文件
        :param l,获取值的路劲
        :param d,获取错误时的默认值
        """
        if not c:
            c = cls.config

        try:
            x = c
            for i in l:
                x = x[i]
        except:
            x = d
        return x
