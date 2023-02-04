import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from PyPDF2 import PdfMerger
from os.path import isfile, join,exists
from PyPDF2 import PdfFileMerger


import linecache
from pdfrw import PdfReader, PdfWriter
import numpy as np
import fitz
import natsort 


def spliit():    
    inputpdf = PdfFileReader(open(r"/home/ds/Documents/WORK/facture/PDF/SS/result1.pdf", "rb"))
     
    
    for i in range(0,inputpdf.numPages, 2):
        output = PdfFileWriter()
        
        output.addPage(inputpdf.getPage(i))
        output.addPage(inputpdf.getPage(i+1))
        name_result = linecache.getline(r"/home/ds/Documents/WORK/facture/PDF/SS/somefile.txt", i+1)
        name_result = name_result.replace("\n","")
        with open(name_result, "wb") as outputStream:
            output.write(outputStream)
    

def vvvvv(): 
    #merger = PdfMerger() 
    merger = PdfFileMerger()
 
    for i in range(1,386):
        name_result = linecache.getline(r"/home/ds/Documents/WORK/facture/PDF/SS/somefile.txt", i)
        name_result = name_result.replace("\n","")
        merger.append(open(name_result, 'rb'))

    with open("resultssss.pdf", "wb") as fout:
        merger.write(fout)
    """name_result = linecache.getline(r"/home/ds/Documents/WORK/facture/PDF/SS/somefile.txt", i)
        name_result = name_result.replace("\n","")
        merger.append(name_result)
        merger.write("resultssss.pdf")
    merger.close()"""
    
    """list_name = list()
    list_name = glob.glob("/media/ds/DISK_IMG/BASE/DELIVEROO/*.pdf")
    array_length = len(list_name)
    list_name = natsort.natsorted(list_name,reverse=True)
    for i in range(2, array_length):
        name = (list_name[i])
        with open('somefile.txt', 'a') as the_file:
            the_file.write(name+'\n')"""


vvvvv()
