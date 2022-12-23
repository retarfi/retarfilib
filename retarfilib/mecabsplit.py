import os
from typing import List

import MeCab


# 文章から単語リストを取得
def get_tango(sen: str) -> list[str]:
    word_list: List[str] = []
    # mecab-ipadic-neologdの場所は環境に依存するので都度変更
    tagger: MeCab.Tagger = MeCab.Tagger(
        "-r /etc/mecabrc -d {0}/local/lib/mecab/dic/mecab-ipadic-neologd".format(
            os.environ["HOME"]
        )
    )

    # UnicodeDecodeErrorを避けるおまじない(?)
    tagger.parse("")
    node: tagger.parseToNode = tagger.parseToNode(sen)
    while node:
        features: List[str] = node.feature.split(",")
        # BOS/EOSは文の開始/終了を示すもの
        if features[0] in ["名詞", "動詞", "形容詞", "副詞"] and features[1] != "数":
            # if features[0]!='BOS/EOS' and features[0]!='記号' and features[1]!='数':
            # 原形を追加
            if features[6] == "*":
                word_list.append(node.surface)
            else:
                word_list.append(features[6])
        node = node.next
    return word_list
