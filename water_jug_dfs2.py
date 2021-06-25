def findSolution(current, path, depth=0):

    # get x and y values of current tuple
    (x, y) = (current[0], current[1])

    # if more than 20 levels of tree traversed, stop (this may be changed)
    if(depth > 20):
        return (False, path)

    # apply the rules one by one and go to next level

    if(x == 2):
        return (True, path)

    if(x < 4):
        new_tuple = (4, y)
        if new_tuple not in path:
            path.append(new_tuple)
            return findSolution(new_tuple, path, depth+1)

    if(y < 3):
        new_tuple = (x, 3)
        if new_tuple not in path:
            path.append(new_tuple)
            return findSolution(new_tuple, path, depth+1)

    if(x > 0):
        new_tuple = (0, y)
        if new_tuple not in path:
            path.append(new_tuple)
            return findSolution(new_tuple, path, depth+1)

    if(y > 0):
        new_tuple = (x, 0)
        if new_tuple not in path:
            path.append(new_tuple)
            return findSolution(new_tuple, path, depth+1)

    if((x+y) >= 4 and y >= 0):
        new_tuple = (4, y-(4-x))
        if new_tuple not in path:
            path.append(new_tuple)
            return findSolution(new_tuple, path, depth+1)

    if((x+y) >= 4 and x > 0):
        new_tuple = (x-(3-y), 3)
        if new_tuple not in path:
            path.append(new_tuple)
            return findSolution(new_tuple, path, depth+1)

    if((x+y) <= 4 and y > 0):
        new_tuple = (x+y, 0)
        if new_tuple not in path:
            path.append(new_tuple)
            return findSolution(new_tuple, path, depth+1)

    if((x+y) <= 3 and x > 0):
        new_tuple = (0, x+y)
        if new_tuple not in path:
            path.append(new_tuple)
            return findSolution(new_tuple, path, depth+1)
    return (False, path)

def main():
    success, path = findSolution((0, 2), [])
    print('\n', success)
    print(path, '\n')

main()