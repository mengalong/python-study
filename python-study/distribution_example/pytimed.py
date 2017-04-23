import pkg_resources
import time

def main():
    seconds_passed = 0
    while True:
        for entry_point in pkg_resources.iter_entry_points('pytimed'):
            try:
                seconds, callable = entry_point.load()()
            except Exception as err:
                print "got exception %s" % err
                pass
            else:
#                if seconds_passed % seconds == 0:
#                    callable()
                callable()
            time.sleep(1)
            seconds_passed += 1
