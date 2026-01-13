from flask import Flask, Response
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    resp = VoiceResponse()
    resp.say(
        "Hello! You have reached Assistly A I. How can I help you today?",
        voice="alice"
    )
    return Response(str(resp), mimetype="text/xml")

if __name__ == "__main__":
    app.run()

