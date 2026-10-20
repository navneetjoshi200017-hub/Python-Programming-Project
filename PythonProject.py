try:
    file_path = input("Enter file path: ")
    # file_path = "Test.txt"
    fopen = open(file_path,"r")

except FileNotFoundError:
    print("File Does Not Exist!!")

else:
    print("File opened successfully!")

    unique_words = dict()

    line = " "
    while(line != ""):
        line = fopen.readline()
        words = line.split()
        for word in words:
            if(word in unique_words):
                unique_words[word] += 1
            else:
                unique_words[word] = 1
    unique_count = len(unique_words)
    print(unique_words)
    print(f"{unique_count =}")

finally:
    print("Exiting...")
