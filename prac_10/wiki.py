import wikipedia

try:
    summary = wikipedia.summary("Chernobyl")
except wikipedia.exceptions.DisambiguationError as error:
    print(error.options)

print(type(summary))
