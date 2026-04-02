import hashlib
import itertools
import time


# -------- Detect Hash Type --------
def detect_hash(hash_value):
    length = len(hash_value)
    if length == 32:
        return "md5"
    elif length == 40:
        return "sha1"
    elif length == 64:
        return "sha256"
    elif length == 128:
        return "sha512"
    else:
        return None


# -------- Hash Function --------
def hash_text(text, algo):
    if algo == "md5":
        return hashlib.md5(text.encode()).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(text.encode()).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(text.encode()).hexdigest()
    elif algo == "sha512":
        return hashlib.sha512(text.encode()).hexdigest()


# -------- Dictionary Attack --------
def dictionary_attack(target_hash, wordlist, algo):
    start = time.time()

    for word in wordlist:
        word = word.strip()
        if hash_text(word, algo) == target_hash:
            return word, time.time() - start

    return None, time.time() - start


# -------- Brute Force Attack --------
def brute_force_attack(target_hash, charset, max_length, algo):
    start = time.time()

    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            candidate = ''.join(combo)

            if hash_text(candidate, algo) == target_hash:
                return candidate, time.time() - start

    return None, time.time() - start


# -------- Main --------
def main():
    print("=== My Cybersecurity Hash Cracker ===")

    target_hash = input("Enter hash: ")

    # NEW FEATURE: auto detect
    algo = detect_hash(target_hash)
    if not algo:
        print("Could not detect hash type!")
        return

    print(f"[+] Detected algorithm: {algo}")

    mode = input("Mode (dict/brute): ").lower()

    if mode == "dict":
        file_path = input("Enter wordlist file path: ")

        try:
            with open(file_path, "r") as f:
                wordlist = f.readlines()
        except:
            print("Error opening file!")
            return

        result, time_taken = dictionary_attack(target_hash, wordlist, algo)

    else:
        charset = "abcdefghijklmnopqrstuvwxyz0123456789"
        max_length = int(input("Max length: "))

        result, time_taken = brute_force_attack(
            target_hash, charset, max_length, algo
        )

    if result:
        print(f"[+] Password found: {result}")
    else:
        print("[-] Password not found")

    print(f"[+] Time taken: {time_taken:.2f} seconds")


if __name__ == "__main__":
    main()