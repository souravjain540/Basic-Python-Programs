import zlib

# Compresses a text file then compares the original size of
# said file with the size of the compressed file and
# displays a compression ratio
with open("lorem_ipsum.txt", "rb") as file:
  data = file.read()
  compressed = zlib.compress(data, zlib.Z_BEST_COMPRESSION)

  diff = len(data) - len(compressed)
  ratio = float(diff) / float(len(data))

  print(f"Original size (bytes): {len(data)}")
  print(f"Compressed size (bytes): {len(compressed)}")
  print(f"compressed {diff} bytes with a ratio of {ratio:.2%}")