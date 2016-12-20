from pyramid.response import Response
# from pyramid.view import view_config
import os


# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'lj_401d5'}


HERE = os.path.dirname(__file__)


# def home_page(request):
#     imported_text = open(os.path.join(HERE, 'sample.txt')).read()
#     return Response(imported_text)
#     return Response("This is a home page.")


def includeme(config):
    # config.add_view(home_page, route_name='home')
    config.add_view(lj_index, route_name='lj_index')
    config.add_view(lj_detail, route_name='lj_detail')
    config.add_view(lj_create, route_name='lj_create')
    config.add_view(lj_update, route_name='lj_update')


def lj_index(request):
    imported_text = open(os.path.join(HERE, 'lj_index.html')).read()
    return Response(imported_text)


def lj_detail(request):
    imported_text = open(os.path.join(HERE, 'lj_detail.html')).read()
    return Response(imported_text)


def lj_create(request):
    imported_text = open(os.path.join(HERE, 'lj_create.html')).read()
    return Response(imported_text)


def lj_update(request):
    imported_text = open(os.path.join(HERE, 'lj_update.html')).read()
    return Response(imported_text)
