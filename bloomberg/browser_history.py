# THIS SOLUTION UNLIKE THE ONE BELOW OPTIMIZES THE TIME COMPLEXITY OF THE VISIT METHOD
class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.cur, self.last  = 0, 0

    def visit(self, url: str) -> None:
        self.cur += 1

        if self.cur < len(self.urls):
            self.urls[self.cur] = url
        else:
            self.urls.append(url)
        
        self.last = self.cur
            

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.urls[self.cur]
        
    def forward(self, steps: int) -> str:
        self.cur = min(self.last, self.cur + steps)
        return self.urls[self.cur]
        
"""
COMPLEXITIES : time 0(1)
               space: 0(l * m) => l = length of strings and m => length of the urls
"""



# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.browser = [homepage]
#         self.curPage = 1

#     def visit(self, url: str) -> None:
#         self.browser = self.browser[0 : self.curPage]
#         self.browser.append(url)
#         self.curPage += 1
            

#     def back(self, steps: int) -> str:
#         state = self.curPage - steps
#         self.curPage = 1 if state < 1 else state
#         return self.browser[self.curPage - 1]
        
#     def forward(self, steps: int) -> str:
#         state = self.curPage + steps
#         self.curPage = state if state <= len(self.browser) else len(self.browser)
#         return self.browser[self.curPage - 1]
        

"""
COMPLEXITIES : time 0(n => page number because of the slicing)
               space: 0(l * m) => l = length of strings and m => length of the urls
"""

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)