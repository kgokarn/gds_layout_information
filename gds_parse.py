from __future__ import print_function
from gdsii import types
from gdsii.record import Record
import sys

def layout(lay_out):
    if lay_out.tag_type == types.ASCII:
        return '"%s"' % lay_out.data.decode()
    elif lay_out.tag_type == types.BITARRAY:
        return str(lay_out.data)
    return ', '.join('{0}'.format(i) for i in lay_out.data)

def main(name):
    with open(name, 'rb') as a_file:
        for item in Record.iterate(a_file):
            if item.tag_type == types.NODATA:
                gds_file.write(item.tag_name)
                gds_file.write("\n")

            else:
                gds_file.write('%s: %s' % (item.tag_name, layout(item)))
                gds_file.write("\n")
        gds_file.close()

if __name__ == '__main__':
    gds_file = open("gds_humanreadable.txt", "w+")
    main("INV_X1.gds")
    sys.exit(0)