import datetime
import os
from urllib.request import Request, urlopen
from constants import USERNAME, EXTENSION, SEPARATOR


def get_filename(id):
    id = id.replace(" ", "_")
    id = id.replace(".", "_")
    id = id.replace("__", "_")
    return id


def get_sorted_problems(existing_problems, new_problem):
    data = []
    for problem in existing_problems:
        problem = problem[1:-1].strip()
        fields = [field.strip() for field in problem.split("|")]
        data.append(fields)
    if data.count(new_problem) == 0:
        data.append(new_problem)
    # Sort by difficulty level
    data = sorted(data, key=lambda x: float(x[2]))
    return data


def get_sorted_problems_table(existing_problems, problem_info, solution_file):
    problem_link = "[{}]({})".format(problem_info["title"],
                                     problem_info["url"])
    solution_link = "[Solution](solutions/{})".format(solution_file)
    new_problem = [problem_link, problem_info["source"],
                   problem_info["difficulty"], solution_link]
    sorted_problems = get_sorted_problems(existing_problems, new_problem)
    lines = []
    for problem in sorted_problems:
        line = "| {} | {} | {} | {} |".format(
            problem[0], problem[1], problem[2], problem[3])
        lines.append(line)
    return lines


def update_readme(problem_info, filename_title):
    separator = SEPARATOR
    with open("../README.md", "r+") as readme:
        lines = [line.strip() for line in readme.readlines()]
        separator_index = lines.index(separator) + 1
        header = lines[:separator_index]
        problems = lines[separator_index:]
        problems = [line.strip() for line in problems if line.strip() != '']
        sorted_problems = get_sorted_problems_table(problems,
                                                    problem_info,
                                                    filename_title)
        # clear the file contents
        readme.seek(0)
        readme.truncate()
        for line in header:
            readme.write(line + "\n")
        for line in sorted_problems:
            readme.write(line + "\n")


def make_problem_directory(repo_path, filename_title):
    directory = os.path.join(repo_path, "solutions", filename_title)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return str(directory)


def make_solution_file(problem_info, solver_info, directory_path):
    filename = "solution_" + solver_info["username"] + solver_info["extension"]
    file_path = os.path.join(directory_path, filename)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.writelines(write_file_header(problem_info, solver_info))
    return file_path


def write_file_header(problem_info, solver_info):
    created_date = datetime.datetime.today().strftime("%d %B %Y")
    multiline_comment_start = '"""\n'
    multiline_comment_end = '"""\n'
    if solver_info["extension"] != ".py":
        multiline_comment_start = '/*\n'
        multiline_comment_end = '*/\n'
    header_str = multiline_comment_start
    header_str += 'Title     : ' + problem_info["title"] + '\n'
    header_str += 'Source    : ' + problem_info["source"] + '\n'
    header_str += 'URL       : ' + problem_info["url"] + '\n'
    header_str += 'Author    : ' + solver_info["username"] + '\n'
    header_str += 'Created   : ' + created_date + '\n'
    header_str += multiline_comment_end
    return header_str


def get_mandatory_field(user_message):
    while True:
        user_input = input(user_message).strip()
        if not user_input:
            print("Invalid input. Please try again.")
        else:
            return user_input


def get_solver_information():
    username = input("Username (keep blank for " + USERNAME + "): ").strip()
    extension = input("Extension (keep blank for " + EXTENSION + "): ").strip()
    if username == '':
        username = USERNAME
    if extension == '':
        extension = EXTENSION
    return {
        "username": username,
        "extension": extension
    }


def get_tag_value(prefix, suffix, data):
    value = ''
    try:
        start_position = data.index(prefix)
        if start_position:
            start_position += len(prefix)
            end_position = start_position + data[start_position:].index(suffix)
            if end_position:
                value = "".join(data[start_position:end_position])
            value = value.strip()
    except ValueError:
        pass
    return value


def get_problem_information():
    problem_url = get_mandatory_field("Enter problem URL: ")
    request_obj = Request(problem_url, headers={'User-Agent': 'Mozilla/5.0'})
    page_data = urlopen(request_obj).read().decode('utf-8')
    title_prefix = '<div class="headline-wrapper"><h1>'
    title = get_tag_value(title_prefix, "<", page_data)
    id = get_tag_value('<strong>Problem ID: </strong>', "<", page_data)
    difficulty_prefix = '<strong>Difficulty:  </strong><span>'
    difficulty = get_tag_value(difficulty_prefix, "<", page_data)
    source_link = get_tag_value('<strong>Source:</strong>', '/a>', page_data)
    source = get_tag_value('">', "<", source_link)
    return {
        "id": id,
        "title": title,
        "difficulty": difficulty,
        "url": problem_url,
        "source": source
    }


if __name__ == '__main__':
    problem_info = get_problem_information()
    solver_info = get_solver_information()
    current_path = os.path.dirname(os.path.realpath(__file__))
    repo_path = os.path.abspath(os.path.join(current_path, os.pardir))
    filename_title = get_filename(problem_info["id"])
    update_readme(problem_info, filename_title)
    directory = make_problem_directory(repo_path, filename_title)
    filepath = make_solution_file(problem_info, solver_info, directory)
    print("Done. Open {}".format(filepath))
