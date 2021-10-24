import pandas as pd 
import plotly.express as px
import psycopg2
import chart_studio.tools as tls 

print("lmao")
# Connect to database
opt = "postgresql://jasmine:Schema1234##@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/wifi_crowdsourcing?sslmode=verify-full&sslrootcert=/Users/jasminelin/.postgresql/root.crt&options=--cluster%3Dwifi-crowdsourcing-4313"
conn = psycopg2.connect(opt)
wifi_df = pd.read_sql("SELECT * FROM wifi_data", conn)
print(wifi_df)

building_coordinates = {}

building_coordinates['Index'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

building_coordinates['Location_Names'] = ["Bancroft Library", "David Blackwell Hall", "California Memorial Stadium", "Cory Hall", "Doe Library", "Dwinelle Hall", 
"C. V. Starr East Asian Library", "Evans Hall", "Haas School of Business", "Li Ka Shing Center", "Martin Luther King Jr. Center Student Union", "Moffitt Library", 
"Soda Hall", "Valley Life Sciences Building", "Wheeler Hall"]

building_coordinates['Latitude'] = [37.872359778544826, 37.867938242407455, 37.870792588866024, 37.875239631248874, 37.872419295531834, 37.87092038181005, 37.87371969744682, 
37.87373951445669, 37.871846879040795, 37.872892390509826, 37.86901620934252, 37.87272746906796, 37.87572091103949, 37.87158013361558, 37.871468295377646]

building_coordinates['Longitude'] = [-122.25906388911869, -122.2611852179538, -122.25076757377833, -122.25738857562385, -122.2595170136872, -122.26063763329417, -122.26035998542721, 
-122.25766920445895, -122.25338168911863, -122.26532291795363, -122.26037288911863, -122.26085806028352, -122.25874358727283, -122.26222526028351, -122.25911711610816]

building_coordinates['Radius'] = [0.00000000000020]

#Converts the dictionary to a dataframe
buildings = pd.DataFrame.from_dict(building_coordinates)


# Using read_sql command to read the database (in SQL) for pandas 
# df = pandas.read_sql("SELECT ShipName, ShipCity FROM Orders WHERE ShipCountry = 'USA'", engine)

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

#What to display on the map: date_time, wifi_name, download_speed, upload_speed, etc. 

# CREATE TABLE jasmine_schema.wifi_crowdsourcing {
#     latitude FLOAT, 
#     longitude FLOAT, 
#     floor_id INT, 
#     building_id INT, 
#     date_time TIMESTAMP, 
#     wifi_name STRING 
#     download_speed INT, 
#     upload_speed FLOAT, 
#     outage BOOL
# };




