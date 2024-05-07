<<<<<<< HEAD

=======
#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
>>>>>>> ea1be80eafaad89a7c2dabf3f7f0f761c12e4266
