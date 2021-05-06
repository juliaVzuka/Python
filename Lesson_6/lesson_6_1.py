from time import sleep

tl_modes = {1: ['Red!(7)', 7], 2: ['Yellow!(2)', 2], 3: ['Green!(5)', 5]}

class TrafficLight:


    def __init__(self, color):
        self.__color = color


    def running(self, color):
        print(tl_modes.get(color)[0])
        sleep(int(tl_modes.get(color)[1]))
        return

n = int(input('Сколько циклов светофора вы хотите наблюдать?: '))
now = int(input('Какой сейчас горит свет? 1 - Red, 2 - Yellow, 3 - Green: '))
tr = TrafficLight(now)
for i in range(n):
    while now <= 3:
        tr.running(now)
        now += 1
    now = 1
