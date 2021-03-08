import logging

import azure.functions as func

import Interact_with_nosql

def main(req: func.HttpRequest) -> func.HttpResponse:

    name = req.route_params.get('id')

    if name:
        logging.info(f'Python HTTP trigger function processed a delete request with name:{name}')
        return Interact_with_nosql.delete_product(name)
    else:
        return "Name for deletion not provided, somehow"
