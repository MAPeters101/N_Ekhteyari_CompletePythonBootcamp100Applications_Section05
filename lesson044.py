import os


def display_menu():
    print("\nNote-taking App")
    print("\n1. View Notes")
    print("\n2. Add Note")
    print("\n3. Delete Note")
    print("\n4. Exit")

def view_notes():
    print("\nExisting Notes: ")
    notes_dir = 'notes'
    if not os.path.exists(notes_dir):
        print("No notes available.")
        return
    for filename in os.listdir(notes_dir):
        with open(os.path.join(notes_dir, filename), 'r') as file:
            content = file.read()
            print(f"{filename[:4]}:{content}")


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


def delete_note():
    note_title = input("Enter the title of the note to delete: ")
    notes_dir = "notes"
    note_path = os.path.join(notes_dir, f"{note_title}.txt")

    if os.path.exists(note_path):
        os.remove(note_path)
        print(f"Note '{note_title}' deleted successfully.")
    else:
        print(f"Note '{note_title}' not found")


def main():

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            view_notes()
        if choice == '2':
            add_note()
        if choice == '3':
            delete_note()
        if choice == '4':
            print("Exiting the Note-taking App. GoodBye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
