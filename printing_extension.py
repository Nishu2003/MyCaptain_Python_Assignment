# program to accept a file name from the user and print the extension of that file
filename = input("Enter file name : ")
extension = filename.split(".")
print("Entension of the file is : "+repr(extension[-1]))
