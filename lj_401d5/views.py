from pyramid.response import Response
# from pyramid.view import view_config


# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'lj_401d5'}


def home_page(request):
    return Response("This is a home page.")


def includeme(config):
    config.add_view(home_page, route_name='home')
