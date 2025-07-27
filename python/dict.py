data = {
    'zebra': 5,
    'apple': 3,
    'banana': 5,
    'cherry': 2,
    'delta': 3,
    'echo': 1,
    'alpha': 3
}



val = sorted(data.items(), key=lambda item:item[1], reverse=True)
print(val)