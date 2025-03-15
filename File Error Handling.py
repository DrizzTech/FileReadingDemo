
import os

if not os.path.exists("example.txt"):
    with open("example.txt", "w") as file:
        file.write("This is an example file.")

try:
    with open("example.txt", "r") as file:
        content = file.read()

except FileNotFoundError: #
    print("The file does not exist.")

except Exception as e:
    print(f"An error occurred: {e}")

else:
    print("File read successfully!")

finally:
    print("File operation attempt complete.")




