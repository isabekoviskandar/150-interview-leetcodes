def hIndex(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
    return h

citations = [3,0,6,1,5]

print(hIndex(citations))
#output must be 1