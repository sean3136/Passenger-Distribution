from bus_stop import get_bus_stop
from bus import get_bus
from detect import detect
import time

bus_stops = get_bus_stop()
bus = get_bus()
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
        print(str(i.stop_name), end="\n")
        print("各站可上車人數: " + str(avail), end="\n")
        print("各站剩餘人數: " + str(i.waiting_people - avail), end="\n")
        print("車上剩餘空位: " + str(init_bus_capacity), end="\n")
        print("====================================", end="\n")

    if (init_bus_capacity > 0):
        max = 0
        max_index = 0
        for i in range(len(bus_stops)):
            if bus_stops[i].waiting_people - bus_stops[i].stop_available >= max:
                if bus_stops[i].stop_weight >= bus_stops[max_index].stop_weight:
                    max = bus_stops[i].waiting_people - \
                        bus_stops[i].stop_available
                    max_index = i
        print(str(bus_stops[max_index].stop_name) +
              "可上車人數: " + str(avail), end="\n")
        bus_stops[max_index].set_stop_available(
            bus_stops[max_index].stop_available + init_bus_capacity)
        init_bus_capacity = 0
        print(str(bus_stops[max_index].stop_name) + "增加上車人數", end="\n")
        print(str(bus_stops[max_index].stop_name) +
              "可上車人數: " + str(bus_stops[max_index].stop_available), end="\n")
        print("車上剩餘空位: " + str(init_bus_capacity), end="\n")
        print("====================================", end="\n")
