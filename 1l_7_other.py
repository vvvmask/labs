# incorrect
def f_index(arr:list = []):
    arr.append(1)

# correct
def index(arr:list = None):
    if arr is None:
        arr = []
    arr.append(1)

def s_index(age: int, name: str):
    print(age,name)

s_index(15,'Dias')