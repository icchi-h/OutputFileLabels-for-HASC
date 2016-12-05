#!/usr/bin/env python
# coding: utf-8

"""
__doc__
HASCデータのラベルデータ出力プログラム
"""
import glob
import os
import sys
import numpy as np
import terminal_position_table
import csv

print(__doc__)
__author__ = "Haruyuki Ichino"
__version__ = "2.0"
__date__ = "2016/12/05"


# ==========================================================
# 関数
# ==========================================================

def get_meta_info(file, meta_tag):
    """
    概要: metaファイルから指定のタグを取り出す関数
    """

    # ファイル読み出し
    f_meta = open(file)
    lines = f_meta.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
    f_meta.close()

    # Noneのエラー処理
    if "None" in lines:
        lines.remove("None")
    for line in lines:
        if line.lower().find(meta_tag.lower()) >= 0:
            meta_info = line.split(":")[1].strip()

            return meta_info

    print("指定のmeta_tagが見つからんで")
    exit(1)


#===============================================================
# 準備
#===============================================================

activity_list = ["stay", "walk", "jog", "skip", "stUp", "stDown"]
activity_count = len(activity_list)
data_path = "./data/"

# ファイル出力
f = open('result.csv', 'w')
writer = csv.writer(f, lineterminator='\n')
writer.writerow(["activity", "person", "meta_file", "terminal_positoin"])


#===============================================================
# 読み込み
#===============================================================

# dataディレクトリの存在確認
if not os.path.isdir(data_path):
    print("dataディレクトリが存在してないで")
    sys.exit(1)


##########################
# 行動ディレクトリでの処理
##########################
activities = np.sort(os.listdir(data_path))
for activity in activities:
    # .DS_Storeのチェック
    if activity == ".DS_Store":
        continue

    input_action_dir = data_path + activity + '/'

    # ディレクトリじゃない場合はスキップ
    if not os.path.isdir(input_action_dir):
        continue

    print("=================================================")
    print(input_action_dir)
    print("=================================================")

    # 被験者別の処理
    persons = np.sort(os.listdir(input_action_dir))
    print("person count =", len(persons))

    for person in persons:
        # .DS_Storeのチェック
        if person == ".DS_Store":
            continue

        input_person_dir = input_action_dir + person + '/'

        # ディレクトリじゃない場合はスキップ
        if not os.path.isdir(input_person_dir):
            continue

        meta_files = np.sort(glob.glob(input_person_dir + '*meta*'))
        # 角速度ファイルリストの作成
        # if self.using_gyro:
        #     input_gyro_files = glob.glob(input_person_dir + '*gyro*')


        print("============================================")
        print(person)
        print("============================================")

        # 加速度ファイル別の処理
        for meta_file in meta_files:
            print("---------------------------------------")
            print(meta_file)
            print("---------------------------------------")

            hasc_id = meta_file.split("/")[4].split("-")[0]
            print(hasc_id)

            # terminal positionをmetaファイルから取り出して重複がなければlistに追加
            # temp_terminal_position = get_meta_info(meta_file, "TerminalPosition")
            terminal_position = terminal_position_table.classify(get_meta_info(meta_file, "TerminalPosition"))
            if not terminal_position:
                # 対応するterminalpositionがなければスキップ
                continue

            # CSVに書き込み
            writer.writerow([activity, person, hasc_id, terminal_position])
# ファイル出力の終了処理
f.close()



