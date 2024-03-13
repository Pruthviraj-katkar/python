import subprocess
subprocess.run(["helm","repo","add","bitnami","https://charts.bitnami.com/bitnami"])
subprocess.run(["helm","repo","update"])
subprocess.run(["helm","install","mydb","bitnami/mysql"])