import os
from typing import List


def get_tango(sen: str) -> list[str]:
    args_mecab: str
    if os.name == "nt":
        # Windows
        args_mecab = "-r 'C:\\Program Files\\MeCab\\etc\\mecabrc' -u 'C:\\Program Files\\MeCab\\dic\\NEologd.dic'"
    elif os.name == "posix":
        # Unix
        args_mecab = (
            "-r /etc/mecabrc -d {0}/local/lib/mecab/dic/mecab-ipadic-neologd".format(
                os.environ["HOME"]
            )
        )
    else:
        raise NotImplementedError()
    mode: str
    try:
        import fugashi

        tagger: fugashi.GenericTagger = fugashi.GenericTagger(args_mecab)
        mode = "fugashi"
    except ModuleNotFoundError:
        try:
            import MeCab

            tagger: MeCab.Tagger = MeCab.Tagger(args_mecab)
            mode = "mecab-python3"
        except ModuleNotFoundError:
            raise ModuleNotFoundError("Neither fugashi nor mecab-python3 is not found")

    word_list: List[str] = []
    if mode == "fugashi":
        for line in tagger.parse(sen).split("\n"):
            if line == "EOS":
                continue
            surface: str
            str_feat: str
            surface, str_feat = line.split("\t")
            features: List[str] = str_feat.split(",")
            if features[0] in ["名詞", "動詞", "形容詞", "副詞"] and features[1] != "数":
                if features[6] == "*":
                    word_list.append(surface)
                else:
                    word_list.append(features[6])
    elif mode == "mecab-python3":
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
    else:
        raise ValueError("Invalid mode")
    return word_list
