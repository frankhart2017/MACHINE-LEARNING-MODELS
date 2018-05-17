# Bag of Words Model

import  operator
import numpy as np

class bow:
    
    def fit(self, X, features = -1):
        unique_words = []
        if(features == -1):
            for i in range(len(X)):
                for word in X[i].split():
                    if word not in unique_words:
                        unique_words.append(word)
                print("Scanned sentence number: " + str(i+1))
        else:
            word_weights = {}
            for i in range(len(X)):
                for word in X[i].split():
                    if word in word_weights:
                        word_weights[word] += 1
                    else:
                        word_weights[word] = 1
                print("Scanned sentence number: " + str(i+1))
            sorted_word = sorted(word_weights.items(), key=operator.itemgetter(1), reverse = True)
            for i in range(features):
                unique_words.append(sorted_word[i][0])
        bag_of_words = np.zeros((len(X), len(unique_words)))
        for i in range(len(X)):
            for x in X[i].split():
                if(x in unique_words):
                    bag_of_words[i][unique_words.index(x)] = 1
        print("Done!")
        return bag_of_words