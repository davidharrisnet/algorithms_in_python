from collections import deque
import string

def main():
    q = deque()
    for i in list(string.ascii_uppercase)[:10]:
        q.append(i)
        print(q)

if __name__ == "__main__":
    main()

