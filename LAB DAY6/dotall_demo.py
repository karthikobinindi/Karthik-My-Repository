import re

text = "Hello\nWorld"

print("Without DOTALL:",
      bool(re.search("Hello.*World", text)))

print("With DOTALL:",
      bool(re.search("Hello.*World", text, re.DOTALL)))
