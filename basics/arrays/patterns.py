#regular rectangular pattern - Pattern 1

'''
* * * *  
* * * *  
* * * *  
* * * * 
'''

def print_rectangular_pattern(num):
    for i in range(0,num):
        for j in range(0,num):
            print("*", end = " ")
        print(" ")


# print_rectangular_pattern(4)

#right angled triangle pattern

'''
*
* *
* * *
* * * *
'''
def print_right_angled_triangle_pattern(num):
    for i in range(0, num):
        for j in range(0, i):
            print("*", end=" ")
        print("*")

# print_right_angled_triangle_pattern(4)


'''
1 
1 2 
1 2 3 
1 2 3 4 
'''

def print_right_angled_numbers(num):
    for i in range(0, num):
        for j in range(1, i):
            print(j, end=" ")
        print()

# print_right_angled_numbers(6)

'''
1 
2 2 
3 3 3 
4 4 4 4 
'''

def print_right_angled_numbers_2(num):
    for i in range(0, num):
        for j in range(0, i+1):
            print(i+1, end=" ")
        print()


# print_right_angled_numbers_2(4)


'''
* * * * 
* * * 
* * 
* 
'''
def inverted_right_pyramid(num):
    for i in range(num, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()

# inverted_right_pyramid(4)


'''
    *     
  * * *   
* * * * * 
'''
def print_star_pyramid(num):
    for i in range(0, num):
        for j in range(0, num-i-1):
            print(" ", end=" ")
        for j in range(0, (2*i)+1):
            print("*", end=" ")
        print()


print_star_pyramid(6)


def print_inverted_star_pyramid(num):
    for i in range(0,num):
        for j in range(0, i):
            print(" ", end = " ")
        for j in range(0, (2*num)-2*(i+1)+1):
            print("*", end=" ")
        print()

#print_inverted_star_pyramid(6)








# Online Python - IDE, Editor, Compiler, Interpreter


'''
        *         
      * * *       
    * * * * *     
  * * * * * * *   
* * * * * * * * * 
* * * * * * * * * 
  * * * * * * *   
    * * * * *     
      * * *       
        * 

'''
    
def pattern_1(num):
    for i in range(0, num):
        for space in range(0, num-i-1):
            print(" ", end = " ")
        for star in range(0, (2*i)+1):
            print("*", end = " ")
        for space in range(0, num-i-1):
            print(" ", end = " ")
        print()
    
def pattern_2(num):
    for i in range(0, num):
        for space in range(0, i):
            print(" ", end = " ")
        
        for star in range(0, ((2*num)-((2*i)+1))):
            print("*", end = " ")
            
        for space in range(0, i):
            print(" ", end = " ")
            
        print()
        
pattern_1(5)
pattern_2(5)

print()

n = 3
row = '*'
while n > 0:
    print("|" * (n-1) + row)
    row = row + '**'
    n = n -1
