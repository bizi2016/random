from functools import lru_cache



@lru_cache
def fib_rec(n):
    
    if n == 1 or n == 2:
        return 1
    
    return fib_rec(n-1) + fib_rec(n-2)



def fib_loop(n):

    a, b = 1, 1
    
    for i in range(n-2):
        a, b = b, a+b
        
    return b



if __name__ == '__main__':
    
    for i in range(1, 21):
        print(i, fib_rec(i), fib_loop(i))



"""
Output:

1 1 1
2 1 1
3 2 2
4 3 3
5 5 5
6 8 8
7 13 13
8 21 21
9 34 34
10 55 55
11 89 89
12 144 144
13 233 233
14 377 377
15 610 610
16 987 987
17 1597 1597
18 2584 2584
19 4181 4181
20 6765 6765
"""
