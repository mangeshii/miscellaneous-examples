import time

second=int(input('Enter in seconds:'))

for i in range(second):
    print((second-i))
    
    time.sleep(1)

print('TIME UP!!')   