# import pandas as pd
#
#
# motanaby = pd.read_csv("all_poems.csv")
#
# print(motanaby.get("poem_text")[1])
#
# allPoemsStr = ""
#
# for poem in motanaby.get("poem_text"):
#     allPoemsStr += str(poem) + " "
#
# print("done")
# characters = list(set(allPoemsStr))
# n_to_chars = {n: char for n, char in enumerate(characters)}
# chars_to_n = {char: n for n, char in enumerate(characters)}
#
# print(characters)
# print("\n\n")
# print(n_to_chars)
# print("\n\n")
# print(chars_to_n)
# print("\n\n")
# print(len(characters), len(n_to_chars), len(chars_to_n))
#
# f = open("allPoemsAllchars.txt", "w")
# f.write(allPoemsStr)

# --------------------------------------------------------------

import codecs


chars = ['إ', 'ط', 'ز', 'ر', 'ا', 'ظ', 'ى', 'ص', 'د', 'غ', 'ه', 'أ', 'ي', 'ئ', ' ', 'ت', 'و', 'م', 'ذ', 'آ', 'ش', 'ك',
         'ن', 'ج', 'ؤ', 'ع', 'ف', 'ق', 'ض', 'خ', 'ة', 'ء', 'ب', 'س', 'ح', 'ل', 'ث', '\n']

print(chars)

if input("file or input? ").lower() == "file":

    allPoems = open("multiplePoets.txt", "r",  encoding="utf-8")
    allPoemsStrUnparsed = allPoems.read()
    allPoemsStr = ""

    for letter in allPoemsStrUnparsed:
        if letter in chars:
            allPoemsStr += letter


    characters = list(set(allPoemsStr))
    n_to_chars = {n: char for n, char in enumerate(characters)}
    chars_to_n = {char: n for n, char in enumerate(characters)}

    f = codecs.open("multiplePoetsParsed.txt", "w", "utf-8")
    f.write(allPoemsStr)

    print(characters)
    print("\n\n")
    print(n_to_chars)
    print("\n\n")
    print(chars_to_n)
    print("\n\n")
    print(len(characters), len(n_to_chars), len(chars_to_n))

else:
    allPoemsStrUnparsed = '''	
دَنا البَينُ مِن أَروى فَزالَت حُمولُها
لِتَشـغَـلَ أَروى عَن هَواهـا شُغـولُها
2
وَما خِفتُ مِنها البَينَ حَتّى تَزَعزَعَت
هَـمــاليـجُهـا وَاِزوَرَّ عَنّـي دَليلُهـا'''
    allPoemsStr = ""

    for letter in allPoemsStrUnparsed:
        if letter in chars:
            allPoemsStr += letter
    print(allPoemsStr)
    print(len(allPoemsStr))


# --------------------------------------------------------------


print(len(chars))
