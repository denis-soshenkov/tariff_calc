import re
url = 'http://www.atsenergo.ru/dload/calcfacthour_regions/201910_ALTAENSB_76209_calcfacthour.xls'
m = re.search(r'_(\d+)_', url)
print(m.group(1))