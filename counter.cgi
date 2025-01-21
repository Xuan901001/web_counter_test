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

# 將數字拆分為一個個字符
DIGITS=$(printf "%05d" "$COUNT") # 保證至少5位數，補零

# 輸出 HTML 頁面
echo "Content-type: text/html"
echo ""
echo "<!DOCTYPE html>"
echo "<html lang='zh-TW'>"
echo "<head><meta charset='UTF-8'><title>計數器</title>"
echo "<style>"
echo "body { font-family: Arial, sans-serif; text-align: center; margin-top: 20%; }"
echo ".digit { font-size: 48px; font-weight: bold; margin: 0 2px; display: inline-block; }"
echo ".digit:nth-child(1), .digit:nth-child(2), .digit:nth-child(3), .digit:nth-child(4) { color: orange; }"
echo ".digit:nth-child(5) { color: cyan; }"
echo "</style>"
echo "</head>"
echo "<body>"
echo "<h1>訪問次數：</h1>"
echo "<div>"
for (( i=0; i<${#DIGITS}; i++ )); do
    DIGIT=${DIGITS:$i:1}
    echo "<span class='digit'>$DIGIT</span>"
done
echo "</div>"
echo "</body>"
echo "</html>"
