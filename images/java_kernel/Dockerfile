ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-minimal-nocuda:sha-f7a5a4b

FROM $BASE_CONTAINER

ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME=fortgeschrittene_programmierung

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

ENV JAVA_HOME=/opt/java/openjdk
ENV PATH=$JAVA_HOME/bin:$PATH
ENV LC_ALL=en_US.UTF-8
ENV JAVA_VERSION=jdk-21.0.9+10
ENV IJAVA_VERSION=1.3.0

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    maven \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O /tmp/openjdk.tar.gz "https://github.com/adoptium/temurin21-binaries/releases/download/${JAVA_VERSION//+/%2B}/OpenJDK21U-jdk_x64_linux_hotspot_21.0.9_10.tar.gz" \
    && mkdir -p "$JAVA_HOME" \
    && tar --extract --file /tmp/openjdk.tar.gz --directory "$JAVA_HOME" --strip-components 1 --no-same-owner \
    && rm -f /tmp/openjdk.tar.gz "${JAVA_HOME}/lib/src.zip" \
    && find "$JAVA_HOME/lib" -name '*.so' -exec dirname '{}' ';' | sort -u > /etc/ld.so.conf.d/docker-openjdk.conf \
    && ldconfig \
    && java -Xshare:dump

RUN wget -O /tmp/ijava.zip "https://github.com/SpencerPark/IJava/releases/download/v${IJAVA_VERSION}/ijava-${IJAVA_VERSION}.zip" \
    && unzip /tmp/ijava.zip -d /tmp/ijava \
    && python3 /tmp/ijava/install.py --sys-prefix \
    && sed -i 's/"display_name": "Java"/"display_name": "Java (jjava)"/' "${CONDA_DIR}/share/jupyter/kernels/java/kernel.json" \
    && jupyter kernelspec list --json > /tmp/kernelspecs.json \
    && grep -q '"java"' /tmp/kernelspecs.json \
    && fix-permissions "$CONDA_DIR" \
    && fix-permissions "/home/$NB_USER" \
    && rm -rf /tmp/*

USER $NB_UID

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Java 21, Maven and IJava kernel for Fortgeschrittene Programmierung"
LABEL org.opencontainers.image.description="Java 21 course image with Jupyter Java kernel for Fortgeschrittene Programmierung"
LABEL org.opencontainers.image.authors="Fachhochschule Suedwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER
