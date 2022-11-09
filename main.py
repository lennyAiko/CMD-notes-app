### THE MAIN PROGRAM

import modules.add as add
import modules.read as read
import modules.delete as delete
import modules.edit as edit
import modules.all_notes as view_all


intro = """
        Hi, my name is Texty, i am a command line notes app.
        Note: Type 'q' on a new line then press enter to quit typing mode.
        What action would you like to perform?
        1. Create a new note (c).
        2. Edit a note (e).
        3. Read a note (r).
        4. Delete a note (d).
        5. See available notes (s).
        6. Quit (q).\n
        
        """

def major():
    notes = []

    while True:
        choice = input(intro)
        if choice.lower() == "c":
            print("You chose to create a new note, you can type below:")
            piece = add.call()
            notes.append(piece)
        if choice.lower() == 'e':
            edit.update_note(notes)
        if choice.lower() == 'r':
            message, item = read.get_note(notes)
            print(*item)
            print(f'{message}')
        if choice.lower() == 'd':
            message = delete.delete_note(notes)
            print(message)
        if choice.lower() == 's':
            view_all.all_notes(notes)
        if choice.lower() == 'q':
            break

if __name__ == '__main__':
    major()
