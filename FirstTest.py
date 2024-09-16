from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(60)
tello.move_right(60)
tello.move_down(30)
tello.move_up(30)

tello.land()