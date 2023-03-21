portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    # write the recursive function here
    if (ports != []):
        for j in range(0, len(ports)):
            route.append(ports[0])
            ports.pop(0)
            j=j+1
            permutations(route, ports)
            ports.append(route[len(route)-1])
            route.pop(len(route)-1)
    else:
    # remember to calculate the emissions of the route as the recursion ends
        distance = D[route[0]][route[1]] + D[route[1]][route[2]] + D[route[2]][route[3]] + D[route[3]][route[4]]
        emissions = distance * co2
        # print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)

        global smallest, bestroute       

        if( emissions <= smallest):
            smallest = emissions
            for i in range(0, len(route)):
                bestroute[i] = route[i]
        # and keep track of the route with the lowest emissions
    

    # pass



def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing

    # this will start the recursion 
    permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()
