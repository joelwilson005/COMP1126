# COMP1126 Lab 4
# Joel Wilson
# 620098136
# October 10, 2022

# -----------------------------------------------------------------------------------------------
# Problem 1
# -----------------------------------------------------------------------------------------------
def removePun(message):
    """Function which removes the following punctuations (“,”,“.”,“?”,“!”,
“;”,“:”)"""
    newMessage = ""

    for i in message:
        if i not in (",",".","?","!",";",":"):
            newMessage += i
    return newMessage

# -----------------------------------------------------------------------------------------------
# Problem 2
# -----------------------------------------------------------------------------------------------
def encode(s):
    if s == '':
        return ''
    else:
        return chr(ord(s[0])+5)+ encode(s[1:])

def decode(s):
    if s == '':
        return ''
    else:
        return chr(ord(s[0]) -5) + decode(s[1:])

# -----------------------------------------------------------------------------------------------
# Problem 3
# -----------------------------------------------------------------------------------------------
def stringList(str1):
    return str1.split()

def encodeM(lst):
    if lst == []:
        return []
    else:
        return [encode(lst[0])] + encodeM(lst[1:])

def decodeM(lst):
    if lst == []:
        return []
    else:
        return [decode(lst[0])] + decodeM(lst[1:])

def main(s):
    slst = removePun(s)
    eList = encodeM(stringList(slst))
    dList = decodeM(eList)
    print(f"Given string => {s}")
    print(f"Punctuation removed => {slst}")
    print(f"List Encoded => {eList}")
    print(f"List Decoded => {dList}")
    print("Encoded Message", ' '.join(eList))
main("COMP1126!! is a, : lot of, fun?")
