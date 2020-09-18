# sysdig-step-alert-disable

This step can disable a [Sysdig](https://sysdig.com/) alert as part of a Relay workflow.

## Usage

```yaml
steps:
- name: disable-alert
  image: relaysh/sysdig-step-alert-disable
  spec:
    alertName: !Parameter alertName
    sysdig:
      connection:
        token: !Secret sysdigToken
```
