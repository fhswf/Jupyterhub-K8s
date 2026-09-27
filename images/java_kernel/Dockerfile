ARG BASE_CONTAINER=ghcr.io/fhswf/jupyterhub-k8s/vscode-minimal-nocuda:sha-f7a5a4b

FROM $BASE_CONTAINER

ARG BASE_CONTAINER
ENV BUILD_IMAGE_NAME=programmierung

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

ENV JAVA_HOME=/opt/java/openjdk
ENV PATH=$JAVA_HOME/bin:$PATH
ENV LC_ALL=en_US.UTF-8
ENV JAVA_VERSION=jdk-25.0.4.1+1
ENV JJAVA_VERSION=1.0-a8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    maven \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget -O /tmp/openjdk.tar.gz "https://github.com/adoptium/temurin25-binaries/releases/download/${JAVA_VERSION//+/%2B}/OpenJDK25U-jdk_x64_linux_hotspot_25.0.4.1_1.tar.gz" \
    && mkdir -p "$JAVA_HOME" \
    && tar --extract --file /tmp/openjdk.tar.gz --directory "$JAVA_HOME" --strip-components 1 --no-same-owner \
    && rm -f /tmp/openjdk.tar.gz "${JAVA_HOME}/lib/src.zip" \
    && find "$JAVA_HOME/lib" -name '*.so' -exec dirname '{}' ';' | sort -u > /etc/ld.so.conf.d/docker-openjdk.conf \
    && ldconfig \
    && java -Xshare:dump

# JJava: maintained successor of IJava (IJava 1.3.0 is from 2019 and does not support current JDKs)
RUN wget -O /tmp/jjava.zip "https://github.com/dflib/jjava/releases/download/${JJAVA_VERSION}/jjava-${JJAVA_VERSION}-kernelspec.zip" \
    && unzip /tmp/jjava.zip -d /tmp/jjava \
    && jupyter kernelspec install /tmp/jjava --sys-prefix --name=java \
    && jupyter kernelspec list --json > /tmp/kernelspecs.json \
    && grep -q '"java"' /tmp/kernelspecs.json \
    && fix-permissions "$CONDA_DIR" \
    && fix-permissions "/home/$NB_USER" \
    && rm -rf /tmp/*

USER $NB_UID

LABEL ki.fh-swf.de.jupyterhub.runtime="CPU"
LABEL ki.fh-swf.de.jupyterhub.namelabel="$BUILD_IMAGE_NAME"
LABEL ki.fh-swf.de.jupyterhub.description="Java 25, Maven and JJava kernel for Grundlagen der Programmierung and Fortgeschrittene Programmierung"
LABEL org.opencontainers.image.description="Java 25 course image with Jupyter Java kernel for Grundlagen der Programmierung and Fortgeschrittene Programmierung"
LABEL org.opencontainers.image.authors="Fachhochschule Suedwestfalen"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.base.name=$BASE_CONTAINER
