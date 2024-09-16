from djitellopy import Tello

tello = Tello()


def start_drone():
    tello.connect()
    tello.takeoff()

    try:
        while True:
            tello.rotate_counter_clockwise(3600)
            tello.curve_xyz_speed(100, 150, 120, 100, 100, 50, 20)
            print("Flight Time: " + str(tello.get_flight_time()))

    except KeyboardInterrupt:
        print("Press Ctrl-C to exit")
        pass

    tello.land()


start_drone()
