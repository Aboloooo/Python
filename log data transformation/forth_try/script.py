import re
import csv
import sys
from datetime import datetime
import hashlib
 
# Read file safely
def read_file(path):
    try:
        with open(path, 'r', encoding='latin-1') as file:
            return file.readlines()
    except Exception as e:
        sys.exit(f"Error reading file: {e}")
 
# Write CSV safely
def write_file(path, header, delimiter, newline, data):
    try:
        with open(path, 'w', newline=newline, encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header, delimiter=delimiter)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        sys.exit(f"Error writing file: {e}")
 
# Extract a single key's value (quoted or unquoted)
def extract_value(log_line, key):
    try:
        match = re.search(rf'{key}="?([^",\s}}]+)"?', log_line)
        return match.group(1) if match else None
    except Exception as e:
        print(f"[WARN] Error extracting key '{key}': {e}")
        return None
 
# Try multiple possible keys
def extract_value_multi(log_line, keys):
    for key in keys:
        value = extract_value(log_line, key)
        if value is not None:
            return value
    return None
 
# Extract known event type or fallback to INFO/WARNING/etc.
def extract_event_type(line):
    try:
        match = re.search(r'(INFO|FINE|WARNING):\s*(\w+)?', line)
        if match:
            level = match.group(1)
            event = match.group(2)
            known_events = [
                'LOGIN', 'LOGOUT', 'SESSION_UPDATED', 'SESSION_TERMINATED', 'SESSION_LOGOUT',
                'REVOKE_PROJECT_GROUP_ROLES', 'ADD_GROUP', 'ASSIGN_GROUP_ROLES', 'ADD_USER'
            ]
            if event and event.upper() in known_events:
                return event
            return level  # fallback to INFO, WARNING
    except Exception as e:
        print(f"[WARN] Failed to extract event type: {e}")
    return 'UNKNOWN'
 
# Extract Status=... from nested Result={...}
def extract_status_from_result(log_line):
    try:
        match_result = re.search(r'Result=\{(.*?)\}', log_line, re.DOTALL)
        if match_result:
            content = match_result.group(1)
            match_status = re.search(r'Status=([^,}}]+)', content)
            return match_status.group(1) if match_status else None
    except Exception as e:
        print(f"[WARN] Failed to extract Status from Result: {e}")
    return None
 
# Core transformation logic
def transform_data(lines, server_name, current_date, field_mapping):
    transformed = []
 
    for line in lines:
        if not line.strip():
            continue  # skip empty lines
 
        try:
            parts = line.split()
            date = ' '.join(parts[0:2]) if len(parts) >= 2 else ''
 
            event_type = extract_event_type(line)
 
            # Extract admin ID from (adminID)
            admin_id_match = re.search(r'\(([^)]+)\)', line)
            admin_id = admin_id_match.group(1) if admin_id_match else ''
 
            # Extract standard fields
            extracted_values = {
                f'IS_{field}': extract_value_multi(line, keys)
                for field, keys in field_mapping.items()
                if field != 'Result'  # handled separately
            }
 
            extracted_values['IS_Result'] = extract_status_from_result(line)
 
            row = {
                'IS_ServerName': server_name,
                'IS_DateEvent': date,
                'IS_TypeEvent': event_type,
                'IS_AdminID': admin_id,
                **extracted_values
            }
 
            # Create a unique HashKey based on sorted content
            hash_input = ''.join(f'{k}:{v if v else ""}' for k, v in sorted(row.items()))
            hash_key = hashlib.md5(hash_input.encode()).hexdigest()
 
            transformed.append({
                'BI_LOAD_DATE': current_date,
                **row,
                'HashKey': hash_key
            })
 
        except Exception as e:
            print(f"[WARN] Skipped line due to error: {e}\nLine: {line}")
            continue
 
    return transformed
 
# Main runner
def main():
    try:
        current_date = datetime.now().strftime("%Y%m%d%H%M%S")
        filepath_source = "/content/fake log.txt"
        filepath_target = "/content/Book1.csv"
        server_name = "serverName1"
 
        field_mapping = {
            'Project': ['Project'],
            'GroupID': ['GroupID', 'GroupIDs'],
            'GroupName': ['GroupName', 'GroupNames'],
            'RoleID': ['RoleID', 'RoleIDs'],
            'UserID': ['UserID', 'UserIDs'],
            'LastName': ['LastName'],
            'FirstName': ['FirstName'],
            'Client': ['Client'],
            'Origin': ['Origin'],
            'SessionID': ['SessionID'],
            'Action': ['Action'],
            'User': ['User'],
            'Product': ['Product'],
            'Archive': ['Archive'],
            'Asset': ['Asset'],
            'Result': ['Status']  # special handling
        }
 
        fields_target = [
            'BI_LOAD_DATE',
            'IS_ServerName',
            'IS_DateEvent',
            'IS_TypeEvent',
            'IS_AdminID',
            'IS_Project',
            'IS_GroupID',
            'IS_GroupName',
            'IS_RoleID',
            'IS_UserID',
            'IS_LastName',
            'IS_FirstName',
            'IS_Client',
            'IS_Origin',
            'IS_SessionID',
            'IS_Action',
            'IS_User',
            'IS_Product',
            'IS_Archive',
            'IS_Asset',
            'IS_Result',
            'HashKey'
        ]
 
        log_lines = read_file(filepath_source)
        transformed_data = transform_data(log_lines, server_name, current_date, field_mapping)
        write_file(filepath_target, fields_target, ',', '', transformed_data)
 
        print(f"✅ Processing complete. Output written to: {filepath_target}")
 
    except Exception as e:
        sys.exit(f"Error in main(): {e}")
 
if __name__ == "__main__":
    main()
 
 