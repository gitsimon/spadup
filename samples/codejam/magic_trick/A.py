if __name__ == "__main__":
    T = int(input())

    for x in range(1, T + 1):

        l1 = int(input())
        for i in range(1, l1):
            input()
        L1 = list(map(int, input().split()))
        for i in range(l1 + 1, 5):
            input()

        l2 = int(input())
        for i in range(1, l2):
            input()
        L2 = list(map(int, input().split()))
        for i in range(l2 + 1, 5):
            input()

        z = 0
        n = 0
        for i in range(4):
            for j in range(4):
                if L1[i] == L2[j]:
                    z += 1
                    n = L1[i]

        if z == 1:
            print(f'Case #{x}: {n}')
        else:
            if z == 0:
                print(f'Case #{x}: Volunteer cheated!')
            else:
                print(f'Case #{x}: Bad magician!')
