set xrange [0:5236300]
set yrange [0:1]
set xlabel "Memory Sequence ID (in millions)" font ",8"
set ylabel "Probability" font ",8"
set grid
set key font ",10
set pointsize 1
set ytics 0,0.25,1.0
set xtics 0,1000000, 5000000
set mxtics 4
set format x "%.0s"
set bmargin 10

#set terminal latex
#set output "eg1.tex"
set term png x222222 xffffff size 1440, 900 font ",12"
set output "MySQLAnal.png"

set style line 1 lt 2 lc rgb "red" lw 3
set key left top
set title "Apache Memory Analysis Using MySQL Features" font ",16"

plot './025/delete1.feat.gp' title 'DELETE', './025/insert1.feat.gp' title 'INSERT', './025/select1.feat.gp' title 'SELECT 1', './025/select2.feat.gp' title 'SELECT 2', './025/select3.feat.gp' title 'SELECT 3', './025/select4.feat.gp' title 'SELECT 4', './025/select5.feat.gp' title 'SELECT 5', './025/update1.feat.gp' title 'UPDATE', .5 ls 1 title 'THRESH'


# On some terminals, nothing gets plotted until this command is issued
unset multiplot

# remove all customization
reset