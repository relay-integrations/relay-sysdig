from relay_sdk import Interface, WebhookServer
from quart import Quart, request, jsonify, make_response

relay = Interface()
app = Quart('alert-created')

@app.route('/', methods=['POST'])
async def handler():

    payload = await request.get_json()
    if payload is None:
        return {'message': 'not a valid webhook'}, 400, {}

    relay.events.emit({
        'eventURL': payload['event']['url'],
        'state': payload['state'],
        'resolved': payload['resolved'],
        'condition': payload['condition'],
      })

    return {'message': 'success'}, 200, {}

if __name__ == '__main__':
    WebhookServer(app).serve_forever()
