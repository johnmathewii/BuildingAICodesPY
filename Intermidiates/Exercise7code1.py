def count11(seq):
    count = 0
    for i in range(0, len(seq)):
        if (seq[i] == 1):
            if seq[i+1] == 1:
                count = count + 1                    
        else:
            continue        
   # define this function and return the number of occurrences as a number
    return count 

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2