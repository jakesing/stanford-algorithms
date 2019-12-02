# code comes from: https://github.com/amirziai/learning/blob/master/algorithms/Merge-Sort.ipynb

# Python program for implementation of MergeSort
def split(input_list):
    """
    Splits a list into two pieces
    :param input_list: list
    :return: left and right lists (list, list)
    """
    input_list_len = len(input_list)
    midpoint = input_list_len // 2
    return input_list[:midpoint], input_list[midpoint:]


def merge_sorted_lists(list_left, list_right):
    split_inv_count = 0
    """
    Merge two sorted lists
    This is a linear operation
    O(len(list_right) + len(list_right))
    :param left_list: list
    :param right_list: list
    :return merged list
    """
    # Special case: one or both of lists are empty
    if len(list_left) == 0:
        return list_right
    elif len(list_right) == 0:
        return list_left

    # General case
    index_left = index_right = 0
    list_merged = []  # list to build and return
    list_len_target = len(list_left) + len(list_right)
    while len(list_merged) < list_len_target:
        if list_left[index_left] <= list_right[index_right]:
            # Value on the left list is smaller (or equal so it should be selected)
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            # Right value smaller
            list_merged.append(list_right[index_right])
            index_right += 1
            splitInv.count += len(list_left) - index_left

        # If we are at the end of one of the lists we can take a shortcut
        if index_right == len(list_right):
            # Reached the end of right
            # Append the remainder of left and break
            list_merged += list_left[index_left:]
            break
        elif index_left == len(list_left):
            # Reached the end of left
            # Append the remainder of right and break
            list_merged += list_right[index_right:]
            break
    return list_merged


class splitInv:
    count = 0

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        left, right = split(input_list)
        # The following line is the most important piece in this whole thing
        result = merge_sorted_lists(merge_sort(left), merge_sort(right))
        return result




