import psycopg2

# Make a connection with the CocokroachDB 
opt = "postgresql://daniel:phzvmt5RRQAq*3@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/wifi_crowdsourcing?sslmode=verify-full&sslrootcert=/home/dendraws/.postgresql/root.crt&options=--cluster%3Dwifi-crowdsourcing-4313"
conn = psycopg2.connect(opt)

# Executed SQL commands with conn.execute(...)
with conn.cursor() as cur:
    cur.execute(
        "DROP TABLE wifi_data;"
    )
    conn.commit()
    cur.execute(
        "CREATE TABLE wifi_data (latitude FLOAT, longitude FLOAT, floor_id INT, building_id INT, date_time TIMESTAMP, wifi_name STRING, download_speed FLOAT, upload_speed FLOAT, outage BOOL);"
    )
    cur.execute("SELECT date_time AT TIME ZONE 'UTC' AT TIME ZONE 'Pacific Standard Time' AS LocalTime FROM wifi_data;")

#Commit and close the connection 
conn.commit()
conn.close()

