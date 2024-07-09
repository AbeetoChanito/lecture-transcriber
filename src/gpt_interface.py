from gpt4all import GPT4All

model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
        
def get_gpt_output(lecture_transcribed: str, audio_transcribed: str, max_tokens : int = 1024):
    with model.chat_session():
        output = f"""
        You have both the text from a lecture's slideshow and its audio transcription. Please summarize the lecture.

        Lecture Transcribed:
        {lecture_transcribed}

        Audio Transcribed:
        {audio_transcribed}
        """

        return model.generate(prompt=output, max_tokens=min(max_tokens, 1024))