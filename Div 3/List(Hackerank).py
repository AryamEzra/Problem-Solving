if __name__ == '__main__':
    n = int(input())
    lst = []
    for i in range(n):
        cmd = input().split()

        for i in range (1, len(cmd)):
            cmd[i] = int(cmd[i])
# this is beacuse our format is smthing like ['insert', '0']
        if cmd[0] == "insert":
            lst.insert(cmd[1],cmd[2])
        if cmd[0] == "remove":
            lst.remove(cmd[1])
        if cmd[0] == "append":
            lst.append(cmd[1])
        if cmd[0] == "sort":
            lst.sort()
        if cmd[0] == "pop":
            lst.pop()
        if cmd[0] == "reverse":
            lst.reverse()
        if cmd[0] == "print":
            print(lst)