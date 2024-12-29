punctuations = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
sentence = "Hello!!!, he said ---and went."
no_punctuation = ""
for char in sentence:
    if char not in punctuations:
        no_punctuation = no_punctuation + char
print(no_punctuation)