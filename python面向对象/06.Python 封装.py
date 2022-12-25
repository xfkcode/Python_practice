class Phone:
    # 私有成员属性__开头，类内使用
    __current__voltage = 0.5
    # 私有成员方法__开头，类内使用
    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5G(self):
        if self.__current__voltage >= 1:
            print("5G通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5G通话，已设置为单核运行进行省电。")

phone = Phone()
phone.call_by_5G()
