ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN apk add python3

# Python 3 HTTP Server serves the current working dir
# So let's set it to our add-on persistent data directory.
WORKDIR /app

COPY app/ /app

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

RUN python3 -m venv .venv && . .venv/bin/activate && pip3 install -r requirements.txt

CMD [ "/run.sh" ]