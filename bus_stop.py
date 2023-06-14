# 建立一個用來儲存公車站牌資訊的類別，裡面要包含站牌名稱、站牌ID、等車人數、可上車人數等資訊
# 並且要能夠回傳該站牌的資訊

class BusStop:
    # stop_name: 站牌名稱 stop_id: 站牌ID  waiting_people: 等車人數
    def __init__(self, stop_name, stop_weight, stop_id, waiting_people, stop_available):
        self.stop_name = stop_name
        self.stop_weight = stop_weight
        self.stop_id = stop_id
        self.waiting_people = waiting_people
        self.stop_available = stop_available

    def set_stop_name(self, name):
        self.stop_name = name

    def set_stop_wight(self, weight):
        self.stop_weight = weight

    def set_stop_id(self, stop_id):
        self.stop_id = stop_id

    def set_waiting_people(self, waiting_people):
        self.waiting_people = waiting_people

    def set_stop_available(self, stop_available):
        self.stop_available = stop_available

    def get_stop_name(self):
        return str(self.stop_name)

    def get_stop_weight(self):
        return str(self.stop_weight)

    def get_stop_id(self):
        return str(self.stop_id)

    def get_waiting_people(self):
        return str(self.waiting_people)

    def get_stop_available(self):
        return str(self.stop_available)

    def __str__(self):
        return "站牌名稱: " + str(self.stop_name) + ", 站牌ID: " + str(self.stop_id) + ", 等車人數: " + str(self.waiting_people) + ", 可上車人數： " + str(self.stop_available) + "\n"

    def __repr__(self):
        return "站牌名稱: " + str(self.stop_name) + ", 站牌ID: " + str(self.stop_id) + ", 等車人數: " + str(self.waiting_people) + ", 可上車人數： " + str(self.stop_available) + "\n"


badouzi_station = BusStop("八斗子車站", 8, "0", None, None)
bisa_fishingport = BusStop("碧砂漁港", 5, "1", None, None)
ntou_gym = BusStop("海大體育館", 16, "2", None, None)
ntou_binhai = BusStop("海大濱海校門", 16, "3", None, None)
ntou_xiangfeng = BusStop("海大祥豐校門", 16, "4", None, None)
erxin_highschool = BusStop("二信高中", 12, "5", None, None)
xiangfeng_market = BusStop("祥豐市場", 7, "6", None, None)
employmen_service = BusStop("就業服務中心", 7, "7", None, None)
keelung_cityhall = BusStop("基隆市政府", 13, "8", None, None)
bus_stop = [badouzi_station, bisa_fishingport, ntou_gym, ntou_binhai, ntou_xiangfeng,
            erxin_highschool, xiangfeng_market, employmen_service, keelung_cityhall]


def get_bus_stop():
    return bus_stop
