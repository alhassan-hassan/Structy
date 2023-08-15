# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        queue = deque([startUrl])
        visited = set()
        d_name = startUrl.split('/')[2]
        result = []

        while queue:
            url = queue.popleft()
            domain = url.split('/')[2]
            if d_name == domain and url not in visited:
                result.append(url)
                visited.add(url)

            neighbors = htmlParser.getUrls(url)
            for neighbor in neighbors:
                dom_name = neighbor.split('/')[2]
                if neighbor not in visited and d_name == dom_name:
                    queue.append(neighbor)

        return result

