from pyramid.response import Response
# from pyramid.view import view_config
import os


# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'lj_401d5'}


HERE = os.path.dirname(__file__)


def home_page(request):
    imported_text = open(os.path.join(HERE, 'sample.txt')).read()
    return Response(imported_text)
    return Response("This is a home page.")


def includeme(config):
    config.add_view(home_page, route_name='home')
