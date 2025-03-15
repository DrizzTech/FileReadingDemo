
import os

# Function to create the file if it does not exist
def file_creator():
    """Create the 'example.txt' file if it doesn't exist."""
    if not os.path.exists("example.txt"):
        with open("example.txt", "w") as file:
            file.write("This is an example file.")
    print("File creation checked or completed.")

# Function to attempt reading the file with error handling
def test_file():
    """Read the content of 'example.txt' and handle exceptions."""
    try:
        with open("example.txt", "r") as file:
            content = file.read()
            print(f"Content of the file: {content}")

    except Exception as e:
        print(f"An error occurred: {e}")

    else:
        print("File read successfully!")

    finally:
        print("File operation attempt complete.")

# Function to provide a simple menu for file operations
def file_menu():
    """Display a menu to manipulate the 'example.txt' file."""
    choice = input("Input 1 to read, 2 to append: ")

    if choice == "1":
        try:
            with open("example.txt", "r") as file:
                file.seek(10)
                content = file.read()
                print(f"Content starting from 10th byte: {content}")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif choice == "2":
        try:
            with open("example.txt", "a") as file:
                file.truncate(20)
                print("File truncated to 20 bytes.")
        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        print("Invalid choice. Please enter 1 or 2.")

# Call the functions
file_creator()  # Ensure the file exists
test_file()     # Test file reading
file_menu()     # Provide file operation menu





