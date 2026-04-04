# Imports

import base64
import urllib.parse
import hashlib

# Banner

def banner():
    title = "Universal Data Converter"
    author = "Made by: Pedro Gomes"
    width = max(len(title), len(author)) + 10  

    print("-" * width)
    print(title.center(width))
    print(author.center(width))
    print("-" * width)
    print("")

# Menu

def main_menu():
    print("\n<---- Main Menu --->")
    print("\n1. Converter")
    print("\n2. Encryption")
    print("\n3. Exit")
    print("")

def converter_menu():
    print("\n<--- Converter --->")
    print("\nFormats: text, hex, bin, dec, base64, base32, base85, url")
    print("\n0. Back")
    print("")

def encryption_menu():
    print("\n<--- Encryption --->")
    print("\n1. Caesar Encrypt")
    print("\n2. Caesar Decrypt")
    print("\n3. Base64 Encode")
    print("\n4. Base64 Decode")
    print("\n5. Hash (MD5/SHA1/SHA256)")
    print("\n0. Back")
    print("")

# Converter


# Input To Bytes

def text_to_bytes(text):
    return text.encode()

def hex_to_bytes(hex_str):
    hex_str = hex_str.strip().lower().replace("0x", "")
    return bytes.fromhex(hex_str)

def bin_to_bytes(bin_str):
    bin_str = bin_str.replace(" ", "")
    return int(bin_str, 2).to_bytes((len(bin_str) + 7) // 8, byteorder='big')

def dec_to_bytes(dec_str):
    num = int(dec_str)
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big')

def base64_to_bytes(b64_str):
    return base64.b64decode(b64_str)

def base32_to_bytes(b32_str):
    return base64.b32decode(b32_str)

def base85_to_bytes(b85_str):
    return base64.b85decode(b85_str)

def url_to_bytes(url_str):
    return urllib.parse.unquote(url_str).encode()


# Bytes To Output

def bytes_to_text(b):
    return b.decode(errors="ignore")

def bytes_to_hex(b):
    return b.hex()

def bytes_to_bin(b):
    return ''.join(format(byte, '08b') for byte in b)

def bytes_to_dec(b):
    return str(int.from_bytes(b, byteorder='big'))

def bytes_to_base64(b):
    return base64.b64encode(b).decode()

def bytes_to_base32(b):
    return base64.b32encode(b).decode()

def bytes_to_base85(b):
    return base64.b85encode(b).decode()

def bytes_to_url(b):
    return urllib.parse.quote(b.decode(errors="ignore"))


# Converter

def convert(input_value, input_format, output_format):
    input_format = input_format.lower()
    output_format = output_format.lower()

    # Convert input to bytes

    if input_format == "text":
        b = text_to_bytes(input_value)
    elif input_format == "hex":
        b = hex_to_bytes(input_value)
    elif input_format == "bin":
        b = bin_to_bytes(input_value)
    elif input_format == "dec":
        b = dec_to_bytes(input_value)
    elif input_format == "base64":
        b = base64_to_bytes(input_value)
    elif input_format == "base32":
        b = base32_to_bytes(input_value)
    elif input_format == "base85":
        b = base85_to_bytes(input_value)
    elif input_format == "url":
        b = url_to_bytes(input_value)
    else:
        raise ValueError("Unsupported input format")

    # Convert to output

    if output_format == "text":
        return bytes_to_text(b)
    elif output_format == "hex":
        return bytes_to_hex(b)
    elif output_format == "bin":
        return bytes_to_bin(b)
    elif output_format == "dec":
        return bytes_to_dec(b)
    elif output_format == "base64":
        return bytes_to_base64(b)
    elif output_format == "base32":
        return bytes_to_base32(b)
    elif output_format == "base85":
        return bytes_to_base85(b)
    elif output_format == "url":
        return bytes_to_url(b)
    else:
        raise ValueError("Unsupported output format")


# Encryption 

def caesar(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result


def encode_base64(text):
    return base64.b64encode(text.encode()).decode()

def decode_base64(text):
    return base64.b64decode(text).decode()


def hash_text(text, algo="sha256"):
    if algo == "md5":
        return hashlib.md5(text.encode()).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(text.encode()).hexdigest()
    else:
        return hashlib.sha256(text.encode()).hexdigest()


# Main Program

def main():
    banner()

    while True:
        main_menu()
        choice = input("Select option: ")

        try:
            # Converter
            if choice == "1":
                while True:
                    converter_menu()
                    sub = input("Press Enter to continue or 0 to go back: ")

                    if sub == "0":
                        break

                    value = input("Enter value: ")
                    in_fmt = input("Input format: ")
                    out_fmt = input("Output format: ")

                    result = convert(value, in_fmt, out_fmt)
                    print("Result:", result)

            # Encryption
            elif choice == "2":
                while True:
                    encryption_menu()
                    sub = input("Select option: ")

                    if sub == "0":
                        break

                    if sub == "1":
                        text = input("Text: ")
                        shift = int(input("Shift: "))
                        print("Result:", caesar(text, shift))

                    elif sub == "2":
                        text = input("Text: ")
                        shift = int(input("Shift: "))
                        print("Result:", caesar(text, -shift))

                    elif sub == "3":
                        text = input("Text: ")
                        print("Result:", encode_base64(text))

                    elif sub == "4":
                        text = input("Text: ")
                        print("Result:", decode_base64(text))

                    elif sub == "5":
                        text = input("Text: ")
                        algo = input("Algorithm (md5/sha1/sha256): ").lower()
                        print("Hash:", hash_text(text, algo))

                    else:
                        print("Invalid option")

            elif choice == "3":
                break

            else:
                print("Invalid option")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
