def main(x, y, z, n):
    xl = [p for p in range(x+1)]
    yl = [q for q in range(y+1)]
    zl = [r for r in range(z+1)]

    list = [[i, j, k] for i in xl for j in yl for k in zl if (i+j+k)!=n]
    print(list)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    main(x, y, z, n)
