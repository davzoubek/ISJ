# minitask 2
# change the last du to DU
import re#negative lookahead
pattern = re.compile(r'(?=(du))(?!du.*du)..')
text = ['du du du', 'du po ledu', 'dopĹedu du', 'i dozadu du', 'dudu dupl', 'Rammstein du hast']
for row in text:
  print(re.sub(pattern, 'DU', row))