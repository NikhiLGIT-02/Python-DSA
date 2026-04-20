matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
rotated = [list(row) for row in zip(*matrix[::-1])]
print(rotated)