import xlwt;
from datetime import datetime;
from xlrd import open_workbook;
from xlwt import Workbook;
from xlutils.copy import copy
from pathlib import Path


def output(filename, sheet,num, name, present, number):
    my_file = Path(r'Attendance/'+filename+str(datetime.now().date())+'.xls');
    if my_file.is_file():
        rb = open_workbook(r'Attendance/'+filename+str(datetime.now().date())+'.xls');
        book = copy(rb);
        sh = book.get_sheet(0)
    else:
        book = xlwt.Workbook()
        sh = book.add_sheet(sheet)
    style0 = xlwt.easyxf('font: name Times New Roman, bold on',
                         num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    sh.write(0,0,datetime.now().date(),style1);


    col1_name = 'Name'
    col2_name = 'Attendnce'


    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")


    sh.write(1,0,col1_name,style0);
    sh.write(1, 1, col2_name,style0);
    sh.write(1, 2, "Time",style0);
    sh.write(1, 3, "USN",style0);

    sh.write(num+1,0,name);
    sh.write(num+1, 1, present);
    sh.write(num+1, 2, current_time);
    sh.write(num+1, 3, "1BY19EC"+number);

    fullname=filename+str(datetime.now().date())+'.xls';
    book.save(r'Attendance/'+fullname)

    print("[INFO]: EXCEL Sheet is Update!!!..")

    return fullname;
