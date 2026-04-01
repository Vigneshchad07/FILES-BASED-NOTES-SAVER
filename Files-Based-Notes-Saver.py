import notes_manager

def main():
    notes_manager.initialize()
    
    print("Welcome to Notes Saver (Create & Read Only)!")
    print("--------------------------------------------")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Create a New Note")
        print("2. Read an Existing Note")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            title = input("Enter note title: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            content = input("Enter note content: ")
            if notes_manager.add_note(title, content):
                print(f"Note '{title}' saved successfully!")
            else:
                print(f"Error: A note with title '{title}' already exists.")
                
        elif choice == '2':
            title = input("Enter note title to read: ").strip()
            content = notes_manager.view_note(title)
            if content is not None:
                print(f"\n--- Reading: {title} ---")
                print(content)
                print("-------------------------")
            else:
                print("Error: Note not found.")
                
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
