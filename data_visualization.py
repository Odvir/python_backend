# make sure to run "pip3 install mpld3" to install package 
# import mpld3
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine 
import chart_studio.tools as tls 

# Need to replace the line --> connection string to grab the CockroachDB database and import into a pandas dataframe
wifi_engine = create_engine("""Connection String to import cockroachDB into CSV file""")
#For the building id and such 
building_engine = create_engine()

# Using read_sql command to read the database (in SQL) for pandas 
# df = pandas.read_sql("SELECT ShipName, ShipCity FROM Orders WHERE ShipCountry = 'USA'", engine)
wifi_df = pd.read_sql("SELECT * FROM jasmine_schema.wifi_crowdsourcing", wifi_engine)

px.set_mapbox_access_token(open('access_token_mapbox.txt')).read()
fig = px.scatter_mapbox(wifi_df, lat="latitude", lon="longitude", color="wifi_name", 
custom_data=["date_time", "upload_speed", "outage"], size="download_speed")

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




