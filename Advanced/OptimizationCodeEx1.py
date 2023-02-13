portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    # Write your recursive code here
    if (ports != []):
        for j in range(0, len(ports)):
            route.append(ports[0])
            ports.pop(0)
            j=j+1
            permutations(route, ports)
            ports.append(route[len(route)-1])
            route.pop(len(route)-1)
    else:
        # Print the port names in route when the recursion terminates
        print(' '.join([portnames[i] for i in route]))

    


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))