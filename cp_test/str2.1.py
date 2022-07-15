# anagram detector in a sentence
def anagram(sentence):
    d = {} # needs to make it robust

    for word in sentence.split(' '): # group words according to the sign
        s = ''.join(sorted(word)) # calculate the sign
        if s in d:
            d[s].append(word) # append it to the existing signature group
        else:
            d[s] = [word]
    return [d[s] for s in d if len(d[s])>1]

sentence = "below the car is a rat drinking cidar and bending its elbow while this thing is an arc that can act like a cat which cried during the night caused by pain in its bowel"
print(anagram(sentence))
