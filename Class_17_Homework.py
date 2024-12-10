import time

num=int(input('Please enter the total bill: '))
num1=int(input('Please put an amount more than the bill. We will give your money back. Enter the money you will pay: '))
amount_due=num1-num

print('We are going to give $', amount_due, 'back to you.')

time.sleep(5)

print('\nProcess complete.\n\nPlease shop here again')
print('\n')