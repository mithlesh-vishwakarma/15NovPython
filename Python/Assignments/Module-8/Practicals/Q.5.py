# Q.5 Write a Python program to read a file and print the data on the console.

try:
    with open("sample.txt", "r") as file:
        data = file.read()
        print("File Data:")
        print(data)
except FileNotFoundError:
    print("File not found. Please run Q.3.py or Q.4.py first.")
