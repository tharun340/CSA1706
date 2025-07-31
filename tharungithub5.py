def list_operations():
    nested_list = [1, 2, [3, 4, 5], 6]
    print("Nested List:", nested_list)
    length = len(nested_list)
    print("Length of nested_list:", length)
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenated = list1 + list2
    print("Concatenated List:", concatenated)
    print("Is 3 in list1?", 3 in list1)
    print("Is 7 in list2?", 7 in list2)
    print("Iterating over list1:")
    for item in list1:
        print(item, end=' ')
    print()
    print("First element of list2:", list2[0])
    print("Last element of nested_list:", nested_list[-1])
    slice1 = concatenated[2:5]
    print("Sliced part of concatenated list (index 2 to 4):", slice1)
    print("Access element '4' from nested_list:", nested_list[2][1])
    list[2] is [3,4,5]

if __name__ == "__main__":
    list_operations()

