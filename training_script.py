import numpy as np
import pandas as pd
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

# motanaby = pd.read_csv("E:\\AAAAAAAAAAAAAAAAAAAA\\projects\\lstmTest\\all_poems.csv")

# print(motanaby.get("poem_text")[1])

# chars = ['ع', 'ي', 'ن', 'ا', 'ك', ' ', 'غ', 'ب', 'ت', 'خ', 'ل', 'س', 'ة', 'ح', 'ر', 'و', 'ش', 'ف', 'ه', 'م', 'ق', 'ص',
#          'ض', 'ء', 'ج', 'ذ', 'د', 'ظ', 'ط', 'ث', 'ز']
# print(len(chars))
#
# chars_to_n = {'ع': 0, 'ي': 1, 'ن': 2, 'ا': 3, 'ك': 4, ' ': 5, 'غ': 6, 'ب': 7, 'ت': 8, 'خ': 9, 'ل': 10, 'س': 11,
#               'ة': 12, 'ح': 13, 'ر': 14, 'و': 15, 'ش': 16, 'ف': 17, 'ه': 18, 'م': 19, 'ق': 20, 'ص': 21, 'ض': 22,
#               'ء': 23, 'ج': 24, 'ذ': 25, 'د': 26, 'ظ': 27, 'ط': 28, 'ث': 29, 'ز': 30}
#
# n_to_chars = {0: 'ع', 1: 'ي', 2: 'ن', 3: 'ا', 4: 'ك', 5: ' ', 6: 'غ', 7: 'ب', 8: 'ت', 9: 'خ', 10: 'ل', 11: 'س',
#               12: 'ة', 13: 'ح', 14: 'ر', 15: 'و', 16: 'ش', 17: 'ف', 18: 'ه', 19: 'م', 20: 'ق', 21: 'ص', 22: 'ض',
#               23: 'ء', 24: 'ج', 25: 'ذ', 26: 'د', 27: 'ظ', 28: 'ط', 29: 'ث', 30: 'ز'}


# ----------------------------------------------------------------------------------

allPoems = open("motanabyAndOthers.txt", "r",  encoding="utf-8")
allPoemsStr = allPoems.read()
ep = 150

characters = sorted(list(set(allPoemsStr)))

n_to_chars = {n:char for n, char in enumerate(characters)}
chars_to_n = {char:n for n, char in enumerate(characters)}
print(characters)
print(chars_to_n)
print(n_to_chars)

X = []
Y = []
seqLen = 30
lenOfTxt = len(allPoemsStr)


for i in range(0,lenOfTxt-seqLen):
    currentSeq = allPoemsStr[i:i+seqLen]
    rightGuess = allPoemsStr[i+seqLen]
    X.append([chars_to_n[char] for char in currentSeq])
    Y.append(chars_to_n[rightGuess])


''' reshaping data for the LSTM input'''
print(Y)
reshapedX = np.reshape(X, (len(X), seqLen, 1))
reshapedX = reshapedX / float(len(characters))
print(reshapedX.shape)
reshapedY = np_utils.to_categorical(Y)
print(reshapedY.shape)

'''making the model'''
fileName = 'motanaby4.h5'
checkpoint = ModelCheckpoint("Best_"+fileName, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]

modelP = Sequential()
modelP.add(LSTM(128, input_shape=(reshapedX.shape[1], reshapedX.shape[2]), return_sequences=True))
modelP.add(Dropout(0.0))
modelP.add(LSTM(128, return_sequences=True))
modelP.add(Dropout(0.0))
modelP.add(LSTM(128, return_sequences=True))
modelP.add(Dropout(0.0))
modelP.add(Flatten())
modelP.add(Dense(reshapedY.shape[1], activation='softmax'))
modelP.compile(loss='categorical_crossentropy', optimizer='adam')
print(reshapedX.shape[1], reshapedX.shape[2])
print(reshapedY.shape[1])
modelP.fit(reshapedX, reshapedY, epochs=ep, batch_size=100, callbacks=callbacks_list)
modelP.save(fileName)


'''testing the model'''
testCase = X[3]

for i in range(seqLen):
    fitTestCase = np.reshape(testCase, (1, len(testCase), 1))
    fitTestCase = fitTestCase / float(len(characters))
    prediction = np.argmax(modelP.predict(fitTestCase, verbose=0))
    seq = [n_to_chars[n] for n in testCase]
    testCase.append(prediction)
    testCase = testCase[1:len(testCase)]

unparsedTxt = [n_to_chars[val] for val in testCase]
txt = ''
for char in unparsedTxt:
    txt += char
print(txt)
print(unparsedTxt)

# for poem in motanaby.get("poem_text"):
#
#     if isinstance(poem, str) and len(poem) > 20:
#         for letter in str(poem):
#             if letter in chars:
#                 allPoems.write(letter)
#         allPoems.write(" ")

# counter = 0
# for char in chars:
#     chars_to_n[char] = counter
#     n_to_chars[counter] = char
#     counter += 1
#
# print(chars_to_n)
# print(n_to_chars)