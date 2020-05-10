
from datetime import date

present_date=date.today().day
present_month=date.today().month
present_year=date.today().year

birthdate=int(input('Enter your Birthdate:'))
birthmonth=int(input('Enter your Birthmonth:'))
birthyear=int(input('Enter your Birthyear:'))


if birthdate >= present_date and birthmonth >= present_month:

    dd=(present_date +30)- birthdate
    mm=((present_month -1)+12) - birthmonth
    yy=(present_year-1)-birthyear
    print('you are {} years, {} months, {} days old'.format(yy,mm,dd))


elif birthdate >= present_date and birthmonth <= present_month:

    dd=(present_date + 30)- birthdate
    mm=(present_month-1) - birthmonth
    yy=(present_year-birthyear)
    print('you are {} years, {} months, {} days old'.format(yy,mm,dd))


elif birthdate <= present_date and birthmonth >= present_month:

    dd=(present_date - birthdate)
    mm=(present_month +12)- birthmonth
    yy=(present_year- 1)-birthyear
    print('you are {} years, {} months, {} days old'.format(yy,mm,dd))



elif birthdate <= present_date and birthmonth <= present_month:

    dd=present_date-birthdate
    mm=present_month=birthmonth
    yy=present_year-birthyear
    print('you are {} years, {} months, {} days old'.format(yy,mm,dd))

else:
    print('sorry')