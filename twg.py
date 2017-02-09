import time
x=1
y = 1.01
print("The Waiting Game.")
while True:
    time.sleep(1.01)
    print("Seconds passed:", x)
    #print("Actual seconds:", y, "\n")
    x += 1
    y += 1.01
    
