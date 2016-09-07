import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")

m = folium.Map(location=[df["LAT"].mean(), df["LON"].mean()], zoom_start=4)

def color(elv):

    minimum = int(min(df["ELEV"]))
    step = int((max(df["ELEV"]) - min(df["ELEV"]))/3)
    if elv in range(minimum, minimum+step):
        color = "red"
    elif elv in range(minimum+step, minimum+step*2):
        color = "green"
    else:
        color = "yellow"
    return color

#m.simple_marker(location=[45.3288, -121.6625], popup = "Mt. Hood Meadows", marker_color='green')
for lat, lon, name, elv in zip(df["LAT"], df["LON"], df["NAME"], df["ELEV"]):
    m.add_child(folium.Marker(location=[lat, lon], popup = name, icon=folium.Icon(color(elv))))



m.save(outfile='map.html')
