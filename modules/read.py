### FOR READING AND DELETING NOTES

from . import all_notes

def get_note(notes):

    choice = input("Read all? (y/n): ")

    if choice.lower() == 'y':
        for i in range(len(notes)):
            note = notes[i]
            print(note)
        message = 'All notes printed on screen'
        item = []
    
    else:

        all_notes.all_notes(notes)

        index = int(input("Please enter index (enter 00 to read all): "))

        print()

        if len(notes) == '0':
            message = 'No note available.'
        elif index > len(notes):
            message = 'Note does not exist'
        else:
            item = notes[int(index)-1]
            message = ''
    return message, item