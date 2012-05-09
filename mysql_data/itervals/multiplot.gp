set xrange [0:13236300]
set yrange [0:1]
set xlabel "Memory Sequence ID (in millions)" font ",6"
set ylabel "Probability" font ",6"
set grid
set key font ",6"
set lmargin 10
set rmargin 0
set tmargin 2
set bmargin 3
set pointsize 1
set ytics 0,0.25,1.0
set xtics 0,4000000, 13000000
set mxtics 4
set format x "%.0s"

# Uncomment the following to line up the axes
# set lmargin 6

# Gnuplot recommends setting the size and origin before going to
# multiplot mode
# This sets up bounding boxes and may be required on some terminals
set size 2,2
set origin 0,0

# Done interactively, this takes gnuplot into multiplot mode
# and brings up a new prompt ("multiplot >" instead of "gnuplot >")
set multiplot

# plot the first graph so that it takes a quarter of the screen
set key left top
set title "Iterval = 25" font ",10"
set size 0.5,0.25
set origin 0,0.75
plot './025/delete1.feat.gp' title 'DELETE', './025/insert1.feat.gp' title 'INSERT', './025/select2.feat.gp' title 'SELECT 1', './025/select4.feat.gp' title 'SELECT 2', './025/select5.feat.gp' title 'SELECT 3', './025/update1.feat.gp' title 'UPDATE'

# plot the second graph so that it takes a quarter of the screen
set nokey
set title "Iterval = 50" font ",10"
set size 0.5,0.25
set origin 0,0.5
plot './050/delete1.feat.gp' title 'DELETE', './050/insert1.feat.gp' title 'INSERT', './050/select2.feat.gp' title 'SELECT 1', './050/select4.feat.gp' title 'SELECT 2', './050/select5.feat.gp' title 'SELECT 3', './050/update1.feat.gp' title 'UPDATE'

# plot the third graph so that it takes a quarter of the screen
set title "Iterval = 75" font ",10"
set size 0.5,0.25
set origin 0.0,0.25
plot './075/delete1.feat.gp' title 'DELETE', './075/insert1.feat.gp' title 'INSERT', './075/select2.feat.gp' title 'SELECT 1', './075/select4.feat.gp' title 'SELECT 2', './075/select5.feat.gp' title 'SELECT 3', './075/update1.feat.gp' title 'UPDATE'

# plot the fourth graph so that it takes a quarter of the screen
set title "Iterval = 100" font ",10"
set size 0.5,0.25
set origin 0.0,0.0
plot './100/delete1.feat.gp' title 'DELETE', './100/insert1.feat.gp' title 'INSERT', './100/select2.feat.gp' title 'SELECT 1', './100/select4.feat.gp' title 'SELECT 2', './100/select5.feat.gp' title 'SELECT 3', './100/update1.feat.gp' title 'UPDATE'


set rmargin 2
# plot the first graph so that it takes a quarter of the screen
set key left top
set title "Iterval = 125" font ",10"
set size 0.5,0.25
set origin 0.5,0.75
plot './125/delete1.feat.gp' title 'DELETE', './125/insert1.feat.gp' title 'INSERT', './125/select2.feat.gp' title 'SELECT 1', './125/select4.feat.gp' title 'SELECT 2', './125/select5.feat.gp' title 'SELECT 3', './125/update1.feat.gp' title 'UPDATE'

# plot the second graph so that it takes a quarter of the screen
set nokey
set title "Iterval = 150" font ",10"
set size 0.5,0.25
set origin 0.5,0.5
plot './150/delete1.feat.gp' title 'DELETE', './150/insert1.feat.gp' title 'INSERT', './150/select2.feat.gp' title 'SELECT 1', './150/select4.feat.gp' title 'SELECT 2', './150/select5.feat.gp' title 'SELECT 3', './150/update1.feat.gp' title 'UPDATE'

# plot the third graph so that it takes a quarter of the screen
set title "Iterval = 175" font ",10"
set size 0.5,0.25
set origin 0.5,0.25
plot './175/delete1.feat.gp' title 'DELETE', './175/insert1.feat.gp' title 'INSERT', './175/select2.feat.gp' title 'SELECT 1', './175/select4.feat.gp' title 'SELECT 2', './175/select5.feat.gp' title 'SELECT 3', './175/update1.feat.gp' title 'UPDATE'

# plot the fourth graph so that it takes a quarter of the screen
set title "Iterval = 200" font ",10"
set size 0.5,0.25
set origin 0.5,0
plot './200/delete1.feat.gp' title 'DELETE', './200/insert1.feat.gp' title 'INSERT', './200/select2.feat.gp' title 'SELECT 1', './200/select4.feat.gp' title 'SELECT 2', './200/select5.feat.gp' title 'SELECT 3', './200/update1.feat.gp' title 'UPDATE'

# On some terminals, nothing gets plotted until this command is issued
unset multiplot

# remove all customization
reset