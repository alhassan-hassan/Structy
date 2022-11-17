import sys
import collections

def solution(A):
  size = len(A)
  
  if size < 4:
    return -1
  
  track = collections.defaultdict(int)
  
  for i in range(size):
    track[A[i]] += 1
    
  for key in track.keys():
    if track[key] >= 4:
      return 0
    
  
  remover = set()
  
  for key in track.keys():
    if track[key] < 2:
      remover.add(key)
      
  for key in remover:
    del(track[key])
    
  allKeys = sorted(track.keys())
  
  
  if len(allKeys) < 2:
    return -1
  
  return int(allKeys[len(allKeys) - 1]) - int(allKeys[len(allKeys) - 2])

print(solution([911,1,3,1000,1000,2,2,999,1000,911]))