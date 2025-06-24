from elevenlabs import generate, save, Voice, VoiceSettings
import os


os.environ["ELEVEN_API_KEY"] = "sk_4e1eb53a02a948e3a165c748c3045f1f5c4bee64f17512cf"

def generate_audio(text: str, output_path="sample.wav"):
    audio = generate(
        text=text,
        voice=Voice(
            voice_id="UgBBYS2sOqTuMpoF3BR0",  
            settings=VoiceSettings(stability=0.5, similarity_boost=0.75)
        ),
        model="eleven_multilingual_v2"
    )
    save(audio, output_path)
    print(f"[✓] Saved audio to {output_path}")
