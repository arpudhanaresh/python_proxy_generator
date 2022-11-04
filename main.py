import mysql.connector

connection = mysql.connector.connect(host='arpudhacheck.online',
                                         database='apqurufmu_proxylist',
                                         user='apqurufmu_arpudha',
                                         password='arpudha@123')

check_query = "SELECT * FROM connection_check;"
cursor = connection.cursor()
cursor.execute(check_query)
    # get all records
records = cursor.fetchall()
print(records, "working");

part1 =1;
part2 =1;
part3 =1;
part4 =1;
port = 80;

proxy = [];

for x1 in range(1,999):
    part1 = x1;
   # print(part1)
    for x2 in range(999):
        part2 = x2;
       # print(str(part1) +"."+ str(part2))
        for x3 in range(999):
             part3 = x3;
            # print(str(part1) +"."+ str(part2)+"."+ str(part3))
             for x4 in range(999):
                  part4 = x4;
                  print(str(part1) +"."+ str(part2)+"."+ str(part3)+"."+ str(part4)+":"+str(port))
                  proxyout = str(part1) +"."+ str(part2)+"."+ str(part3)+"."+ str(part4)+":"+str(port);
                  
                  isexistquery = "SELECT count(proxy_id) FROM proxylists where proxyNumber = "+ '''"'''+proxyout+ '''"''';

                  count = cursor.execute(isexistquery);
                  output = cursor.fetchall()
                  output = output[0];
                  output = str(output)
                  output = output.replace('(', '')
                  output = output.replace(')', '')
                  output = output.replace(',', '')
                  isproxyExist = output;
                  isproxyExist = int(isproxyExist)
                  print(isproxyExist)
                  if(isproxyExist > 0):
                    print(proxyout, "already exist");
                  else:
                    # insertQuery = "insert into `proxylists` (`proxyNumber`) VALUES ( %s)"
                    # val = proxyout
                    # cursor.execute(insertQuery, val)
                    insertQuery = "insert into `proxylists` (`proxyNumber`) VALUES ("+ '''"'''  + proxyout + '''"'''+ ")";
                    print(insertQuery)
                    cursor.execute(insertQuery)
                    print(cursor.rowcount, "record inserted.");
                    connection.commit()
                

                

                  

                  


print(proxy);
