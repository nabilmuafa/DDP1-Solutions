biner = input("String biner\t: ")

pangkat = 1
twos_comp = 0
for i in range(len(biner)-1, -1, -1):
    if i==0:
        twos_comp += int(biner[i])*pangkat*-1
        break
    twos_comp += int(biner[i])*pangkat
    pangkat *= 2
    
print("Signed integer\t:", twos_comp)
    
