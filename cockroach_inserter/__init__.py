import logging
from . import insterter 
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.get_json()
    if not data:
        return func.HttpResponse("No input!", status_code = 400)
    return insterter.write_into_db(data)