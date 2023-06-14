import time
import cv2
from bus_stop import get_bus_stop
from bus import get_bus
bus_stops = get_bus_stop()
bus = get_bus()


def detect():
    sum_num = 0
    for i in bus_stops:
        image = cv2.imread('./image/busStop' + i.get_stop_id() + '.jpg')
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        (rects, _) = hog.detectMultiScale(
            image, winStride=(4, 4), padding=(8, 8), scale=1.05)
        i.set_waiting_people(rects.shape[0])
        sum_num += int(i.get_waiting_people())
    # 欲查詢站牌後面各站總等待人數
    return sum_num
    # time.sleep(5)
