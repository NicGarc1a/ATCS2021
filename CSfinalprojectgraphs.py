
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("REALdata.csv")
print(df.info())


#
#
# df1 = df.groupby("Platforms").sum()
# df.plot.pie(y="Platforms", labels=df.index, colors = ['red', 'pink'], autopct = "%.2f%%")
# plt.show()

# df.plot.hist(color = "red", title= "funny title", ec="blue")
# plt.show()

df.plot(kind="scatter", x="ALBUM ", y="DANCEABILITY ", color="blue")

df.plot(kind="scatter", x="ALBUM ", y="ALBUM AVG DANCEABILITY", color="blue")
plt.show()

df.plot(kind="scatter", x="ALBUM ", y="ENERGY", color="red")
plt.show()

df.plot(kind="scatter", x="ALBUM ", y="ALBUM AVG ENERGY ", color="red")
plt.show()

df.plot(kind="scatter", x="ALBUM ", y="COLLABORATORS", color="green")
plt.show()

df.plot(kind="scatter", x="ALBUM ", y="AVERAGE COLLABORATORS", color="green")
plt.show()


df.plot(kind="scatter", x="ALBUM ", y="ALBUM METACRITIC USER REVIEW", color="yellow")
plt.show()

df.plot(kind="bar", x="ALBUM ", y="First Week Album Sales", color="yellow")
plt.show()

df.plot(kind="scatter", x="ALBUM ", y="ALBUM' AOTY USER REVIEW", color="cyan")
plt.show()

df.plot(kind="bar", x="ALBUM ", y="PLAYS SPOTIFY BY ALBUM", color="cyan")
plt.show()


df.plot(kind="scatter", x="ALBUM ", y="ALBUM GRAMMY NOMINATIONS", color="RED")
plt.show()


df.plot(kind="scatter", x="ALBUM ", y="ALBUMS PITCHFORK REVIEW", color="GREEN")
plt.show()
df.plot(kind="scatter", x="ALBUM ", y="ALBUM METACRITIC REVIEW", color="GREEN")
plt.show()



