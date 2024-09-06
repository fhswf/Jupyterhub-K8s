from setuptools import find_packages, setup

setup_args = dict(
    name='py_cmd_launcher_gui',
    packages=find_packages(),
    version='1.0.0',
    description="WebUI for py_cmd_launcher",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Max Kuhmichel, FH SWF",
    author_email="kuhmichel.max@fh-swf.de",
    url="https://github.com/fhswf",
    license="MIT",
    python_requires=">=3.6",
    #include_package_data=True,
    entry_points={
        'console_scripts': [
            'py_cmd_launcher_gui = py_cmd_launcher_gui.app:main',
            ]
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