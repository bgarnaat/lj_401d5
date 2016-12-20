def includeme(config):
    """This function adds routes to configurator."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    # config.add_route('home', '/')
    config.add_route('lj_index', '/')
    config.add_route('lj_detail', '/lj/{id:\d+}')
    config.add_route('lj_create', '/lj/new')
    config.add_route('lj_update', '/lj/{id:\d+}/edit')
