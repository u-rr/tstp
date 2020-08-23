def main():
    # one()
    # two()
    # three()
    # four()
    five()

def one():
    dramas = ['ウォーキング・デッド', 'アントラージュ', 'ザ・ソプラノズ', 'ヴァンパイア・ダイアリーズ']
    for drama in dramas:
        print(drama)

def two():
    for i in range(25, 50):
        print(i)
        
def three():
    dramas = ['ウォーキング・デッド', 'アントラージュ', 'ザ・ソプラノズ', 'ヴァンパイア・ダイアリーズ']
    for i,drama in enumerate(dramas, 1):
        print(i, drama)

def four():
    nums = ['1', '2', '3', '4', '5']
    while True:
        c = input()
        if c == 'q':
            break
        elif c.isdecimal() and c in nums:
                print('正解')
        elif c.isdecimal() and c not in nums:
                print('不正解')
        else:
            print("数字を入力するか、qで終了します")

def five():
    lst1 = [8, 19, 148, 4]
    lst2 = [9, 1, 33, 83]
    new_lst = []

    for i in lst1:
        for j in lst2:
            new_lst.append(i * j)

    print(new_lst)

if __name__ == "__main__":
    main()
