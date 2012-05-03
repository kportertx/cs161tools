# Instructions:
1. Generate traces.
2. Build features
    1. Optional: ./removeInstructions.py <path/to/trace/directory> <desired/output/directory>
        * Note: this removes all the instruction lines (and any other line that does not start with I) from the traces.
    1. from build features directory: ./intersect.py <path/to/trace/directory>
        * Note: All traces should be of a particular 'feature' of the program.  For example in mysql we created a feature on select statements.
				* Note: This writes to stdout so you will need to redirect to a file to use later.
				* Note: The analyzer requires all the features to be in one directory.
3. Locate the trace you wish to analyze with this feature.
    1.  Run ./analyzer.py <path/to/features> <path/to/trace/of/interest> <numeric step size>
		    * Note: If you did the optional step in 2 then you will need to run removeInstructions.py against the trace to be analyzed.
        * The lower the step size the more data points you will recieve.
        * This outputs a file per feature to the pwd.  If your feature was 'select' then it would output 'select.gp'
4. Use gnuplot to prot your results
    * Eample: gnuplot> plot "update_query.gp" using 1:2 title 'Update', "select_query.gp" using 1:2 title 'Select'
        * Note: The only parts of this you will need to change are the actual gp file sand the key identifiers.  Obviously you can add more gp files to a trace by extending this line.
        * Note: For large files it may be useful to zoom in on the plot here is an example of that:
            *  gnuplot> set yrange [0:1]
            *  gnuplot> set xrange [280000: 330000]
