# Q.3. Write a Python program to open a file in write mode, write some text, and then close it.(Write a Python program to create a file and write a string into it.)

file = open("sample.txt", "w")
file.write("This is a sample string.")
file.close()
print("File created and text written successfully.")
