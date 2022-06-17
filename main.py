#input starting salary, percentage increase, and number of years
startingSalary = float(input("Enter teacher's starting salary: $"))
percentage = int(input("Enter percentage increase to salary each year (in %): "))
years = int(input("Enter number years teacher has been working: "))

#turn the percentage into a decimal number, make the starting salary into salary
rate = float(percentage/100)
salary = startingSalary

print("\nYear |Salary")
for year in range(years):
  print("%-5d|$%0.2f" % (year + 1, salary))
  salary += (salary*rate)