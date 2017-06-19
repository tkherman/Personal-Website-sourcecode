#!/usr/bin/python

import sys
from datetime import datetime

TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day} {hour}:{minute:02d}
slug: {slug}
"""

def make_post(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    
    f_create = "content/blog/{}_{}_{:0>2}_{:0>2}.md".format(
        slug, today.year, today.month, today.day)
    
    t = TEMPLATE.strip().format(title=title, year=today.year, month=today.month,
        day=today.day, hour=today.hour, minute=today.minute, slug=slug)
    
    with open(f_create, 'w') as w:
        w.write(t)

    print("File created -> " + f_create)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("Making new post...")
        make_post(sys.argv[1])
    else:
        print "No title given"

