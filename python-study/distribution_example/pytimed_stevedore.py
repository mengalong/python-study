from stevedore.extension import ExtensionManager
import time

def main():
    seconds_passed = 0
    while True:
        for extension in ExtensionManager('pytimed', invoke_on_load=True):
            try:
                seconds, callable = extension.obj
            except:
                pass
            else:
                if seconds_passed % seconds == 0:
                    callable()
            time.sleep(1)
            seconds_passed += 1
