from Helpers.ConfigHelper import ConfigHelper
from Helpers.CSVHelper import CSVHelper
cfg = ConfigHelper()
csv = CSVHelper()
files_to_run = cfg.readFilesToRunConfig()
for file in files_to_run:
    data = csv.read_csv(file)
    print(data)