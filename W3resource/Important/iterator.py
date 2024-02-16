class Finditrator:
    def __init__(self):
        self.mystr ="abcdiouefghkl"
    def __iter__(self):
        return self
    def __next__(self):
        mylist=[]
        for i in self.mystr:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                yield i
char = Finditrator()
print(char.__next__())
print(char.__next__())
print(char.__next__())
print(char.__next__())
# for i in char:
    # print(i.next())