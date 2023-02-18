#! bin/bash
echo "Enter a phrase"
read $phrase
count_words = $(echo $phrase | wc - c)
whitespace = $(echo $phrase | tr -d -c ' ' | wc -c)
echo "Number of words = $count_words"
echo "Number of whitespace = $whitespace"
