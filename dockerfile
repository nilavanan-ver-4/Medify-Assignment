# Deriving the latest base image
FROM python:latest

# Labels as key value pair
LABEL Maintainer="nilavanan"

# Any working directory can be chosen as per choice like '/' or '/home' etc
WORKDIR /usr/app/src

# Copy the remote file at the working directory in container
COPY code.py ./
# Now the structure looks like this '/usr/app/src/test.py'
# Install any needed packages specified in requirements.txt
# RUN pip install  -r requirements.txt

# Install google.generativeai package
RUN pip install google-generativeai 
RUN pip install google

# CMD instruction should be used to run the software
# contained by your image, along with any arguments.
CMD [ "python", "./code.py" ]
