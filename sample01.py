print('hello')
print('hello day01!!!')
print('Tom')

# コメント：半角の # を書くと、　それ以降は無視されます
# メモを残す(勉強用)

# わざとエラーを起こそう！最後のカッコが抜けている！！
# SyntaxError: unexpected EOF while parsing
# SyntaxError: Syntaxは文法や構文って意味⇒構文エラー
# print('hello'

# わざとErrorその2:シングルクオートの閉じ忘れ
# SyntaxError: EOL while scanning string literal
# print('hello)

# わざとErrorその3:記号が全角(最後の閉じカッコが全角になっている)
# SyntaxError: invalid character in identifier
# print('hello'）

# 整数の基本的な演算
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)

# わざとErrorを出すコーナー
# TypeError: can only concatenate str (not "int") to str
# TypeError: データの型(≒データの種類に関するエラー)
# print('12' + 34)    # 文字の「12」と 整数の「34」 を + しようとしてるけどダメ！
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(56 + '56')




