import os
import yaml
import subprocess
config_file = "mkdocs.yml"

def merge_nav(nav, new_nav):
    folder_name = list(new_nav[0].keys())[0]
    existing_folder = next((item for item in nav if isinstance(item, dict) and folder_name in item), None)
    if existing_folder:
        existing_folder[folder_name] = merge_nav(existing_folder[folder_name], new_nav[0][folder_name])
    else:
        nav.append(new_nav[0])
    return nav


def zagniezdzanie(nav,page_name, file):
    if len(nav) == 1:
        return [{page_name: file}]
    else:
        return [{nav[0]: zagniezdzanie(nav[1:],page_name, file)}]


def generate_nav(name_with_files):
    nav = []
    for page_name, file in name_with_files:
        current_nav = []
        path_splited = file.split("/")
        if len(path_splited) > 1:
            current_nav = zagniezdzanie(path_splited,page_name, file)
            nav =merge_nav(nav, current_nav)
        else:
            current_nav = [{page_name:file}]
            nav.extend(current_nav)
    return nav


def update_mkdocs_yml(name_with_files):
    with open(config_file, "r", encoding="utf-8") as ymlfile:
         config = yaml.safe_load(ymlfile)

    nav = generate_nav(name_with_files)
    config["nav"] = nav

    with open(config_file, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, allow_unicode=True, default_flow_style=False)


    # print("[INFO] Plik mkdocs.yml został zaktualizowany!")
def find_all_md_files_with_path(directory, base_path=""):
    files = []
    with os.scandir(directory) as entries:
        for entry in entries:
            relative_path = os.path.join(base_path, entry.name) 
            if entry.is_file():
                files.append(relative_path)
            elif entry.is_dir():
                files.extend(find_all_md_files_with_path(entry.path, relative_path))
    return files

def create_site_name(filename):
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line.startswith("# "):  
                return line[2:].strip()  
    return  os.path.basename(filename)[:-3] 

def print_tree(nav, level=0):
    """ Rekurencyjnie wyświetla listę jako drzewo katalogów. """
    for item in nav:
        if isinstance(item, dict):  # Jeśli to folder
            for key, value in item.items():
                print("  " * level + f"📂 {key}")  
                if isinstance(value, list):  # Sprawdza, czy zawartość to lista (np. kolejne katalogi lub pliki)
                    print_tree(value, level + 1)
                else:  # Jeśli wartość to string (plik), wyświetl jako plik
                    print("  " * (level + 1) + f"📄 {value}")
        elif isinstance(item, str):  # Jeśli to plik, wyświetl go
            print("  " * level + f"📄 {item}")


if __name__ == "__main__":
    try:
        os.chdir('docs')
    except:
        print("[ERROR] Directory 'docs' not found")
        exit()
    files = find_all_md_files_with_path(".")
    name_with_files = list(map(lambda x: (create_site_name(x),x), files))
    os.chdir('..')
    # update_mkdocs_yml(name_with_files)
    print(generate_nav(name_with_files))
    print_tree(generate_nav(name_with_files))
    update_mkdocs_yml(name_with_files)
                
    print("[INFO] Uruchamiam MkDocs...")
    # subprocess.run(["mkdocs", "serve"])
