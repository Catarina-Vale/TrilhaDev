import logging

import azure.functions as func

import Interact_with_nosql
def main(req: func.HttpRequest) -> func.HttpResponse:

    name = req.params.get('Name')
    desc = req.params.get('Desc')
    value = req.params.get('Value')
    if not name:
        return "Name is required"
    else:
        return Interact_with_nosql.post_product(name,desc,value)
