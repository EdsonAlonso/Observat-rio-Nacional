# --------------------------------------------------------------------------------------------------
# Title: Space Weather codes
# Author: Edson Alonso Falla Luza
# Description: Source codes 
# Collaboratores: Alexandre Andrei
# --------------------------------------------------------------------------------------------------

#-------------------- Importing Python Internal Libraries ----------------#
import xlrd


#DEFININDO A FUNCAO PARA LER O ARQUIVO EXCEL(XLS) 
def xlsread(arq_xls,pg):   #Funcao para ler arquivo excel
    # Abre o arquivo
    xls = xlrd.open_workbook(arq_xls)
    # Pega a planilha pg do arquivo
    plan = xls.sheets()[pg]
    # Para i de zero ao numero de linhas da planilha
    for i in range(plan.nrows):
        # Le os valores nas linhas da planilha
        yield plan.row_values(i) 