def replace_polish_chars(text):
  mapping = {
    'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l',
    'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'
  }
  for k, v in mapping.items():
    text = text.replace(k, v)
  return text