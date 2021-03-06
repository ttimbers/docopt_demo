# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: docopt.py <arg1> [<another_arg>] --arg2=<arg2> [--arg3=<arg3>]

Options:
<arg>             Takes any value (this is a required positional argument)
[<another_arg>]   Takes any value (this is an optional positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
"""

from docopt import docopt
opt = docopt(__doc__)

def main(options):
    print(options)
    print(type(options))

if __name__ == "__main__":
    main(opt)
