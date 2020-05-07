user=input('Enter you email id:')
a=user.split('@')
print('Your username is {} and your domain name is {}'.format(a[0],a[1]))  