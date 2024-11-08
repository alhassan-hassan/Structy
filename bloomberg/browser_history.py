class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = [homepage]
        self.curPage = 0
        self.lastPage = 0
    
    def visit(self, url: str) -> None:
        self.curPage += 1

        if self.curPage < len(self.browser):
            self.browser[self.curPage] = url
        else:
            self.browser.append(url)

        self.lastPage = self.curPage

    def back(self, steps: int) -> str:
        self.curPage = max(self.curPage - steps, 0)
        return self.browser[self.curPage]

    def forward(self, steps: int) -> str:
        self.curPage = min(self.curPage + steps, self.lastPage)
        return self.browser[self.curPage]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


# THIS SOLUTION UNLIKE THE ONE BELOW OPTIMIZES THE TIME COMPLEXITY OF THE VISIT METHOD
# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.urls = [homepage]
#         self.cur, self.last  = 0, 0

#     def visit(self, url: str) -> None:
#         self.cur += 1

#         if self.cur < len(self.urls):
#             self.urls[self.cur] = url
#         else:
#             self.urls.append(url)
        
#         self.last = self.cur
            

#     def back(self, steps: int) -> str:
#         self.cur = max(0, self.cur - steps)
#         return self.urls[self.cur]
        
#     def forward(self, steps: int) -> str:
#         self.cur = min(self.last, self.cur + steps)
#         return self.urls[self.cur]
       
        
# # class BrowserHistory:

# #     def __init__(self, homepage: str):
# #         self.browser = [homepage]
# #         self.curPage = 1

# #     def visit(self, url: str) -> None:
# #         self.browser = self.browser[0 : self.curPage]
# #         self.browser.append(url)
# #         self.curPage += 1
            

# #     def back(self, steps: int) -> str:
# #         state = self.curPage - steps
# #         self.curPage = 1 if state < 1 else state
# #         return self.browser[self.curPage - 1]
        
# #     def forward(self, steps: int) -> str:
# #         state = self.curPage + steps
# #         self.curPage = state if state <= len(self.browser) else len(self.browser)
# #         return self.browser[self.curPage - 1]
        

# """
# COMPLEXITIES : 
# """

# # Your BrowserHistory object will be instantiated and called as such:
# # obj = BrowserHistory(homepage)
# # obj.visit(url)
# # param_2 = obj.back(steps)
# # param_3 = obj.forward(steps)