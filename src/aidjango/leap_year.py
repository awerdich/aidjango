def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap_year(2000))  # Expected output: True
print(is_leap_year(1900))  # Expected output: False
print(is_leap_year(2024))  # Expected output: True