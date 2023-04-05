#!/usr/bin/python3
'''
    A module which contains a function that prints prints a
    text with 2 new lines after each of these characters: ., ? and :
'''


def text_indentation(text):
    ''' Function that prints 2 new lines each of these char (".?:")

     Arguments:
          text: string

     Return: None

     Raises:
         TypeError: if text != string

    '''

    if type(text) is not str:
        raise TypeError("text must be a string")

    new = text[:]  # cloning text

    for dem in ".?:":
        new_list = new.split(dem)
        new = ""
        for itr in new_list:
            itr = itr.strip()
            if new is "":
                new = itr + dem
            else:
                new += "\n\n" + itr + dem
    print(new[:-3], end="")
