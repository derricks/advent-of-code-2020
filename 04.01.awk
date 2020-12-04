# https://adventofcode.com/2020/day/4
# Passport validator for advent of code
# valid = 8 fields
# valid = 7 fields but no cid
# else invalid
# input is on single lines or multiple lines

function is_record_valid(record) {
   delete(fields)
   num_fields = split(record, fields)

   if (num_fields == 8) {
     return 1
   }
   if (num_fields == 7 && record !~ /cid:/) {
     return 1
   }
   return 0
}

function process_record(record) {
  if (is_record_valid(record)) {
     print "VALID"
  } else {
     print "INVALID"
  }
}

# non-blank line
!/^$/ {
  record = (record " " $0)
}

/^$/ {
  process_record(record)
  record = ""
}

# handle the last one
END {
  process_record(record)
}
