from re import compile


class Tokenizer:
  __TOKEN_TYPES__ = [
    ['def', r'/\bdef\b/'],
    ['end', r'/\bend\b/'],
    ['identifier', r'/\b[a-zA-Z]+\b/'],
    ['integers', r'/\b[0-9]+\b/'],
    ['o_paren', r'/\(/'],
    ['c_paren', r'/\)/'],
  ]

  def  __init__(self, code):
    self.code = code

  # def tokenize(self):
  #   while not len(self.code) == 0:
