# instructions at https://adventofcode.com/2020/day/6
# for each group, find all the unique letters

/^[a-z]+$/ {
  split($0,yesses,"")
  for (idx in yesses) {
    question = yesses[idx]
    if (!letters_present[question]) {
       letters_present[question] = 1
       unique_yesses++
    }
  }
}

/^ *$/ {
  print unique_yesses
  delete(letters_present)
  unique_yesses = 0
}

END {
  print unique_yesses
}
