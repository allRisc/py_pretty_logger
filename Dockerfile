# Set base image
FROM ubuntu:22.04

# Pepare APT
RUN apt-get -qq update
RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y locales
RUN apt-get -qq update

RUN locale-gen en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV DEBIAN_FRONTEND noninteractive

# Install Python
RUN apt-get install -y --no-install-recommends python3.7 python3.7-distutils python3.7-dev
RUN apt-get install -y --no-install-recommends python3.8 python3.8-distutils python3.8-dev
RUN apt-get install -y --no-install-recommends python3.9 python3.9-distutils python3.9-dev
RUN apt-get install -y --no-install-recommends python3.10 python3.10-distutils python3.10-dev
RUN apt-get install -y --no-install-recommends python3.11 python3.11-distutils python3.11-dev
RUN apt-get install -y --no-install-recommends python3.12 python3.12-distutils python3.12-dev
RUN apt-get install -y --no-install-recommends python3-pip

# Setup Python
RUN pip3 install --upgrade pip
RUN pip3 install setuptools
RUN pip3 install wheel