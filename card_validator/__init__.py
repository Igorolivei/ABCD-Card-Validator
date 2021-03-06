from pyramid.config import Configurator

def main(global_config, **settings):

    config = Configurator(settings=settings)

    config.include('pyramid_jinja2')
    config.add_route('home', '/')
    config.add_route('validator_file', '/validate/file')
    config.add_route('validator_typed', '/validate/typed')
    config.add_static_view(name='style', path='card_validator:static')

    config.scan('.views')
    return config.make_wsgi_app()