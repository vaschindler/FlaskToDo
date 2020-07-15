from flask import Flask, render_template
from helper import todo, descriptions, due
from forms import ToDoForm

app = Flask(__name__)
app.config["SECRET_KEY"] ="mysecret"


@app.route("/", methods=["GET","POST"])
def index():
    todo_form= ToDoForm()
    if todo_form.validate_on_submit():
        new_id=len(todo)+1
        todo[new_id] = todo_form.todo.data
        descriptions[new_id] = todo_form.descriptions.data
    return render_template("index.html", template_todo=todo, template_form=todo_form)

@app.route("/todos/<int:id>", methods=["GET", "POST"])
def todos(id):
    return render_template("todos.html", template_todo=todo[id], template_descriptions=descriptions[id])

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
