'''
733. Flood Fill

Easy

4853

474

Add to List

Share
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

 

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n
'''



# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         starting = image[sr][sc]
#         print('starting:', starting)
#         print('height:', len(image[0]))
        
#         def flood_fill(image, starting, color, x_coord, y_coord):
#             if x_coord < 0 or x_coord >= len(image) or y_coord < 0 or y_coord >= len(image[0]) or image[x_coord][y_coord] == color or image[x_coord][y_coord] != starting:
#                 print(x_coord, y_coord, image[x_coord][y_coord])
#                 return
#             else:
#                 image[x_coord][y_coord] = color
#                 flood_fill(image, starting, color, x_coord, (y_coord - 1))
#                 flood_fill(image, starting, color, x_coord, (y_coord + 1))
#                 flood_fill(image, starting, color, (x_coord - 1), y_coord)
#                 flood_fill(image, starting, color, (x_coord - 1), y_coord)
#                 return
                
        
#         flood_fill(image, starting, color, sr, sc)
        
#         print(image)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        y_coord = sr
        x_coord = sc
        print('starting:', starting, "x:", x_coord, "y:", y_coord, "newcolor:", color, "starting color:", image[sr][sc])
        if image == None or image[y_coord][x_coord] == color:
            return image
        
        def flood_fill(image, starting, color, x_coord, y_coord):
            if x_coord < 0 or x_coord >= len(image) or y_coord < 0 or y_coord >= len(image[0]) or image[x_coord][y_coord] != starting:
                return
            image[x_coord][y_coord] = color
            flood_fill(image, starting, color, x_coord, (y_coord + 1)) #up
            flood_fill(image, starting, color, x_coord, (y_coord - 1)) #down
            flood_fill(image, starting, color, (x_coord - 1), y_coord) #left
            flood_fill(image, starting, color, (x_coord + 1), y_coord) #right
                
        
        flood_fill(image, starting, color, sr, sc)
        return image

'''
Success
Details 
Runtime: 99 ms, faster than 68.20% of Python3 online submissions for Flood Fill.
Memory Usage: 14.2 MB, less than 38.09% of Python3 online submissions for Flood Fill.
'''