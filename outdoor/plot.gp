set format x "%d/%m %H:%M:%S"
set timefmt '%Y-%m-%d %H:%M:%S'
set xdata time

est=0.1
p 'ambientePila.tsv' u 1:3:(est) w yerr, 'ambienteTecho.tsv' u 1:3:(est) w yerr
#pause -1
