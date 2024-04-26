def message(msg):
    return f"Hello, {msg}"

def main(msg):
    return message(msg)

if __name__ == "__main__":
    msg = input("Write your name:")
    print(main(msg))