arr = [0,3,0,0,0,4,0,0]
print(arr)

def troca(arranjo):
    arranjo[1], arranjo[5] = arranjo[5], arranjo[1]

    return arranjo

troca(arr[:])

print(arr)
