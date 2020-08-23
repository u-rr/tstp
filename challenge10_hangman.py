import random

def main():
    words = [('cat','にゃ〜'), ('dog','わん！'), ('pig','ぶ〜'), ('bird','ぴぃ')]
    i = random.randint(0,3)
    hangman(words[i][0], words[i][1])

def hangman(word, hint):
    wrong = 0
    stages = [
        "",
        "_______        ",
        "|              ",
        "|      |       ",
        "|      O       ",
        "|     /|\      ",
        "|     / \      ",
        "|              "
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    
    while wrong < len(stages) - 1:
        char = input("文字を当ててね：")
        
        if char in rletters:
            i = rletters.index(char)
            board[i] = char
            rletters[i] = "$"
        else:
            wrong += 1
            print('ヒント：{}'.format(hint))
        print(" ".join(board))
        print("\n".join(stages[0: wrong + 1]))
        
        if "_" not in board:
            print("正解です！おめでとう！")
            print(" ".join(board))
            win = True
            break
            
    if not win:
        print("\n".join(stages))
        print("ゲームオーバーです。正解は{}".format(word))

if __name__ == "__main__":
    main()
