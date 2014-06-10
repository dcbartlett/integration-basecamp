# Helloworld plugin

import re
import requests

from auth import *

from genshi.builder import tag
from trac.core import *
from trac.perm import IPermissionPolicy, IPermissionRequestor
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor, ITemplateProvider

class HelloWorldPlugin(Component):
    implements(INavigationContributor, IRequestHandler, ITemplateProvider, IPermissionPolicy)

    # IPermissionRequestor methods  
    def get_permission_actions(self):
        yield 'BASECAMP_VIEW'

    # IPermissionPolicy methods
    def check_permission(self, action, username, resource, perm):
        if resource and resource.id is not None:
            for keywords, summary in self.env.db_query(
                    "SELECT keywords, summary FROM ticket WHERE id=%s",
                    (resource.id,)):
                fields = ''.join(f for f in (keywords, summary) if f).lower()
                if 'security' in fields or 'vulnerability' in fields:
                    if 'VULNERABILITY_VIEW' not in perm:
                        return False

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
        r = requests.get(uri + '/todolists.json', auth=(bcuser, bcpass))
        data = {
            'json': r.json()
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