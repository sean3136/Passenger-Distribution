# 建立一個用來儲存公車站牌資訊的類別，裡面要包含站牌名稱、站牌ID、等車人數、可上車人數等資訊
# 並且要能夠回傳該站牌的資訊

class BusStop:
  # stop_name: 站牌名稱 stop_id: 站牌ID  waiting_people: 等車人數
  def __init__(self, stop_name, stop_id, waiting_people):
    self.stop_name = stop_name
    self.stop_id = stop_id
    self.waiting_people = waiting_people

  def set_stop_name(self, name):
    self.stop_name = name
  def set_stop_id(self, stop_id):
    self.stop_id = stop_id
  def set_waiting_people(self, waiting_people):
    self.waiting_people = waiting_people

  def get_stop_name(self):
    return str(self.stop_name)
  def get_stop_id(self):
    return str(self.stop_id)
  def get_waiting_people(self):
    return str(self.waiting_people)
  

  def __str__(self):
    return "站牌名稱: " + str(self.stop_name) + ", 站牌ID: " + str(self.stop_id) + ", 等車人數: " + str(self.waiting_people) + "\n"
  def __repr__(self):
    return "站牌名稱: " + str(self.stop_name) + ", 站牌ID: " + str(self.stop_id) + ", 等車人數: " + str(self.waiting_people) + "\n"

ntou_bus_stop = BusStop("八斗子車站", "0", None)
ntou_bus_stop1 = BusStop("海科館", "1", None)
ntou_bus_stop2 = BusStop("八斗子", "2", None)
ntou_bus_stop3 = BusStop("嶺林巷", "3", None)
ntou_bus_stop4 = BusStop("義胞新村", "4", None)
ntou_bus_stop5 = BusStop("漁貨直銷中心", "5", None)
ntou_bus_stop6 = BusStop("籃投溝", "6", None)
ntou_bus_stop7 = BusStop("北寧路", "7", None)
ntou_bus_stop8 = BusStop("海大(體育館)", "8", None)
ntou_bus_stop9 = BusStop("海大(濱海校門)", "9", None)
ntou_bus_stop10 = BusStop("海大(祥豐校門)", "10", None)
ntou_bus_stop11 = BusStop("二信中學", "11", None)
ntou_bus_stop12 = BusStop("祥豐市場", "12", None)
ntou_bus_stop13 = BusStop("天主堂", "13", None)
ntou_bus_stop14 = BusStop("中正區行政大樓", "14", None)
ntou_bus_stop15 = BusStop("就業中心", "15", None)
ntou_bus_stop16 = BusStop("信五路口", "16", None)
ntou_bus_stop17= BusStop("市政府", "17", None)
bus_stop = [ntou_bus_stop,ntou_bus_stop1,ntou_bus_stop2,ntou_bus_stop3,
            ntou_bus_stop4,ntou_bus_stop5,ntou_bus_stop6,ntou_bus_stop7,
            ntou_bus_stop8,ntou_bus_stop9,ntou_bus_stop10,ntou_bus_stop11,
            ntou_bus_stop12,ntou_bus_stop13,ntou_bus_stop14,ntou_bus_stop15,
            ntou_bus_stop16,ntou_bus_stop17]
def get_bus_stop():
  return bus_stop