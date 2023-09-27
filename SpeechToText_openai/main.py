import openai
openai.api_key = "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"

with open("audio/audio1.mp3", "rb") as audio_file:
    transcript = openai.Audio.transcribe(
        file=audio_file,
        model="whisper-1",
        response_format="text",
        language="en"
    )
print(transcript)