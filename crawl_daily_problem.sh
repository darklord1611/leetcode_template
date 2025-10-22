#!/bin/bash
# Usage: ./fetch_leetcode_daily.sh [folder_name]
# If no folder_name is provided, a date-based folder will be created.

# -------------------------------
# 1. Setup
# -------------------------------

FOLDER_NAME=${1:-$(date +"%d_%m_%Y")}
BASE_DIR="leetcode_daily/$FOLDER_NAME"
API_URL="https://leetcode-api-pied.vercel.app/daily"

mkdir -p "$BASE_DIR"
cd "$BASE_DIR" || exit 1

# -------------------------------
# 2. Fetch from API
# -------------------------------

echo "📡 Fetching LeetCode daily challenge..."
RESPONSE=$(curl -s "$API_URL")

if [[ -z "$RESPONSE" ]]; then
    echo "❌ No response from API. Check your connection."
    exit 1
fi

# -------------------------------
# 3. Extract fields with jq
# -------------------------------

DATE=$(echo "$RESPONSE" | jq -r '.date')
TITLE=$(echo "$RESPONSE" | jq -r '.question.title')
SLUG=$(echo "$RESPONSE" | jq -r '.question.titleSlug')
DIFFICULTY=$(echo "$RESPONSE" | jq -r '.question.difficulty')
DESCRIPTION=$(echo "$RESPONSE" | jq -r '.question.content')
AC_RATE=$(echo "$RESPONSE" | jq -r '.question.acRate')
TAGS=$(echo "$RESPONSE" | jq -r '[.question.topicTags[].name] | join(", ")')

# Validate data
if [[ -z "$TITLE" || "$TITLE" == "null" ]]; then
    echo "❌ Failed to parse API response. The structure might have changed."
    exit 1
fi

# -------------------------------
# 4. Clean HTML from description
# -------------------------------

DESCRIPTION_CLEAN=$(echo "$DESCRIPTION" | sed -E 's/<[^>]+>//g' | sed 's/&nbsp;/ /g' | awk '
    /Example [0-9]+:/ {exit}
    {print}
')

# -------------------------------
# 5. Format as Python comment
# -------------------------------

COMMENT="# LeetCode Daily Challenge ($DATE)\n"
COMMENT+="# Title: $TITLE\n"
COMMENT+="# Difficulty: $DIFFICULTY\n"
COMMENT+="# Acceptance Rate: $AC_RATE\n"
COMMENT+="# Tags: $TAGS\n"
COMMENT+="# URL: https://leetcode.com/problems/$SLUG/\n#\n"
COMMENT+=$(echo "$DESCRIPTION_CLEAN" | sed 's/^/# /')

# -------------------------------
# 6. Save solution template
# -------------------------------

cat <<EOF > solution.py
$COMMENT


# Your solution starts here
def solution():
    pass
EOF

# -------------------------------
# 7. Done
# -------------------------------

cd - > /dev/null
echo "✅ Problem saved in leetcode_daily/$FOLDER_NAME/solution.py"
