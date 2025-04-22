#   (m,n,s)从1到m取n个不同的数，和为s，有多少种取法
#   n<=10, s<=20
#   如果m>s，边界就是s不是m了，所以是(s,n,s)
#   如果m<=s，取m，剩下的最多到(s-m)，所以就是(m-1,n-1,s-m)
#   如果m<=s，不取m，m里肯定没有m了，n，s不变，所以是（m-1,n,s）
def ways(m, n, s):
    if n == 0 and s == 0:
        return 1
    if n == 0 and s != 0:
        return 0
    if m < n:
        return 0
    if m == 0 and (n != 0 or s != 0):
        return 0
    if m > s:
        return ways(s, n, s)
    else:
        return ways(m-1, n-1, s-m) + ways(m-1, n, s)
        


m = int(input("请输入m"))
n = int(input("请输入n"))
s = int(input("请输入s"))
print('m={}, n={}, s={}'.format(m, n, s))
print(ways(m, n, s))
