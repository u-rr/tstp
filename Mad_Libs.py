import re

text = """キリンは大昔から ＿＿複数名刺＿＿ の興味の対象でした。
キリンは ＿＿複数名詞＿＿ の中で一番背が高いですが、科学者たちはそのような
長い ＿＿体の一部＿＿ をどうやって獲得したのか説明できません。
キリンの身長は ＿＿数値＿＿ ＿＿単位＿＿ 近くあり、その高さのほとんどは脚と ＿＿体の一部＿＿ によるものです。
"""

def mad_libs(text):
    """
    :param mls: 文字列で、ユーザーに入力してもらいたい単語（ヒント）の部分は
    後を２つのアンダースコアで挟んでください。ヒントの単語にはアンダースコアを含めないでください。
    """
    hints = re.findall("＿＿.*?＿＿", text)
    if hints is not None:
        for word in hints:
            new = input('{}を入力'.format(word))
            text = text.replace(word, new)
        print('\n')
        text = text.replace('\n', '')
        print(text)
    else:
        print('引数textが無効です')
        
mad_libs(text)
