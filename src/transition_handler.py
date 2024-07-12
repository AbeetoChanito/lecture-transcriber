def handle_transitions(video_reader):
    transition_read_text = []

    for frame_text in video_reader:
        if len(transition_read_text) != 0 and all(e in frame_text for e in transition_read_text[-1]):
            transition_read_text.pop()

        transition_read_text.append(frame_text)

    return transition_read_text