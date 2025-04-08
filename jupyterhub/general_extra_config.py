
# load the config object (satisfies linters)
c = get_config()  # noqa

# ===========================================================================
#         Extra Configuration for a general z2jh extended Image  
# ===========================================================================

# templates, note that already exsists in our docker image /opt/jupyterhub/hub
c.JupyterHub.template_paths = ["/opt/jupyterhub/hub/templates"]
