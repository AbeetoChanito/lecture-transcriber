def handle_transitions(video_reader):
    transition_read_text = []

    for frame_text in video_reader:
        if len(transition_read_text) != 0 and all(any(text in text2 for text2 in frame_text) for text in transition_read_text[-1]):
            transition_read_text.pop()

        transition_read_text.append(frame_text)

    return "\n".join([
        " ".join(phrase)
        for phrase in transition_read_text
    ])