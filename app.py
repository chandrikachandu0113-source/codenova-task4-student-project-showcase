from flask import Flask, render_template, request, redirect, url_for, flash
from database import (
    init_db,
    add_project,
    get_approved_projects,
    get_all_projects,
    update_project_status,
    delete_project
)

app = Flask(__name__)
app.secret_key = "codenova_student_showcase"

# Initialize database
init_db()


@app.route("/")
def index():
    projects = get_approved_projects()
    return render_template("index.html", projects=projects)


@app.route("/submit", methods=["POST"])
def submit_project():
    student_name = request.form.get("student_name", "").strip()
    project_title = request.form.get("project_title", "").strip()
    description = request.form.get("description", "").strip()
    technology = request.form.get("technology", "").strip()
    category = request.form.get("category", "").strip()
    email = request.form.get("email", "").strip()

    if not all([student_name, project_title, description,
                technology, category, email]):
        flash("Please fill in all fields.")
        return redirect(url_for("index"))

    add_project(
        student_name,
        project_title,
        description,
        technology,
        category,
        email
    )

    flash("Project submitted successfully! Waiting for admin approval.")
    return redirect(url_for("index"))


@app.route("/admin")
def admin():
    projects = get_all_projects()
    return render_template("admin.html", projects=projects)


@app.route("/admin/approve/<int:project_id>")
def approve_project(project_id):
    update_project_status(project_id, "Approved")
    flash("Project approved successfully.")
    return redirect(url_for("admin"))


@app.route("/admin/reject/<int:project_id>")
def reject_project(project_id):
    update_project_status(project_id, "Rejected")
    flash("Project rejected.")
    return redirect(url_for("admin"))


@app.route("/admin/delete/<int:project_id>")
def delete_project_route(project_id):
    delete_project(project_id)
    flash("Project deleted.")
    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(debug=True)