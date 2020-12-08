Implementations for Advent of Code 2020

These are intended to be quick solutions. So generally there aren't tests or any of the other things one would add for a production system. I'm storing here just for my own recollection.

Some notes on how to run these:

  1. Done at command line: [Instructions](https://adventofcode.com/2020/day/1)
  2. [Instructions](https://adventofcode.com/2020/day/2)

          pbpaste | awk -f 02.01.awk | grep -v INVALID | wc -l

          pbpaste | awk -f 02.02.awk | grep -v INVALID | wc -l

  3. [Instructions](https://adventofcode.com/2020/day/3)

          python3 03.py 1 1 | awk '/#/' | wc -l

          python3 03.py 1 3 | awk '/#/' | wc -l

          python3 03.py 1 5 | awk '/#/' | wc -l

          python3 03.py 1 7 | awk '/#/' | wc -l

          python3 03.py 2 1 | awk '/#/' | wc -l

  4. [Instructions](https://adventofcode.com/2020/day/4)

          pbpaste | awk -f 04.01.awk | grep -v INVALID | wc -l

          pbpaste | awk -f 04.02.awk | grep -v INVALID | wc -l

  5. [Instructions](https://adventofcode.com/2020/day/5)]

          python3 05.01.py | sort -n | tail -n 1
          python3 05.02.py

  6. [Instructions](https://adventofcode.com/2020/day/6)

         pbpaste | awk -f 06.01.awk | awk '{sum += (0 + $0)} END {print sum}'
         pbpaste | awk -f 06.02.awk | awk '{sum += (0+$0)} END {print sum}'

  7. [Instructions](https://adventofcode.com/2020/day/7)

        python3 07.01.py | wc -l
        python3 07.02.py | wc -l

  8. [Instructions](https://adventofcode.com/2020/day/8) - requires awk to be gawk

        pbpaste | awk -f 08.01.awk
        pbpaste | awk -f 08.02.awk | grep Success
