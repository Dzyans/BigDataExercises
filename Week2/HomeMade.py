import json

def get_count_sorted_bag_of_words(filename, key):
    with open(filename) as data_file:
        data = json.load(data_file)

    word_dict = {}
    word_counts = 0
    for x in data:
        word_str = x.get(key)

        ##trim out commas and periods etc etc
        word_str = trim_string(word_str)

        word_list = word_str.split(' ')

        word_counts = word_counts + len(word_list) ## total number of words
        for word in word_list:
            # print(word)
            if word in word_dict:
                if word == '':
                    break  ##ignore lefter over blank sapaces
                ##increment word count
                value = word_dict[word]
                value += 1
                word_dict[word] = value
            else:
                word_dict[word] = 1
    # print(word_counts)
    # print("worddict lenght " + str(len(word_dict)))

    new_word_dict = dict(word_dict)
    for key, value in new_word_dict.items():
        if not value > 8:
            del word_dict[key]

    return sorted(word_dict.keys(), key=lambda item: word_dict[item])


def trim_string(word_str):
    word_str = word_str.replace(',', '') \
        .replace('.', '') \
        .replace('!', '') \
        .replace('?', '') \
        .replace('\n', ' ') \
        .replace(')', '') \
        .replace('(', '')
    return word_str


bag_of_words = get_count_sorted_bag_of_words("pizza-train.json", "request_text")
print(bag_of_words)
print(len(bag_of_words))