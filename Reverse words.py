def reverse_words(text):
    words=text.split(' ')
    invertendo=[]
    for i in words:
        invertendo.append(i[len(i)::-1])
    return " ".join(invertendo)
