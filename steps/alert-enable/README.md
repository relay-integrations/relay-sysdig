# sysdig-step-alert-enable

This step can enable a [Sysdig](https://sysdig.com/) alert as part of a Relay workflow.

## Usage

```yaml
steps:
- name: enable-alert
  image: relaysh/sysdig-step-alert-enable
  spec:
    alert_name: !Parameter alertName
    sysdig:
      connection:
        token: !Secret sysdigToken
```
