
# load the config object (satisfies linters)
# traitlets config
c # noqa
# k8s_config = get_config("key") # noqa

# ===========================================================================
#         Extra Configuration for a general z2jh extended Image  
# ===========================================================================

# templates, note that already exsists in our docker image /opt/jupyterhub/hub
c.JupyterHub.template_paths = ["/opt/jupyterhub/hub/templates"]
