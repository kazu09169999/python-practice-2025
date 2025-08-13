print("hello test")

def add(a, b):
    return a + b

# エラーメッセージ付きassert
assert add(2, 3) == 5, f"期待値: 5, 実際の値: {add(2, 3)}"
print("テスト1: 成功")

assert add(-1, 1) == 0, f"期待値: 0, 実際の値: {add(-1, 1)}"
print("テスト2: 成功")

# 失敗するテスト（詳細なエラーメッセージ付き）
assert add(2, 3) == 6, f"期待値: 6, 実際の値: {add(2, 3)}"
print("この行は実行されません")
