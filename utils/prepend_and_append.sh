#!/bin/bash

cd /home/prdx/Documents/CS6200-Summer/A1/AP_DATA/ap89_collection/ 

for d in ap*; do
  echo '<DOCS>' | cat - ${d} > temp && mv temp ${d}
  echo '</DOCS>' >> ${d}
done
