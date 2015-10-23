
def greeting(name: str) -> str:
    return 'Hello ' + name

print(greeting('Peter'))

try:
    print(greeting(1))
except TypeError as ter:
    print(ter)
