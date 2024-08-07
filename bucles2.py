#infinite loop until a specific order is executed
while True :
#infinite loop
    line = input("> ")
    if line[0] == "#" :
        continue
    #continue the loop
    if line == "fin" :
        break
    #the specific order
    print(line)
print("¡Terminado!")