from tokenizer import Tokenizer

with open('./tests/test.src') as test_file:
  code = test_file.read()
  tokens = Tokenizer(code)
