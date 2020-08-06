# sysdig-step-alert-enable

This step can enable a [Sysdig](https://sysdig.com/) alert as part of a Relay workflow.

## Specification

This step expects the following fields in the `spec` section of a workflow step definition that uses it:

| Setting      | Data type        | Description                              | Default | Required |
|--------------|------------------|------------------------------------------|---------|----------|
| `connection` | Relay connection | Sysdig connection containing API token   | None    | Yes      |
| `alert_name` | String           | Comma separated list of alerts to enable | None    | Yes      |

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
