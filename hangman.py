#Hangman p134

import random

def hangman(target_word):
    wrong_count = 0
    hanging_stages = ["",
                      "_______     ",
                      "|     |     ",
                      "|     |     ",
                      "|     O     ",
                      "|    /|\    ",
                      "|    / \    ",
                      "|           "
                      ]
    
    targets = list(target_word)
    
    #target_wordの文字列長数だけhintの要素を _ で格納する 
    hint = ["_"] * len(target_word)
    win = False
    print("ハングマンへようこそ！")

    
    while wrong_count < len(hanging_stages) - 1:# hanging_stages の要素数だけループ処理
        print("\n")
        msg = "1文字を予想してね :"
        
        #例外処理
        answer_char = input(msg)
      
        if answer_char in targets:
              targets_index = targets.index(answer_char) #targets_index is int type
              hint[targets_index] = answer_char #hint リスト内の _ を answer_char に書き換える
              targets[targets_index] = '$'
        else:
            wrong_count += 1

        #hintの中身 ["_"] * len(target_word)の要素の間に空白文字列を挿入する
        print("".join(hint))
        
        #end = wrong_count + 1
        print("\n".join(hanging_stages[0:wrong_count+1])) #slice

        if "_" not in hint:
            print("あなたの勝ち！")
            print("".join(hint))
            win = True
            break
    if not win:
        print("\n".join(hanging_stages[0:wrong_count+1]))
        print("あなたの負け！正解は{}.".format(target_word))

def targets_list():
    word_list = ["java", "xml", "javafx","cat", "rust", "snake","pioneer", "apple", "domaindriven"]
    hangman(random.choice(word_list))

targets_list()
