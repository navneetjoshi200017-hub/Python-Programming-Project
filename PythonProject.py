punctuations = ",/.<>?:;\"\\'|!@#$%^&*()[]{}_"                           

#Stop words : Excessively repeating words that are to be skipped
stop_words = {
    "the", "a", "an", "and", "or", "but",
    "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are",
    "was", "were", "be", "been", "being",
    "it", "this", "that", "these", "those",
    "i", "you", "he", "she", "we", "they"
}

try:

    # file_path = input("Enter file path: ")        
    file_path = "Test.txt"
    fopen = open(file_path,"r")

except FileNotFoundError:
    print("File Does Not Exist!!")

else:
    print("File opened successfully!")

    #Add a custom stop word to the set that user entered
    stop_word = input("Enter the word you want to ignore(Press enter if no stop word)\n(Custom stop word): ")
    stop_word = stop_word.strip().strip(punctuations).lower()
    if stop_word not in stop_words:
        stop_words.add(stop_word)


    unique_words = dict()
    total_words = 0                 #Total words



    line = " "                      #To enter the while loop set line = " " so that it can read line without problem
    while(line != ""):
        line = fopen.readline()     #Read file line by line to save memory
        words = line.split()        #Create a list of words in "line"


        #Frequency Counter
        for word in words:
            
            # Cleaning the words
            word = word.strip(punctuations)
            word = word.lower()     #Converting every word to lowercase 
            if word == "":          #If the word was only a punctuation
                continue


            total_words += 1
            if  word in stop_words:
                continue


            if(word in unique_words):
                unique_words[word] += 1
            else:
                unique_words[word] = 1


    unique_count = len(unique_words)        #Length of the dictionary is equal to no. of unique words 

    # Results
    print(f"{unique_words = }")
    print(f"{unique_count = }")
    print(f"{total_words = }")

    fopen.close()                   #Close the file

finally:
    
    print("Exiting...")
