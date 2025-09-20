import mistune
from mistune.renderers.markdown import MarkdownRenderer
from mistune.core import BlockState

markdown = mistune.create_markdown(renderer=None)

text = """

# heading

- item 1
- item 2
"""

tokens = markdown(text)

tokens[1]["children"][0]["raw"] = "new heading"
tokens[3]["bullet"] = "*"

renderer = MarkdownRenderer()

print(renderer(tokens, state=BlockState()))
