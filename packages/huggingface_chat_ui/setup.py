from setuptools import find_packages, setup

with open("README.md", encoding="utf8") as f:
    readme = f.read()

setup_args = dict(
    name="huggingface_chat_ui",
    packages=find_packages(),
    version='0.1.0',
    description="JupyterHub Huggingface Chat UI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Björn Heller, FH SWF",
    author_email="heller.bjoern@fh-swf.de",
    url="https://github.com/fhswf",
    license="MIT",
    python_requires=">=3.8",
    include_package_data=True,
    package_data={"jupyter_vscodeserver_proxy": ["icons/*"]},
    entry_points={"jupyter_serverproxy_servers": ["vscode = jupyter_vscodeserver_proxy:run_vscode"] }
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
