

PARKING_PLACES=7
FREE_PLACES= 3

print("#"*PARKING_PLACES*5)

for places_index in range(1, PARKING_PLACES+1):
    if places_index == 3:
        print ("|   |",end="")
    else:
        print("| x |", end="")

print("\n","#"*PARKING_PLACES*5, sep="")


 # с функ'sep' пока не разобрался, она как "пустой" разделитель вроде бы в данном примере, если ее убираешь появляется пробел по умолчанию