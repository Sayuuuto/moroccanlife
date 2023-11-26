
from flask import Flask, request, jsonify

app = Flask(__name__)

# Your verify token should be a random string that you set
VERIFY_TOKEN = 'MOROCCAN_VERIFY_TOKEN'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Facebook sends a verification request
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        
        if mode and token:
            if mode == 'subscribe' and token == VERIFY_TOKEN:
                print('WEBHOOK_VERIFIED')
                return challenge
            else:
                return 'Verification token mismatch', 403
    elif request.method == 'POST':
        # Handle the message event sent by Facebook
        data = request.json

        # You can process the incoming data here

        return 'EVENT_RECEIVED', 200

if __name__ == '__main__':
    app.run(port=5000)
