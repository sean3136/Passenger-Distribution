from bus_stop import get_bus_stop
from bus import get_bus
from detect import detect
import numpy as np
bus_stops = get_bus_stop()
bus = get_bus()

def passenger_distribute(stop_id):
  # 更新站牌等待人數
  sum_num = detect(stop_id)
  bus_stop = bus_stops[int(stop_id)]
  stop_waiting = int(bus_stop.get_waiting_people())
  bus_capacity = int(bus.get_bus_capacity())

  # 等待人數小於車輛剩餘空間
  if sum_num <= bus_capacity:
    print("可上車人數為: " + str(stop_waiting) + "人")
    bus_stop.set_waiting_people(0)
    bus.set_bus_capacity(bus_capacity - stop_waiting)
  # 等待人數大於車輛剩餘空間
  elif sum_num > bus_capacity:
    allow_num = round(stop_waiting * bus_capacity / sum_num)
    print("可上車人數為: " + str(allow_num) + "人")
    # 經系統分配後，車輛剩餘空間足夠
    if allow_num <= bus_capacity:
      print("經系統分配後")
      print("可上車人數為: " + str(allow_num) + "人")
      bus_stop.set_waiting_people(stop_waiting - allow_num)
      bus.set_bus_capacity(bus_capacity - allow_num)
    # 經系統分配後，車輛剩餘空間不足
    else: 
      print("車輛剩餘空間不足")
      print("可上車人數為: " + str(bus_capacity) + "人")
      bus_stop.set_waiting_people(stop_waiting - bus_capacity)
      bus.set_bus_capacity(0)