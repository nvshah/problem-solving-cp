
words = ['hello', 'gothca', 'on']
lr = zip(range(len(words)), words, reversed(words))
for i, w, rw in lr:
    print(i, w, rw)