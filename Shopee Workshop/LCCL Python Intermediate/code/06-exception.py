# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

# EXCEPTION HANDLING
# ======================
print()

try:
    # code may raise exception
    a = int(input('Enter a number: '))
    b = int(input('Enter another number: '))
except ValueError:
    # there is an exception, run this code
    print("Can't understand one of your input. Abort.")
else: 
    # there is no exception, run this code
    print('Sum:', a+b)
finally:
    # no matter if there is an exception or not, run this code
    print('Thanks for using this program.')

print()