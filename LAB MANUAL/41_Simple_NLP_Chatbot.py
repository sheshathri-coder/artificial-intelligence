def chatbot(text):
    t=text.lower()
    if 'hello' in t: return 'Hello! How can I help you?'
    if 'python' in t: return 'Python is a programming language.'
    return 'Sorry, I do not understand.'
print(chatbot('hello'))
print(chatbot('tell me about python'))
# Output:
# Hello! How can I help you?
# Python is a programming language.