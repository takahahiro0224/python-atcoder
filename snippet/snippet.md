# IO

- 文字列の受け取り

```python
s = input()
```

- 数値の受け取り

```python
n = int(input())
```

- 空白区切りの入力を文字列で受け取る
```python
s, t = input().split()
```

- 空白区切りの入力を数値で受け取る
```python
a, b, c, x = map(int, input().split())
```

- 空白区切りの入力をList[int]で受け取る
```
l = list(map(int, input().split()))
```

