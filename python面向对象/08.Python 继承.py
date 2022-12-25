class Phone:
    IMEI = None
    producer = "ITcast"

    def call_by_4G(self):
        print("4G通话")
# 单继承
class Phone2022(Phone):
    face_Id = "10001"

    def call_by_5G(self):
        print("5G通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_4G()
phone.call_by_5G()

class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

# 多继承
# 多个父类中，同名成员，默认继承顺序（从左到右）为优先级
class myPhone(Phone,NFCReader,RemoteControl):
    pass

myphone = myPhone()
myphone.call_by_4G()
myphone.read_card()
myphone.write_card()
myphone.control()

print(myphone.producer)