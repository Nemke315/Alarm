#KOMENTAR
 
def month_input(month):
    dicmonth={'january':31,
          'february':28,
          'march':31,
          'april':30,
          'may':31,
          "jun":30,
          "july":31,
          "august":31,
          "september":30,
          "october":31,
          "november":30,
          "december":31}
    if month in dicmonth:
        days=dicmonth.get(month)
        return days
    
def day_input(days):
    day= int(input('Enter a day'))
    if day in range(days):
        return day
    else:
        return "Date out of range"  
     
def year_input(year):
    if year >=2022:
        return year
    else:
        return 'Wrong Year'
                        
def setDate():
    
    month=input('Enter a month')
    days=month_input(month)
    dan=day_input(days)
    year= int(input("Enter a year"))
    godina=year_input(year)
    
    return "Its {}.{}.{}".format(dan,month,godina)
    
print(setDate())

      
#KOMENTAR 2
   

