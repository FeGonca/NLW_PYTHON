from src.views.http_types.http_request import HttpRequiest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''

    def validate_and_create(self, http_resquest: HttpRequiest) -> HttpResponse:
        # body = http_resquest.body
        # product_code = body["product_code"]

        # logica da regra de negocio
        print('Estou na minha view')
        print(http_resquest)
        # retorno http
        return HttpResponse(status_code=200, body={"hello": "world"})
