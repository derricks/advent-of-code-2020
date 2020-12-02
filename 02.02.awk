# For example, suppose you have the following list:

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

{
  positions = $1
  split(positions, pos1pos2, "-")
  pos1 = 0 + pos1pos2[1]
  pos2 = 0 + pos1pos2[2]

  letter = $2
  gsub(":", "", letter)

  password = $3
  split(password, password_letters, "")
  at_pos_1 = password_letters[pos1] == letter
  at_pos_2 = password_letters[pos2] == letter

  if ((at_pos_1 || at_pos_2) && !(at_pos_1 && at_pos_2)) {
    print "VALID"
  } else {
    print "INVALID"
  }
}
