class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = list()
        self.curpage = 1
        self.history.append(homepage)

    def visit(self, url: str) -> None:
        self.history = self.history[:self.curpage]
        self.history.append(url)
        self.curpage += 1

    def back(self, steps: int) -> str:
        if self.curpage - steps >= 1:
            self.curpage -= steps
            return self.history[self.curpage - 1]
        else:
            self.curpage = 1
        
            return self.history[self.curpage - 1]

    def forward(self, steps: int) -> str:
        if self.curpage + steps > len(self.history):
            self.curpage = len(self.history)
            return self.history[self.curpage - 1]
        else:
            self.curpage += steps
            return self.history[self.curpage - 1]