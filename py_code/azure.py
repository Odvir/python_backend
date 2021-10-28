import logging
import azure.functions as func
import psycopg2

def main(req: func.HttpRequest, context:func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        data = req.get_json()
    except ValueError:
        return func.HttpResponse(
             "Bad json.",
             status_code=400
        )

    if data:
        # return func.HttpResponse(
        #      "This HTTP triggered function executed successfully.",
        #      status_code=200
        # )
        write_into_db(data, context.function_directory)
        return func.HttpResponse(
             "This HTTP triggered function executed successfully.",
             status_code=200
        )

def write_into_db(data, func_dir):
    link = f'postgresql://ofir:zPfIA64Mol4tYZCf@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/wifi_crowdsourcing?sslmode=verify-full&sslrootcert={func_dir}/root.crt&options=--cluster%3Dwifi-crowdsourcing-4313'
    conn = psycopg2.connect(link)
    payload = data
    with conn.cursor() as cur:
        cur.execute("INSERT INTO wifi_data (latitude, longitude, floor_id, building_id, date_time, "
                    "wifi_name, download_speed, upload_speed, outage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    vars=(payload["lat"], payload["long"], payload['flrID'], payload['bldID'], payload["dateTime"], payload["wifiName"],
                    payload["dwnldSpd"], payload["upldSpd"], payload["outage"]))

    conn.commit()
    conn.close()