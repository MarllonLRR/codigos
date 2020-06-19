###################################
#!/usr/bin/env python3           
# -*- coding: utf-8 -*-
# developed by: Marllon Rodrigues 
###################################

def is_valid_position(word, position):
    return len(word) > position

def is_letter(word, position):
    # Checks whether the position of my string i'm accessing is valid
    # and if the character i'm accessing is a letter
    return is_valid_position(word, position) and word[position].isalpha() 	

def get_hashtag(word):
    hashtag = "#"
    i = 1
    # If char in 'i' is letter
    while(is_letter(word, i)):
        hashtag += word[i]
        i += 1

    if(len(hashtag) > 1): # return hashtag if it is valid
        return hashtag.lower()
    else:
        return ""

def get_hashtags(phrase):
    list_words = phrase.split()
    list_hashtags = []

    for word in list_words:
        if word[0] == '#':
            hashtag = get_hashtag(word)
            if hashtag: # if hashtag is valid i attach in my list of hashtags
                list_hashtags.append(hashtag)

    return list_hashtags

def insert_phase(phrase,list_phrase, list_hashtags, list_count_hashtags):
    list_phrase.append(phrase) # Insert sentence in the list
    list_phrase_hashtags = get_hashtags(phrase) # Takes all the hashtags in the sentence

    # For each value in the list of hashtags do:
    for hashtag in list_phrase_hashtags:
        
        # If i have my hashtag in my list
        if hashtag in list_hashtags: 
            index = list_hashtags.index(hashtag)
            list_count_hashtags[index] += 1
        else:
            list_hashtags.append(hashtag)
            list_count_hashtags.append(1)


def show_hashtags(list_hashtags, list_count_hashtags):
    for i in range(len(list_hashtags)):
        print("{} {}".format(list_hashtags[i], list_count_hashtags[i]))

def show_phrase_hashtag(hashtag, list_phrase):
    for phrase in list_phrase:
        list_hashtags = get_hashtags(phrase)

        if hashtag in list_hashtags:
            print(phrase)

def main():
    n_cases = int(input())

    # For each case
    for i in range(n_cases):
        
        list_phrase = []
        list_hashtags = []
        list_count_hashtags = []

        # whitespace input
        read_on = True
        space = input()

        # For each case
        while(read_on):
            line_input = input()

            if(line_input[0] == 'I'): # Insert post
                insert_phase(line_input[2:], list_phrase, list_hashtags, list_count_hashtags)

            if(line_input[0] == 'L'): # Show count hashtags
                show_hashtags(list_hashtags, list_count_hashtags)
                
            if(line_input[0] == 'P'): # Shows the posts containing the hashtag
                hashtag = get_hashtag(line_input[2:])
                # if it is a valid hashtag
                if hashtag:
                    show_phrase_hashtag(hashtag, list_phrase)

            if(line_input[0] == 'F'): # Exit case
                print() # Print break line
                read_on = False

if __name__ == '__main__':
    main()
