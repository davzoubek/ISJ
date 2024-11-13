def ng(a, n):
    z = (a[i:] for i in range(n))
    return zip(*z)
print(list(ng([1,2,3,4,5,6], 4)))

def sort_by_second_key(item):
    if isinstance(item[0][1], str):
        return ord(item[0][1].lower())
    else:
        return item[0][1]

def sort_by_third_key(item):
    if isinstance(item[0][2], str):
        return ord(item[0][2].lower())
    else:
        return item[0][2]

def sort_by_len_key(item):
    return len(item[1])

mydict = {("a", "B", 5):[2, 0], ("A", "c", 5):[2,1], (6, "a", "C"):[0, 0, 0], ("A", "A", "A"):[2], ("e", "e", "t"):[2, 3]}

print(sorted(sorted(sorted(mydict.items(), key=sort_by_second_key, reverse=True), key=sort_by_third_key, reverse=True), key=sort_by_len_key))
#print(sorted(sorted(sorted(mydict.items(), key=lambda i: i[0][1].lower()), key=lambda i: i[0][2].lower(), reverse=True), key=lambda i: len(i[1])))

class A(object):
    def __init__(self):
        print("entering A")
        super().__init__()
        print("leaving A")

class B(A):
    def __init__(self):
        print("entering B")
        super().__init__()
        print("leaving B")

class C(A):
    def __init__(self):
        print("entering C")
        super().__init__()
        print("leaving C")

class D(object):
    def __init__(self):
        print("entering D")
        super().__init__()
        print("leaving D")

class E(object):
    def __init__(self):
        print("no super() in E")
    
class F(object):
    def __init__(self):
        print("entering F")
        super().__init__()
        print("leaving F")

class G(B, C, D, E, F):
    def __init__(self):
        print("entering G")
        super().__init__()
        print("leaving G")

g = G()

s = { 'FORTRAN' : '1960', 'ALGOL' : '1950', 'C++'  : '1985' }
a = (c[1] for c in sorted(s, key=s.get))
for u in a:
    print(u)


class ListWAdd:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        print('enter ListWAdd')
        self._items.append(item)
        print('leave ListWAdd')

class SortedList(ListWAdd):
    def __init__(self, items=()):
        super().__init__(items)
        self._items.sort()

    def add(self, item):
        print('enter SortedList')
        super().add(item)
        self._items.sort()
        print('leave SortedList')

class IntList(ListWAdd):
    def __init__(self, items=()):
        for item in items:
            self._validate(item)
        super().__init__(items)

    @classmethod
    def _validate(cls, it):
        if not isinstance(it, int):
            raise TypeError(
                f'{cls.__name__} only supports int'
            )

    def add(self, item):
        print('enter IntList')
        self._validate(item)
        super().add(item)
        print('leave IntList')

class SortedIntList(IntList, SortedList):
        pass

s = SortedIntList([42, 23, 2])
s.add(1)