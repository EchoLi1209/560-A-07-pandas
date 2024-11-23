# https://goheels.com/sports/mens-basketball/roster
import pandas as pd


player = {"Last Name" : ["Claude", "Brown", "Hawkins", "Davis", "Tyson","Davis",
          "Trimble", "Powell", "Jackson", "Washington"],
          "First Name" : ["Ty","James","Elliot","RJ","Cade","Elijah","Seth",
          "Drack","Ian","Jalen"],
          "Height" : [79,82,73,72,79,75,75,78,76,82],
          "Weight" : [230,215,180,180,200,215,195,195,190,235]
          }
data = pd.DataFrame(player)

# bmi = weight in KG / height in meters squared
data["bmi"] = round((data["Weight"]/2.205)/((data["Height"]/39.37)**2),2)

print(data)

data.to_csv("bmi.csv")
