import logging
import db_inserter as inserter
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.params.get('data')
    if data:
        inserter.write_into_db(data)