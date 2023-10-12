def partition(nums, low, high):
    """
    分区函数，用于将数组nums在区间[low, high]中进行分区操作，选择最右边的元素作为pivot，
    将小于等于pivot的元素放在pivot的左边，大于pivot的元素放在pivot的右边，
    并返回pivot的索引位置。
    
    Args:
        nums (list): 待分区的数组。
        low (int): 分区的起始索引。
        high (int): 分区的结束索引。
        
    Returns:
        int: pivot的索引位置。
    """
    i = low - 1  # 初始化最小元素索引
    pivot = nums[high]  # 选择最右边的元素作为pivot
    
    for j in range(low, high):
        # 当前元素小于或等于pivot，将其交换到已处理区间的末尾
        if nums[j] <= pivot:
            i += 1
            # 如果i不等于j，交换当前元素和已处理区间的下一个元素
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]

    i += 1
    # 将pivot放到正确的位置上，即已处理区间的末尾
    nums[i], nums[high] = nums[high], nums[i]
    return i  # 返回pivot的索引位置



def median_of_medians(nums, low, high, n_smallest):
    """
    使用Median of Medians算法寻找数组nums在区间[low, high]中的第n_smallest小元素。
    
    Args:
        nums (list): 待查找的数组。
        low (int): 数组的起始索引。
        high (int): 数组的结束索引。
        n_smallest (int): 要查找的第n_smallest小元素的索引。
        
    Returns:
        int: 第n_smallest小元素的值。
    """
    if low == high:
        return nums[low]  # 如果区间只有一个元素，直接返回，找到 n_smallest 了
    
    num_elements = high - low + 1
    num_groups = (num_elements + 4) // 5  # ceil 函数
    medians = [0] * num_groups
    
    # 计算每个小组的中位数
    for i in range(num_groups):
        group_low = low + i*5
        group_high = min(low + i*5+4, high)
        medians[i] = sorted(nums[group_low:group_high + 1])[len(nums[group_low:group_high + 1]) // 2]
    
    # 寻找 medians 数组的中位数作为 pivot
    pivot = median_of_medians(medians, 0, len(medians) - 1, len(medians) // 2)
    pivot_index = nums.index(pivot)
    nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
    partition_index = partition(nums, low, high)  # 分区操作，得到新的 pivot 的索引
    
    # 如果 n_smallest 等于新的 pivot 的索引，直接返回 pivot；否则，在左边或右边递归寻找
    if n_smallest == partition_index:
        return nums[partition_index]
    elif n_smallest < partition_index:
        return median_of_medians(nums, low, partition_index - 1, n_smallest)
    else:
        return median_of_medians(nums, partition_index + 1, high, n_smallest)



if __name__ == '__main__':
    # 当模块直接运行时执行以下代码
    
    import random
    
    nums = list(range(20))  # 创建一个包含0到19的整数列表
    range_20 = list(range(20))  # 创建包含0到19的整数列表的副本，用于比较
    ans = [0] * len(nums)  # 用于存储计算结果的列表

    # 测试正确性
    for i in range(10000):
        random.shuffle(nums)  # 将列表中的元素随机打乱
        
        # 使用Median of Medians算法计算每个位置上的第n_smallest小元素
        for n_smallest in range(len(nums)):
            ans[n_smallest] = median_of_medians(nums, 0, len(nums)-1, n_smallest)
        
        # 如果计算结果不等于0到19的整数列表，打印错误的结果
        if ans != range_20:
            print(ans)
























