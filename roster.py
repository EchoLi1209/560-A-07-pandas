# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

roster = ["Claude", "Brown", "Hawkins", "Davis", "Tyson", "Davis", 
          "Withers", "Powell", "Jackson", "Washington"]
player = {"Last Name" : roster}
data = pd.DataFrame(player)
print(data)

