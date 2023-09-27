import elevenlabs
elevenlabs.set_api_key("6e15aee606cd9db423a38cb8e42b7c30")
elevenlabs.voices()
voice_settings = elevenlabs.VoiceSettings(
    stability=0.5,
    similarity_boost=0.8
)
voice = elevenlabs.Voice(
    voice_id="IKne3meq5aSn9XLyUdCD",
    settings=voice_settings
)
text = ""
while text != "bye":
    audio = elevenlabs.generate(
        text=input("Enter text: "),
        api_key="6e15aee606cd9db423a38cb8e42b7c30",
        voice="Charlie",
        model="eleven_monolingual_v1",
    )
    elevenlabs.play(audio)
