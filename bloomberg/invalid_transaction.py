import collections
class Solution:
    # DOES NOT PASS ALL CASES
    # def invalidTransactions(self, transactions: List[str]) -> List[str]:
    #     memo = collections.defaultdict(list)    
    #     invalid_tran = set()                   
    #     for i,transaction  in enumerate (transactions):

    #         name, time, amount, city = (int(i) if i.isnumeric() else i for i in transaction.split(','))

    #         if amount > 1000:                   
    #             invalid_tran.add(transaction)               

    #         if name in memo:            
    #             for tran in memo[name]:
    #                 _, prev_time, _, prev_city =(int(i) if i.isnumeric() else i for i in  tran.split(','))
    #                 if abs(time-prev_time) <= 60 and prev_city != city:
    #                     invalid_tran.add(tran) 
    #                     invalid_tran.add(transaction)                    

    #         memo[name].append(transaction)
    #     return invalid_tran


# DOES THE JOB O(N^2) TIME AND LINEAR SPACE
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalids = []
        trans = collections.defaultdict(list)

        for tran in transactions:
            n, t, a, c = tran.split(",")
            trans[n].append([t, a, c])

        for tran in range(len(transactions)):
            n, t, a, c = transactions[tran].split(",")
            if int(a) > 1000:
                invalids.append(transactions[tran])
            else:
                for newTran in trans[n]:
                    tm, amt, cty = newTran
                    if c != cty and abs(int(tm) - int(t)) <= 60:
                        invalids.append(transactions[tran])
                        break
        return invalids 