from pynput.mouse import Button, Controller
from datetime import datetime, timedelta
from threading import Timer

# config variables
SECONDS = 5  # between clicks

# do not touch below
mouse = Controller()

seconds_to_wait = SECONDS


def do_click():
    mouse.click(Button.left)
    print(datetime.now())
    print('CLICKED.')
    begin_timer()
    

def begin_timer():
    t = Timer(seconds_to_wait, do_click)
    t.start()


begin_timer()
