"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Examples:

Input:   
11110    1111
11010 => 11 1
11000    11
00000
Output: 1



Input:
11000    11
11000 => 11 <- island
00100      1 <- island
00011       11 <- island
Output: 3

0010010
0010010
0011110
Output: 1

00100010
00101010
00111100
Output: 2

00100010
00101010
00111110
Output: 1
"""

def islandCount(lst):
    """
    Iterate through each elem of the matrix, if see 1, change it to 2 to mark that it's part of an island that we've visited. 
    Check its neighbors for 2, if there is any 2, move on to the next elem. Also, mark any 1 that you see in the neighbors as 2. 
    Otherwise, add 1 to the island count
    """
    island_count = 0 
    
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] == 1:
                island_count += 1
                dfs(lst, i, j)

    print("island_count: ", island_count)
    print(lst)
    return island_count

def dfs(lst, i, j):
    lst[i][j] = 2
    
    # check the neighbor above
    if i - 1 >= 0 and lst[i-1][j] == 1: 
        dfs(lst, i-1, j)

    # check the neighbor below  
    if i + 1 < len(lst):
        if lst[i+1][j] == 1:
            dfs(lst, i+1, j)
        
    # check the left neighbor   
    if j - 1 >= 0 and lst[i][j-1] == 1:
        dfs(lst, i, j-1)

    # check the right neighbor
    if j + 1 < len(lst[0]):
        if lst[i][j+1] == 1:
            dfs(lst, i, j+1)


  

"""
    0020020
    0020020
    0022220
    0000000
"""


#test1 outputs 1
test1 = [[1,1,1,1,0],
         [1,1,0,1,0],
         [1,1,0,0,0],
         [0,0,0,0,0]]
print(f"Test 1: {islandCount(test1) == 1}")

#test2 outputs 3
test2 = [[1,1,0,0,0],
         [1,1,0,0,0],
         [0,0,1,0,0],
         [0,0,0,1,1]]
print(f"Test 1: {islandCount(test2) == 3}")


"""
0010010
0010010
0011110
Output: 1
"""
test3 = [[0,0,1,0,0,1,0],
         [0,0,1,0,0,1,0],
         [0,0,1,1,1,1,0],
         [0,0,0,0,0,0,0]]
print(f"Test 3: {islandCount(test3) == 1}")