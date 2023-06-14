from passenger_distribute import passenger_distribute
from bus_stop import get_bus_stop
from bus import get_bus
from detect import detect
import time
bus_stops = get_bus_stop()
bus = get_bus()

print("公車站-代號: ")
for i in bus_stops:
  print(i.get_stop_name() + "-" + i.get_stop_id())
print("輸入q離開")

stop_id = ""
while True:
  stop_id = input("請輸入欲查詢站牌代號: ")
  if stop_id == "q":
    break
  elif stop_id not in ["0", "1", "2"]:
    print("輸入錯誤，請重新輸入")
    continue
  else:
    while(time.localtime().tm_sec % 5 != 0):
      stop_person = detect(stop_id)
    if(time.localtime().tm_sec % 5 == 0):
      passenger_distribute(stop_id)