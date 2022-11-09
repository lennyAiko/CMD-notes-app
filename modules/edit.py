### FOR MAKING CHANGES TO NOTES

from . import add
from . import all_notes
from . import time


date, get_time = time.get_time_date()

def update_note(notes):

    all_notes.all_notes(notes)

    index = int(input("Please enter index: "))

    num = len(notes)

    note = notes[index-1]

    if index > num:
        print("Does not exist")
        return
    else:

        string = list(note[0])

        buffer = add.call(string)

        decision = input("Do you agree to make changes? (y/n): ")

        if decision == 'y':
            notes[index-1] = buffer
        else:
            return