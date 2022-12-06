class BrowserHistory:
    def __init__(self, homepage: str):
        self.browser = [homepage]
        self.page = 1

    def visit(self, url: str) -> None:
        self.browser = self.browser[0 : self.page]
        self.browser.append(url)
        self.page += 1
        
    def back(self, steps: int) -> str:
        valid = self.page - steps
        self.page = 1 if valid < 1 else self.page - steps
        return self.browser[self.page - 1]

    def forward(self, steps: int) -> str:
        movement = self.page + steps
        self.page = movement if movement <= len(self.browser) else len(self.browser)
        return self.browser[self.page - 1]