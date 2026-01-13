from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

BUSINESS_NAME = "Assistly AI"
CALENDLY_LINK = "https://calendly.com/YOUR-LINK-HERE"

@app.route("/voice", methods=["POST"])
def voice():
    resp = VoiceResponse()

    gather = resp.gather(
        input="speech",
        action="/process",
        timeout=5,
        speechTimeout="auto",
        language="en-US"
    )

    gather.say(
        f"Hello, you’ve reached {BUSINESS_NAME}. "
        "I can help book an appointment, answer questions, "
        "or connect you to the owner. What would you like to do?",
        voice="Polly.Joanna"
    )

    resp.say("I didn’t catch that. Please call again.")
    return str(resp)

@app.route("/process", methods=["POST"])
def process():
    user_input = request.values.get("SpeechResult", "")
    resp = VoiceResponse()

    if "appointment" in user_input.lower() or "book" in user_input.lower():
        resp.say(
            f"No problem. I’ll text you a link to book an appointment now.",
            voice="Polly.Joanna"
        )
        resp.sms(f"Book here: {CALENDLY_LINK}")
        resp.say("Thanks for calling. Goodbye.")
    else:
        resp.say(
            "Thanks for calling. A team member will follow up shortly.",
            voice="Polly.Joanna"
        )

    return str(resp)

if __name__ == "__main__":
    app.run()
