import json
import os
from setuptools.command.install import install


class InstallEntry(install):

    def run(self):

        default_site = 'codeforces'
        cache_dir = os.path.join(os.path.expanduser('~'), '.cache', 'ACedIt')

        from acedit.main import supported_sites

        for site in supported_sites:
                # create cache directory structure
            if not os.path.isdir(os.path.join(cache_dir, site)):
                os.makedirs(os.path.join(cache_dir, site))

        data = {'default_site': default_site.strip(
        ), 'default_contest': None, 'cachedir': cache_dir}
        with open(os.path.join(cache_dir, 'constants.json'), 'w') as f:
            f.write(json.dumps(data, indent=2))
        install.run(self)
