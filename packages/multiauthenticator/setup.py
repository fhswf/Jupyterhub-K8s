from setuptools import find_packages, setup

setup_args = dict(
    name='multiauthenticator',
    packages=find_packages(),
    version='0.1.0',
    description="JupyterHub multiauthenticator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Max Kuhmichel, FH SWF",
    author_email="kuhmichel.max@fh-swf.de",
    url="https://github.com/fhswf",
    license="MIT",
    python_requires=">=3.8",
    include_package_data=True,
    entry_points={
    'jupyterhub.authenticators': [
        'MultiAuthenticator = multiauthenticator.multiauthenticator:MultiAuthenticator',
    ],
  },
)

setup_args['install_requires'] = install_requires = []
with open('requirements.txt') as f:
    for line in f.readlines():
        req = line.strip()
        if not req or req.startswith(('-e', '#')):
            continue
        install_requires.append(req)

if __name__ == '__main__':
    setup(**setup_args)