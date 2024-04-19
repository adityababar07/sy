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
