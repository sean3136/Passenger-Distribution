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

ntou_gym = BusStop("海大體育館", "0", None)
ntou_binhai = BusStop("海大濱海校門", "1", None)
ntou_xiangfeng = BusStop("海大祥豐校門", "2", None)
bus_stop = [ntou_gym, ntou_binhai, ntou_xiangfeng]

def get_bus_stop():
  return bus_stop