class Sort:  
    def descending_sort(self,arr):
        for i ,num1 in enumerate(arr):
            for j, num2 in enumerate(arr, i+1):
                if(num1< num2):
                    num1, num2 = num2, num1 
        return arr

n = Sort()

print(n.descending_sort([8, 5, 1, 3, 7, 1]))
