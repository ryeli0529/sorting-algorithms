import random, time, os, sys

print("failsafe")
delay = 0.01

def delline():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def check(a):
    delline()
    print(*a)
    print("checking list")
    for i in range(1, len(a)):
        print(f"{a[i - 1]} {a[i]}", end="  ")
        if a[i - 1] <= a[i]:
            pass
        else:
            return False
    print("yippee")
    return True

def bubble(a, iteration=[]):
    print("bubble sort\ntime complexity:O(n^2)")
    print(*a, "\n")
    while True:
        n = 0
        while n != len(a):
            for i in range(1, len(a) - n):
                delline()
                for t in a:
                    if t == a[i - 1] or t == a[i]:
                        print("\033[91m{}\033[00m" .format(t), end=" ")
                    else:
                        print(t, end=" ")
                print()
                iteration.extend(a)
                iteration.extend([" ", a[i - 1], a[i]])
                iteration.append("\n")
                if a[i - 1] >= a[i]:
                    a[i - 1], a[i] = a[i], a[i - 1]
                time.sleep(delay)
            n += 1
        if check(a):
            iteration.extend(a)
            return a, iteration
            
def selection(a, iteration=[]):
    print("selection sort\ntime complexity:O(n^2)")
    print(*a, "\n")
    while True:
        n = 0
        while n != len(a):
            s = n
            for i in range(1 + n, len(a)):
                delline()
                for t in a:
                    if t == a[n]:
                        print("\033[92m{}\033[00m" .format(t), end=" ")
                    elif t == a[s] or t == a[i]:
                        print("\033[91m{}\033[00m" .format(t), end=" ")
                    else:
                        print(t, end=" ")
                print()
                iteration.extend(a)
                iteration.extend([" ", a[s], a[i]])
                iteration.append("\n")
                if a[s] > a[i]:
                    s = i
                time.sleep(delay)
            a[n], a[s] = a[s], a[n]
            n += 1
        if check(a):
            iteration.extend(a)
            return a, iteration

def insertion(a, iteration=[]):
    print("insertion sort\ntime complexity:O(n^2)")
    print(*a, "\n")
    while True:
        n = 0
        while n != len(a):
            for i in range(0, n):
                delline()
                for t in a:
                    if t == a[n - 1 - i] or t == a[n - i]:
                        print("\033[91m{}\033[00m" .format(t), end=" ")
                    else:
                        print(t, end=" ")
                print()
                iteration.extend(a)
                iteration.extend([" ", a[n - 1 - i], a[n - i]])
                iteration.append("\n")
                if a[n - 1 - i] > a[n - i]:
                    a[n - 1 - i], a[n - i] = a[n - i], a[n - 1 - i]
                    i += 1
                    time.sleep(delay)
                else:
                    time.sleep(delay)
                    break
            n += 1
        if check(a):
            iteration.extend(a)
            return a, iteration

def merge(a, n=1, iteration=[]):
    suba = []
    divlist = {}
    for i in a:
        divlist[f"d{n}"] = [i]
        n += 1
    n = 2
    divkeys = list(divlist.keys())
    os.system('cls')
    print("merge sort\ntime complexity:O(n log n)")
    print(*a, "\n")
    while True:
        for key in range(0, len(divkeys)):
            divlist["ph"] = False
            divkeys = list(divlist.keys())
            if divlist[divkeys[key]] == False:
                break
            elif divlist[divkeys[key + 1]] == False:
                break
            divlist.pop("ph")
            divkeys.pop(-1)
            while True:
                delline()
                for t in a:
                    if t == divlist[divkeys[key]][0] or t == divlist[divkeys[key + 1]][0]:
                        print("\033[91m{}\033[00m" .format(t), end=" ")
                    else:
                        print(t, end=" ")
                print()
                print(*a, f"comparing {divlist[divkeys[key]][0]} and {divlist[divkeys[key + 1]][0]}")
                iteration.extend(a)
                iteration.extend([" ", divlist[divkeys[key]][0], divlist[divkeys[key + 1]][0]])
                iteration.append("\n")
                if divlist[divkeys[key]][0] <= divlist[divkeys[key + 1]][0]:
                    suba.append(divlist[divkeys[key]][0])
                    divlist[divkeys[key]].pop(0)
                else:
                    suba.append(divlist[divkeys[key + 1]][0])
                    divlist[divkeys[key + 1]].pop(0)
                time.sleep(delay)
                delline()
                print(*a, "checking if one is empty")
                iteration.extend(a)
                iteration.append("\n")
                if len(divlist[divkeys[key]]) == 0:
                    suba.extend(divlist[divkeys[key + 1]])
                    divlist[divkeys[key + 1]].clear()
                    break
                elif len(divlist[divkeys[key + 1]]) == 0:
                    suba.extend(divlist[divkeys[key]])
                    divlist[divkeys[key]].clear()
                    break
                time.sleep(delay)
            time.sleep(delay)
            del(divlist[divkeys[key + 1]])
            divkeys.pop(key + 1)
            divlist[divkeys[key]].extend(suba)
            suba.clear()
            place = 0
            for i in divlist[divkeys[key]]:
                a.pop(place + (key * n))
                a.insert(place + (key * n), i)
                iteration.extend(a)
                iteration.append("\n")
                delline()
                oner = 1
                for t in a:
                    if t == a[place + (key * n)] and oner == 1:
                        print("\033[91m{}\033[00m" .format(t), end=" ")
                        oner = 0
                    else:
                        print(t, end=" ")
                print()
                print(*a, "merging")
                time.sleep(delay)
                place += 1
        n *= 2
        if len(divlist[divkeys[0]]) == len(a):
            a = divlist[divkeys[0]]
            if check(a):
                iteration.extend(a)
                return a, iteration

n = 30
while True:
    views = list(range(1, n + 1))
    random.shuffle(views)
    views, iterations = bubble(views)
    print(*views)
    if input("iter for iterations ") == "iter":
        print(" ", end="")
        for i in iterations:
            print(i, end=" ")
        input()
    random.shuffle(views)
    views, iterations = selection(views)
    print(*views)
    if input("iter for iterations ") == "iter":
        print(" ", end="")
        for i in iterations:
            print(i, end=" ")
        input()
    random.shuffle(views)
    views, iterations = insertion(views)
    print(*views)
    if input("iter for iterations ") == "iter":
        print(" ", end="")
        for i in iterations:
            print(i, end=" ")
        input()
    random.shuffle(views)
    views, iterations = merge(views)
    print(*views)
    if input("iter for iterations ") == "iter":
        print(" ", end="")
        for i in iterations:
            print(i, end=" ")
        input()