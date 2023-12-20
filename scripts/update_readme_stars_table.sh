#!/bin/bash

stars_file="stars.json"
readme_file="README.md"
tmp=$(mktemp)

# Write Table Header.
echo -e "## Table of challenges\n" >> $tmp
echo "Day | Challenge Name | Stars |" >> $tmp
echo ":-:| :-: | :-: |" >> $tmp

for directory in Day*; do
  day=$(echo "${directory}" | tr -dc '0-9')
  day_stars=$(jq ".days[\"$day\"]" $stars_file)
  day_readme_file="${directory}/README.md"
  day_title=$(head -n 1 $day_readme_file | sed "s/# Day $(($day)): //")
  echo "$day | [$day_title]($directory) | $(for ((i=0; i<${day_stars}; i++)); do printf '⭐️'; done) |" >> $tmp
done


sed -i '/## Table of challenges/,$d' $readme_file
cat $tmp >> $readme_file
rm $tmp
