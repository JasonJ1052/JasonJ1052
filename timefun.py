from datetime import datetime
from datetime import date

print(str(datetime.now()))
today = date.today()
now = datetime.now()

# dd/mm/YY
d1 = now.strftime("%Y%m%d%H%M%S")
print("d1 =", d1)
print("Now:",now)
# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)