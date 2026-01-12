from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    resp = VoiceResponse()
    resp.say(
        "Hello! You have reached Assistly AI. How can I help you today?",
        voice="alice"
    )
    return str(resp)

if __name__ == "__main__":
    app.run()
