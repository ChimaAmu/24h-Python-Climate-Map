import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#Global emissions information from Our World in Data
co2_data = pd.read_csv('https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv')

#Data frame for the world using Gapminder
df = px.data.gapminder()

#Establishing choropleth graph of the world
fig_choro = px.choropleth(
	co2_data,
	locations="iso_code",
	hover_name="country",
	color="energy_per_capita",
	scope="world",
	color_continuous_scale="Plasma"
	)

#Establishing scatter graph of the world
fig_scatter = px.scatter_geo(
	df,
	locations="iso_alpha",
	hover_name="country",
	size="gdpPercap"
	)

#Overlays scatter graph on choropleth graph
fig_choro.add_trace(fig_scatter.data[0])

#Adds additional geographical information to the graph
fig_choro.update_geos(
	resolution=50,
	showocean=True, oceancolor="LightBlue",
)

#Adds labels and title
fig_choro.update_layout(
	height=500,
	margin={"r":0, "t":0, "l":0, "b":0},
	title = dict(text='Relationship Between Energy Consumption per Capita (kWh) and GDP per Capita',
			font=dict(size=20),
			automargin=True,
			yref='paper'),
	annotations = [dict(
		x=0.6,
		y=0.1,
		text='Source: <a href="https://github.com/owid/co2-data">Our World in Data</a>',
		showarrow=False
		)]
	)

fig_choro.write_html("choro_graph.html", auto_open=True)
