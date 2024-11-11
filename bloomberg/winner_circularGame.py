class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1: return n
        dq = deque([x for x in range(1, n+1)])
        winner = None

        while len(dq) != 1:
            for i in range(k - 1):
                dq.append(dq.popleft())

            dq.popleft()

        return dq.popleft()


        # if k == 1:
        #     return n

        # deq = deque([x for x in range(1, n+1)])
        # last = 0

        # while len(deq) != 1:
        #     for i in range(k - 1):
        #         popped = deq.popleft()
        #         deq.append(popped)
        #     deq.popleft()

        # return deq.popleft()


        winner = 0
        for i in range(2, n+1):
            winner = (winner + k) % i

        return winner + 1







        # winner = 0  # Initialize the winner index
        # for i in range(2, n + 1):
        #     winner = (winner + k) % i
        # return winner + 1  # Adding 1 to convert zero-based index to one-based index


            

        