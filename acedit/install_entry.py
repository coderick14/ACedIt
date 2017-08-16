import json
import os
from setuptools.command.install import install


class InstallEntry(install):

    def run(self):

		default_site = 'codeforces'
		workdir = os.path.join(os.path.expanduser('~'), 'ACedIt')
		cache_dir = os.path.join(os.path.expanduser('~'), '.cache', 'ACedIt')

		from main import supported_sites

		for site in supported_sites:
			# create cache directory and working directory structure
		    if not os.path.isdir(os.path.join(cache_dir, site)):
		        os.makedirs(os.path.join(cache_dir, site))
		    if not os.path.isdir(os.path.join(workdir, site)):
		    	os.makedirs(os.path.join(workdir, site))

		data = {'default_site': default_site.strip(), 'workdir': os.path.expanduser('~'),
		        'cachedir': cache_dir}
		with open(os.path.join(cache_dir, 'constants.json'), 'w') as f:
		    f.write(json.dumps(data, indent=2))
		install.run(self)