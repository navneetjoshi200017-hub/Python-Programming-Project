try:

    file_path = input("Enter file path: ")        
    # file_path = "Test.txt"
    fopen = open(file_path,"r")

except FileNotFoundError:
    print("File Does Not Exist!!")

else:
    print("File opened successfully!")

    unique_words = dict()

    line = " "              #To enter the while loop set line = " " so that it can read line without problem
    while(line != ""):
        line = fopen.readline()     #Read file line by line to save memory
        words = line.split()        #Create a list of words in "line"

        #Frequency Counter
        for word in words:
            if(word in unique_words):
                unique_words[word] += 1
            else:
                unique_words[word] = 1

    unique_count = len(unique_words)        #Length of the dictionary is equal to no. of unique words 
    
    print(unique_words)
    print(f"{unique_count =}")

    fopen.close()       #Close the file

finally:
    
    print("Exiting...")
