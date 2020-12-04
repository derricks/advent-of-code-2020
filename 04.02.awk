# https://adventofcode.com/2020/day/4
# Passport validator for advent of code
# valid = 8 fields
# valid = 7 fields but no cid
# plus new validation rules
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
# else invalid
# input is on single lines or multiple lines

# determines if the given number is between (inclusively) the min and max
function number_between(number, min, max) {
  return (0+number) >= min && (0+number) <= max
}

# determine if the input value is four digits
function value_is_four_digits(value) {
  return value ~ /^[0-9]{4}$/
}

# validates birth year according to above
function validate_byr(value) {
  return value_is_four_digits(value) && number_between(value, 1920, 2002)
}

# validates issue year according to the above
function validate_iyr(value) {
  return value_is_four_digits(value) && number_between(value, 2010, 2020)
}

# validates expiration year according to the above
function validate_eyr(value) {
  return value_is_four_digits(value) && number_between(value, 2020, 2030)
}

# validate hgt field
function validate_hgt(value) {
  if (value !~ /^[0-9]+(cm|in)$/) {
     return 0
  }

  if (value ~ /cm$/) {
     # validate centimeters height
     height = substr(value, 1, index(value, "cm") - 1)
     return number_between(height, 150, 193)
  }

  if (value ~ /in$/) {
    height = substr(value, 1, index(value, "in") - 1)
    return number_between(height, 59, 76)
  }
}

# validate hcl field according to above
function validate_hcl(value) {
  return value ~ /^#[0-9a-f]{6}$/
}

# validate ecl according to above
function validate_ecl(value) {
  return value ~ /^(amb|blu|brn|gry|grn|hzl|oth)$/
}

# validate pid according to above
function validate_pid(value) {
  return value ~ /^[0-9]{9}$/
}

# does fine-grained validation of fields according
function validate_fields(record) {
  delete(field_map)
  split(record, temp_fields)
  for (field_idx in temp_fields) {
     split(temp_fields[field_idx], key_value, ":")
     field_map[key_value[1]] = key_value[2]
  }

  return validate_byr(field_map["byr"]) &&
         validate_iyr(field_map["iyr"]) &&
         validate_eyr(field_map["eyr"]) &&
         validate_hgt(field_map["hgt"]) &&
         validate_hcl(field_map["hcl"]) &&
         validate_ecl(field_map["ecl"]) &&
         validate_pid(field_map["pid"])
}


function is_record_valid(record) {
   delete(fields)
   num_fields = split(record, fields)

   if (num_fields == 8 && validate_fields(record)) {
     return 1
   }

   if (num_fields == 7 && record !~ /cid:/ && validate_fields(record)) {
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
