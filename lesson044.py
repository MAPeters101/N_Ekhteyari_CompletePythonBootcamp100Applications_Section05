import os


def display_menu():
    print("\nNote-taking App")
    print("\n1. View Notes")
    print("\n2. Add Note")
    print("\n3. Delete Note")
    print("\n4. Exit")

def add_note():
    note_title = input("Enter the note title: ")
    note_content = input("Enter the note content: ")

    notes_dir = 'notes'
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)

    note_path = os.path.join(notes_dir, f"{note_title}.txt")
    with open(note_path, 'a') as file:
        file.write(f"{note_content}\n")
    print(f"Note '{note_title}' added Successfully.")


