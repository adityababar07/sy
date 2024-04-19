list1 = [1, 2, 3, 'apple', 'banana', 'orange']
list2 = ['jackfruit', 'cherry']

# Concatenation: Combining two lists
list3 = list1 + list2
print(f"After concatenation: {list3}")

# Indexing: Finding the index of a specific element
print(f"\nIndex of 'jackfruit' is {list3.index('jackfruit')}")

# Accessing: Retrieving an element by index
print(f"\nThe element at index 3 in list3 is {list3[3]}")

# Pop: Removing and returning an element by index
print(f"\nUsing the pop function on index 1, result is: {list3.pop(1)}")

# Insert: Adding an element at a specific index
list3.insert(3, "mango")
print(f"List3 after inserting 'mango':\t {list3}")

# Remove: Removing a specific element
list3.remove("mango")
print(f"List3 after removing 'mango':\t {list3}")

# Reverse: Reversing the order of elements in the list
list3.reverse()
print(f"List3 after reversing:\t {list3}")

# Append: Adding an element to the end of the list
list3.append("mango")
print(f"List3 after appending 'mango':\t {list3}")

# Sort: Sorting the elements in ascending order
list3.sort()
print(f"List3 after sorting in ascending order:\t {list3}")

# Sort (descending order): Sorting the elements in descending order
list3.sort(reverse=True)
print(f"List3 after sorting in descending order:\t {list3}")

# Merge: Merging list2 into list1 (Note: This operation doesn't exist in Python)
# list1.merge(list2)
# print(f"List1 after merging with list2:\t {list1}")

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
