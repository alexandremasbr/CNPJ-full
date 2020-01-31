import os

for i in range(1,21):
    os.system("wget -c  http://200.152.38.155/CNPJ/DADOS_ABERTOS_CNPJ_{0}.zip".format(str(i).zfill(2)))