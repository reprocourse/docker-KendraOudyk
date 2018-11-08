# FROM tells us where to start
## here we're using a base image from a registry (DockerHub) to build a base image of an Ubuntu operating system
FROM ubuntu:16.04 

# RUN gives specific instructions to the environment
RUN apt-get update -qqq
## whoami prints the user name
RUN whoami

# ENTRYPOINT dictates what happens when the computer turns on
ENTRYPOINT ["/bin/echo","hi","world"]

# install python
CMD ["sudo","apt-get","install","python"]

# install python libraries
CMD ["sudo", "pip", "install", "numpy"]
CMD ["sudo", "pip", "install", "pandas"]
CMD ["sudo", "pip", "install", "statsmodels"]

# add data
ADD hie_data.csv

# add script
ADD hie_analysis.py

CMD ["python","./hie_analysis.py"]

