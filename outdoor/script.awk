#!/usr/bin/awk -f
BEGIN { FS="[ ,]" }
{print $1,$2 "\t" $5 "\t" $6 "\t" $7}
