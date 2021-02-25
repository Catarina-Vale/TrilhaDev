curr = 1
base = 1
print("selecione até que numero de fibbonaci deseja:")
limit = int(input())
while(curr <= limit):
    print(curr)
    aux = curr
    curr = base + curr
    base = aux