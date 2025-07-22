def romanToInt(s):
    mapp = {"I":1,"V":5,"X":10,'L':50,'C':100,'D':500, 'M':1000}
    n = len(s)
    i = 1
    summ = 0
    if(n == 1):
        return mapp[s[0]]
    while (i < n):
        if(mapp[s[i-1]] >= mapp[s[i]]):
            summ = summ + mapp[s[i-1]]
            i += 1
        else:
            summ = summ + (mapp[s[i]] - mapp[s[i-1]])
            i += 2
        if( i == n):
            summ = summ + mapp[s[n-1]]
    return summ




print(romanToInt("D"))