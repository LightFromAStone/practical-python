from re import X


expenses =  []

num_expenses = int(input('Enter # of expenses: '))

for i in range(num_expenses):
   expenses.append(float(input('Enter and expense: ')))

sum_var = 0

for expense in expenses:
   sum_var = sum_var + expense
   
print('You spent $', sum_var, ' on lunch this week', sep='')

total = sum(expenses)

print('You spent $', total, ' on lunch this week', sep='')

