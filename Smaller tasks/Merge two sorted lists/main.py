from random import randint


def merge_sorted_lists_with_extend(list1: list[int], list2: list[int]) -> list[int]:
    """
    Merges two sorted lists of integers.
    :param list1: The first list.
    :param list2: The second list.
    :return: A combined sorted list of the integers found in the two input lists.
    """
    # Extend one of the lists by the other.
    list1.extend(list2)
    # Sort and return the extended list.
    return sorted(list1)


def merge_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
    """
    Merges two sorted lists of integers.

    It creates a new list, then iterate through the input lists, whichever has the smallest number next will
    be appended to the output list. Once the end of one of the lists is reached, we extend the result list
    by the remaining slices from both of the lists.
    :param list1: The first list.
    :param list2: The second list.
    :return: A combined sorted list of the integers found in the two input lists.
    """
    # Pointers that keep track of where we are within the two lists
    l1_ptr, l2_ptr = 0, 0
    result = []

    # While we have not reached the end of either of the lists
    while l1_ptr < len(list1) and l2_ptr < len(list2):
        # Appending by the next element in the first list,
        # if it's smaller than or equal to the next element in the second list,
        # then incrementing the pointer of the first list.
        if list1[l1_ptr] <= list2[l2_ptr]:
            result.append(list1[l1_ptr])
            l1_ptr += 1
        # Same idea but with the second list.
        else:
            result.append(list2[l2_ptr])
            l2_ptr += 1

    # Extending the result list by the remaining slices.
    # If the slice happens to be empty, it still doesn't affect the result array in a bad way,
    # so no need to check if the slice is empty.
    result.extend(list1[l1_ptr:])
    result.extend(list2[l2_ptr:])

    return result


L1 = [1, 2, 4]
L2 = [1, 3, 4, 5]
print(merge_sorted_lists(L1, L2))
