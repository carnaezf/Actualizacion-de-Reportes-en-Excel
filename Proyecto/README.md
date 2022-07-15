# -automatic-excel-reports
Tool used: Python and Jupyter Notebooks


Report automation project, consists of 3 parts:
Part I:
Copy and paste base txt files from one location to another.
Read all lines and filter lines of interest to save them in another location in CSV format.
Output:
Copy of txt files (Jobs SAP).
Equivalent csv files.

Part II:
Program takes CSV created in previous step, they are formatted in xlsx format.
Then, for reporting purposes, book crosses (or DataFrames) are made to generate report bases.
Output:
Equivalent Excel workbooks and combined Excel workbooks.

Part III.
We take databases created in part II and enter Excel fromulas using Python library xlwings.
Output:
Base Excel workbooks with Excel formulas written with Python.


Part II can be deleted, but choose to keep it for experimentation/learning purposes.
