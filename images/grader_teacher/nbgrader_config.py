#this file geos to /etc/jupyter/nbgrader_config.py
# it represents the global config

from nbgrader.auth import JupyterHubAuthPlugin
c = get_config()  # noqa

c.Exchange.path_includes_course = True
c.Authenticator.plugin_class = JupyterHubAuthPlugin

c.NbGrader.logfile = '/opt/conda/envs/jhub/share/jupyter/nbgrader.log'