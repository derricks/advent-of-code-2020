# For example, suppose you have the following list:

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

# Given input and a letter, return the number of times the letter
# appears in the input
function letter_counts(input, letter) {
   delete(counts)
   split(input, letters, "")
   for (cur_letter in letters) {
     counts[letters[cur_letter]] += 1
   }
   return counts[letter]
}

{
  range = $1
  split(range, minmax, "-")
  min = 0 + minmax[1]
  max = 0 + minmax[2]

  letter = $2
  gsub(":", "", letter)

  password = $3

  count = letter_counts(password, letter)
  if (count >= min && count <= max ) {
    print "VALID"
  } else {
    print "INVALID"
  }
}
