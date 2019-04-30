import pickle
import os


if os.path.isfile("student.pickle"):
    foo = pickle.load(open("student.pickle", "rb"))
else:
    foo = []
    pickle.dump(foo, open("student.pickle", "wb"))


def add_student_to_db(student_details):
    try:
        pickle_out = open("student.pickle", "rb")
        row_data = []
        final = {}
        file_data = pickle.load(pickle_out)
        for i in student_details.values():
            row_data.append(i)
        final[student_details['roll_number']] = row_data
        file_data.append(final)
        pickle_out = open("student.pickle", "wb")
        pickle.dump(file_data, pickle_out)
        pickle_out.close()
    except Exception as e:
        print('Exception Raised in add_student_to_db function', e)


def search_student_details(roll_number=None):
    try:
        pickle_out = open("student.pickle", "rb")
        file_data = pickle.load(pickle_out)
        data = {}
        for i in file_data:
            for j in i.items():
                if j[0] == roll_number:
                    student_data = {}
                    student_data['roll_number'] = j[0]
                    student_data['name'] = j[1][1]
                    student_data['age'] = j[1][2]
                    student_data['gender'] = j[1][3]
                    data[j[0]] = student_data
                    break
        return data
    except Exception as e:
        print('Exception Raised in search_Student_details', e)
        return None


def show_student_details(roll_number=None):
    try:
        with open('student.pickle', 'rb') as pickle_in:
            file_data = pickle.load(pickle_in)
        data = []
        for i in file_data:
            for j in i.items():
                student_data = dict()
                student_data['roll_number'] = j[0]
                student_data['name'] = j[1][1]
                student_data['age'] = j[1][2]
                student_data['gender'] = j[1][3]
                data.append(student_data)
        return data
    except Exception as e:
        print('Exception Raised in show_student_details', e)
        return None


def delete_student_from_file(roll_number):
    try:
        pickle_in = open("student.pickle", "rb")
        file_data = pickle.load(pickle_in)
        for i in range(len(file_data)):
            try:
                if file_data[i][str(roll_number)]:
                    del (file_data[i])
                    break
            except Exception:
                pass

        pickle_out = open("student.pickle", "wb")
        pickle.dump(file_data, pickle_out)
    except Exception as e:
        print('Exception Raised in delete_student_from_file', e)


def edit_student(student_edit_details=None):
    try:
        pickle_in = open("student.pickle", "rb")
        file_data = pickle.load(pickle_in)
        for i in range(len(file_data)):
            try:
                if file_data[i][str(student_edit_details['roll_number'])]:
                    if student_edit_details.__getitem__('name'):
                        file_data[i][str(student_edit_details['roll_number'])][1] = student_edit_details['name']
                    if student_edit_details.__getitem__('age'):
                        file_data[i][str(student_edit_details['roll_number'])][2] = student_edit_details['age']
                    if student_edit_details.__getitem__('gender'):
                        file_data[i][str(student_edit_details['roll_number'])][3] = student_edit_details['gender']
                    break
            except Exception as e:
                pass
        pickle_out = open("student.pickle", "wb")
        pickle.dump(file_data, pickle_out)
        pickle_out.close()
    except Exception as e:
        print('Exception Raised in edit_student_details', e)
