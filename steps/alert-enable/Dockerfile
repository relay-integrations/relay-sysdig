FROM relaysh/core:latest-python
RUN pip install sdcclient
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Sysdig Alert Enable"
LABEL "org.opencontainers.image.description"="This step enables an alert in Sysdig"
LABEL "com.puppet.nebula.sdk.version"="v1"
