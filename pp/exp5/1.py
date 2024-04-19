
list1 = [1, 2, 3, 'apple', 'banana', 'orange']

list2 = ['jackfruit', 'cherry']

# concatenation

list3 = list1 + list2
print(f"After concatenation {list3}")

# indexing

print(f"\nindex of jackfruit is {list3.index('jackfruit')}")

#accessing

print(f"\nThe element at index 3 in list3 is {list3[3]}")

#pop()

print(f"\nusing the pop function on index 1 , result is :- {list3.pop(1)}")

#insert()

list3.insert(3,"mango")
print(f"list3 after inserting 'mango' :\t {list3}")

# remove()

list3.remove("mango")
print(f"list3 after removing 'mango' :\t {list3}")

# reverse()

list3.reverse()
print(f"list3 after reversing :\t {list3}")

# append()

list3.append("mango")
print(f"list3 after appending 'mango' :\t {list3}")

# sort()

list2.sort()
print(f"list2 after sorting in ascending order :\t {list2}")

list2.sort(reverse=True)
print(f"list2 after sorting in descending order :\t {list2}")

'''
Output :-

@adityababar07 ➜ /workspaces/sy-pp- (master) $ python pp/exp5/1.py
After concatenation [1, 2, 3, 'apple', 'banana', 'orange', 'jackfruit', 'cherry']

index of jackfruit is 6

The element at index 3 in list3 is apple

using the pop function on index 1 , result is :- 2
list3 after inserting 'mango' :  [1, 3, 'apple', 'mango', 'banana', 'orange', 'jackfruit', 'cherry']
list3 after removing 'mango' :   [1, 3, 'apple', 'banana', 'orange', 'jackfruit', 'cherry']
list3 after reversing :  ['cherry', 'jackfruit', 'orange', 'banana', 'apple', 3, 1]
list3 after appending 'mango' :  ['cherry', 'jackfruit', 'orange', 'banana', 'apple', 3, 1, 'mango']
list2 after sorting in ascending order :         ['cherry', 'jackfruit']
list2 after sorting in descending order :        ['jackfruit', 'cherry']
@adityababar07 ➜ /workspaces/sy-pp- (master) $ 
'''