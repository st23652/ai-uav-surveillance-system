from djitellopy import Tello

# Initialize drone object
tello = Tello()

def connect_drone():
    """
    Connect to DJI Tello drone.
    """

    tello.connect()

    print("Connected to Drone")


def get_battery():
    """
    Retrieve drone battery percentage.
    """

    battery = tello.get_battery()

    return battery
