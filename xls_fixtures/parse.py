import xlrd

#Opens workbook fixtures.xls
wb = xlrd.open_workbook('fixtures.xls')

#prints sheet names
##for i in wb.sheet_names():
##   print i

#Creates sheet names from sheet list for viewing
sh_accounts = wb.sheet_by_name('Accounts')
sh_policy_areas = wb.sheet_by_name('Policy Areas')
sh_approval_flows = wb.sheet_by_name('Approval Flows')
sh_policies = wb.sheet_by_name('Policies')
sh_approvals = wb.sheet_by_name('Approvals')
sh_overview = wb.sheet_by_name('Overview')

#Displays contents of rows in sheets
for rows in range(sh_accounts.nrows):
    print sh_accounts.row_values(rows)
    

#Displays contents of column 0
label_column = sh_accounts.col_values(0)
for items in label_column:
    print items
    
#Displays contents of all columns
for col_data in range(sh_accounts.ncols):
    print col_data

#Prints number of columns    
##print sh_accounts.ncols
    
#Displays contents of columns as list
print sh_accounts.col_values(0)