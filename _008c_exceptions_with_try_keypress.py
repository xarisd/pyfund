"""keypress - A module for detecting a single keyypress."""

try:
    import msvcrt

    def get_key():
        """Wait for a keypress and return a single character string."""
        return msvcrt.getch()

except ImportError:
    import sys
    import tty
    import termios

    def get_key():
        """Wait for a keypress and return a single character string."""
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
        return ch


# if either of the Unix-specific tty or termios are not found,
# we allow the ImportError to propagate from here


if __name__ == '__main__':
    c = get_key()
    print("You typed : {}".format(c))