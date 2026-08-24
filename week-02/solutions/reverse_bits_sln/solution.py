def reverseBits(n):
    result = 0

    for i in range(32):
        # Extract rightmost bit
        bit = n & 1

        # Shift result left and add bit
        result = (result << 1) | bit

        # Remove processed bit from n
        n >>= 1

    return result