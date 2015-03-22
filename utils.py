"""Utils for playing with Python"""

# import sys
from pprint import pprint as pp


def hrule(title, width=70):
    """Prints a convenient header with title and horizontal rule

    Args:
        title: The title
        width: The width of the horizontal rule (default 50)
    """
    width = max([width, len(title)])
    print("\n")
    print(title.center(width))
    print("=" * width)


def main():
    hrule("First Paragraph")
    hrule("Second Paragraph")
    pp(None)

if __name__ == '__main__':
    main()