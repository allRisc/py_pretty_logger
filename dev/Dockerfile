# Set base image
FROM python:3.7

# Set working directory
WORKDIR /code

# Copy the PyPI info
COPY .pypirc /root/.pypirc

# Copy the content of the local directory
COPY . .

# Install this project locally with optional dev dependencies
RUN pip install -e .[dev,deploy]
