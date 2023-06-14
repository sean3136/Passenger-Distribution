from bus_stop import get_bus_stop
from bus import get_bus
from detect import detect
import time

bus_stops = get_bus_stop()
bus = get_bus()
sum_num = detect()
bus_capacity = int(bus.get_bus_capacity())


def algorithm():
    total_weight = 0
    init_bus_capacity = int(bus.get_bus_capacity())
    for i in bus_stops:
        total_weight += i.waiting_people * i.stop_weight

    for i in bus_stops:
        avail = round((i.waiting_people * i.stop_weight) /
                      total_weight * bus_capacity)
        i.set_stop_available(avail)
        init_bus_capacity -= avail
        print("各站可上車人數: " + str(avail), end="\n")
        print("各站剩餘人數: " + str(i.waiting_people - avail), end="\n")
        print("車上剩餘空位: " + str(init_bus_capacity), end="\n")
    time.sleep(5)
