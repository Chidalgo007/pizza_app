import json
import os

class StorageManager:
    def __init__(self):
       # Get the directory of the script
       script_directory = os.path.dirname(os.path.abspath(__file__))
       self.folder_path = script_directory

    def load_data(self, data_name):
        filename = os.path.join(self.folder_path, self.get_filename(data_name))
        try:
            file = open(filename,'r')
            data = file.read()
            file.close
        except FileNotFoundError:
            return None    
        return json.loads(data)

    def save_data(self, data_name, data_content):
        filename = os.path.join(self.folder_path, self.get_filename(data_name))
        data_str = json.dumps(data_content)
        file = open(filename, 'w')
        file.write(data_str)
        file.close()

    def get_filename(self, data_name):
        return data_name + '.json'
