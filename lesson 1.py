def strcounter(s):
    for sym in s:
        counter = 0
        for sub_sym in s:
            if sub_sym == sym:
                counter += 1
        print(sym, counter)

#strcounter('abacda')
print(set('abacda'))     