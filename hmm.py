# import sys
# import collections

# def solution(A):
#   size = len(A)
  
#   if size < 4:
#     return -1
  
#   track = collections.defaultdict(int)
  
#   for i in range(size):
#     track[A[i]] += 1
    
#   for key in track.keys():
#     if track[key] >= 4:
#       return 0
    
  
#   remover = set()
  
#   for key in track.keys():
#     if track[key] < 2:
#       remover.add(key)
      
#   for key in remover:
#     del(track[key])
    
#   allKeys = sorted(track.keys())
  
  
#   if len(allKeys) < 2:
#     return -1
  
#   return int(allKeys[len(allKeys) - 1]) - int(allKeys[len(allKeys) - 2])

# print(solution([911,1,3,1000,1000,2,2,999,1000,911]))

import numpy as np

# Percentage data for black faculty
faculty_percentages = [2.5, 2.5, 2.7, 2.6, 2.5, 2.5, 2.3, 3.1, 2.4, 2.5, 2.5]

# Percentage data for black individuals who graduate
graduation_percentages = [4.7, 5.1, 4.9, 4.7, 4.7, 4.4, 4.7, 4.7, 4.8, 4.8, 5.0]

# Reshape the arrays as 2D arrays
faculty_percentages = np.array(faculty_percentages).reshape(-1, 1)
graduation_percentages = np.array(graduation_percentages).reshape(-1, 1)

# Calculate the correlation coefficient
correlation_coefficient = np.corrcoef(faculty_percentages[:, 0], graduation_percentages[:, 0])[0, 1]

print("Correlation coefficient:", correlation_coefficient)

