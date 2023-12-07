from ngshare_exchange import configureExchange
c=get_config()
# Note: It's important to specify the right ngshare URL when not using k8s

# configureExchange(c, 'http://hub:8890/services/ngshare')
configureExchange(c, 'http://hub:8890/jupyterhub-dev/services/ngshare')

# Add the following to let students access courses without configuration
# For more information, read Notes for Instructors in the documentation
c.CourseDirectory.course_id = '*'