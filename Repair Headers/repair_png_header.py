def repair_png_header(file_path):
    # Correct PNG header
    correct_header = b'\x89PNG\r\n\x1a\n'

    with open(file_path, 'rb') as f:
        data = f.read()

    repaired_data = correct_header + data[8:]

    with open('repaired_' + file_path, 'wb') as f:
        f.write(repaired_data)

# Path to your corrupt PNG file
file_path = 'Leave_me_alone.png'
repair_png_header(file_path)
