f = 'dndsci_zppg.csv'

file = open(f)

col_name_line = file.readline()
col_names = col_name_line.split(',')
col_names = [x.replace('\n','') for x in col_names]
print(col_names)

rows = []

while True:
    line = file.readline()
    if len(line) < 1:
        break
    if "\"" in line: # we need logic for this :(
        [pre, sounds, post] = line.split("\"")
        vals = pre.split(',') + [sounds] + post.split(',')
    else:
        vals = line.split(',')
        
    vals = [x.replace('\n','') for x in vals]
    vals = [x for x in vals if len(x)]
    row_struct = {}
    for i in range(len(vals)):
        row_struct[col_names[i]] = vals[i]
    rows.append(row_struct)


for float_col in ["Longitude", "Latitude", "Shortitude", "Deltitude", "Local Value of Pi", "Murphy's Constant"]:
    col_vals = [float(x[float_col]) for x in rows]
    print('\n{} varies from {:.4f} to {:.4f}, average {:.4f}'.format(float_col, min(col_vals), max(col_vals), sum(col_vals)/len(col_vals)))
