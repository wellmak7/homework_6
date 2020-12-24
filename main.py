import time

work_time = 12

class TrafficLight:
    __color = "red"
    def running(self):
        for i in range(0, work_time):
            if i < 7:
                print("red")
            elif i < 9:
                print('yellow')
            else:
                print('green')
            time.sleep()

lights = TrafficLight()
lights.running()
