class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # # Step 1: Parse transactions into a list of dictionaries for easier handling
        # parsed_transactions = []
        # for i, transaction in enumerate(transactions):
        #     name, time, amount, city = transaction.split(',')
        #     parsed_transactions.append({
        #         'index': i,
        #         'name': name,
        #         'time': int(time),
        #         'amount': int(amount),
        #         'city': city
        #     })
        
        # # Step 2: Use a set to keep track of invalid transaction indices
        # invalid_indices = set()
        
        # # Step 3: Group transactions by name for efficient comparison
        # transactions_by_name = collections.defaultdict(list)
        # for transaction in parsed_transactions:
        #     transactions_by_name[transaction['name']].append(transaction)
        
        # # Step 4: Check each transaction for the two invalid conditions
        # for transaction in parsed_transactions:
        #     # Condition 1: Check if amount > 1000
        #     if transaction['amount'] > 1000:
        #         invalid_indices.add(transaction['index'])
            
        #     # Condition 2: Check for other transactions with the same name in different cities within 60 minutes
        #     for other in transactions_by_name[transaction['name']]:
        #         if transaction['index'] != other['index']:
        #             time_diff = abs(transaction['time'] - other['time'])
        #             if time_diff <= 60 and transaction['city'] != other['city']:
        #                 invalid_indices.add(transaction['index'])
        #                 invalid_indices.add(other['index'])
        
        # # Step 5: Collect invalid transactions based on indices
        # result = [transactions[i] for i in invalid_indices]
        # return result

        if not transactions:
            return []

        trans = collections.defaultdict(list)
        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            trans[name].append([time, amount, city])

        invalid = []

        for transaction in transactions:
            name, time, amount, city = transaction.split(",")
            if int(amount) > 1000:
                invalid.append(transaction)
            else:
                for sameTransactionsName in trans[name]:
                    newTime, newAmount, newCity = sameTransactionsName
                    if city != newCity and abs(int(time) - int(newTime)) <= 60:
                        invalid.append(transaction)
                        break
        return invalid


        # invalids = []
        # trans = collections.defaultdict(list)

        # for tran in transactions:
        #     n, t, a, c = tran.split(",")
        #     trans[n].append([t, a, c])

        # for tran in range(len(transactions)):
        #     n, t, a, c = transactions[tran].split(",")
        #     if int(a) > 1000:
        #         invalids.append(transactions[tran])
        #     else:
        #         for newTran in trans[n]:
        #             tm, amt, cty = newTran
        #             if c != cty and abs(int(tm) - int(t)) <= 60:
        #                 invalids.append(transactions[tran])
        #                 break

        # return invalids