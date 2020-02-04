# coding: utf-8
from random import randrange


def excel(date):
    print()
    print("\n\n炭）先輩、できました〜")
    print("\nあなたは EXCEL に {} 日悩まされました．".format(date))


def exile(date):
    S = [
        "表現者が EXILE．表計算が EXCEL．",
        "セールスを記録するのが EXILE．セルに記録するのが EXCEL．",
        "新曲はヒットチャートなのが EXILE．進捗はガンチャートなのが EXCEL．",
        "真っ黒のサングラスをかけるのが EXILE．マクロの線グラフをかけるのが EXCEL．",
        "ボーカルがデュエットなのが EXILE．テーブルがピボットなのが EXCEL．",
    ]

    print()
    print("\n\n" + S[date % len(S)])
    print("\nあなたは EXILE に負けました")


def main():
    S = "CEEILX"
    S1 = "EXCEL"
    S2 = "EXILE"
    buf = " " * 5
    i = 1

    while True:
        if buf == S1:
            excel(i)
            break
        if buf == S2:
            exile(i)
            break
        r = randrange(0, 6)
        c = S[r]
        print(c, end="")
        buf = buf[1:5] + c
        i += 1
    print()


if __name__ == "__main__":
    main()
