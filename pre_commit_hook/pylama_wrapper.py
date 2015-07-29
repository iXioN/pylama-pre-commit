#!/usr/bin/env python
import sys
from pylama.hook import git_hook


def main(argv=None):
    return sys.exit(git_hook())

if __name__ == '__main__':
    exit(main())
