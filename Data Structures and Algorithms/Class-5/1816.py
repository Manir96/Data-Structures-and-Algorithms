# import keyword
# import signal


def truncateSentence(s, k):
    split_s = s.split()
    return " ".join(split_s[0:k])


print(truncateSentence("Hello how are you Contestant",5))

# def truncateSentence(s, k):
#     split_s = s.split()
#     return " ".join(split_s[0:k])


# print(truncateSentence("Hello how are you Contestant", 5))