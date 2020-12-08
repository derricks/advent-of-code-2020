# instructions: https://adventofcode.com/2020/day/8

{
  line_count++
  lines[FNR] = $0
}

END {
  accumulator = 0
  position = 1

  while(seen_positions[position] == 0 && position <= line_count) {
    seen_positions[position] = 1
    split(lines[position], tokens)

    if (tokens[1] ~ /^nop/) {
      position++
    }

    if (tokens[1] ~ /^acc/) {
      accumulator += (0 + tokens[2])
      position++
    }

    if (tokens[1] ~ /^jmp/) {
      position += (0 + tokens[2])
    }
  }

  if (position > line_count) {
     print "Success! Accumulator = " accumulator
  } else {
     print "Loop! Accumulator before loop:", accumulator
  }
}
