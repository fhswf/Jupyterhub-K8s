ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-minimal-nocuda:sha-d39be35 

FROM $BASE_CONTAINER

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

ENV JAVA_HOME /opt/java/openjdk
ENV PATH $JAVA_HOME/bin:$PATH   
ENV LC_ALL='en_US.UTF-8'
ENV JAVA_VERSION jdk-20.0.1+9

RUN wget -O /tmp/openjdk.tar.gz  https://github.com/adoptium/temurin20-binaries/releases/download/jdk-20.0.1%2B9/OpenJDK20U-jdk_x64_linux_hotspot_20.0.1_9.tar.gz \
    && mkdir -p "$JAVA_HOME" \
    && tar --extract --file /tmp/openjdk.tar.gz --directory "$JAVA_HOME"  --strip-components 1 --no-same-owner \
    && rm -f /tmp/openjdk.tar.gz ${JAVA_HOME}/lib/src.zip  \
    && find "$JAVA_HOME/lib" -name '*.so' -exec dirname '{}' ';' | sort -u > /etc/ld.so.conf.d/docker-openjdk.conf \
    && ldconfig \
    && java -Xshare:dump

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    maven \
    # openjdk-17-jre \
    # openjdk-17-jdk \
    && rm -rf /var/lib/apt/lists/*

USER $NB_UID

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="java"
LABEL ki.fh-swf.de.jupyterhub.description="Java"
LABEL org.opencontainers.image.description="Java" 
LABEL org.opencontainers.image.authors="Fachhoschschule Südwestfalen"
LABEL org.opencontainers.image.licenses="MIT"