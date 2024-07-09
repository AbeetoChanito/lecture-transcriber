from gpt4all import GPT4All

class GPTInterface:
    def __init__(self, model: str = "orca-mini-3b-gguf2-q4_0.gguf"):
        self.model = GPT4All(model)
        
    def get_gpt_output(self, lecture_transcribed: str, audio_transcribed: str, max_tokens=1024):
        with self.model.chat_session():
            output = f"""
            You have both the text from a lecture's slideshow and its audio transcription. Please summarize the lecture.

            Lecture Transcribed:
            {lecture_transcribed}

            Audio Transcribed:
            {audio_transcribed}
            """

            return self.model.generate(prompt=output, max_tokens=min(max_tokens, 1024))