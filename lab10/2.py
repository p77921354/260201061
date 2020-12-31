def hailstone(x, hail_str=""):
    if x == 1:
        hail_str += "1"
        return hail_str
    else:
        if x % 2 == 0:
            hail_str += str(x) + ", "
            return hail_str + hailstone(x//2)
        else:
            hail_str += str(x) + ", "
            return hail_str + hailstone(3*x+1)
print(hailstone(11))