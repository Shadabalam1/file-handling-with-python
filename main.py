from pathlib import Path

def read_file_and_folder():
    path = Path(".")
    items = list(path.rglob("*"))
    for i, item in enumerate(items):
        print(f"{i+1}. {item}")

def createfile():
    try:
        read_file_and_folder()
        file_name = input("Enter the name of the file: ")

        if not Path(file_name).exists():
            content = input("Enter content: ")

            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(content)

            print(f"{file_name} created successfully.")
        else:
            print(f"{file_name} already exists.")

    except Exception as e:
        print(f"Error: {e}")


def read_file():
    try:
        read_file_and_folder()
        file_name = input("Enter the name of the file to read: ")
        path = Path(file_name)

        if path.exists():
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
                print(f"Content of {file_name}:\n{content}")
        else:
            print(f"{file_name} does not exist.")

    except Exception as e:
        print(f"Error: {e}")


def update_file():
    try:
        read_file_and_folder()
        file_name = input("Enter the name of the file to update: ")
        path = Path(file_name)

        if path.exists() and path.is_file():
            print("press 1 to change the file name :- ")
            print("press 2 to change content previously content will be deleted:- ")
            print("press 3 to append to the file :- ")

            choice = input("Enter your choice: ")

            if choice == "1":
                new_name = input("Enter new file name: ")
                new_path = Path(new_name)

                if not new_path.exists():
                    path.rename(new_path)
                    print(f"File renamed to {new_name}")

                else:
                    print(f"File {new_name} already exists.")

            elif choice == "2":
                new_content = input("Enter new content previously content will be deleted: ")
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                    print(f"Content of {file_name} updated successfully.")


            elif choice == "3":
                new_content = input("Enter new content to append: ")
                with open(path, 'a', encoding='utf-8') as file:
                    file.write(new_content)
                    print(f"Content appended to {file_name} successfully.")

            print(f"{file_name} updated successfully.")
        else:
            print(f"{file_name} does not exist.")

    except Exception as e:
        print(f"Error: {e}") 

def delete_file():
    try:
        read_file_and_folder()
        file_name = input("Enter the name of the file to delete: ")
        path = Path(file_name)

        if path.exists() and path.is_file():
            path.unlink()
            print(f"{file_name} deleted successfully.")
        else:
            print(f"{file_name} does not exist.")

    except Exception as e:
        print(f"Error: {e}")

print("1. Create File")
print("2. Read Files/Folders")
print("3. Update File")
print("4. Delete File")

check = int(input("Enter your choice: "))

if check == 1:
    createfile()

elif check == 2:
   read_file() 
elif check == 3:
    update_file()
elif check == 4:   
   delete_file()