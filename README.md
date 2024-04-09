# Braille Translator
Here is a basic braille translator python class.
it translates latin chars into french braille characters.
# Install
Copy braille_translator.py and chars.json files at root of your project.
```bash
git clone git@github.com:jtarrieu/braille-translator.git
```

```python
from braille_translator import BrailleTranslator
```
# Usage
Basic string translation:
```python
text = 'Hello World!'
translator = BrailleTranslator()
braille_text = translator.text_to_braille(text)
print(braille_text)
```

Interactive shell:
> Having a spacing allow better understanding when reading braille characters in the teminal
```python
BrailleTranslator().interactive(spacing=" ")
```

Custom braille dictionnary ; you can use your own json dictionnary:
```python
translator = BrailleTranslator('<path to your dict.json>')
```
```json
// chars.json example
{
  "a": "⠁",
  "b": "⠃",
  "c": "⠉",
  "d": "⠙",
}
```