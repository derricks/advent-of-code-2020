# instructions https://adventofcode.com/2020/day/6


function process_current_counts(letter_counts, people_in_group) {
  all_said_yes = 0
  for (letter in letter_counts) {
     count = letter_counts[letter]
     if (count == people_in_group) {
       all_said_yes ++
     }
  }
  return all_said_yes
}

/^[a-z]+$/ {
  people_in_group++
  split($0, letters, "")
  for (idx in letters) {
    letter_counts[letters[idx]]++
  }
}

/^ *$/ {
  print process_current_counts(letter_counts, people_in_group)
}

END {
  print process_current_counts(letter_counts, people_in_group)
}

/^ *$/ {
  delete(letter_counts)
  people_in_group = 0
}
