from pynput.mouse import Button, Controller
from datetime import datetime, timedelta
from threading import Timer

# config variables
POSITION = (1350, 180)  # x, y mouse position, set through trial and error
DAYS_IN_ADVANCE = 0  # 0 if today, 1 if tomorrow, etc.
HOUR = 7  # 0 for 12am, 23 for 11pm
MINUTE = 0  # 0 to 59
SECOND = 0  # 0 to 59
MICROSECOND = 0  # 0 to 999999

# do not touch below
mouse = Controller()

today = datetime.today()
target = today.replace(day=today.day, hour=HOUR, minute=MINUTE, second=SECOND, microsecond=MICROSECOND) + timedelta(days=DAYS_IN_ADVANCE)
delta_t = target - today
seconds_to_wait = delta_t.total_seconds()


def prepare():
    mouse.position = POSITION
    print('MOVING CURSOR TO POSITION, CLICKING IN 5 SECONDS...')


def do_click():
    mouse.click(Button.left)
    print(datetime.now())
    print('CLICKED.')
    

t1 = Timer(seconds_to_wait - 5, prepare)
t2 = Timer(seconds_to_wait, do_click)

t1.start()
t2.start()
