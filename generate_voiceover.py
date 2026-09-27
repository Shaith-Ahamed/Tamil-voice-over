
import base64
from google import genai

# ---------------------------------------------------------
# Gemini client
# ---------------------------------------------------------
client = genai.Client()

# ---------------------------------------------------------
# Complete Tamil promotional narration
# All scenes are intentionally combined into ONE transcript.
# ---------------------------------------------------------
script = """
உங்களுக்கு தேவையான திகதி மற்றும் நேரத்தைத் தெரிவு செய்யுங்கள்.

""".strip()

# ---------------------------------------------------------
# Voice style
# IMPORTANT:
# These instructions are NOT included in the transcript.
# They are sent as speech metadata.
# ---------------------------------------------------------
voice_style = """
Professional Tamil male narrator for a medical-service
promotional video.

Use natural Sri Lankan Tamil pronunciation.
Warm, calm, reassuring and professional.
Moderate speaking pace with clear articulation.
Sound natural and human, not robotic.
Maintain one consistent narrator identity throughout
the entire recording.

Pronounce the English words naturally when they appear,
including booking, tracking, platform, phone number, OTP,
register, verify, sign in, map, pickup location, destination,
distance, route, vehicle types, confirmation, drivers,
assignments, status, real time, dashboard, settings,
password and online.

Use natural short pauses at commas and slightly longer
pauses between sentences.
Do not sound overly dramatic.
Do not change voice character or accent during the narration.
"""

# ---------------------------------------------------------
# Generate ONE continuous audio file
# ---------------------------------------------------------
interaction = client.interactions.create(
    model="gemini-3.8-flash-tts",
    input=[
        {
            "type": "user_input",
            "content": [
                {
                    "type": "text",
                    "text": script,
                    "annotations": [
                        {
                            "type": "speech_metadata",
                            "style": voice_style,
                        }
                    ],
                }
            ],
        }
    ],
    response_format={
        "type": "audio"
    },
    generation_config={
        "speech_config": [
            {
                "voice": "Kore"
            }
        ]
    },
)

# ---------------------------------------------------------
# Save the complete narration as ONE WAV file
# ---------------------------------------------------------
output_file = "st_johns_ambulance_tamil_voiceover.wav"

with open(output_file, "wb") as f:
    f.write(base64.b64decode(interaction.output_audio.data))

print()
print("Voice-over generated successfully.")
print(f"Output: {output_file}")

