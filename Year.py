#####Leap Year Calculator######

year=int(input("Enter a year:: \n"))
if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      print("Its a Leap Year")
    else:
     print("Not a Leap Year")
  else:
    print("Its a Leap Year")
else:
  print("Not a Leap Year")
