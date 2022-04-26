# # string is symmetrical or not
def symmetry(a):
    n = len(a)
    flag = 0

    # Check if the string's length
    # is odd or even
    if n % 2:
        mid = n // 2 + 1
    else:
        mid = n // 2

    start1 = 0
    start2 = mid

    while (start1 < mid and start2 < n):

        if (a[start1] == a[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break

    # Checking the flag variable to
    # check if the string is symmetrical
    # or not
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")


# Driver code
string = 'amaama'
# palindrome(string)
symmetry(string)

# Python program to find Cumulative sum of a list
# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]
#
# Input : list = [4, 10, 15, 18, 20]
# Output : [4, 14, 29, 47, 67]

def cumulative_sum_of_list(n):

    tmp = []
    sum = 0
    for i in range(len(n)):
        sum = sum + n[i]
        tmp.append(sum)

    return tmp

print(cumulative_sum_of_list([4, 10, 15, 18, 20]))

def sorting_of_element(list1, list2):
    # initializing blank dictionary
    f_1 = {}

    # initializing blank list
    final_list = []

    # Addition of two list in one dictionary
    f_1 = {list1[i]: list2[i] for i in range(len(list2))}
    print(f_1)

    # sorting of dictionary based on value
    f_lst = {k: v for k, v in sorted(f_1.items(), key=lambda item: item[1])}
    print(f_lst)

    # Element addition in the list
    for i in f_lst.keys():
        final_list.append(i)
    return final_list


list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

print(sorting_of_element(list1, list2))


# Python program to check if a string is palindrome or not.


def palindrome_string(s):

    tmp =''

    for i in range(1,len(s)+1):
        tmp = tmp + s[-i]
    print(tmp)
    if tmp == s:
        print(s, "THis is palindrome")
    else:
        print(s, "This is not a palindrome")

palindrome_string("PAPA")
palindrome_string("MOM")

# Reverse words in a given String in Python

def reverse_string(s):
    tmp = ''
    for i in range(1,len(s)+1):
        tmp = tmp + s[-i]

    return tmp

print(reverse_string("AMITSAXENA"))

# Ways to remove ith character from string in Python

def remove_nth_element(s, j):
   new_string = ''

   for i in range(len(s)):
       if i != j:
           new_string = new_string + s[i]

   return new_string

print(remove_nth_element("Amit",1))

# Python | Check if a Substring is Present in a Given String

def string_substring(string, substring):

    for i in string.split(" "):
        if i == substring:
            return True


print(string_substring("I Love my india","Lov")
      )

## Python Words Frequency in String Shorthands

def word_frequency(s):

    a = {}

    for i in (s.split(" ")):
        if i not in a:
            a[i] = 1

        else:
            a[i] += 1

    return a

print(word_frequency('Gfg is Gfg'))

def second_largrest(list):

    lar = list[0]
    sec_lar = list[0]

    for i in range(len(list)):
        if list[i] > lar :
            lar = list[i]

    for j in range(len(list)):
        if list[j] > sec_lar and list[j] < lar:
            sec_lar = list[j]

    return sec_lar

print(second_largrest([1,21,100,3,5,6,991,98]))

def palindrome_str(string):
    a = []
    tmp =''
    for i in range(1, len(string)+1):
        a.append(string[-i])

    print(a)

    for j in a:
        tmp = tmp + j

    print(tmp)

    if string == tmp:
        print("Palidnrome")
    else:
        print("Not Pandirome")

#
# palindrome_str("popa")

def fibonacci_srirs(n):
    a = 0
    b = 1

    if n< 1:
        print(a)
    else:
        print(a)
        print(b)
        for j in range(2,n):
            c = a+ b
            a = b
            b =c
            print(c)

fibonacci_srirs(7)

# revrese_number
#
def revrese_number(num):
    a = 0
    tmp = num

    while (num>0):
        rem = num%10
        a = a*10+rem
        tmp = tmp//10

    if tmp == a:
        print("palindorom")
    else:
        print("not")

#
revrese_number(121)

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


def print_triangle(n):

    for i in range(0,n-1):
        for j in range(i):
            #print(j+1,end=' ')
            pass
        print("\n")

print_triangle(5)

# # Second largest number
#
#
#
def second_largest(arr):

    lar = arr[0]
    second = arr[0]

    for i in range (len(arr)):
        if arr[i] > lar:
            lar = arr[i]

    for j in range (len(arr)):
        if arr[j] > second and arr[j] != lar:
            second = arr[j]

    return second


print(second_largest([1,21,31,3,1,3,4,99,100]))


# Max number


def find_max(arr):
    ma = arr[0]

    for i in range (len(arr)):
        if arr[i] > ma:
            ma =arr[i]

    return ma
print(find_max([1,21,31,3,1,3,4,99,100]))

# Min number

def min_num(arr):
    mi = arr[0]

    for i in range (len (arr)):
        if arr[i] < mi:
            mi = arr[i]

    return mi

print(min_num([1,21,31,3,1,3,4,99,100,-1]))

# palindrome number

def palindrome_str(stri):
    tmp = []
    s = ''

    for i in range (1 , len(stri)+1):
        tmp.append(stri[-i])

    for j in tmp:
        s = s+j

    if s == stri:
        print ("yes")
    else:
        print("no")


palindrome_str("amit")
#
#
# # reverse_string
#
#
def reverse_String(string):

    tmp =''

    for i in range(1,len(string)+1):
        tmp =tmp + string[-i]

    return tmp


print(reverse_String("india"))

#
# Fibonacci_series

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(10)


# revrese_number


# Python program to Reverse a number in Python
num = int(input())
rev = 0
while num > 0:
  rem = num % 10  # Finding the remainder
  rev = (rev*10) + rem
  num = num//10  # Finding the quotient
print("%d " %rev)

# Simple Number Triangle Pattern


def triangle(n):
    for i in range(n):
        for j in range(i+1, n):
            # print(j, end=" ")
            pass
        print("\n")

triangle(6)


def triangle_fir(n):

    for i in range(n):

        for j in range(n, i,-1):
            #print(j,end=' ')
            pass
        print("\n")
triangle_fir(5)

def triangle_firrst(n):

    for i in range(n):

        for j in range(n, i,-1):
            #print(j,end=' ')
            pass
        print("\n")
triangle_firrst(5)

def triangle_firrst1(n):

    for i in range(n):

        for j in range(n, i,-1):
            #print(n,end=' ')
            pass
        print("\n")
triangle_firrst1(5)


def triangless(rows):
    for i in range(1, rows):
        for j in range(0, i):
            #print(j,  end=" ")
            pass
        print("\n")


triangless(6)

rows = 6

for row in range(1, rows):

    for column in range(row, 0, -1):

        #print(column, end=' ')
        pass

    print(' ')


# fibonacci Series

def fibonnaci_series(num):
    a = 0
    b = 1
    if num < 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, num):
            c = a + b
            a = b
            b = c
            print(c)

fibonnaci_series(10)

#
# Factorial number


def factorial_num(num):

    tmp = 1

    for i in range(1, num+1):

        tmp = tmp * i

    return tmp

print(factorial_num(4))

# Python program to interchange first and last elements in a list.

def change_first_last_element(lis):

    fir = lis[0]

    length = len(lis)
    las = length-1
    lis[0] = lis[las]
    lis[las] = fir
    print(lis)


change_first_last_element(["A","B","C","D"])

# Python program to swap two elements in a list




# Python  Ways to check if element exists in list


def find_exist_element(num):

    a = []

    for i in num :
        if i not in a:
            a.append(i)
        else:
            print("duplicate element", i)

find_exist_element([1,1,3,4,2,2])

# Python | Reversing a List

def reversing_list(lis):
    a = []
    for i in range(1,len(lis)+1):
        a.append(lis[-i])

    return a

print(reversing_list([1,2,3,4,5]))

# Python | Count occurrences of an element in a list

def occuring_element(lsi):

    count = 0
    tmp =[]

    for i in lsi:

        if i not in tmp:
            tmp.append(i)
        else:
            count += 1

    return count
print(occuring_element([1,2,1,2,3]))

# Multiple occurrences of 3 consecutively occurring elements.

a=int(input("enter the number"))
for i in range(2,a+1,2):
    print(i)
def find_consecutively_occurring_ele(lis):

    length = len(lis)

    for i in range(length-1):
        if len(lis)> i:
            if lis[i] ==lis[i+1] and lis[i+1] == lis[i+2]:

                print(lis[i])

find_consecutively_occurring_ele([1,1,2,3,4,4,7,8,9,9,10,10])

# # symmetric
#
def symmetric_str(s):
    length = len(s)
    flag = 0

    if length %2 != 0:
        mid = length //2 + 1

    else:
        mid = length//2

    start1 = 0
    start2 = mid

    while( start1 < mid and start2 < length):
            if s[start1] == s[start2]:
                    start1 = start1 +1
                    start2 = start2 +1

            else:
                flag = 1
                break

    if flag == 0:
        print("string is symmetric")
    else:
        print("string is not symmetric")

(symmetric_str("AMAAMA"))
(symmetric_str("PAPA"))
(symmetric_str("MOM"))
(symmetric_str("GOAT"))

# Python program to find Cumulative sum of a list
# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]
#
# Input : list = [4, 10, 15, 18, 20]
# Output : [4, 14, 29, 47, 67]

def cumulative_sum(lis):
    sum = 0
    tmp =[]

    for i in range(len(lis)):
        sum = sum + lis[i]
        tmp.append(sum)
    return tmp

print(cumulative_sum([4, 10, 15, 18, 20]))

#
def sorting_of_element(list1, list2):
    # initializing blank dictionary
    f_1 = {}

    # initializing blank list
    final_list = []

    # Addition of two list in one dictionary
    f_1 = {list1[i]: list2[i] for i in range(len(list2))}
    print(f_1)

    # sorting of dictionary based on value
    f_lst = {k: v for k, v in sorted(f_1.items(), key=lambda item: item[1])}
    print(f_lst)

    # Element addition in the list
    for i in f_lst.keys():
        final_list.append(i)
    return final_list
#
def sorting_element(list1,list2):

    tmp = []
    dic = {list1[i] : list2[i] for i in range(len(list2))}
    print(dic)

    dic1 = {k : v for k ,v in sorted(dic.items(),key=lambda  item : item[1])}
    print(dic1)

    for i in dic1.keys():
        tmp.append(i)
    return  tmp

print(sorting_element([4, 10, 15, 18, 20],[0,1,1,1,0]))

#  Python program to check if a string is palindrome or not.

def string_palindrome(s):
    n =len(s)
    s1 = ''

    for  i in range(1,len(s)+1):
        s1 = s1 + s[-i]

    if s1 == s :
        print("palindorm")
    else:
        print("not plaindrome")


string_palindrome("MOM")

#Second largest number



def second_largest(arr):

    lar = arr[0]
    second = arr[0]

    for i in range (len(arr)):
        if arr[i] > lar:
            lar = arr[i]

    for j in range (len(arr)):
        if arr[j] > second and arr[j] != lar:
            second = arr[j]

    return second


print(second_largest([1,21,31,3,1,3,4,99,100]))


# Max number


def find_max(arr):
    ma = arr[0]

    for i in range (len(arr)):
        if arr[i] > ma:
            ma =arr[i]

    return ma
print(find_max([1,21,31,3,1,3,4,99,100]))

# Min number

def min_num(arr):
    mi = arr[0]

    for i in range (len (arr)):
        if arr[i] < mi:
            mi = arr[i]

    return mi

print(min_num([1,21,31,3,1,3,4,99,100,-1]))

# palindrome number
#
def palindrome_str(stri):
    tmp = []
    s = ''

    for i in range (1 , len(stri)+1):
        tmp.append(stri[-i])

    for j in tmp:
        s = s+j

    if s == stri:
        print ("yes")
    else:
        print("no")


palindrome_str("amit")
#
#
# # reverse_string
#
#
def reverse_String(string):

    tmp =''

    for i in range(1,len(string)+1):
        tmp =tmp + string[-i]

    return tmp


print(reverse_String("india"))


# Fibonacci_series

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(10)


# revrese_number


# Python program to Reverse a number in Python
num = int(input())
rev = 0
while num > 0:
  rem = num % 10  # Finding the remainder
  rev = (rev*10) + rem
  num = num//10  # Finding the quotient
print("%d " %rev)

# Simple Number Triangle Pattern


def triangle(n):
    for i in range(n):
        for j in range(i+1, n):
            #print(j, end=" ")
            pass
        print("\n")

triangle(6)


def triangle_fir(n):

    for i in range(n):

        for j in range(n, i,-1):
            #print(j,end=' ')
            pass
        print("\n")
triangle_fir(5)

def triangle_firrst(n):

    for i in range(n):

        for j in range(n, i,-1):
            #print(j,end=' ')
            pass
        print("\n")
triangle_firrst(5)

def triangle_firrst1(n):

    for i in range(n):

        for j in range(n, i,-1):
            #print(n,end=' ')
            pass
        print("\n")
triangle_firrst1(5)


def triangless(rows):
    for i in range(1, rows):
        for j in range(0, i):
            #print(j,  end=" ")
            pass
        print("\n")


triangless(6)

rows = 6

for row in range(1, rows):

    for column in range(row, 0, -1):

        #print(column, end=' ')
        pass

    print(' ')


# fibonacci Series

def fibonnaci_series(num):
    a = 0
    b = 1
    if num < 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, num):
            c = a + b
            a = b
            b = c
            print(c)

fibonnaci_series(10)


# Factorial number


def factorial_num(num):

    tmp = 1

    for i in range(1, num+1):

        tmp = tmp * i

    return tmp

print(factorial_num(4))

# Python program to interchange first and last elements in a list.

def change_first_last_element(lis):

    fir = lis[0]

    length = len(lis)
    las = length-1
    lis[0] = lis[las]
    lis[las] = fir
    print(lis)


change_first_last_element(["A","B","C","D"])


# Python  Ways to check if element exists in list


def find_exist_element(num):

    a = []

    for i in num :
        if i not in a:
            a.append(i)
        else:
            print("duplicate element", i)

find_exist_element([1,1,3,4,2,2])

# Python | Reversing a List

def reversing_list(lis):
    a = []
    for i in range(1,len(lis)+1):
        a.append(lis[-i])

    return a

print(reversing_list([1,2,3,4,5]))

# Python | Count occurrences of an element in a list

def occuring_element(lsi):

    count = 0
    tmp =[]

    for i in lsi:

        if i not in tmp:
            tmp.append(i)
        else:
            count += 1

    return count
print(occuring_element([1,2,1,2,3]))

# Multiple occurrences of 3 consecutively occurring elements.

a=int(input("enter the number"))
for i in range(2,a+1,2):
    print(i)
def find_consecutively_occurring_ele(lis):

    length = len(lis)

    for i in range(length-1):
        if len(lis)> i:
            if lis[i] ==lis[i+1] and lis[i+1] == lis[i+2]:

                print(lis[i])

find_consecutively_occurring_ele([1,1,2,3,4,4,7,8,9,9,10,10])


a = [['A', 34], ['B', 21], ['C', 26]]
for i in range(0, len(a)):
    for j in range(0, len(a) - i - 1):
        if (a[j][1] > a[j + 1][1]):
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

print(a)










