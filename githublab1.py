# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days

user_input = eval(input("Enter the minutes: "))
total_days = user_input//(60*24)
num_year = total_days // 365
remaining_days = total_days % 365
print(f"{user_input} is approxiamately {num_year} years and {remaining_days} days")