import logging

import azure.functions as func

import Interact_with_nosql

def main(req: func.HttpRequest) -> func.HttpResponse:

    name = req.route_params.get('id')

    if name:
        logging.info(f'Python HTTP trigger function processed a get request with name:{name}')
        return Interact_with_nosql.get_single_product(name)
    else:
        logging.info('Python HTTP trigger function processed a get request')
        return Interact_with_nosql.get_all_products()
