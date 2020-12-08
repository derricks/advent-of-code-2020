# https://adventofcode.com/2020/day/8#part2
# this program will read in the lines and then modify instructions one by one, using 08.01.awk to interpret the resulting program

{
  line_count++
  lines[FNR] = $0
}

END {
  for(idx = 1; idx <= line_count; idx++) {
    current_value = lines[idx]
    split(current_value, current_tokens)

    if (current_tokens[1] ~ /^nop/) {
      lines[idx] = ("jmp " current_tokens[2])
    }
    if (current_tokens[1] ~ /^jmp/) {
      lines[idx] = ("nop " current_tokens[2])
    }

    command = "awk -f 08.01.awk"
    for (line in lines) {
      print lines[line] |& command
    }
    close(command, "to")
    command |& getline result
    print result
    close(command)

    lines[idx] = current_value
  }
}
