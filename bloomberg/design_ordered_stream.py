class OrderedStream:

    def __init__(self, n: int):
        self.dic = [None] * n
        self.pointer = 0
        
    def insert(self, idkey: int, value: str) -> List[str]:
        self.dic[idkey - 1] = value
        tempt = []
        while self.pointer < len(self.dic):
            if self.dic[self.pointer] == None:
                break
            tempt.append(self.dic[self.pointer])
            self.pointer += 1
            
        return tempt
            
        