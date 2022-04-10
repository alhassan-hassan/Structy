class Node:
      def __init__(self, val):
    self.val = val
    self.next = None

def longest_streak(head):
  if head is None:
    return 0
  
  res = 0
  track = 1
  cur = head
  currentNode = head.next
  
  while currentNode is not None:
    if cur.val == currentNode.val:
      track += 1
    else:
      res = max(track, res)
      track = 1
      cur = currentNode
    currentNode = currentNode.next
    
  return max(res, track)
  