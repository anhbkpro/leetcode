Input: s = "11011000"

Find balanced chunks (count = 0 points):
  1 1 0 1 1 0 0 0
  ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
  1 2 1 2 3 2 1 0 ← count values
                ↑
              count=0 → found chunk "11011000"

Since it's one chunk, extract inner: "101100"

Recursively process "101100":
  1 0 1 1 0 0
  ↓ ↓ ↓ ↓ ↓ ↓
  1 0 1 2 1 0 ← count values
    ↑       ↑
  Chunks: "10" and "1100"

Process "10": inner="" → ""
  Result: "1" + "" + "0" = "10"

Process "1100": inner="100"
  Recursively on "100":
    1 0 0
    ↓ ↓ ↓
    1 0 ← found "100"
    Inner: "0" → base case → "0"
    Result: "1" + "0" + "0" = "100"
  Result: "1" + "100" + "0" = "1100"

Chunks: ["10", "1100"]
Sort descending: ["1100", "10"]
Join: "110010"

Final wrap: "1" + "110010" + "0" = "11100100"
