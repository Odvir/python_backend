import logging
from . import insterter 
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.params.get('data')
    try:
        insterter.write_into_db(data)
        return func.HttpResponse("Payload inserted into cockroach sucessfully!", status_code = 200)
    except BaseException as e:
        return func.HttpResponse(str(e), status_code = 400)