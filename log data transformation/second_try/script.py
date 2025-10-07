import re
import csv
 
with open("test-log.log") as logs:
  lines = logs.readlines()
 
# Extracting info from each line of logs
def extract_value(log_line, key):
    match = re.search(rf'{key}="([^"]+)"', log_line)
    if match:
        return match.group(1)
    return None
try:
  fields  =  ['IS_DateEvent','IS_TypeEvent','IS_AdminID','IS_UserID','IS_Client','IS_Origin','IS_SessionID','IS_Action','IS_Archive','IS_Asset','IS_ResultAsset']
  keys = ['UserID','Client','Origin','SessionID','Action','Archive','Asset','ResultAsset']
  # Writing in CSV filew
  with open('logs.csv', 'w') as csvfile:
    pass
  with open('logs.csv', 'a') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields )
    # writing headers (field names)
    writer.writeheader()
    for line in lines:
      if line:
        # splitting words by space
        partsOfEachLine = line.split()
 
        # Ensure we don't go out of bounds
        num_parts_to_take = min(11, len(partsOfEachLine))
        values = partsOfEachLine[:num_parts_to_take]
 
        parts = line.split()
        date = ' '.join(parts[0:2])
 
        info = values[4]
 
        before_UserID = line.split('UserID')[0]
        adminID_Value = before_UserID.split('(')[1].split(')')[0] # the first () before UserID would be adminID_Value
 
        extracted_values = {f"IS_{key}": extract_value(line, key) for key in keys}
 
        row = [{
            'IS_DateEvent':date,
            'IS_TypeEvent':info,
            'IS_AdminID':adminID_Value,
            **extracted_values
        }]
        # writing data rows
        writer.writerows(row)
 
except Exception as e:
  print(f"failed: {e}")