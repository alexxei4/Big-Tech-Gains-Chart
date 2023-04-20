import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar
# Load the necessary datasets
google = pd.read_csv("GOOGL.csv")
amazon = pd.read_csv("AMZN.csv")
microsoft = pd.read_csv("MSFT.csv")
# Define a function to calculate percentage change in open column
def percentage(data):
    one_per = data[0] / 100
    return data / one_per
# Create a percentage new feature from the data
google["Pec"] = percentage(google["Open"])
amazon["Pec"] = percentage(amazon["Open"])
microsoft["Pec"] = percentage(microsoft["Open"])
# Create a month column
def month(data, column="Date"):
    data["Month"] = pd.DatetimeIndex(data[column]).month
    return data
google = month(google)
amazon = month(amazon)
microsoft = month(microsoft)
# Create 3D bar and line plot of all three datasets
fig = plt.figure(figsize=(8, 16), dpi=100)
ax = fig.add_subplot(111, projection="3d")
# Define company names and xs values
company = ["Amazon", "Microsoft", "Google"]
xs = google["Month"].index
for z in range(len(company)):
    if z == 0:
        ys = amazon["Pec"]
        ax.plot(xs, ys, zs=z, zdir="y", lw=2, color="k")
        ax.bar(xs, ys, zs=z, zdir="y", alpha=0.2)
    elif z == 1:
        ys = microsoft["Pec"]
        ax.plot(xs, ys, zs=z, zdir="y", lw=2, color="k")
        ax.bar(xs, ys, zs=z, zdir="y", alpha=0.2)
    else:
        ys = google["Pec"]
        ax.plot(xs, ys, zs=z, zdir="y", lw=2, color="k")
        ax.bar(xs, ys, zs=z, zdir="y", alpha=0.2)
# Set the number of ticks for each axis
ax.locator_params(axis="x", nbins=12)
ax.locator_params(axis="y", nbins=len(company))
ax.locator_params(axis="z", nbins=6)
a=ax.get_yticks().tolist()
a[1]='Amazon'
a[2]='Microsoft'
a[3]='Google'
ax.set_yticklabels(a)
b=ax.get_xticks().tolist()
b[1]='Jan'
b[2]='Feb'
b[3]='Mar'
b[4]='Apr'
b[5]='May'
b[6]='June'
b[7]='July'
b[8]='Aug'
b[9]='Sep'
b[10]='Oct'
b[11]='Nov'
b[12]='Dec'
ax.set_xticklabels(b)
c=ax.get_zticks().tolist()
c[1]='100%'
c[2]='110%'
c[3]='120%'
c[2]='130%'
c[3]='140%'
c[3]='150%'
ax.set_zticklabels(c)
# Customize the title and view angle of the plot
ax.set_title("Tech Stock Gains 2021", fontsize=20)
ax.view_init(elev=10, azim=-65)

plt.show()
