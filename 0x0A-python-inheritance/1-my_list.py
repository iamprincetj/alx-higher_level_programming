#!/usr/bin/python3
'''A module that contain a class (MyList) which inherits from
   the class (List)
'''


class MyList(list):
    '''The class MyList inheriting from list
    '''
    def print_sorted(self):
        print(sorted(self))
