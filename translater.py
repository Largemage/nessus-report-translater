import sqlite3
import csv
import sys

import unicodecsv as u_csv


def import_and_export():
    resultname = filename.replace('.csv', '') + '_translation.csv'
    with open(resultname, 'wb') as nf:
        w = u_csv.writer(nf, encoding='GBK')
        with open(filename, 'r', encoding='UTF-8') as of:
            reader = csv.reader(of)
            first = 1
            for row in reader:
                if first:
                    w.writerow(row)
                    first = 0
                else:
                    try:
                        if translate(row[0]) is not None:
                            name, description, solution = translate(row[0])
                            w.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], name, row[8],
                                    description, solution, row[11], row[12]])
                        else:
                            w.writerow(row)
                    except:
                        print("报错ID："+row[0])
                        

def translate(plugin_id):
    conn = sqlite3.connect("vulLib.db")
    conn.text_factory = lambda x: str(x, 'gbk', 'ignore')
    cursor = conn.cursor()
    for row in cursor.execute("select * from VULNDB where Plugin_ID=?", (plugin_id,)):
        if row is not None:
            return row[1], row[3], row[4]
        else:
            return None


if __name__ == '__main__':
    filename = sys.argv[1]
    print('请耐心等待！')
    import_and_export()
    print('翻译结束！')
