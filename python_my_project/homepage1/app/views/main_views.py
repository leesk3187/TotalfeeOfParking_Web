from flask import Blueprint, render_template, request, flash
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/', methods=["GET", "POST"])
def index():
    form_data = request.form
    INPUT = 'index.html'
    if request.method == "POST":
        time = request.form.get("time", type=int)
        error = None
        #time = int(form_data["time"])
        if form_data["btn"] == "btn":
            if time == 0:
                flash("0보다 큰 정수를 입력하세요!")
                error = 'type error'
                return render_template(INPUT, error=error)
            elif form_data["time"] == "":
                flash("1 이상의 정수를 입력하세요!")
                error = 'Invalid credentials'
                return render_template(INPUT, error=error)
            else:
                return render_template(
                    INPUT, fee = total_fee(time),time=time, day=str(total_Day(time))
                )   
    return render_template(template_name_or_list=INPUT)

def Hour(time): # 시간 구하기
    hour = time % 24
    return hour

def Day(time):  # 날짜 구하기
    day = time // 24
    return day

def total_fee(time):    #(Day, Hour 사용)금액 구하기
    day = Day(time)
    hour = Hour(time)
    fee=0
    if time > 24:
        if day>=1: fee = 15000 + (day-1) * (24*2000)
        if hour > 0: fee += hour*2000
    else:
        fee = 3000
        time -= 2
        if time > 0: fee += time*2000
        if fee>15000: fee = 15000
    return fee

def total_Day(time):
    day = int(Day(time))    # 형 변환
    hour =  int(Hour(time))
    
    if day>=1:
        return "%d 일 %d 시간" % (day, hour)
    else:
        return "%d 시간" % hour

if __name__ == '__main__':
    bp.run()
    