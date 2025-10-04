import re
import csv
import sys
 
def read_file(path):
    try:
      with open(path, 'r') as file:
        lines = file.readlines()
      return lines
    except Exception as e:
      exit(f"Error : {e}")
 
def write_file(path, header, delimiter, newline, data):
    try:
      with open(path, 'w', newline=newline) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header, delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)
    except Exception as e:
      exit(f"Error : {e}")
 
def extract_value(log_line, key):
  try:
      match = re.search(rf'{key}="([^"]+)"', log_line)
      if match:
        return match.group(1)
      return None
  except Exception as e:
    exit(f"Error : {e}")
 
def transform_data(data, fields_source):
    try:
      transformed_data = []
      for line in data:
        if line.strip():
          parts = line.split()
          date = ' '.join(parts[0:2]) if len(parts) >= 2 else ''
          info = parts[4]
 
          before_UserID = line.split('UserID')[0]
          adminID_Value = before_UserID.split('(')[1].split(')')[0] if '(' in before_UserID and ')' in before_UserID else ''
          extracted_values = {f"IS_{field}": extract_value(line, field) for field in fields_source}
 
          row = {
              'IS_DateEvent': date,
              'IS_TypeEvent': info,
              'IS_AdminID': adminID_Value,
              **extracted_values
          }
          transformed_data.append(row)
      return transformed_data
    except Exception as e:
      exit(f"Error : {e}")
 
def main():
    try:
        #Parameters (filepath source & target)
        filepath_source = sys.argv[1]
        filepath_target = sys.argv[2]
 
        #Variables (source_fields & target_fields)
        fields_source = ['UserID','Client','Origin','SessionID','Action','Archive','Asset','ResultAsset']
        fields_target = ['IS_DateEvent','IS_TypeEvent','IS_AdminID','IS_UserID','IS_Client','IS_Origin','IS_SessionID','IS_Action','IS_Archive','IS_Asset','IS_ResultAsset']
 
        #Read source data
        logs_line = read_file(filepath_source)
 
        #transform data
        data = transform_data(logs_line, fields_source)
 
        #Write transformed data
        write_file(filepath_target, fields_target, ',', '', data)
 
    except Exception as e:
        exit(f"Error : {e}")
 
if __name__ == "__main__":
    main()