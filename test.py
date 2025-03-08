def recursev(limit:int, n:int):
    if n <= limit:
        print(n)
        n+=1
        recursev(limit, n)
    

recursev(100, 1)