FROM relaysh/core:latest-python
RUN pip install sdcclient
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Sysdig Alert Disabling"
LABEL "org.opencontainers.image.description"="This step disables an alert in Sysdig"
LABEL "com.puppet.nebula.sdk.version"="v1"
