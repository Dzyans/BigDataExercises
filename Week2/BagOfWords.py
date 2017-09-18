import json

def get_bag_of_words(filename, key):
    with open(filename) as data_file:
        data = json.load(data_file)

    word_dict = {}
    word_counts = 0
    for x in data:
        word_str = x.get(key)

        ##trim out commas and periods etc etc
        word_str = word_str = trim_string(word_str)

        word_list = word_str.split(' ')

        word_counts = word_counts + len(word_list)
        for word in word_list:
            #print(word)
            if word in word_dict:
                if word == '':
                    break ##ignore lefter over blank sapaces
                ##increment word count
                value = word_dict[word]
                value += 1
                word_dict[word] = value
            else:
                word_dict[word] = 1
    #print(word_counts)
    #print("worddict lenght " + str(len(word_dict)))

    ##now create an actual word bag, iteration again :(
    bag_of_words = []
    counter = 0
    for x in data:
        string_count_list = []
        word_str = x.get("request_text")


        word_str = trim_string(word_str) #trim out commas and periods etc etc

        word_list = word_str.split(' ') # split the words into a list

        for dict_word, word_count in word_dict.items():
            #print(dict_word)
            if dict_word in word_list:
                amount = word_list.count(dict_word)
                string_count_list.append(amount)
            else:
                string_count_list.append(0)

        bag_of_words.append(string_count_list)
        ##print("one line done")
        counter = counter+1
        togo = str(4040 - counter)
        if counter%100 == 0:
            print("another 100 lines done " + togo + " lines to go")
        if counter % 1000 == 0:
            print("another 1000 lines done " +togo + " lines to go")
    #print(len(word_dict))
    #print(len(bag_of_words))
    return bag_of_words


def trim_string(word_str):
    word_str = word_str.replace(',', '') \
        .replace('.', '') \
        .replace('!', '') \
        .replace('?', '') \
        .replace('\n', ' ') \
        .replace(')', '') \
        .replace('(', '')
    return word_str

#run the method to get the bag of words
bag_of_words = get_bag_of_words("pizza-train.json", "request_text")

#print(bag_of_words)
for w_list in bag_of_words:
    print(w_list)
