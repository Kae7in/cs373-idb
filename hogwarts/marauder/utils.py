from haystack.utils import Highlighter

class CustomHighlight(Highlighter):

    def render_html(self, highlight_locations=None, start_offset=50, 
                    end_offset=50):
        highlighted_chunk = self.text_block[start_offset:end_offset]

        return highlighted_chunk
