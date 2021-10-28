import logging
from . import insterter 
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        data = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "HTTP request does not contain valid JSON data", 
            status_code = 400
        )
    if not data:
        return func.HttpResponse("No input!", status_code = 400)
    return insterter.write_into_db(data)