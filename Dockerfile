FROM ubuntu:20.04
MAINTAINER Pierre Cabral

# Install requirements
RUN apt-get -y update && apt-get install -y python3 python3-pip
ADD requirements.txt /data/requirements.txt
RUN pip3 install -r /data/requirements.txt

# Copy files
ADD app.py /data/cripto-check/
ADD templates /data/cripto-check/templates

# Customise Environment
WORKDIR /data/cripto-check/
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
