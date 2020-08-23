def main():
    one()
    three_four()
    five()

def one():
    musicians = ['muse', 'take that', 'trivium']
    
def two():
    stations = [(35.577492, 139.558527),(35.579331, 139.572930)]

def three_four():
    personal = {'身長': 153, '好きな色': 'orange'}
    
    line = input("'身長'か'好きな色'っていれてね：")
    try:
        print(personal[line])
    except:
        print("そのキーはないよ")

def five():
    favorite_musics = {
        '椎名林檎': ['丸の内サディスティック', '依存症', '獣ゆく細道']
    }
    print(favorite_musics)

if __name__ == "__main__":
    main()
