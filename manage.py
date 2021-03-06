#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "joshgrid.settings")

    args = [argument for argument in sys.argv]

    execute_from_command_line(args)
