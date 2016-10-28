# Medusa Performance Test Automation

These two scripts can be used on any Linux systems for Medusa Performance testing.

1.	“maim_run.py” -> This script will run all the test we want to run. 
2.	“maim_report.py” -> This script can be used to get the results which we can straight away use in out report, it filters and normalizes the results from the raw medusa test result

How to use it:

1.	Copy the above to scripts in the host 
2.	Edit “maim_run.py” ->  Just edit the first few line, with the test configurations, like threads, block size, duration, etc.
3.	Run > python maim_run.py
4.	Wait for the test to get over
5.	Run > python maim_report.py
6.	The above script will create two result files:
a.	Raw_Report.csv > Detailed Report
b.	Maim_Report.csv > Summary Report
