def arrayStringsAreEqual(word1, word2):
    
    join_word1 = "".join(word1)
    join_word2 = "".join(word2)

    if join_word1 == join_word2:
        return True
    else:
        return False


print(arrayStringsAreEqual(["ab", "ccmdk"], ["ab", "ccmdk"]))