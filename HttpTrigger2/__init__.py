import logging
import azure.functions as func
import psycopg2

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.get_json()
    if data:
        write_into_db(data)
        return func.HttpResponse(
             "This HTTP triggered function executed successfully.",
             status_code=200
        )

def write_into_db(data):
    link = 'postgresql://ofir:zPfIA64Mol4tYZCf@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/wifi_crowdsourcing?sslmode=verify-full&sslrootcert=/Users/ofirdvir/.postgresql/root.crt&options=--cluster%3Dwifi-crowdsourcing-4313'
    conn = psycopg2.connect(link)
    payload = data
    with conn.cursor() as cur:
        cur.execute("INSERT INTO wifi_data (latitude, longitude, floor_id, building_id, date_time, "
                    "wifi_name, download_speed, upload_speed, outage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    vars=(payload["lat"], payload["long"], payload['flrID'], payload['bldID'], payload["dateTime"], payload["wifiName"],
                    payload["dwnldSpd"], payload["upldSpd"], payload["outage"]))

    conn.commit()
    conn.close()