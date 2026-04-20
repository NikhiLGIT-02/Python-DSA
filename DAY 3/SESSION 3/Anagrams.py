def group_anagrams(words):
    group=[]
    for word in words:
        key=" ".join(sorted(word))
        if key not in group:
            group[key]=[]
        group[key].append[word]
    return list(group.values())



words=['tea','ate','team','bin','meat','nib']
result=group_anagrams(words)
print(result)
