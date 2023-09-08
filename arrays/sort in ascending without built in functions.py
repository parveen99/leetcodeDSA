class Sort:
    def ascending_sort(self, arr):
        for i ,num1 in enumerate(arr):
            for j, num2 in enumerate(arr, i+1):
                if(num1> num2):
                    num1, num2 = num2, num1 
        return arr

n = Sort()

print(n.ascending_sort([8, 5, 4, 3, 2, 1]))
