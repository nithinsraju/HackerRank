def main(lst):
    length = len(lst)
    sublist.sort(reverse=True)
    mn = min(sublist[0], sublist[1])
    second = max(sublist[0], sublist[1])
    for i in range(2, length):
        if sublist[i] < mn:
            second = mn
            mn = sublist[i]
        elif second > sublist[i] != mn:
            second = sublist[i]

    secName = []

    for names in lst:
        if names[1] == second:
            secName.append(names[0])
        else:
            continue

    sorted_list = sorted(secName, key=str.casefold)

    #print(length)
    #print(lst)
    #print(sublist)
    #print(second)
    for values in sorted_list:
        print(values)


if __name__ == '__main__':
    list1 = []
    sublist = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name, score])
        sublist.append(score)
    main(list1)
