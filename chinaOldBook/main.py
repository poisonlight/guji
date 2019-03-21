import os
import sys
from scrapy.cmdline import execute

path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)
execute(['scrapy', 'crawl', 'guji'])
