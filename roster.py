# https://goheels.com/sports/mens-basketball/roster
import pandas as pd

roster = ["Claude", "Brown", "Hawkins", "Davis", "Tyson", "Davis", 
          "Trimble", "Powell", "Jackson", "Washington"]
player = {"Last Name" : roster,
          "First Name" : ["Ty","James","Elliot","RJ","Cade","Elijah","Seth",
          "Drack","Ian","Jalen"],
          "Height" : [67,610,61,60,67,63,63,66,64,610],
          "Weight" : [230,215,180,180,200,215,195,195,190,235]}
data = pd.DataFrame(player)
print(data)

