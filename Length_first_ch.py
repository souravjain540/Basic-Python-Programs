def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        result = (0, None)
        return result
    else:
        res = (length, sentence[0:1])
        return res

sentence = "At School , I learnt C!"
length , first = multiple_returns(sentence)
print("Length: {:d} - first character: {}".format(length, first))