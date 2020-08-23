def main():
    # one()
    # two()
    three()
    # four()
    # five()
    # six()
    # seven()
    # eight()
    # nine()
    ten()

def one():
    line = 'カミュ'
    print(line[0])
    print(line[1])
    print(line[2])

def two():
    text1 = input('入力１：')
    text2 = input('入力２：')
    print('私は昨日{}を書いて、{}に送った！'.format(text1, text2))

def three():
    line = 'aldous Huxley was born in 1894'.title()
    print(line)

def four():
    line = "どこで？　だれが？　いつ？".split()
    print(line)

def five():
    lst = ['The','fox','jumped','over','the','fence','.']
    print(" ".join(lst[:-1]) + '.')

def six():
    print('A screaming comes across the sky.'.replace('s', '$'))

def seven():
    print('Hemingway'.index('m'))

def eight():
    print('やめてくれ！！"この人"に誰も殺させたくないんだ！！邪魔をしないでくれお願いだから！！')

def nine():
    print('three ' + 'three ' + 'three')
    print('three '* 3)

def ten():
    text = '四月の晴れた寒い日で、時計がどれも十三時を打っていた。'
    print(text[:10])

if __name__ == "__main__":
    main()
