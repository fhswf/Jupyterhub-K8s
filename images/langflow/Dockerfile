ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-scipy-nocuda:sha-2c18bf4
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME eml

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

USER $NB_UID

RUN pip install uv &&\
    uv venv &&\
    uv pip install -U langflow jhsingle-native-proxy

ENTRYPOINT ["/bin/bash", "-c", "source .venv/bin/activate && exec \"$@\"", "--"]

# Patch BASE-HREF in der built index.html
# RUN sed -i 's|<base href="/" />|<base href="./" />|' \
#     /app/.venv/lib/python3.12/site-packages/langflow/frontend/index.html
# RUN sed -i \
#   -e 's|http://localhost:7860|.|g' \
#   /app/.venv/lib/python3.12/site-packages/langflow/frontend/assets/*.js

# 2) Frontend‐Assets patchen:
ARG SITE_PACKAGES=.venv/lib/python3.12/site-packages
RUN sed -i 's|<base href="/" />|<base href="./" />|' "$SITE_PACKAGES/langflow/frontend/index.html"
RUN find "$SITE_PACKAGES/langflow/frontend/assets" -type f -name '*.js' -exec sed -i \
    -e 's|http://localhost:[0-9]\+|.|g' \
    -e 's|fetch("/|fetch("./|g' \
    -e 's|axios\.\(get\|post\)("/|axios.\1("./|g' \
    -e 's|/api/|./api/|g' \
    -e 's|/health_check|./health_check|g' \
{} +


ENV LANGFLOW_AUTO_LOGIN="true"
ENV AUTHENTICATION_DISABLED="true"
ENV DO_NOT_TRACK="true"

EXPOSE 8888

CMD ["jhsingle-native-proxy", \
     "--port", "8888", \
     "--destport", "7860", \
     "--request-timeout", "600", \
     "--ready-timeout", "60", \
     "--", \
     "python", "-m", "langflow", "run", "--host", "0.0.0.0", "--port", "7860"]

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Langflow JupyterHub"
LABEL org.opencontainers.image.description="Langflow JupyterHub"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER