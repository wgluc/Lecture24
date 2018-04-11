from flask import Flask, render_template, request

def init_bball(csv_file_name=BB_FILE_NAME):
    global bb_seasons
    with open(csv_file_name) as f:
        reader = csv.reader(f)
        next(reader) # throw away headers
        next(reader) # throw away headers
        global bb_seasons
        bb_seasons = [] # reset, start clean
        for r in reader:
            bb_seasons.append(r)


    with open(csv_file_name) as f:
            reader = csv.reader(f)
            next(reader) # throw away headers
            next(reader) # throw away headers
            global bb_seasons
            bb_seasons = [] # reset, start clean
            for r in reader:
                r[3] = int(r[3])
                r[4] = int(r[4])
                r[5] = float(r[5])
                bb_seasons.append(r)


@app.route('/bball', methods=['GET', 'POST'])
def bball():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_bball_seasons(sortby, sortorder)
    else:
        seasons = model.get_bball_seasons()

    return render_template("seasons.html", seasons=seasons)


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    return render_template("hello.html", firstname=firstname, lastname=lastname)


def get_bball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
