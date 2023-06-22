import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title="ALERT!!",
            message="TAKE A BREAK ITS BEEN AN HOURS OF CODING AND DEBUGGING!!!!",
            timeout=10
        )
        time.sleep(3600)