# app.py (Your Flask backend)
from flask import Flask, request, jsonify
from flask_cors import CORS # For handling CORS issues between frontend and backend
from google.adk.agents import Agent
from google.adk.tools import google_search

app = Flask(__name__)
CORS(app) # Enable CORS for your React app

# Initialize your ADK agent once when the server starts
root_agent = Agent(
   name="basic_search_agent",
   model="gemini-live-2.5-flash-preview-native-audio",
   description="Agent to answer questions using Google Search.",
   instruction="You are an expert researcher. You always stick to the facts.",
   tools=[google_search] # Make sure to add the tool if you want to use it
)

# This is a conceptual endpoint for handling microphone input
# For actual live audio streaming, you would typically use WebSockets.
@app.route('/start_audio_session', methods=['POST'])
def start_audio_session():
    # In a real application, you'd handle audio streaming here.
    # For a simple "hit the microphone" event, you might just acknowledge.
    # If using live audio, you'd set up a streaming session with the agent.

    # Example: You could start a new conversation session or just prepare for input
    print("Microphone hit! Preparing for audio input...")

    # For demonstration, let's just return a success message.
    # In a real scenario with 'gemini-live-2.5-flash-preview-native-audio',
    # you'd likely initiate an audio stream with the ADK agent here.
    # This might involve creating a session and sending audio chunks.
    # For example:
    # try:
    #     response_generator = root_agent.generate_response(audio_input_stream)
    #     # Then stream responses back to the client via WebSockets
    # except Exception as e:
    #     return jsonify({"status": "error", "message": str(e)}), 500

    return jsonify({"status": "success", "message": "Microphone activated, ready for audio!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000) # Run on port 5000s