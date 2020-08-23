import csv

def main():
    # one()
    # two()
    three()
    four()
    
def one():
    with open('challenge8.py', 'r') as f:
        file = f.read()
        print(file)
        
def two():
    with open('question.md', 'w') as f:
        f.write(input('出身はどこですか？：'))

def three():
    movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
    with open('list.csv', 'w', newline='') as f:
        w = csv.writer(f, delimiter=',')
        for movie in movies:
            w.writerow(movie)
        
    # with open('list.csv', 'r') as f:
    #     r = csv.reader(f, delimiter=',')
    #     for row in r:
    #         print(','.join(row))
    
def four():
    with open('list_j.csv', 'w', newline='') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(['トップガン','リスキービジネス', 'マイノリティリポート'])
        w.writerow(['タイタニック', 'レヴェナント', 'インセプション'])
        w.writerow(['トレーニングデイ', 'マンオブファイヤー', 'フライト'])
    
if __name__ == "__main__":
    main()
