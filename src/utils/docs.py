import os 
import glob

def get_json_files(path):
    """
    @param path: path to the directory containing the json files
    @return: list of paths to the json files
    """
    #  os.path.join(OUTPUT_DIR, [f for f in all_output_files if re.match("^.*worker.*\.json$", f)][0] if len(all_output_files) > 0 else "")
    return glob.glob(os.path.join(path, "*.json"))