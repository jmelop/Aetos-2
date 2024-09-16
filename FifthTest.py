import threading
from djitellopy import Tello

tello = Tello()


def start_drone():
    tello.connect()
    tello.takeoff()


def start_route():
    first_circuit()

    tello.land()
    tello.end()


def first_circuit():
    tello.curve_xyz_speed(120, 120, 100, 60, 190, 70, 30)
    tello.move_forward(50)
    tello.move_up(20)
    tello.move_forward(50)
    tello.move_down(20)
    tello.move_left(30)
