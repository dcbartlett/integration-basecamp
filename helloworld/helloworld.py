# Helloworld plugin

from trac.core import *
from trac.web.chrome import INavigationContributor
from trac.web.main import IRequestHandler
from trac.util import escape, Markup

class HelloWorldPlugin(Component):
    implements(INavigationContributor, IRequestHandler)

    # INavigationContributor methods
    def get_active_navigation_item(self, req):
        return 'helloworld'

    def get_navigation_items(self, req):
        yield 'mainnav', 'helloworld', Markup('<a href="%s">Hello</a>' % (
                self.env.href.helloworld() ) )

    # IRequestHandler methods
    def match_request(self, req):
        return req.path_info == '/helloworld'

    def process_request(self, req):
        req.send_response(200)
        abuffer = 'Hello world!'
        req.send_header('Content-Type', 'text/plain')
        req.send_header('Content-length', str(len(abuffer)))
        req.end_headers()
        req.write(abuffer)