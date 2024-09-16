import threading
from djitellopy import Tello

tello = Tello()


def start_drone():
    tello.connect()
    tello.takeoff()


def get_current_battery():
    print('Current battery: ' + str(tello.get_battery()) + '%', flush=True)


def get_current_height():
    print('Get Height: ' + str(tello.get_height()), flush=True)


if __name__ == '__main__':
    start_drone()

    firstThread = threading.Thread(target=get_current_battery, args=())
    secondThread = threading.Thread(target=get_current_height, args=())

    firstThread.start()
    secondThread.start()

    firstThread.join()
    secondThread.join()

    tello.land()
    tello.end()
