def countConsistency(allowed,words):
    allowed_set=set(allowed)
    count=0
    for word in words:
        consistent= True

        for ch in word:
            if ch not in allowed_set:
                consistent=False
                break
            if consistent:
                count+=1
        return count


#Main
allowedString = "ab"
words=["ad","bd","aaab","badab"]  #1
print(countConsistency(allowedString,words))
