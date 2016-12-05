#!/usr/bin/env python
# coding: utf-8

"""
__doc__
HASCデータのTerminalPositionの変換テーブル
"""

print(__doc__)
__author__ = "Haruyuki Ichino"
__version__ = "0.3"
__date__ = "2016/11/06"


dict = {"arm;hand":"hand", "arm;left":"hand", "arm;left;elbow":"hand", "arm;left;hand":"hand", "arm;rigft;hand":"hand", "arm;right;hand":"hand", "hand":"hand", "hand;left":"hand", "hand;right":"hand", "bag":"bag", "bag;arm;right;shoulder":"bag", "bag;back":"bag", "bag;hand":"bag", "bag;messenger":"bag", "bag;position":"bag", "bag;right;arm;shoulder":"bag", "bag;shoulder":"bag", "wear;bag":"bag", "chest":"chest", "chest;pocket":"chest", "neck":"chest", "pocket":"chest", "strap;neck":"chest", "wear;outer;chest":"chest", "wear;outer;chest;left":"chest", "wear;outer;chest;right":"chest", "wear;pans;waist;ruse;right-front":"pants-pocket", "wear;pants":"pants-pocket", "wear;pants;back;left":"pants-pocket", "wear;pants;back;right":"pants-pocket", "wear;pants;fit;right-front":"pants-pocket", "wear;pants;fit;ruse;right-rear":"pants-pocket", "wear;pants;front":"pants-pocket", "wear;pants;rear":"pants-pocket", "wear;pants;right-back;pocket":"pants-pocket", "wear;pants;right-front;pocket":"pants-pocket", "wear;pants;ruse;left-rear":"pants-pocket", "wear;pants;ruse;right-rear":"pants-pocket", "wear;pants;waist;fit;left":"pants-pocket", "wear;pants;waist;fit;left-front":"pants-pocket", "wear;pants;waist;fit;left-rear":"pants-pocket", "wear;pants;waist;fit;right":"pants-pocket", "wear;pants;waist;fit;right-back":"pants-pocket", "wear;pants;waist;fit;right-front":"pants-pocket", "wear;pants;waist;fit;right-rear":"pants-pocket", "wear;pants;waist;fit;rigtht-front":"pants-pocket", "wear;pants;waist;front":"pants-pocket", "wear;pants;waist;loose;right-front":"pants-pocket", "wear;pants;waist;right-front":"pants-pocket", "wear;pants;waist;roose;right-front":"pants-pocket", "wear;pants;waist;ruse;left":"pants-pocket", "wear;pants;waist;ruse;left-front":"pants-pocket", "wear;pants;waist;ruse;left-rear":"pants-pocket", "wear;pants;waist;ruse;right":"pants-pocket", "wear;pants;waist;ruse;right-back":"pants-pocket", "wear;pants;waist;ruse;right-front":"pants-pocket", "wear;pants;waist;ruse;right-rear":"pants-pocket", "wear;pants;weist;left-front":"pants-pocket", "wear;pants;weist;right-front":"pants-pocket", "wear;outer;waist":"waist", "wear;outer;waist;front":"waist", "wear;outer;waist;left":"waist", "wear;outer;waist;left-front":"waist", "wear;outer;waist;right":"waist", "wear;outerouter;waist;right":"waist", "wear;waist":"waist", "left;front;pants;pocket":"pants-pocket", "strap;waist;front":"waist", "wear; pants; waist; fit; left-front":"pants-pocket", "wear;outer;waist;left-front":"waist", "waist;pocket":"pants-pocket", "wear;outer;waist;left":"waist", "waist":"waist", "waist;holder":"waist", "wear;outer;waist;front":"waist", "waist;left;pocket":"pants-pocket", "wear;outer;waist;right":"waist", "waist;holder;right":"waist", "waist;pocket":"pants-pocket", "strap;waist;rear":"waist"}
# dict = {"arm;hand":"arm", "arm;left":"arm", "arm;left;elbow":"arm", "arm;left;hand":"arm", "arm;left;wrist":"arm", "arm;rigft;hand":"arm", "arm;right":"arm", "arm;right;elbow":"arm", "arm;right;hand":"arm", "arm;right;wrist":"arm", "armpit":"arm", "hand":"arm", "hand;left":"arm", "hand;right":"arm", "bag":"bag", "bag;arm;right;shoulder":"bag", "bag;back":"bag", "bag;hand":"bag", "bag;messenger":"bag", "bag;position":"bag", "bag;right;arm;shoulder":"bag", "bag;shoulder":"bag", "wear;bag":"bag", "chest":"chest", "chest;pocket":"chest", "neck":"chest", "pocket":"chest", "strap;neck":"chest", "wear;outer;chest":"chest", "wear;outer;chest;left":"chest", "wear;outer;chest;right":"chest", "wear;pans;waist;ruse;right-front":"pants-pocket", "wear;pants":"pants-pocket", "wear;pants;back;left":"pants-pocket", "wear;pants;back;right":"pants-pocket", "wear;pants;fit;right-front":"pants-pocket", "wear;pants;fit;ruse;right-rear":"pants-pocket", "wear;pants;front":"pants-pocket", "wear;pants;rear":"pants-pocket", "wear;pants;right-back;pocket":"pants-pocket", "wear;pants;right-front;pocket":"pants-pocket", "wear;pants;ruse;left-rear":"pants-pocket", "wear;pants;ruse;right-rear":"pants-pocket", "wear;pants;waist;fit;left":"pants-pocket", "wear;pants;waist;fit;left-front":"pants-pocket", "wear;pants;waist;fit;left-rear":"pants-pocket", "wear;pants;waist;fit;right":"pants-pocket", "wear;pants;waist;fit;right-back":"pants-pocket", "wear;pants;waist;fit;right-front":"pants-pocket", "wear;pants;waist;fit;right-rear":"pants-pocket", "wear;pants;waist;fit;rigtht-front":"pants-pocket", "wear;pants;waist;front":"pants-pocket", "wear;pants;waist;loose;right-front":"pants-pocket", "wear;pants;waist;right-front":"pants-pocket", "wear;pants;waist;roose;right-front":"pants-pocket", "wear;pants;waist;ruse;left":"pants-pocket", "wear;pants;waist;ruse;left-front":"pants-pocket", "wear;pants;waist;ruse;left-rear":"pants-pocket", "wear;pants;waist;ruse;right":"pants-pocket", "wear;pants;waist;ruse;right-back":"pants-pocket", "wear;pants;waist;ruse;right-front":"pants-pocket", "wear;pants;waist;ruse;right-rear":"pants-pocket", "wear;pants;weist;left-front":"pants-pocket", "wear;pants;weist;right-front":"pants-pocket", "wear;outer;waist":"waist", "wear;outer;waist;front":"waist", "wear;outer;waist;left":"waist", "wear;outer;waist;left-front":"waist", "wear;outer;waist;right":"waist", "wear;outerouter;waist;right":"waist", "wear;waist":"waist", "left;front;pants;pocket":"pants-pocket", "strap;waist;front":"waist", "wear; pants; waist; fit; left-front":"pants-pocket", "wear;outer;waist;left-front":"waist", "waist;pocket":"pants-pocket", "wear;outer;waist;left":"waist", "waist":"waist", "waist;holder":"waist", "wear;outer;waist;front":"waist", "waist;left;pocket":"pants-pocket", "wear;outer;waist;right":"waist", "waist;holder;right":"waist", "waist;pocket":"pants-pocket", "strap;waist;rear":"waist"}
# "ankle;right":"foot", "foot;left;ankle":"foot", "foot;left;upper":"foot", "foot;right;ankle":"foot", "waer;pants;foot;right;upper":"foot", "wear;outer;foot;front":"foot", "wear;outer;foot;left":"foot", "wear;outer;foot;left":"foot", "head":"head"


filter_list = ["AttachmentDirection", "("]

def classify(raw_tp):
    terminal_position = raw_tp

    # ngワードを含んでいるかのチェック
    for ng in filter_list:
        if ng in raw_tp:
            idx = raw_tp.index(ng)
            # ngワードの取り除き
            terminal_position = raw_tp[0:idx]
            break

    try:
        return dict[terminal_position]
    except:
        print("error: %s" % terminal_position)
        print("上記の端末位置に対応する変換端末位置が用意されてないで")
        return False
