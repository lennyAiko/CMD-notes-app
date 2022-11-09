### VIEW ALL NOTES

def all_notes(notes):
    if len(notes) > 0:
        print("""
        index | note
        -------------
        """)
        for i in range(len(notes)):
            if notes[i][0]:
                note = notes[i][0]
                print(f"\t{i+1} | {note[:5]}...")
    else:
        print("\nNo note available.")