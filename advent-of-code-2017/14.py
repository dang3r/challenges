def knot_hash(value):
    lengths = [ord(length) for length in value]
    lengths.extend([17, 31, 73, 47, 23])

    init = list(range(0, 256))
    pos = 0
    skip_length = 0

    for it in range(64):
        for length in lengths:
            for j in range(length // 2):
                tmp = init[(pos + j) % 256]
                init[(pos + j) % 256] = init[(pos + length - 1 - j) % 256]
                init[(pos + length - 1 - j) % 256] = tmp
            pos += (length + skip_length) % 256
            skip_length += 1

    xored  = [0] * 16
    for i in range(0, 256, 16):
        for j in range(i, i+16):
            xored[i // 16] ^= init[j]

    mapping = "0123456789abcdef"
    hash = ""
    for val in xored:
        first = val >> 4
        second = val & 15
        hash += mapping[first]
        hash += mapping[second]

    return hash

def bits(val):
    total = 0
    while val:
        total += val % 2
        val //= 2
    return total

hex_chars = dict(zip("0123456789abcdef", range(16)))
print(hex_chars)
i = "ugkiagan"
total = 0
board = [] 
for row in range(128):
    key = f"{i}-{row}"
    hash = knot_hash(key)
    total += sum([bits(hex_chars[char]) for char in hash])
    board.append("".join(["{0:04b}".format(hex_chars[char]) for char in hash]))
print(total)
print(board)
print(len(board))

def dfs(board, seen, row_idx, col_idx):
    if (row_idx, col_idx) in seen:
        return
    seen.add((row_idx, col_idx))
    if row_idx - 1 >= 0 and board[row_idx-1][col_idx] == "1":
        dfs(board, seen, row_idx - 1, col_idx)
    if row_idx + 1  < 128 and board[row_idx+1][col_idx] == "1":
        dfs(board, seen, row_idx + 1, col_idx)
    if col_idx + 1 < 128 and board[row_idx][col_idx + 1] == "1":
        dfs(board, seen, row_idx, col_idx + 1)
    if col_idx - 1 >= 0 and board[row_idx][col_idx-1] == "1":
        dfs(board, seen, row_idx, col_idx - 1)

seen = set()
total = 0
for row_idx, row in enumerate(board):
    for col_idx, col in enumerate(row):
        if (row_idx, col_idx) not in seen and board[row_idx][col_idx] == "1":
            dfs(board, seen, row_idx, col_idx)
            total += 1
print(total)
