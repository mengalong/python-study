from tempfile import TemporaryFile, NamedTemporaryFile

f = TemporaryFile()
f.write("abcdef" * 10000)
f.seek(0)

print f.read(100)

ntf = NamedTemporaryFile()
print ntf.name
ntf = NamedTemporaryFile(delete=False)
print ntf.name

