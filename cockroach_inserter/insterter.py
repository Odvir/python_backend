import psycopg2
import pathlib
import azure.functions as func
import logging


def write_into_db(payload: dict):
    link = f"postgresql://ofir:zPfIA64Mol4tYZCf@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/wifi_crowdsourcing?sslmode=verify-full&sslrootcert={pathlib.Path(__file__).parent}/root.crt&options=--cluster%3Dwifi-crowdsourcing-4313"
    # Could also pass in context.function_directory as an input from __init__.py
    conn = psycopg2.connect(link)
    with conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO wifi_data (latitude, longitude, floor_id, building_id, date_time, "
                        "wifi_name, download_speed, upload_speed, outage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        vars=(payload["lat"], payload["long"], payload['flrID'], payload['bldID'], payload["dateTime"], payload["wifiName"],
                        payload["dwnldSpd"], payload["upldSpd"], payload["outage"]))
            logging.info("Inserted into DB")
        except BaseException as err:
            logging.exception(str(err))
            return func.HttpResponse("Malformed JSON input", status_code = 400)
    conn.commit()
    conn.close()
    return func.HttpResponse("Payload inserted into cockroach sucessfully!", status_code = 200)

