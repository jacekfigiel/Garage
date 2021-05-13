import json

from motorcycle_klasy import Motorcycle, MotoGP, SportMotorcycle
from plotly.graph_objs import Bar, Layout
from plotly import offline

val = Motorcycle("Yamaha", "R6", 600, 120, 170, 210, 3.2, 44)
mir = Motorcycle("Suzuki", "GSR", 600, 120, 160, 230, 3.1, 44)
print(val)
compare = [val, mir]
data = []
result = val.top_speed, mir.top_speed
data.append(result)

print(data)

readable_file = "moto_garage.json"
with open(readable_file, "w") as f:
    json.dump(data, f)

x_values = compare
window = [Bar(x=x_values, y=result)]

x_axis_config = {"title": "Motorcycle model"}
y_axis_config = {"title": " Top speed"}
my_layout = Layout( title="Compering the top speed",
                    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": window, "layout": my_layout}, filename="top_speed_compare.html")