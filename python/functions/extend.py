'''
Extends lists -> only mutable objects

Immutable objects like Dict -> use update; 
For Str -> Concatenate s3 = s1 + s2
For tuple also create a new tuple t3 = t1 + t2
'''

# For Dict -> Use Update


class Extends():
    def extendList(self, arr1, arr2):
        print(arr1.extend(arr2))  # None
        print(arr1)  # [1, 2, 3, 'a', 'b', 'c']
        print(arr2.extend(arr1))  # None
        print(arr2)  # ['a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c']

    def extendDict(self, dict1, dict2):
        # print(dict1.extend(dict2)) # Dict object has no attribute extend, use update -> throws attributeError
        print(dict1.update(dict2))  # None
        print(dict1)  # {'a': 'apple', 'b': 'ball'}

    def extendStr(self, str1, str2):
        # str1.extend(str2) # Str object has no attribute extend, use concatenate -> throws attributeError
        s3 = str1 + str2
        print(s3)

    def extendTuple(self, tup1, tup2):
        t3 = tup1 + tup2
        print(t3)




a = Extends()
# a.extendList([1, 2, 3], ['a', 'b', 'c'])
a.extendDict({'a': 'apple'}, {'b': 'ball'})
a.extendStr("Hello", "World")
a.extendTuple((1,2,3), (4,5,6))
