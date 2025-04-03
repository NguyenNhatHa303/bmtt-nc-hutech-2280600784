from Crypto.Hash import SHA3_256

def sha3(message):
    """Tính toán mã băm SHA3-256 cho chuỗi đầu vào."""
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    """Hàm chính để minh họa việc sử dụng SHA3-256."""
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hashed_text = sha3(text)
    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("SHA-3 Hash:", hashed_text.hex())

if __name__ == "__main__":
    main()