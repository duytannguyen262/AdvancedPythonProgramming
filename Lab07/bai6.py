from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    tentruong = ' Dai hoc Van Lang!'
    lienket = '<a href="https://www.vanlanguni.edu.vn">' +tentruong+' </a> <br>'
    chuoi = lienket
    import datetime
    nam = datetime.date.today().year
    chuoi = chuoi + ' <b>Xin <i>chao</i> Tan sinh vien nam ' +     str(nam) + '!</b> '
    return chuoi

@app.route('/monhoc')
def learn():
    return "Đây là trang môn học !"

@app.route('/monhoc/<tenmon>')
def subjects(tenmon):
    chuoi = "Đây là trang môn học"
    monhoc = str(tenmon).upper()
    if monhoc == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + monhoc
    return chuoi

@app.route('/sinhvien')
def students():
    chuoi = "Đây là trang các khóa học"
    return chuoi

@app.route('/sinhvien/<khoa>')
def school_year(khoa):
    chuoi = "Đây là năm học"
    namHoc = str(khoa).upper()
    if namHoc == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + namHoc
    return chuoi
if __name__ == '__main__':
    app.run(port=5050)