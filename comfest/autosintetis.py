def solve():
    import sys
    input = sys.stdin.readline
    
    N = int(input().strip())
    A = list(map(int, input().split()))
    
    R = []
    P = []
    
    for i in range(N):
        val = A[i]
        R.append(val)
        if 1 <= val <= N:
            P.append(val)
        else:
            print(-1)
            return
    
    if R == P:
        print(len(P))
        print(*P)
    else:
        print(-1)


if __name__ == "__main__":
    solve()
