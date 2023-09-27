import whisper

model = whisper.load_model('base')
result = model.transcribe('audio/audio1.mp3',fp16=False)

print(result["text"])