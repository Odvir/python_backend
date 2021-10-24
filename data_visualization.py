import pandas as pd 
import plotly.express as px
import psycopg2
import chart_studio.tools as tls 

# Connect to database
opt = "postgresql://jasmine:Schema1234##@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/wifi_crowdsourcing?sslmode=verify-full&sslrootcert=/Users/jasminelin/.postgresql/root.crt&options=--cluster%3Dwifi-crowdsourcing-4313"
conn = psycopg2.connect(opt)
wifi_df = pd.read_sql("SELECT * FROM wifi_data", conn)
conn.close() 

# Create an empty dictionary first
building_coordinates = {}

# Populate the dictionary with respective values of index, location names, the building latitude, the building longitude and radius
building_coordinates['index'] = [range(0, 17)]

building_coordinates['location_names'] = ["No Building", "Bancroft Library", "David Blackwell Hall", "California Memorial Stadium", "Cory Hall", "Doe Library", "Dwinelle Hall", 
"C. V. Starr East Asian Library", "Evans Hall", "Haas School of Business", "Li Ka Shing Center", "Martin Luther King Jr. Center Student Union", "Moffitt Library", 
"Soda Hall", "Valley Life Sciences Building", "Wheeler Hall", "The Addison Apartments"]

building_coordinates['building_latitude'] = [0, 37.872359778544826, 37.867938242407455, 37.870792588866024, 37.875239631248874, 37.872419295531834, 37.87092038181005, 37.87371969744682, 
37.87373951445669, 37.871846879040795, 37.872892390509826, 37.86901620934252, 37.87272746906796, 37.87572091103949, 37.87158013361558, 37.871468295377646, 37.871150946955936]

building_coordinates['building_longitude'] = [0, -122.25906388911869, -122.2611852179538, -122.25076757377833, -122.25738857562385, -122.2595170136872, -122.26063763329417, -122.26035998542721, 
-122.25766920445895, -122.25338168911863, -122.26532291795363, -122.26037288911863, -122.26085806028352, -122.25874358727283, -122.26222526028351, -122.25911711610816, -122.27174771266547]

# building_coordinates['radius'] = [0, 0.00000000000020, 0.00000000000020, 0.00000000000020, 0.00000000000020, 0.00000000000020, 0.00000000000020, 0.00000000000020, 0.00000000000020, 
# 0.00000000000020, 0.00000000000020, 0.00000000000020, 0.00000000000020, 0.00000000000020, 0.00000000000020, 0.00000000000020, 0.00000000000020]

# Converts the dictionary to a dataframe
buildings = pd.DataFrame.from_dict(building_coordinates)

# Merge the two dataframes based on the index column 
merged_data = wifi_df.merge(buildings, how="left", left_on="building_id", right_on="index")

# Isolate the buildings that are within the radius of the different building locations
building_present_df = merged_data[merged_data["location_names"] != "No Building"]

# Group based off of the building names and take the average of the download and upload speed 
averaged_speed = building_present_df.groupby("location_names", as_index=False)["download_speed", "upload_speed"].average().reset_index()

# Plot all the points in merged_data, including those with a building and without a building 
px.set_mapbox_access_token(open('access_token_mapbox.txt')).read()
fig = px.scatter_mapbox(wifi_df, lat="latitude", lon="longitude", color="wifi_name", custom_data=["date_time", "upload_speed", "outage"], size="download_speed")
fig.update_traces(
    hovertemplate="<br>".join([
        "Wifi Name: %{color}"
        "Latitude: %{lat}", 
        "Longitude: %{lon}", 
        "Date: %{customdata[0]}", 
        "Download Speed: %{size}", 
        "Upload Speed: %{customdata[1]}", 
        "Outage: %{customdata[2]}",
    ])
)

# Plot the averaged_speed of each building
fig2 = px.scatter_mapbox(building_coordinates, lat="building_latitude", lon="building_longitude", custom_data=["location_names", "upload_speed"], size="download_speed")
fig2.update_traces(
    hovertemplate="<br>".join([
        "Building: %{customdata[1]}", 
        "Average Download Speed: %{size}", 
        "Average Upload Speed: %{customdata[0]}",
    ])
)
fig.add_trace(fig2.data[0]) # adds the line trace to the first figure
fig.show()

# fig.update_traces(
#     hovertemplate="<br>".join([
#         "ColX: %{x}",
#         "ColY: %{y}",
#         "Col1: %{customdata[0]}",
#         "Col2: %{customdata[1]}",
#         "Col3: %{customdata[2]}",
#     ])
# )

html_string = fig.write_html("path/to/file.html")
iframe_string = tls.get_embed(html_string)





