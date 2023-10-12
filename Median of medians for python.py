import random



def median_of_medians(arr, n_smallest):

    # Divide input list into sublists of len 5
    sublists = [ arr[j:j+5] for j in range(0, len(arr), 5) ]
    medians = [ sorted(sublist)[ len(sublist)//2 ] for sublist in sublists ]
    if len(medians) <= 5:
        pivot = sorted(medians)[ len(medians)//2 ]
    else:
        # The pivot is the median of the medians
        # Divide and conquer
        pivot = median_of_medians( medians, len(medians)//2 )

    # Partition
    low = [ j for j in arr if j < pivot ]
    high = [ j for j in arr if j > pivot ]

    # Divide and conquer
    pivot_index = len(low)
    if n_smallest < pivot_index:
        return median_of_medians(low, n_smallest)
    elif n_smallest > pivot_index:
        return median_of_medians(high, n_smallest - pivot_index - 1)
    else:  # pivot = pivot_index, find it!
        return pivot



if __name__ == '__main__':

    nums, ans = list(range(20)), list(range(20))

    for i in range(100000):
        
        random.shuffle(nums)

        nums_sorted = []
        for n_smallest in range(len(nums)):
            nums_sorted.append( median_of_medians(nums, n_smallest) )

        if nums_sorted != ans:
            print(nums_sorted)

















