##################################################################
#       Dockerfile to build container image for playground
#       using scikit-learn + flask_restful
##################################################################

FROM ubuntu

RUN apt-get update; \
    apt-get install -y \
      python python-pip \
      python-numpy python-scipy \
      build-essential python-dev python-setuptools \
      libatlas-dev libatlas3gf-base

RUN update-alternatives --set libblas.so.3 \
      /usr/lib/atlas-base/atlas/libblas.so.3; \
    update-alternatives --set liblapack.so.3 \
      /usr/lib/atlas-base/atlas/liblapack.so.3

RUN pip install -U scikit-learn

# Install flask restful package
RUN pip install flask_restful

# Setup directory for store our brain
RUN mkdir -p /data

# Setup directory for app
RUN mkdir -p /usr/local/app
VOLUME /usr/local/app
VOLUME /data

WORKDIR /usr/local/app

COPY ./app /usr/local/app

RUN python iris.py

EXPOSE 5000

CMD ["python", "api.py"]