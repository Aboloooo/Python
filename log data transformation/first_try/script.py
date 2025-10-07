with open("demofile.txt", "w") as f:
  f.write('2025-06-27 02:47:39.681 CEST INFO: SESSION_TERMINATED (InformationServerSystemUser): UserID="first-user-test", Client="client1", Origin="pc1", SessionID="4111wlkmeg4" \n')
  f.write('2025-06-27 07:55:57.427 CEST INFO: LOGIN (x099153): UserID="ojkgepr1", Client="Unknown", Origin="10.232.2.241", SessionID="éeljrglb6-7ced4a8e5c19" \n')
  f.write('2025-06-27 07:55:57.472 CEST INFO: SESSION_UPDATED (kjnt): UserID="x0991e5g53", Client="ertgklm", Origin="erg", SessionID="eroge5c19" \n')
  f.write('2025-06-27 08:24:53.018 CEST INFO: LOGIN (erh): UserID="ert", Client="erg", Origin="10th", SessionID="ert" \n')
 
with open("demofile.txt") as dem:
  lines = dem.readlines()
 
eachLine_array = []
 
for eachLine in lines:
  if eachLine:
    try:
      ''' splitting words by space '''
      partsOfEachLine = eachLine.split()
 
      # Ensure we don't go out of bounds
      num_parts_to_take = min(10, len(partsOfEachLine))
      values = partsOfEachLine[:num_parts_to_take]
 
      eachLine_array.append(values)
 
    except Exception as e:
      print(f"failed: {e}")
 
print(eachLine_array)