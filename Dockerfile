# FROM tells us where to start - which base image to use
FROM ubuntu:16.04 

# RUN gives specific instructions to the environment
RUN apt-get update -qqq
## whoami prints the user name
RUN whoami

# ENTRYPOINT dictates what happens when the computer turns on
# ENTRYPOINT ["/bin/echo","hi","world"]

# install python
RUN apt-get install python-pip python-dev build-essential -y
RUN pip install --upgrade pip

# install python libraries
RUN pip install numpy 
RUN pip install pandas
RUN pip install scipy
RUN pip install statsmodels

# add data
ADD hie_data.csv /

# add script
ADD hie_analysis.py /

# run script - CMD tells Docker to execute the command when the image loads
CMD ["python","./hie_analysis.py"]
