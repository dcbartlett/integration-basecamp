# Helloworld plugin

from trac.core import *
from trac.web.chrome import INavigationContributor, ITemplateProvider
from trac.web.main import IRequestHandler
from trac.util import escape, Markup

class HelloWorldPlugin(Component):
	implements(INavigationContributor, IRequestHandler, ITemplateProvider)

	# INavigationContributor methods
	def get_active_navigation_item(self, req):
		return 'helloworld'

	def get_navigation_items(self, req):
		yield 'mainnav', 'helloworld', Markup('<a href="%s">Hello</a>' % (
			self.env.href.helloworld()
			)
		)

	# IRequestHandler methods
	def match_request(self, req):
		return req.path_info == '/helloworld'

	def process_request(self, req):
		return 'helloworld.cs', None

	# ITemplateProvider methods
	def get_templates_dirs(self):
		"""Return a list of directories containing the provided ClearSilver
		templates.
		"""

		from pkg_resources import resource_filename
		return [resource_filename(__name__, 'templates')]