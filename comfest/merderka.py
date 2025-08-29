def solve():
    A, B = map(int, input().split())
    if B >= 2 * A:
        print("Ya")
    else:
        print("Tidak")

if __name__ == "__main__":
    solve()
