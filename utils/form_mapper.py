from models.student import Student


class FormMapper:

    @staticmethod
    def student(form):

        return Student(
            student_id=form.student_id.get(),
            admission_no=form.admission_no.get(),

            first_name=form.first_name.get(),
            last_name=form.last_name.get(),

            gender=form.gender.get(),

            dob=form.dob.get(),

            phone=form.phone.get(),
            email=form.email.get(),

            address=form.address.get(),

            course=form.course.get(),
            department=form.department.get(),

            semester=int(form.semester.get()),
            batch=form.batch.get()
        )