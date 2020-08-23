def main():
    chall3()


def chall3():
    print("hello")
    print("rina")
    print("challenge")

    num = int(input())
    if num <= 10:
        print("10以下です")
    else:
        print("10以上だよ")

    if num > 25:
        print("25以上だよ")
    elif num > 10:
        print("10より大きく25より小さいよ")
    else:
        print("10より小さい")

    print(40 % 3)
    print(40 // 3)

    age = int(input())
    if age > 30:
        print("りな")
    elif age > 25:
        print("かなた")
    elif age == 2:
        print("はるき")
    elif age == 0:
        print("ちあき")


if __name__ == "__main__":
    main()
