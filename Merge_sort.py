import random
import cProfile
import time

def merge_sort(unsorted_list):
    """
    Recursively sorts an unsorted list using the merge sort algorithm.
    
    Merge sort is a divide-and-conquer algorithm that splits the list into two halves,
    sorts each half recursively, and then merges the sorted halves back together.

    Args:
        unsorted_list (list): A list of unsorted elements.

    Returns:
        list: A sorted list obtained by merging the two sorted halves.
    """
    if len(unsorted_list) <= 1:
        return unsorted_list  # Base case: A list with one or zero elements is already sorted
    
    middle = len(unsorted_list) // 2  # Find the midpoint of the list
    
    # Recursively divide the list into two halves
    left_list = merge_sort(unsorted_list[:middle])
    right_list = merge_sort(unsorted_list[middle:])
    
    return merge(left_list, right_list)  # Merge the sorted halves and return the result

def merge(left_half, right_half):
    """
    Merges two sorted lists into a single sorted list.
    
    This function iterates through both lists, taking the smallest element from either
    the left or the right list until all elements are sorted into a single merged list.

    Args:
        left_half (list): The left half of a divided list, already sorted.
        right_half (list): The right half of a divided list, already sorted.
    
    Returns:
        list: A sorted list obtained by merging the two halves.
    """
    res = []  # Initialize an empty list to store the merged elements
    
    while left_half and right_half:
        if left_half[0] < right_half[0]:
            res.append(left_half.pop(0))  # Take the smallest element from the left list
        else:
            res.append(right_half.pop(0))  # Take the smallest element from the right list
    
    # Append any remaining elements from either half
    res.extend(left_half or right_half)
    return res  # Return the merged sorted list

def vectors(size):
    """
    Generates a list of random integers and sorts it using merge sort.
    
    The function starts with an array of `size` random integers, sorts it using merge sort,
    measures the execution time, and prints the size and execution time. It then recursively
    increases the size of the array by 1000 until it reaches 10,000.

    Args:
        size (int): The initial size of the randomly generated list.
    """
    A = [random.randint(0, 500) for _ in range(size)]  # Generate a list of random integers
    
    start_time = time.time()  # Record start time
    merge_sort(A)  # Sort the list using merge sort
    end_time = time.time()  # Record end time
    
    execution_time = end_time - start_time  # Compute execution time
    print(f"Size: {size}, Execution time: {execution_time:.6f} seconds")
    
    if size < 10000:
        vectors(size + 1000)  # Recursively increase the size and repeat sorting

def main():
    """
    Entry point of the program. Calls the `vectors` function with an initial size of 1000.
    """
    vectors(1000)

if __name__ == "__main__":
    cProfile.run("main()")  # Run performance profiling on the `main` function
