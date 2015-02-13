
__author__ = 'Andrew'

from itertools import cycle
import time
import itertools


def get_letter_phonetics():
    f = open("letter_sounds.txt", "r")
    text = f.read()
    lines = text.split("\n")
    phonetics = {}
    for line in lines:
        l = line.split("=")
        phonetics[l[0]]=l[1]

    return phonetics

def get_dictionary_words():
    f = open("dictionary_short.txt")
    text = f.read()
    lines = text.split("\n")
    words = []
    for line in lines:
        words.append(line)
    return words



print "Processing words"
letter_phonetics = get_letter_phonetics()
words = get_dictionary_words()
word_phonetics =[]
for word in words:
    if len(word) > 6:
	break
    str = ""
    word = word.lower()
    letters = list(word)
    i = 0
    tmp = len(letters)
    while i < len(letters):
        if i == len(letters)-1:
            str = str+letter_phonetics[letters[i]]+"|"
            break
        tmp_key = []
        tmp_key.append(letters[i])
        done = False
        # base case
        str_tmp = "".join(tmp_key)
        while not done and i < len(letters)-1:
            tmp = tmp_key
            tmp.append(letters[i+1])
            k = "".join(tmp)
            if k in letter_phonetics:
                l = letters[i+1]
                str_tmp = "".join(tmp)
                tmp_key.append(l)
                i += 1
            else:
                done = True
                i += 1

                # letter_itr.pr

        str = str+letter_phonetics[str_tmp]+"|"
    #
    #
    #
    # #
    #
    # print('The word {0} took {1} to process'.format(word,stop-start))
    # print(format("time taken on word {0}: {1}", word stop-start))
    #
    # letter_itr = cycle(letters)
    # for letter in letter_itr:
    #     tmp_key = []
    #     tmp_key.append(letter)
    #     done = False
    #     str_tmp = ""
    #     #ok, so here we're getting the spelling that matches the phonetics eau in beautiful for example
    #     while not done:
    #         tmp = tmp_key
    #         str_tmp = "".join(tmp)
    #         tmp_iter =letter_itr
    #         tmp.append(tmp_iter.next())
    #         k = "".join(tmp)
    #         if k in letter_phonetics:
    #             l = next(letter_itr)
    #             str_tmp = "".join(tmp)
    #             tmp_key.append(l)
    #         else:
    #             done = True
    #             # letter_itr.pr

        #now that we have our key
        # str = str+letter_phonetics[str_tmp]+"|"
    str=str[:-1]
    word_phonetics.append(str+"="+word)

print("done")
finished_dictionary = []
for item in word_phonetics:
    if len(item.split("=")[1]) > 6:

        break
    t=item.split("=")
    outcomes = t[0].split("|")
    first_letters = outcomes[0].split(",")
    final = []
    for l in first_letters:
        tmp = []
        tmp.append("/"+l+"/")
        final.append(tmp)

    first_letters=tmp

    i = 1
    container = []
    while i < len(outcomes):
        container = itertools.product(first_letters, outcomes[i].split(","))
        # for selection in outcomes[i].split(","):
        #     for l in final:
        #         l.append("/"+selection+"/")
        tmp_container=[]
        for it in container:
            tmp_container.append("+/".join(it)+"/")
        first_letters = tmp_container
        i += 1

    for f in first_letters:
        f = f+"="+t[1]
        finished_dictionary.append(f)
    print ('Finished processing word: {0}'.format(item.split("=")[1]))

print ("Now we're done?")


with open("words.txt", "a") as myfile:
    for i in finished_dictionary:
        myfile.write(i+"\n")









    # while i <len(letters):
        # if len(letters) == 1:
        #     break
        # stop = False
        # key = letters[i]
        # while not stop:
        #     if i+1 < len(letters):
        #         if join(letters[i:i+2]) in letter_phonetics:
        #             key =












