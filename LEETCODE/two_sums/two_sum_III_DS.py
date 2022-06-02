class TwoSum:
    
    def __init__(self):
        self.numbers = []
        

    def add(self, number: int) -> None:
        self.numbers.append(number)

    def find(self, value: int) -> bool:
        dic = {}
        
        for i in range(len(self.numbers)):
            target = value - self.numbers[i]
            if target in dic:
                return True
            dic[self.numbers[i]] = target