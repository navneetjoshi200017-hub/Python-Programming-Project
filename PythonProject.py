try:
    file_path = input("Enter file path: ")
    # file_path = "Test.txt"
    fopen = open(file_path,"r")

except FileNotFoundError:
    print("File Does Not Exist!!")

else:
    print("File opened successfully!")

finally:
    print("Exiting...")
