def hello():
    return 'Hello'
def hi():
    return 'Hi'
def aloha():
    return 'Alloha'


my_list = [hello, hi, aloha]
print(my_list)
print(my_list[1])
print(my_list[1]())