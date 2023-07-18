from framework import Simpleprofiler

p = Simpleprofiler()

# test 1: for loop vs while loop
p.start("for loop test")

for i in range(10000):
    
    pass

p.stop()

i = 0

p.start("while loop test")

while i < 10000:
    
    i += 1

p.stop()

# test 2: finding matching string to access row in list, vs reading row index from dictionary key
ls = [["a",1],["b",1],["c",1],["d",1],["e",1],["f",1],["g",1]]

p.start("finding matching row by looping")
for i in range(len(ls)):
    
    if ls[i][0] == "g":
        
        ls[i][1] += 1
        break
p.stop()

dict = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6}

p.start("finding match via key dictionary")
ls[dict["g"]][1] += 1
p.stop()