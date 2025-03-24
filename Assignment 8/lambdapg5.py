test_strings = ["123", "45.67", "abc", "98a", "", "0", "-123"]


is_number = lambda s: s.replace('.','',1).isdigit() if s else False

for i in test_strings:
    print(is_number(i))