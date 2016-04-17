# Latin collation

This directory provides tests and files for Latin collation.

To use it, you must install Python 3 and [PyICU](http://pyicu.osafoundation.org/).

To run the tests, simply run `./test.py`.

See [ICU doc](http://userguide.icu-project.org/collation/customization) and [Unicode doc](http://www.unicode.org/reports/tr35/tr35-collation.html#Orderings) for rule file format.

It seems that Latin collation is correctly handled by the root collation, except [this bug](http://unicode.org/cldr/trac/ticket/9374).
