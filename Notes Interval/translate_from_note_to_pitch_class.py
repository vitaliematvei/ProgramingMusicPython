
from pitch_class import pitch_class
from determinate_interval import determinate_interval


def translate_from_note_to_pitch_class(f_note, s_note):
    first_note_pitch = pitch_class(f_note)
    second_note_pitch = pitch_class(s_note)

    try:
        interval = second_note_pitch - first_note_pitch
    except Exception:
        return "Bad Input!!!"

    if interval < 0:
        interval += 12
    elif interval > 11:
        interval -= 12

    result = determinate_interval(interval)
    return result