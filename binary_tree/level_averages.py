from collections import deque
def level_averages(root):
  if not root:
    return []
  
  res=[]
  dq = deque([root])
  
  while dq:
    tempt = []
    size = len(dq)
    for i in range(size):
      cur = dq.popleft()
      tempt.append(cur.val)
      
      if cur.left:
        dq.append(cur.left)
        
      if cur.right:
        dq.append(cur.right)
        
    res.append(sum(tempt) / len(tempt))
    
  return res
      