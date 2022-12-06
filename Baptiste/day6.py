
def find_marker_index(marker_size: int) -> int:
    with open("day6.txt", "r") as f:
        buffer = f.read(marker_size)
        marker_index = marker_size
        while True:
            if len(set(buffer)) == marker_size:
                return marker_index

            marker_index += 1
            buffer = buffer[1:] + f.read(1)
            # Ignoring case where there is no marker and this loops forever


print(find_marker_index(4))
print(find_marker_index(14))
