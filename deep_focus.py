from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.created_at = datetime.now()

class Task(Note):
    def __init__(self, title, content):
        super().__init__(title, content)
        self.completed = False

    def complete(self):
        self.completed = True

class Event(Note):
    def __init__(self, title, content, start_time, end_time):
        super().__init__(title, content)
        self.start_time = start_time
        self.end_time = end_time

class Planner:
    def __init__(self):
        self.notes = []
        self.tasks = []
        self.events = []

    def add_note(self, note):
        self.notes.append(note)

    def add_task(self, task):
        self.tasks.append(task)

    def add_event(self, event):
        self.events.append(event)

    def get_all_notes(self):
        return self.notes

    def get_all_tasks(self):
        return self.tasks

    def get_all_events(self):
        return self.events

planner = Planner()

@app.route('/')
def home():
    return render_template('index.html', notes=planner.get_all_notes(), tasks=planner.get_all_tasks(), events=planner.get_all_events())

@app.route('/add_note', methods=['POST'])
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')
    note = Note(title, content)
    planner.add_note(note)
    return redirect(url_for('home'))

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    content = request.form.get('content')
    task = Task(title, content)
    planner.add_task(task)
    return redirect(url_for('home'))

@app.route('/add_event', methods=['POST'])
def add_event():
    title = request.form.get('title')
    content = request.form.get('content')
    start_time = request.form.get('start_time')
    end_time = request.form.get('end_time')
    event = Event(title, content, start_time, end_time)
    planner.add_event(event)
    return redirect(url_for('home'))

@app.route('/complete_task/<title>')
def complete_task(title):
    task = next((t for t in planner.tasks if t.title == title), None)
    if task is not None:
        task.complete()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)