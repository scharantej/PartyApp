 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

parties = []

@app.route('/')
def index():
    return render_template('index.html', parties=parties)

@app.route('/create_party', methods=['GET', 'POST'])
def create_party():
    if request.method == 'GET':
        return render_template('create_party.html')
    else:
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        party = {'name': name, 'date': date, 'time': time, 'location': location}
        parties.append(party)
        return redirect(url_for('index'))

@app.route('/edit_party/<int:party_id>', methods=['GET', 'POST'])
def edit_party(party_id):
    if request.method == 'GET':
        party = parties[party_id]
        return render_template('edit_party.html', party=party)
    else:
        name = request.form['name']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        party = parties[party_id]
        party['name'] = name
        party['date'] = date
        party['time'] = time
        party['location'] = location
        return redirect(url_for('index'))

@app.route('/delete_party/<int:party_id>')
def delete_party(party_id):
    parties.pop(party_id)
    return redirect(url_for('index'))

@app.route('/rsvp_party/<int:party_id>')
def rsvp_party(party_id):
    party = parties[party_id]
    party['rsvps'].append(request.remote_addr)
    return redirect(url_for('index'))

@app.route('/view_parties')
def view_parties():
    return render_template('view_parties.html', parties=parties)

@app.route('/view_attending_parties')
def view_attending_parties():
    attending_parties = [party for party in parties if request.remote_addr in party['rsvps']]
    return render_template('view_attending_parties.html', parties=attending_parties)

if __name__ == '__main__':
    app.run(debug=True)


html code

html
<!DOCTYPE html>
<html>
<head>
    <title>Party Application</title>
</head>
<body>
    <h1>Party Application</h1>
    <ul>
        {% for party in parties %}
            <li><a href="/view_party/{{ party.id }}">{{ party.name }}</a></li>
        {% endfor %}
    </ul>
    <a href="/create_party">Create a Party</a>
</body>
</html>


html
<!DOCTYPE html>
<html>
<head>
    <title>Create a Party</title>
</head>
<body>
    <h1>Create a Party</h1>
    <form action="/create_party" method="post">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name">
        <br>
        <label for="date">Date:</label>
        <input type="date" name="date" id="date">
        <br>
        <label for="time">Time:</label>
        <input type="time" name="time" id="time">
        <br>
        <label for="location">Location:</label>
        <input type="text" name="location" id="location">
        <br>
        <input type="submit" value="Create Party">
    </form>
</body>
</html>


html
<!DOCTYPE html>
<html>
<head>
    <title>Edit a Party</title>
</head>
<body>
    <h1>Edit a Party</h1>
    <form action="/edit_party/{{ party.id }}" method="post">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" value="{{ party.name }}">
        <br>
        <label for="date">Date:</label>
        <input type="date" name="date" id="date" value="{{ party.date }}">
        <br>
        <label for="time">Time:</label>
        <input type="time" name="time" id="time" value="{{ party.time }}">
        <br>
        <label for="location">Location:</label>
        <input type="text" name="location" id="location" value="{{ party.location }}">
        <br>
        <input type="submit" value="Edit Party">
    </form>
</body>
</html>


html
<!DOCTYPE html>
<html>
<head>
    <title>Delete a Party</title>
</head>
<body>
    <h1>Delete a Party</h1>
    <p>Are you sure you want to delete the party "{{ party.name }}"?