import json
from mdutils.mdutils import MdUtils

# Read the raw data
action_file_pointer = open('data/action_source_file.json', 'r')
action_data = json.load(action_file_pointer)
action_file_pointer.close()

# Create the markdown and place it in a local file
markdown = MdUtils(file_name=action_data['name'], title=action_data['name'])
markdown.new_header(level=1, title='Overview')
markdown.new_paragraph(action_data['description'])
markdown.new_paragraph()

# Header element in markdown file

markdown.new_header(level=2, title='Id:')
markdown.new_line(action_data['id'])
markdown.new_header(level=2, title='Fqn')
markdown.new_line(action_data['fqn'])
markdown.new_paragraph()

# Input Parameters
data = ['name', 'type', 'description']
markdown.new_header(level=2, title='Input Parameters')
for input_parameter in action_data['input-parameters']:
    data.extend([input_parameter['name'], input_parameter['type'], input_parameter['description']])
data.extend(['', '', ''])
markdown.new_table(columns=3, rows=len(action_data['input-parameters']) + 2, text=data, text_align='left')

markdown.new_header(level=2, title='Script')
markdown.insert_code(action_data['script'], language='javascript')

markdown.new_table_of_contents(table_title='Contents', depth=2)
markdown.create_md_file()
