while True :
  year = input("Enter a name of year:\n")
  try:
    year = int(year)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
      print(f"{year} is a leap year.")
    else:
      print(f"{year} isn't a leap year.")

  except ValueError:
    print("Please enter a number!")
