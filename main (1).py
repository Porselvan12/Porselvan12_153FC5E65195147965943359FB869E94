def is_leap_year(year):
 if(year % 4 == 0): 
  if(year % 100 ==0) : 
    if (year%400==0):
      return True
  else:
      return False
# Example usage year = int(input("Enter a year: ")) 
 if is_leap_year(year): 
   print({}, "is a leap year")
 00else:
   print({}, "is not a leap year")