from flask import Flask, redirect, url_for, render_template, request
from mechanic.hamilton import Hamilton
from mechanic.PPotential.harmonic_oscillation import HarmonicOscillation
from mechanic.kinetic import Kinetic
from mechanic.momentum import Momentum
from mechanic.speed import Speed
from mechanic.mass import Mass
from modules.classical import Classical

a = Classical(speed=5, force=10)
print("Vận tốc vừa nhập", a.get_speed())
print("Lực vừa nhập", a.get_force())
# Thay giá trị m và gia tốc mới vào
a.set_mass(10)
a.set_accelation(10)
# Gọi hàm tính lực
a.cal_force()
print("Lực mới", a.get_force())
print(a.set_energy(None))


m = Mass(5)
v = Speed(10)

T = Kinetic(m, v)
# Lớp con có thể kế thừa chức năng truyền vào của lớp cha
U = HarmonicOscillation(10)
H = Hamilton(T, U)
print(H.get_())

#
#
#
#
#
#
#
#
#
#
#
#


app = Flask(__name__)
import sys
import json
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/energy")
def energy():
    return render_template("energy.html")

# Vì input từ form trong HTML là nhận vào giá trị kiểu str nên cần ép kiểu sang float để thực hiện phép tính
@app.route("/get-energy", methods=['post'])
def get_energy():
    # Nhận giá trị khối lượng và vận tốc từ form
    m1 = Mass(float(request.form['input_khoiluong']))
    v1 = Speed(float(request.form['input_vantoc']))
    # Tính toán Động năng
    K1 = Kinetic(m1, v1)
    U1 = HarmonicOscillation(float(request.form['input_thenang']))
    # Hamilton = Năng lượng ở cơ học cổ điển
    H1 = Hamilton(K1, U1)
    return render_template("return_energy.html", energy=H1.get_())


@app.route("/science-text")
def markdown():
    return render_template("marktex.html")

@app.route("/save_markdown",methods = ['post'])
def save():
    filename = request.form['filename_mde']
    value = request.form['name_area_mde']
    new_dict = {
        "name" : filename,
        "value" : value
    }
    json_str = json.dumps(new_dict)
    with open("./static/src/"+ filename,"w") as f:
        f.write(json_str)
    f.closed
    return render_template("save_success.html", file = filename)

@app.route("/list-mde",methods=['post','get'])
def list_mde():
    with open("./static/src/hello.json" ,"r") as f:
        result = f.read()
    f.closed
    print(result)
    return result

@app.route("/read")
def read():
    return render_template("return_marktex.html")

if __name__ == '__main__':
    app.run(host="localhost", port=2000, debug=True)
