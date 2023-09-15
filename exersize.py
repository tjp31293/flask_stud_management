#Maximum product of two integers
def max_product(arr):
    arr.sort()
    return max(arr[-1] * arr[-2], arr[0] * arr[1])

# Example usage:
my_list = [1, 2, 3, 10, 5, 6, 7]
print("Maximum product of two integers:", max_product(my_list))
'''
my_list.sort()
print(max(my_list[-1] * my_list[-2], my_list[0] * my_list[1]))

'''
#=======================================================
print("*" * 1)
#Find the Second Largest Element in a List:
my_list = [12, 45, 2, 41, 31, 10, 8, 6]
my_list.sort()
print(my_list)
print("Second largest ele",my_list[-2])

#==========================================
print("*" * 2)
#Remove Duplicates from a List:(not use set)
list1 = [1,3,4,6,2,3,4,5,6,7]
print(list1)
list2 = list(set(list1))
print("list using set",list2)
x2 = []
for x in list1:
    if x not in x2:
        x2.append(x)
print("list without set",x2)
#==========================================
print("*" * 3)
#Check if a List is Palindrome:
my_list = [1,2,3,2,1]
x = my_list[::-1]
if my_list == x:
    print("list is palindrome")
else:
    print("list is not palindrome")

#==========================================
print("*" * 4)
#Find the Intersection of Two Lists:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
x = set(list1)
y = set(list2)
print(list(x.intersection(y)))

#==========================================
print("*" * 5)
#Count the Frequency of Elements in a List:
my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
freq ={}
for item in my_list:
    if item in freq:
        freq[item] = freq[item] +1
    else:
        freq[item] = 1
print(freq)
for key ,value in freq.items():
    print(key,":",value)
print("*" * 10)


print(" ================ Tuple================")
########### Tuple
#Find the Index of an Element in a Tuple:
my_tuple = (1,2,3,4,5)
print(my_tuple.index(3))


#==========================================
print("*" * 1)
#Count the Occurrences of an Element in a Tuple:
my_tuple = (1,2,3,4,5,3,6,7,8,3)
print(my_tuple.count(3))


#==========================================
print("*" * 2)
#Concatenate Two Tuples:
tuple1 = (1,2,3)
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)

#==========================================
print("*" * 3)
#Check if a Tuple Contains Duplicate Elements:
my_tuple = (1,2,3,3,5,6,2,4)
#my_tuple = (1,2,3)
set1 = set(my_tuple)
if len(my_tuple) == len(set1):
    print("Tuple not contain duplicate value")
else:
    print("Tuple contain duplicate value")

#==========================================
print("*" * 4)
#Find the Minimum and Maximum Values in a Tuple:
my_tuple = (1, 5, 2, 8, 3)
max_value = max(my_tuple)
min_value = min(my_tuple)
print("maximum value:- ",max_value)
print("minimum value:- ",min_value)

#==========================================
print("*" * 5)
#Swapping Values of Two Variables Using Tuples:
a = 5
b = 10
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)


#==========================================
print("*" * 6)
# Concatenate Tuples:
def concatenate_tuples(*tuples):
    return tuple(item for tpl in tuples for item in tpl)
# Example usage:
tuple1 = (1, 2)
tuple2 = (3, 4)
tuple3 = (5, 6)
concatenated = concatenate_tuples(tuple1, tuple2, tuple3)
print("Concatenated tuple:", concatenated)
'''
for item in tuples
tuples :- ((1,2)(3,4)(5,6))
'''
#==========================================
#Convert a List of Tuples to a List of Elements:
my_tup = [(2,1),(3,4),(5,6)]
x = []
for item in my_tup:
    for ele in item:
        x.append(ele)
print(x)

# ============ SET ========================
print(" ***********  SET ****************")
#Remove Duplicates from a List using Sets:
l1 = [1, 2, 2, 3, 4, 4, 5]
print(list(set(l1)))
#===================
print("================")
print("example:-2")
#Find the Intersection of Two Sets:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
result = set1.intersection(set2)
print(result)
#===================
print("================")
print("example:-3")
#Check if a Set is a Subset of Another Set:
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))
#===================
print("================")
#Calculate the Union of Multiple Sets:
print("example:-4")
x = {1, 2, 3}
y = {3, 4, 5}
z = {5, 6, 7}
x.update(y)
x.update(z)
print(x)
#==========================
#Remove Common Elements from Two Sets:
print(" example:-4 ================ ")
def remove_common_elements(set1, set2):
    return set1.difference(set2)

# Example usage:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
result_set = remove_common_elements(set1, set2)
print(result_set)
