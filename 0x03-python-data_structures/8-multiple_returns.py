def multiple_returns(sentence):
    n = 0
    if len(sentence) == 0:
        sentence[0] = None
    for i in range(len(sentence)):
        n += 1
    return (n, sentence[0])

