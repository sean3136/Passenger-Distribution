from passenger_distribute import passenger_distribute
from bus import get_bus
from detect import detect
bus = get_bus()
stop_id = ""
while True:
  stop_id = input("請輸入欲查詢站牌名稱: ")
  if stop_id == "q":
    break
  else:
    passenger_distribute(stop_id)