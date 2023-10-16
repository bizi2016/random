import numpy as np



# 使用分治算法找到最小距离的两个点
def find_closest_points(points):

    if len(points) <= 3: # 结束条件
        return brute_force_distance(points)



    # 将点按照x坐标排序
    sorted_points = sorted( points, key=lambda x: x[0] )
    
    mid = len(points) // 2
    
    # print('mid =', mid)
    # print()
    
    left_half = sorted_points[ :mid ]
    right_half = sorted_points[ mid: ]

    # print('left_half =', left_half)
    # print('right_half =', right_half)
    # print()



    # 递归地在左右半部分查找最小距离
    left_pair, left_distance = find_closest_points( left_half )
    right_pair, right_distance = find_closest_points( right_half )



    # 取左右半部分中最小距离的值
    if left_distance < right_distance:
        dc_min_distance = left_distance
        dc_min_pair = left_pair
    else:
        dc_min_distance = right_distance
        dc_min_pair = right_pair



    # 考虑中间区域的点
    mid_x = sorted_points[mid][0]
    
    strip = []
    
    for point in sorted_points:
        if abs(point[0] - mid_x) < dc_min_distance: # 中间区域
            strip.append(point)

    # print()
    # print('strip =', strip)
    # print()

    # 在中间区域中查找可能更小的距离
    strip_pair, strip_distance = find_closest_strip(strip, dc_min_distance)

    # 返回三个区域中的最小距离
    if strip_distance < dc_min_distance:
        return strip_pair, strip_distance
    else:
        return dc_min_pair, dc_min_distance





# 在中间区域中查找最小距离
def find_closest_strip(strip, dc_min_distance):
    
    strip.sort( key=lambda point: point[1] ) # 按照y坐标排序
    
    dc_min_pair = None
    
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] < dc_min_distance:
                distance = np.linalg.norm(strip[i] - strip[j])
                if distance < dc_min_distance:
                    dc_min_distance = distance
                    dc_min_pair = [ strip[i], strip[j] ]
            else:
                # 如果y坐标差距大于等于当前最小距离，就可以退出内层循环
                break

    # print('dc_min_pair =', dc_min_pair, end='\t')
    # print('dc_min_distance =', dc_min_distance)

    return dc_min_pair, dc_min_distance





# 验证算法（也是分治算法的一部分）
def brute_force_distance(points):
    
    bf_min_distance = float('inf')
    bf_min_pair = None
    
    for i in range( len(points) ):
        for j in range( i+1, len(points) ):
            
            distance = np.linalg.norm( points[i] - points[j] )
            
            if distance < bf_min_distance:
                bf_min_distance = distance
                bf_min_pair = [ points[i], points[j] ]

    # print('bf_min_pair =', bf_min_pair, end='\t')
    # print('bf_min_distance =', bf_min_distance)
                
    return bf_min_pair, bf_min_distance





# 测试程序
if __name__ == '__main__':
    
    # points = np.array([ [1, 2], [4, 6], [7, 8], [3, 5], [9, 10] ])
    # points = np.array([ [2, 3], [12, 30], [5, 1], [14, 10], [3, 4], [5.2, 0.3] ])
    # points = np.array([ [21, 17], [11, 98], [87, 50], [2, 46], [37, 54] ])



    # 设置随机数种子，以便结果可重现
    np.random.seed(42)

    # 生成100个不重复的随机点
    num_points = 100

    min_coordinates = 0
    max_coordinates = 100



    for times in range( 10000 ):

        # 进度条
        if times%100 == 0: print(times//100, end=' ')


        
        # 随机生成无重复的x坐标和y坐标
        x_coordinates = np.random.choice(
            range( min_coordinates, max_coordinates ),
            size=num_points, replace=False,
            )
        
        y_coordinates = np.random.choice(
            range( min_coordinates, max_coordinates ),
            size=num_points, replace=False,
            )

        # 组合x坐标和y坐标成为一个100x2的数组
        points = np.column_stack( (x_coordinates, y_coordinates) )


    
        bf_min_pair, bf_min_distance = brute_force_distance( points )
        '''
        print()
        print('=== 暴力算法 ===')
        print()
        print('最近的两个点 =', bf_min_pair)
        print('最小距离 =', bf_min_distance)
        print()
        '''
        dc_min_pair, dc_min_distance = find_closest_points( points )
        '''
        print()
        print('=== 分治算法 ===')
        print()
        print('最近的两个点 =', dc_min_pair)
        print('最小距离 =', dc_min_distance)
        '''
        if bf_min_distance != dc_min_distance:

            print()
            print(bf_min_pair,'\t', dc_min_pair)
            print(bf_min_distance,'\t\t\t', dc_min_distance)















