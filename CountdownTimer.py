import time
import sys

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        sys.stdout.write("\r" + str(t))
        sys.stdout.flush()
        time.sleep(1)
        t -= 1

    print("\nTime's up!")

t = input("Enter the time in seconds: ")

countdown(int(t))