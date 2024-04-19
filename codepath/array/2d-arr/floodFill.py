"""
    An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

    You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

    To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor

    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

    Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
    Output: [[2,2,2],[2,2,2]]

    Leetcode link: https://leetcode.com/problems/flood-fill/
"""
def print2dArray(arr):
    for row in arr:
        print(row)

#### Anh's sol (recursion) ####
# Can use BFS/DFS or recursion
def floodFill(image, sr, sc, newColor):
  visited = set()
  originalColor = image[sr][sc]

  if image[sr][sc] != newColor:
    image[sr][sc] = newColor
    visited.add((sr, sc))
  
    flood_fill_helper(image, sr + 1, sc, originalColor, newColor, visited)
    flood_fill_helper(image, sr - 1, sc, originalColor, newColor, visited)
    flood_fill_helper(image, sr, sc + 1, originalColor, newColor, visited)
    flood_fill_helper(image, sr, sc - 1, originalColor, newColor, visited)

def flood_fill_helper(image, sr, sc, originalColor, newColor, visited):
  if (sr, sc) in visited:
    return
  
  if sr not in range(len(image)) or sc not in range(len(image[0])): 
    return

  if image[sr][sc] == originalColor:
    image[sr][sc] = newColor
    visited.add((sr, sc))
    flood_fill_helper(image, sr + 1, sc, originalColor, newColor, visited)
    flood_fill_helper(image, sr - 1, sc, originalColor, newColor, visited)
    flood_fill_helper(image, sr, sc + 1, originalColor, newColor, visited)
    flood_fill_helper(image, sr, sc - 1, originalColor, newColor, visited)


test_1 = [[1,1,1],
          [1,1,0],
          [1,0,1]]

floodFill(test_1, 1, 1, 2)
print2dArray(test_1)

test_2 = [[1,1,1,1,1],
          [1,1,0,0,1],
          [1,0,1,0,1],
          [1,1,0,0,1],
          [1,1,1,1,1]]

floodFill(test_2, 3, 2, 2)
print2dArray(test_2)
 
 

##### Instructor's sol #####
# another Dfs method
# Time: O(M*N), Space: O(1) if not counting the stack trace in mem, O(M*N) if do?
def flood_fill2(image, sr, sc, newColor):
    starting_pixel = image[sr][sc]
    dfs(image, sr, sc, newColor, starting_pixel)

    return image


def dfs(image, sr, sc, newColor, starting_pixel):

    """!!! image[sr][sc] == newColor => this allows us to not need a visited set since if it's been visited, it'd been colored newColor"""
    if sr < 0 or sr > len(image)-1 \
        or sc < 0 or sc > len(image[0]) - 1 \
        or image[sr][sc] == newColor or image[sr][sc] != starting_pixel: 
        return

    image[sr][sc] = newColor
    dfs(image, sr + 1, sc, newColor, starting_pixel)
    dfs(image, sr - 1, sc, newColor, starting_pixel)
    dfs(image, sr, sc + 1, newColor, starting_pixel)
    dfs(image, sr, sc - 1, newColor, starting_pixel)

print2dArray([[1,1,1],[1,1,0],[1,0,1]])