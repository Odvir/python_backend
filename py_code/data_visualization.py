import pandas as pd 
import plotly.express as px
import psycopg2
import chart_studio
import chart_studio.tools as tls 
import chart_studio.plotly as py 

username = "jas_lin1128"
api_key = "KGZ6v6jZ0y5BIUDDBNmW"
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

# Connect to database
opt = "postgresql://jasmine:Schema1234##@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/wifi_crowdsourcing?sslmode=verify-full&sslrootcert=/Users/jasminelin/.postgresql/root.crt&options=--cluster%3Dwifi-crowdsourcing-4313"
conn = psycopg2.connect(opt)
wifi_df = pd.read_sql("SELECT * FROM wifi_data", conn)
conn.close() 

# Populate the dictionary with respective values of index, location names, the building latitude, the building longitude and radius
row0 = [0, "No Building", 0, 0]
row1 = [1, "Valley Life Sciences Building", 37.87158013361558, -122.26222526028351]
row2 = [2, "Bancroft Library", 37.872359778544826, -122.25906388911869]
row3 = [3, "David Blackwell Hall", 37.867938242407455, -122.2611852179538]
row4 = [4, "California Memorial Stadium", 37.870792588866024, -122.25076757377833]
row5 = [5, "Cory Hall", 37.875239631248874, -122.25738857562385]
row6 = [6, "Doe Library", 37.872419295531834, -122.2595170136872]
row7 = [7, "Dwinelle Hall", 37.87092038181005, -122.26063763329417]
row8 = [8, "C. V. Starr East Asian Library", 37.87371969744682, -122.26035998542721]
row9 = [9, "Evans Hall", 37.87373951445669, -122.25766920445895]
row10 = [10, "Haas School of Business", 37.871846879040795, -122.25338168911863]
row11 = [11, "Li Ka Shing Center", 37.872892390509826, -122.26532291795363]
row12 = [12, "Martin Luther King Jr. Center Student Union", 37.86901620934252, -122.26037288911863]
row13 = [13, "Moffitt Library", 37.87272746906796, -122.26085806028352]
row14 = [14, "Soda Hall", 37.87572091103949, -122.25874358727283]
row15 = [15, "Wheeler Hall", 37.871468295377646, -122.25911711610816]

building_coordinates = {'row0' : row0, 'row1' : row1, 'row2' : row2, 'row3' : row3, 'row4' : row4, 'row5' : row5, 'row6' : row6, 'row7' : row7, 'row8' : row8, 'row9' : row9, 
'row10' : row10, 'row11' : row11, 'row12' : row12, 'row3' : row3, 'row14' : row14, 'row15' : row15}

buildings = pd.DataFrame.from_dict(building_coordinates, orient='index', columns=['index', 'location_names', 'building_latitude', 'building_longitude'])

# Merge the two dataframes based on the index column 
merged_data = wifi_df.merge(buildings, how="left", left_on="building_id", right_on="index")

# Isolate the buildings that are within the radius of the different building locations
building_present_df = merged_data[merged_data["location_names"] != "No Building"]

# Group based off of the building names and take the average of the download and upload speed 
averaged_speed = building_present_df.groupby("location_names", as_index=False)["download_speed", "upload_speed", "building_latitude", "building_longitude"].mean().reset_index()

# Plot all the points in merged_data, including those with a building and without a building 
px.set_mapbox_access_token(open('access_token_mapbox.txt').read())
fig = px.scatter_mapbox(wifi_df, lat="latitude", lon="longitude", color="download_speed", 
custom_data=["wifi_name", "date_time", "upload_speed", "outage", "download_speed"], size="download_speed", color_continuous_scale=px.colors.cyclical.IceFire, 
size_max=15, zoom=15)

fig.update_traces(
    hovertemplate="<br>".join([
        "Wifi Name: %{customdata[0]}", 
        "Latitude: %{lat}", 
        "Longitude: %{lon}", 
        "Date: %{customdata[1]}", 
        "Download Speed: %{customdata[4]}", 
        "Upload Speed: %{customdata[2]}", 
        "Outage: %{customdata[3]}",
    ])
)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Plot the averaged_speed of each building
fig2 = px.scatter_mapbox(averaged_speed, lat="building_latitude", lon="building_longitude", custom_data=["location_names", "upload_speed", "download_speed"], size="download_speed", 
size_max=15, zoom=15)
fig2.update_traces(
    hovertemplate="<br>".join([
        "Building: %{customdata[0]}", 
        "Average Download Speed: %{customdata[2]}", 
        "Average Upload Speed: %{customdata[1]}",
    ])
)

# fig2.update_layout(mapbox_style="open-street-map")
# fig2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.add_trace(fig2.data[0]) # adds the line trace to the first figure
fig.update_layout(mapbox_style="carto-positron")

py.plot(fig, filename = "wifi crowdsourcing graph", auto_open=False)
fig.show()

iframe_string = tls.get_embed('https://plotly.com/~jas_lin1128/1/')





