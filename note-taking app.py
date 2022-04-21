import os
files =  os.listdir()
userFileInput = input("please enter a filename eg hello.txt:" "\n")
BASE_PATH = os.path.dirname(os.path.abspath(__file__)) # Best practice

if userFileInput in files: 
    print( "A) read file " "\n" "B) Delete the file and start over " "\n" "C) Append the file" "\n" ) 
    option = str(input("select A,B and C to specify action:\n" )).upper() # Make sure we strngify the user input to avoid edge cases
    if option == "A":
        f = os.path.join(BASE_PATH, userFileInput) # Best practice 
        with open(f, "r") as selectedFile: # Always best practice to use context managers when handling files
            fileContent = selectedFile.read() # Reads the contends of the selected file
            print(fileContent)

    elif option == "B":
        os.remove(userFileInput) # Delete the file
        with open(userFileInput,"w") as newFile: # Create a new file with the same name as the deleted one
            newFileContent = input("enter text here:\n") # write some content to the file
            newFile.write(f"{newFileContent}\n")

    elif option == "C":
        with open(userFileInput,"a") as fileToAppend: 
            appendContent = input("continue text here:\n")
            fileToAppend.write(f"{appendContent}\n")
            print("Appended successfully!!")

else:
     with open(userFileInput, "w") as createFile:
         createFileContent = input("enter the text to write to the file:\n")
         createFile.write(f"{createFileContent}\n")
         print("File created sucessfully")