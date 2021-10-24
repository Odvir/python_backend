import psycopg2

opt = "postgresql://jasmine:Schema1234##@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/wifi_crowdsourcing?sslmode=verify-full&sslrootcert=/Users/jasminelin/.postgresql/root.crt&options=--cluster%3Dwifi-crowdsourcing-4313"
conn = psycopg2.connect(opt)


with conn.cursor() as cur:
    cur.execute(
        "CREATE TABLE wifi_data (latitude FLOAT, longitude FLOAT, floor_id INT, building_id INT, date_time TIMESTAMP, wifi_name STRING, download_speed INT, upload_speed FLOAT, outage BOOL);"
    )
    cur.execute("SELECT date_time AT TIME ZONE 'UTC' AT TIME ZONE 'Pacific Standard Time' AS LocalTime FROM wifi_data;")

conn.commit()
conn.close()

