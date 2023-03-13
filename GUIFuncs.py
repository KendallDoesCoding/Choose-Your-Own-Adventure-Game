import pygame
pygame.init()


def seperate_text_to_rows(text: str, max_width: int, font_to_use: pygame.font.Font) -> list:
    """Takes in: text to split\n max_width allowed, example: screen width\n font to use: What font will the text be rendered in \n
    RETURNS pygame.Surface renders of the text that are split according to max_width"""

    output_text_objs = []
    words = text.split(" ")
    
    # The index of 'words' where the text was longer than 'max_width'
    last_overflow_index = 0
    
    _index_in_words = 0
    # every loop add 1 more word to sentece
    while _index_in_words < len(words) + 1:
        _index_in_words += 1

        # get words that are up to current '_index_in_words'
        _text = words[last_overflow_index : _index_in_words]
        _text_render = font_to_use.render(" ".join(_text), True, (0,0,0))

        # if last word, add rest and break from loop
        if _index_in_words == len(words):
            _out_text = " ".join(words[last_overflow_index : _index_in_words])
            _final_text = font_to_use.render(_out_text, True, (0,0,0))
            output_text_objs.append(_final_text)
            break

        # if the render is wider than allowed, render the things that fit in
        if _text_render.get_size()[0] > max_width:
            _out_text = " ".join(words[last_overflow_index : _index_in_words - 1])
            _final_text = font_to_use.render(_out_text, True, (0,0,0))
            output_text_objs.append(_final_text)

            last_overflow_index = _index_in_words - 1
            _index_in_words -= 1

        
    return output_text_objs