# basic structure
# import re
# text = ''
# scanner = re.Scanner([
#     (r'', lambda scanner, token: ())
# ])


import re
text = '78 lambo,48 buggati, .,lambo 98.'
scanner = re.Scanner([
    (r'\s+', lambda scanner, token: ('SPACE', token)),
    (r'\d+', lambda scanner, token:('NUMBER', token)),
    (r'\w+', lambda scanner, token: ('IDENTIFIER', token)),
    (r',', lambda scanner, token: ('PUNCTUATION', token)),
    (r'.', lambda scanner, token: ('PUNCTUATION', token)),
])
result, _ = scanner.scan(text)
print(result)