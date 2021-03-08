import logging

import azure.functions as func

import Interact_with_nosql

def main(req: func.HttpRequest) -> func.HttpResponse:

    return Interact_with_nosql.get_all_products()
