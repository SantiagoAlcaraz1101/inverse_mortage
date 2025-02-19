count: int = 0 

def fact(string):
    a = len(string)
    number= 1
    for i in range(a):
        number = number*a
    return number, a

def permutaciones(string: str) -> int:
    count +=1
    permutaciones(string)
    if count >= len(string):
        pass

print(fact("holas"))
