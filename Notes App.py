g = True
while g == True:
    print("1. Add note")
    print("2. View notes")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        note = input("Enter the note: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        print("Note added successfully!")
    if choice == 2:
        with open("notes.txt", "r") as file:
            notes = file.read()
            if notes == "":
                print("No notes available.")
            else:
                print(notes)
    if choice == 3:
        g = False
        print("Exiting the application.")