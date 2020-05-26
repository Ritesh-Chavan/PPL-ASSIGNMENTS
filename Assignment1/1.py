shore1 = {
    "1" : "Grass",
    "3" : "Goat",
    "6" : "Tiger"
}
shore2 = {}
direction = 0

while 1:
    print("At shore1:", list(shore1.values()))
    print("At shore2:", list(shore2.values()))
    
    if direction:
        print("The man is at shore2")
        if len(shore1.items()) == 2:
            ls = list(shore1.keys())
            if int(ls[0]) & int(ls[1]):
                print(shore1.get(str(max(ls))), "ate the", shore1.get(str(min(ls))))
                break
        elif len(shore1.items()) == 3:
            print("You just demonstrated a food chain")
            break
        elif len(shore2.items()) == 3:
            print("Solved!! Man reached safely to other shore")
            break
    else:
        print("The man is at shore1")
        if len(shore2.items()) == 2:
            ls = list(shore2.keys())
            if int(ls[0]) & int(ls[1]):
                print(shore2.get(str(max(ls))), "ate the", shore2.get(str(min(ls))))
                break
    
    print("What should the man take with him?\n1. Grass\n2. Goat\n3. Tiger\n4. Nothing")
    val = input()
    if val == "3": val = "6"
    elif val == "2": val = "3"
    if val != "4":
        if direction:
            shore1.update(dict({str(val) : shore2[val]}))
            shore2.pop(val)
        else:
            shore2.update(dict({str(val) : shore1[val]}))
            shore1.pop(val)
    direction ^= 1
    print()
