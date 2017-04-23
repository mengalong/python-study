#!/usr/bin/env python
#coding: utf8
import sys
import warnings

class TestModule(object):
    def __init__(self):
        pass

    def get_modules_imported_default(self):
        for name in sys.modules.keys():
            print name, sys.modules[name]


"""documented API change with warning
   Since python2.7, DeprecationWarning are not display by default.
   To disable this filter, you need call python with the -W all 
   option.
   Such as: you can exec this example code like this:
        python -W error basic_info.py
"""
class Car(object):
    def turn_left(self):
        """Turn the car left
        .. deprecated:: 1.1
           Use : func:`turn` instead with the direction argument set to left.
        """
        warnings.warn("turn_left is deprecated, use trun instead", 
                DeprecationWarning)
        self.turn(direction='left')

    def turn(self, direction):
        """Turn the car in some direction.
        :param direction: The direction to turn to.
        :type direction: str
        """
        print "I will turn to:%s" % direction

if __name__ == "__main__":
    mod_obj = TestModule()
    #mod_obj.get_modules_imported_default()

    car_obj = Car()
    car_obj.turn_left()


