def main():
    print(one(4))
    two("こんにちは")
    three(175, 56, 24, "かなた", "7/18")
    print(four_2(2))
    five("りな")


def one(num: int):
    """
    渡した数字の二乗を返す
    """
    return num ** 2


def two(text: str):
    """
    引数の文字列をそのまま表示する
    """
    print(text)


def three(height: int, weight: int, foot: int, name: str = "rina", date: str = "今日"):
    """
    身長と体重と足のサイズを説明する文章が表示される
    """
    print("{0}、{1}は、身長は{2}です。".format(date, name, height))
    print("{0}、{1}は、体重は{2}です。".format(date, name, weight))
    print("{0}、{1}は、足は{2}です。".format(date, name, foot))


def four_1(num: int):
    """
    引数から2を割った数を返す
    """
    return num / 2


def four_2(num: int):
    """
    引数割る2のfour_1()を受け取って4を掛ける
    """
    num = four_1(num)
    return num * 4


def five(text: str):
    """
    textをfloat型にしたValueErrorをキャッチしてエラー文を出す
    """
    try:
        print(float(text))
    except ValueError:
        print("文字列はfloatにできないよ")


if __name__ == "__main__":
    main()
