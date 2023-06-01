from flask import Flask, request, abort
from lab1.solution import Solution

app = Flask(__name__)


@app.route("/")
def show_form():
    return "<html><head><title>This is Test App</title></head>" \
           "<body>" \
           "<form action='/result' method=POST>" \
           "<label for='intervals'>Input intervals</label><br />" \
           "<textarea name='intervals' autofocus='True'></textarea><br />" \
           "<label for='newInterval'>Input new interval</label><br />" \
           "<textarea name='newInterval' autofocus='True'></textarea><br />" \
           "<input id='go' type='submit' />" \
           "</form>" \
           "</body></html>"


@app.route("/result", methods=['POST'])
def result():
    data_intervals = request.form['intervals']
    intervals = []
    temp_lst = []
    temp = ""

    for i in range(len(data_intervals) - 1):
        if data_intervals[i] == " " or data_intervals[i] == "[" or data_intervals[i] == "]" or data_intervals[i] == ",":
            continue
        else:
            temp = temp + data_intervals[i]
            if data_intervals[i+1] == " " or data_intervals[i+1] == "[" or data_intervals[i+1] == "]" or data_intervals[i+1] == ",":
                temp_lst.append(int(temp))
                temp = ""
            if len(temp_lst) == 2:
                intervals.append(temp_lst)
                temp_lst = []

    data_newInterval = request.form['newInterval']
    newInterval = []

    for i in range(0, len(data_newInterval)):
        if data_newInterval[i] == " " or data_newInterval[i] == "[" or data_newInterval[i] == "]" or data_newInterval[i] == ",":
            continue
        else:
            newInterval.append(int(data_newInterval[i]))

    try:
        result = str(Solution.insert(None, intervals, newInterval))
    except ValueError:
        abort(400)

    return result, 200, {'Content-Type': 'text/plain; charset=utf-8'}