ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/deepml:sha-7343713
FROM $BASE_CONTAINER
ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME geodata

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# # dev dependencies for geopandas
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#     libproj-dev proj-data proj-bin \
#     libgeos-dev libgeos++-dev \
#     libgdal-dev=3.10.2+dfsg-1 gdal-bin \
#     && apt-get clean \
#     && rm -rf /tmp/* /var/lib/apt/lists/*

# Install Postgres Client
RUN apt install libpq-dev \
    && apt-get clean \
    && rm -rf /tmp/* /var/lib/apt/lists/*

USER $NB_UID

# Install Python Libs
RUN pip install \
    sqlalchemy psycopg2-binary GeoAlchemy2 gdal geopandas shapely fiona rasterio osgeo rasterio.transform rasterio.warp folium pyproj requests tsfresh\
    && rm -rf /tmp/* $HOME/.cache

LABEL ki.fh-swf.de.jupyterhub.runtime="NVIDIA-GPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Image for Geo Data analysis"
LABEL org.opencontainers.image.description="Image for Geo Data analysis"
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER

LABEL ki.fh-swf.de.jupyterhub.project="geodata"
    