# correos-tracking-lookup
The tracking number [lookup page from the spanish post office](https://www.correos.es/es/en/tools/tracker/items) is slow.

This script just sends one request per tracking number to lookup the state of your delivery.

You can pass one or multiple tracking-numbers as cli-args, or a file containing one number each line. If you pass nothing, it will try to look for the default file `tracking-numbers.txt`.
