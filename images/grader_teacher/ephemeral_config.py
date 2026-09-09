
# reference: https://nbgrader.readthedocs.io/en/latest/configuration/jupyterhub_config.html
from nbgrader.auth import JupyterHubAuthPlugin
import os
c = get_config() # noqa 

# nbgrader lab image related config, note that is static in grader lab images for now (fhswf specfic)
# this needs to be rebound/set/overwritten by the spawner at runtime
# Theese config options tell local nbgrader where the notebook execution environment is (something maybe expect a nbgrader_config.py there?)
# CourseDirectory root should be the path where this file is located at?
# i.e.: '/home/test_course1/CourseDirectory/test_course1/ephemeral_config.py'
_course_name = "test_course1"
_course_path = f"/home/{_course_name}"
_course_user_dir = os.path.join(_course_path, "course_user_dir")

# ensure existance at runtime
os.makedirs(_course_path, exist_ok=True) 

c.CourseDirectory.root = os.path.join(_course_user_dir, _course_name)
c.CourseDirectory.course_id = _course_name

# course specific location of the exchange service
c.Exchange.root = os.path.join(_course_path, "nbgrader_exchange")

# ananke specific
#c.NbGrader.course_titles = {}

# /home/instructor/.jupyter/nbgrader_config.py