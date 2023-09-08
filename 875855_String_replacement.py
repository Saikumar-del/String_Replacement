#C875855: File preparation - string replacement
#Author: Sai kumar
#Creation Date: 27/05/2023
import os, pathlib, csv, itertools, sys, logging, time
import subprocess
from datetime import datetime
import shutil



#opens MonarchUtility bat file
os.chdir('C:\\Program Files\\Altair Monarch 2023')
os.system('MonarchUtility.Automation.exe "C:\Monarch Classic\MonarchUtility\Input\Classic.prn" "C:\Monarch Classic\MonarchUtility\Output\Classic.prn" /cr "10" "20" /chset:ansi')
test = 'C875855 File preparation - string replacement'


#looks for Classic.prn file after replacing 10 with 20
file = pathlib.Path("C:\Monarch Classic\MonarchUtility\Output\Classic.prn")

if file.exists() == False:
    os.chdir('C:\Monarch Classic\MonarchUtility\CLI Logs')
    timestr = time.strftime("%Y%m%d")
    Name = 'PythonCLI_' + timestr + '.txt'
    logging.basicConfig(format='%(asctime)s &(message)s',
    datefmt='%d-%m-%Y:%H:%M:%s',
    level = logging.DEBUG,
    filename=Name)
    logger = logging.getLogger('my_app')
    logger.debug(test + ':Failed; file does not exists')
    sys.exit(0)

#file compare
if sys.version_info.major == 2:
    zip_longest = itertools.izip_longest
else:
    zip_longest = itertools.zip_longest

actual_output = open("C:\Monarch Classic\MonarchUtility\Input\Classic.prn")
Expected_Output = open("C:\Monarch Classic\MonarchUtility\Expected Output\Classic.prn")

csv_f1 = csv.reader(Expected_Output)
csv_f2 = csv.reader(actual_output)


RowNum = 38

for Exp, Act in list(zip_longest(csv_f1, csv_f2)):
    
    if Exp != Act:
        deff = 'Row Number ' + str(RowNum) + ' Expected: ' + Exp[0] + ' :Actual: ' + Act[0]
        os.chdir('C:\Monarch Classic\MonarchUtility\CLI Logs')
        timestr = time.strftime("%Y%m%d")
        #Add the vertion of monarch
        Name = 'PythonCLI_' + timestr + '.txt'
        logging.basicConfig(format='%(asctime)s %(message)s', #to create logger file for the outpput condition
        datefmt='%d-%m-%Y:%H:%M:%S',
        level = logging.DEBUG,
        filename=Name)
        logger = logging.getLogger('my_app')
        logger.debug(test + ':Failed; File does not match to the expected output.  '+ deff)
        sys.exit(0)

    else: result = test + 'Passed' + deff
    
    RowNum = RowNum + 1


os.chdir('C:\Monarch Classic\MonarchUtility\CLI Logs')
timestr = time.strftime("%Y%m%d")
Name = 'PythonCLI_' + timestr + '.txt'
logging.basicConfig(format='%(asctime)s %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename= Name)

logger = logging.getLogger('my_app')

logger.debug(result)


