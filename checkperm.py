import gspread
gc = gspread.service_account(filename='streamlitdb-480711-71a2f70e3be0.json')
sh = gc.open_by_key('1sLauq7g2XVXDoFdf9DTsvqri8B3uhVfJUKbG2Bi_GEU')
worksheet = sh.sheet1
print(worksheet.get_all_values())