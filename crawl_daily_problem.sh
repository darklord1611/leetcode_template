#!/bin/bash

# Get current date in DD_MM_YYYY format if no argument is provided
FOLDER_NAME=${1:-$(date +"%d_%m_%Y")}

# Create the daily folder
mkdir -p "leetcode_daily/$FOLDER_NAME"

# Move into the folder
cd "leetcode_daily/$FOLDER_NAME" || exit 1

# API Endpoint
API_URL="https://alfa-leetcode-api.onrender.com/dailyQuestion"

# Fetch data from API
RESPONSE=$(curl -s "$API_URL")

# Extract values using jq (handles Unicode properly)
TITLE=$(echo "$RESPONSE" | jq -r '.data.activeDailyCodingChallengeQuestion.question.title' 2>/dev/null)
SLUG=$(echo "$RESPONSE" | jq -r '.data.activeDailyCodingChallengeQuestion.question.titleSlug' 2>/dev/null)
DATE=$(echo "$RESPONSE" | jq -r '.data.activeDailyCodingChallengeQuestion.date' 2>/dev/null)
DIFFICULTY=$(echo "$RESPONSE" | jq -r '.data.activeDailyCodingChallengeQuestion.question.difficulty' 2>/dev/null)
DESCRIPTION=$(echo "$RESPONSE" | jq -r '.data.activeDailyCodingChallengeQuestion.question.content' 2>/dev/null)

# Check if API returned valid data
if [[ -z "$TITLE" || -z "$DESCRIPTION" ]]; then
    echo "❌ Failed to fetch problem data. Check your internet connection or API status."
fi

# Remove HTML tags and strip out examples
DESCRIPTION_CLEAN=$(echo "$DESCRIPTION" | sed -E 's/<[^>]+>//g' | sed 's/&nbsp;/ /g' | awk '
    /Example [0-9]+:/ {exit} 
    {print}
')

# Format the output as a Python comment block
COMMENT="# LeetCode Daily Challenge ($DATE)\n"
COMMENT+="# Title: $TITLE\n"
COMMENT+="# Difficulty: $DIFFICULTY\n"
COMMENT+="# URL: https://leetcode.com/problems/$SLUG/\n#\n"
COMMENT+=$(echo "$DESCRIPTION_CLEAN" | sed 's/^/# /')

# Write the comment block to solution.py
echo -e "$COMMENT\n\n\n# Your solution starts here\n\ndef solution():\n    pass" > solution.py

# Move back to the original directory
cd - > /dev/null

echo "✅ Problem saved in daily/$FOLDER_NAME/solution.py"
