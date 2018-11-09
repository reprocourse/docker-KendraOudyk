# base image
FROM ubuntu:16.04
RUN apt-get update -qqq
RUN whoami

# install python
RUN apt-get install python-pip python-dev build-essential -y
RUN pip install --upgrade pip

# install python libraries
RUN pip install numpy
RUN pip install pandas
RUN pip install scipy
RUN pip install statsmodels

# add script
ADD hie_analysis.py /opt/hie_analysis.py

# run analysis
ENTRYPOINT ["python", "/opt/hie_analysis.py"] 

# add data (added in a volume in the command to run the image)
CMD 
