#!/bin/bash

stars_file="stars.json"
tmp=$(mktemp)

for directory in Day*; do
  day=\"$(echo "${directory}" | tr -dc '0-9')\"
  day_stars=0
  echo "Checking day ${day}..."
  if find "./${directory}" -name "*2.py" -type f | grep -q .; then
    day_stars=2
    echo "  Day ${day} has 2 stars"
  elif find "./${directory}" -name "*1.py" -type f | grep -q .; then
    day_stars=1
    echo "  Day ${day} has 1 star"
  else
    day_stars=0
    echo "  Day ${day} has no stars"
  fi
  cat $stars_file | jq --indent 4 ".days[$day] = $day_stars" > $tmp && mv $tmp $stars_file
done
