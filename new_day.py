import os
import shutil
import sys
from datetime import datetime


def print_on_stderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def execute():
    template_file_name = "template.md"
    date_pattern_to_replace = "@date@"

    date = setup_date()

    current_path = os.path.dirname(os.path.realpath(__file__))

    template_file_path = current_path + "/" + template_file_name
    if not os.path.exists(template_file_path):
        print_on_stderr("No template file: {}".format(template_file_path))
        exit(1)

    new_journal_entry_file_path = "{}/{}.md".format(current_path, date)

    if os.path.exists(new_journal_entry_file_path):
        print_on_stderr("Journal entry from: {} already exists. ({})".format(date, new_journal_entry_file_path))
        exit(2)

    copy_file(new_journal_entry_file_path, template_file_path)
    replace_date_pattern_with_data(date, date_pattern_to_replace, new_journal_entry_file_path)


def copy_file(new_journal_entry_file_path, template_file_path):
    shutil.copy(template_file_path, new_journal_entry_file_path)
    print("Created new file: {}".format(new_journal_entry_file_path))


def replace_date_pattern_with_data(date, date_pattern_to_replace, new_journal_entry_file_path):
    with open(new_journal_entry_file_path, "r") as file:
        file_contents = file.read()
    updated_content = file_contents.replace(date_pattern_to_replace, date)
    with open(new_journal_entry_file_path, "w") as file:
        file.write(updated_content)


def setup_date():
    if len(sys.argv) > 1 and len(sys.argv[1]) > 0:
        return sys.argv[1]
    return datetime.now().strftime("%d.%m.%Y")


if __name__ == "__main__":
    execute()
