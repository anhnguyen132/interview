def destCity(paths):
    """
    You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

    It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

    Example 1:

    Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    Output: "Sao Paulo" 
    Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

    Example 2:

    Input: paths = [["B","C"],["D","B"],["C","A"]]
    Output: "A"
    Explanation: All possible trips are: 
    "D" -> "B" -> "C" -> "A". 
    "B" -> "C" -> "A". 
    "C" -> "A". 
    "A". 
    Clearly the destination city is "A".

    Example 3:

    Input: paths = [["A","Z"]]
    Output: "Z"
    """
    # n = number of paths (ie size of paths)
    # Time: O(n)
    # Space: 2 sets, each is O(2n) since 2n = number of cities => Space = O(n)
    not_dest = set()
    potential_dest = set()

    for start, end in paths:
        not_dest.add(start)
        if start in potential_dest:
            potential_dest.remove(start)

        if end not in not_dest:
            potential_dest.add(end)

    if len(potential_dest) > 0:
        return list(potential_dest)[0]
    
    return "No destination city"

def destCityHashTable(paths):
    my_map = {}
    for start, end in paths:
        my_map[start] = end
    
    start, end = paths[0]
    while end in my_map.keys():
        start = end
        end = my_map[start]
    
    return end



def main():
    print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]) == "Sao Paulo")
    print(destCity([["B","C"],["D","B"],["C","A"]]) == "A")
    print(destCity([["A","Z"]]) == "Z")

    print(destCityHashTable([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]) == "Sao Paulo")
    print(destCityHashTable([["B","C"],["D","B"],["C","A"]]) == "A")
    print(destCityHashTable([["A","Z"]]) == "Z")

if __name__ == "__main__":
    main()