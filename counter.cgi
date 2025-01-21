#!/usr/bin/env bash

COUNTER_FILE="/usr/lib/cgi-bin/counter.txt"

# 確保檔案存在
if [ ! -f "$COUNTER_FILE" ]; then
    echo 0 > "$COUNTER_FILE"
fi

# 讀取當前計數值
COUNT=$(cat "$COUNTER_FILE")

# 計數器加 1
COUNT=$((COUNT + 1))

# 更新計數器檔案
echo "$COUNT" > "$COUNTER_FILE"

DIGITS=$(printf "%05d" "$COUNT")

# 生成圖片
IMAGE_FILE="/tmp/counter.png"
convert -size 300x100 xc:white -gravity center \
    -pointsize 48 -fill black -annotate 0 "$DIGITS" "$IMAGE_FILE"

echo "Content-type: image/png"
echo ""
cat "$IMAGE_FILE"
