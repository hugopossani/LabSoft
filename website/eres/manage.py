#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eres.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

def escreverArq(content):
    with open('saida.txt', 'w') as out:
        out.write(content)
    
