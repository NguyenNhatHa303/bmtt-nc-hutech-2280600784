import hashlib

def blake2(message):
    """Tính toán mã băm BLAKE2b cho chuỗi đầu vào."""
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)
    return blake2_hash.digest()

def main():
    """Hàm chính để minh họa việc sử dụng BLAKE2b."""
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hashed_text = blake2(text)
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("BLAKE2 Hash:", hashed_text.hex())

if __name__ == "__main__":
    main()