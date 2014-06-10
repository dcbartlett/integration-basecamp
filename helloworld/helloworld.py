# Helloworld plugin

import re
import requests

from auth import *

from genshi.builder import tag
from trac.core import *
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor, ITemplateProvider

class HelloWorldPlugin(Component):
    implements(INavigationContributor, IRequestHandler, ITemplateProvider)

    # INavigationContributor methods
    def get_active_navigation_item(self, req):
        return 'helloworld'

    def get_navigation_items(self, req):
        yield ('mainnav', 'helloworld',
               tag.a('Hello World', href=req.href.helloworld()))

    # IRequestHandler methods
    def match_request(self, req):
        return re.match(r'/helloworld(?:_trac)?(?:/.*)?$', req.path_info)

    def process_request(self, req):

    	uri = 'https://basecamp.com/1759332/api/v1'
    	r = requests.get( uri + '/todolists.json', auth=(bcuser, bcpass))
        data = {
        	json: r.json()
        }
        # This tuple is for Genshi (template_name, data, content_type)
        # Without data the trac layout will not appear.
        return 'helloworld.html', data, None

    # ITemplateProvider methods
    # Used to add the plugin's templates and htdocs 
    def get_templates_dirs(self):
        from pkg_resources import resource_filename
        return [resource_filename(__name__, 'templates')]

    def get_htdocs_dirs(self):
        return []