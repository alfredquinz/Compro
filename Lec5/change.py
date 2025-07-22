counter = 0

def increment():    
    counter = 3
    counter += 1
    print(counter)

increment()
increment()  # This will print 4 again, as the counter is local to the function
print(counter)  # This will print 0, as the global counter is not modified by