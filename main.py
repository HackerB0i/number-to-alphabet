"""
thing for decoding matrices. top 10 most useless script
"""

import string

askfornumber = True
numberlist = []
characters = ["0", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
while askfornumber:
    number = input("number: (s to stop) | ")
    if (number == "s"):
        askfornumber = False
    else:
        numberlist.append(number)

print("your generated text is below:")
text = ""
for i in range(len(numberlist)):
    text = text + characters[int(numberlist[i])]

print(text)