import numpy as np

def main():
    print("Hallo World")
    with open("test4.txt", "w") as f:
        f.write("Hi")
    print(np.abs(3.5))

if __name__ == "__main__":
    main()