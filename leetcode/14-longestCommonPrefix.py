def longestOptimal(strs):
    val = min(len(i) for i in strs)
    for i in range(val):
        for word in strs:
            

    # for i in range()


strs = ["flower", "flow", "flight"]
res = longestOptimal(strs)
print(res)
