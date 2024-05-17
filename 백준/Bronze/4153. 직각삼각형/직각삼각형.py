while True :
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0 :
        break
    cal1 = x**2 + y**2
    cal2 = x**2 + z**2
    cal3 = y**2 + z**2
    if cal1 == z**2 or cal2 == y**2 or cal3 == x**2 :
        print("right")
    else :
        print("wrong")