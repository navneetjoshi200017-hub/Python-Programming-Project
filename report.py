
def get_frequency(item):
    return item[1]


def get_top_words(unique_words, limit):
    word_list = list(unique_words.items())
    sorted_words = sorted(
        word_list,
        key = get_frequency,
        reverse = True
    )

    top_words = sorted_words[:limit]
    return top_words

def display_report(unique_words, total_words, limit = 5):
    counted_words = sum(unique_words.values())

    print("\n"+ "="*51)
    print(" "*13+"WORD FREQUENCY REPORT")
    print("="*51)

    print(f"\nTotal words (including stop words) : {total_words}")
    print(f"Words after removing stop words    : {counted_words}")
    print(f"Total unique words                 : {len(unique_words)}")

    if not unique_words:
        print("\nNo non-stop unique words to display.")
        return

    top_words = get_top_words(unique_words,limit)
    rank = 1
    print(f"\nTop {len(top_words)} words: ")

    print("-"*55)
    print(f"{'Rank':<6}{'Word':<25}{'Frequency':>10}{'Percentage':>12}")
    print("-"*55)
    for item in top_words:
        word = item[0]
        frequency = item[1]

        percentage = frequency / counted_words * 100
        print(f"{rank:<6}{word:<25}{frequency:>10}{percentage:>11.2f}%")

        rank += 1

    print("-"*55)