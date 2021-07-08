# Sysdig Alert Created

This [Sysdig](https://sysdig.com/) integration triggers when an alert is created.

## Data Emitted

The JSON [Sysdig alert POST data](https://docs.sysdig.com/en/configure-a-webhook-channel.html) is emitted directly by the trigger.

## Usage

For a complete usage guide, see the [Using triggers in workflows](https://relay.sh/docs/using-workflows/using-triggers/) documentation.

```yaml
parameters:
  eventURL:
    description: The sysdig event URL
  state:
    description: The sysdig event state

triggers:
- name: sysdig-trigger-alert-created
  image: relaysh/sysdig-trigger-alert-created
  binding:
    parameters:
      eventURL: !Data event_payload.event.url
      state: !Data event_payload.state

steps:
- name: slack-notify
  image: relaysh/slack-step-message-send
  spec:
    connection: !Connection { type: slack, name: my-slack }
    channel: !Parameter slackChannel
    message: !Fn.concat
    - "Got an alert: "
    - !Parameter eventURL
    - " that is "
    - !Parameter state
```

## Example Raw Data

``` json
{
    "timestamp": 1471457820000000,
    "timespan": 60000000,
    "alert": {
        "severity": 4,
        "editUrl": "http://app.sysdigcloud.com/#/alerting/alerts/1/edit",
        "scope": "host.mac = \"00:0c:29:04:07:c1\"",
        "name": "alertName",
        "description": "alertDescription",
        "id": 1
    },
    "event": {
        "id": 1,
        "url": "http://app.sysdigcloud.com/#/alerting/notifications/l:604800/1/details"
    },
    "state": "ACTIVE",
    "resolved": false,
    "entities": [
        {
            "entity": "host.mac = '00:0c:29:04:07:c1'",
            "metricValues": [
                {
                    "metric": "cpu.used.percent",
                    "aggregation": "timeAvg",
                    "groupAggregation": "none",
                    "value": 100.0
                }
            ],
            "additionalInfo": [
                {
                    "metric": "host.hostName",
                    "value": "sergio-virtual-machine"
                }
            ]
        }
    ],
    "condition": "timeAvg(cpu.used.percent) > 10"
}
```
