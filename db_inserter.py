import psycopg2
import Json_Parser as parser


def write_into_db(filename):
    link = 'postgresql://ofir:zPfIA64Mol4tYZCf@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/wifi_crowdsourcing?sslmode=verify-full&sslrootcert=/Users/ofirdvir/.postgresql/root.crt&options=--cluster%3Dwifi-crowdsourcing-4313'
    conn = psycopg2.connect(link)
    payload = parser.decode_jwt(filename)
    with conn.cursor() as cur:
        cur.execute("INSERT INTO wifi_data (latitude, longitude, floor_id, building_id, date_time, "
                    "wifi_name, download_speed, upload_speed, outage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    vars=(payload["lat"], payload["long"], payload['flrID'], payload['bldID'], payload["dateTime"], payload["wifiName"],
                    payload["dwnldSpd"], payload["upldSpd"], payload["outage"]))

    conn.commit()
    conn.close()

