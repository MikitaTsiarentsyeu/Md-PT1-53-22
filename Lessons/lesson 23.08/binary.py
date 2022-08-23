chunk_size = 100

# with open("test.jpg", 'rb') as f:
#     f.seek(chunk_size*15)
#     res = f.read(chunk_size)

# with open("test.jpg", 'ab') as f:
#     f.write(res)

with open("test.jpg", 'rb') as donor:
    with open("new_test.jpg", 'wb') as receiver:
        while True:
            file_part = donor.read(chunk_size)
            if file_part:
                receiver.write(file_part)
            else:
                break

print("done!")