import cv2
import random
import threading
import time
import keyboard

from djitellopy import Tello

tello = Tello()
v_width = 320
v_height = 240
type_of_fly = 1
finish_Action = False


def garage(option: int):
    global type_of_fly
    type_of_fly = option
    start_drone()


def start_drone():
    turn_on_drone()
    if type_of_fly == 1:
        rotate_drone()
    elif type_of_fly == 2:
        move_drone()
    else:
        multiple_flips()

    land_drone()


def move_drone():
    tello.move_up(60)
    tello.move_down(50)
    tello.move_left(20)
    tello.move_right(20)


def multiple_flips():
    tello.flip_forward()
    tello.flip_back()
    tello.flip_left()
    tello.flip_right()


def rotate_drone():
    for x in range(2):
        tello.rotate_clockwise(60)
        tello.rotate_counter_clockwise(120)
        tello.rotate_clockwise(60)
        tello.flip_back()
        tello.move_forward(30)
    tello.move_up(40)
    tello.flip_back()


def turn_on_drone():
    tello.connect()
    tello.takeoff()


def land_drone():
    tello.land()


def turn_on_video():
    random_number = random.randint(0, 10000)
    tello.streamon()
    frame_read = tello.get_frame_read()
    cv2.imwrite("picture" + str(random_number) + ".png", frame_read.frame)
    tello.streamoff()


def turn_on_led():
    while True:
        if keyboard.read_key() == "p":
            print("You pressed p, turning on the communication")
            break


def drone_status():
    global finish_Action
    while finish_Action:
        time.sleep(3)
        print('Current battery: ' + str(tello.get_battery()) + '%')
        print('Current barometer data: ' + str(tello.get_barometer()))
        print('-----------------------------------------------')
        print('Get other data of the drone: ')
        print('-----------------------------------------------')
        print('Get Temperature: ' + str(tello.get_temperature()))
        print('Get Height: ' + str(tello.get_height()))


if __name__ == '__main__':
    startDroneThread = threading.Thread(target=garage, args=(3,))
    statusThread = threading.Thread(target=drone_status, args=())
    ledThread = threading.Thread(target=turn_on_led, args=())

    startDroneThread.start()
    statusThread.start()
    ledThread.start()

    startDroneThread.join()
    statusThread.join()
    ledThread.join()

    tello.land()
    finish_Action = True
    tello.end()
