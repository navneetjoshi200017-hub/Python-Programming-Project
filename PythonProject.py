from text_utils import get_stop_words
from word_counter import count_words
from report import display_report


def main():
    # file_path = "Test.txt"
    file_path = input("Enter file path: ")        
    print("===Text Frequency Counter===")

    stop_word = input("Enter one word to ignore\n(Press Enter to skip): ")

    stop_words = get_stop_words(stop_word)

    try:

        unique_words,total_words = count_words(file_path,stop_words)

    except FileNotFoundError:
        print("\nFile Does Not Exist!!")

    else:
        print("\nFile read successfully!")

        if not unique_words:
            display_report(unique_words,total_words,0)
            return

        while True:
            try:
                limit = int(input("\nEnter the number of top words to display: "))

                if limit <= 0:
                    print("Enter a number greater than zero.")
                    continue
                break
            except ValueError:
                print("Invalid Input. Enter a whole number.")
        display_report(unique_words,total_words,limit)


if __name__ == "__main__":
    main()
