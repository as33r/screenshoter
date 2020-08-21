import pyautogui
import time
import argparse
import sys
import getpass
from datetime import datetime

os = sys.platform
if "win" in os:
    path = "C:/Users/" + getpass.getuser() + "/Desktop/"
else:
    if 'root' in getpass.getuser():
        path = "/root/"
    else:
        path = "/home/" + getpass.getuser() + "/"

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--time", dest="time", type=int, default=5, help="Time interval for capturing screenshots")
parser.add_argument("-n", "--name", dest="name", default="capture", help="Prefix for image capture name")
parser.add_argument("-p", "--path", dest="path", default=path, help="Provide path to save image")
options = parser.parse_args()

try:
    while True:
        now = datetime.now()
        name = "screenshot__" + str(now.day) + "-" + str(now.month) + "-" + str(now.year) + "__" + str(now.hour) + "-" + str(now.minute) + "-" + str(now.second)
        print(name)
        pyautogui.screenshot(options.path + name + ".png" )
        time.sleep(options.time)
except KeyboardInterrupt:
    print("Bye Bye")
except Exception as error:
    print("[-] Got an error : " + str(error))