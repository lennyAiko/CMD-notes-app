### DELETE NOTES

from . import all_notes

def delete_note(notes):

    all_notes.all_notes(notes)
    
    index = int(input("Please enter index (enter 0 to delete all): "))

    if index == 0:
        decision = input("Do you agree to delete all notes? (y/n): ")
        if decision == 'y':
            notes.clear()
            message = 'All notes deleted.'
        else:
            return
    elif index not in range(len(notes)+1):
        message = 'Note does not exist.'
    else:
        decision = input("Do you agree to delete this note? (y/n): ")
        if decision == 'y':
            del notes[index-1]
            message = 'Note successfully deleted.'
        else:
            return

    return message
