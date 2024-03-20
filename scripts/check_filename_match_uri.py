import sys
import os
from pathlib import Path
from rdflib import Graph, RDF, RDFS, OWL, SKOS, Namespace

def extract_main_uri(ttl_file,root_dir):
    """
    Extracts the main URI relative to the specified TTL file.

    Args:
        ttl_file (str): The path of the TTL file.

    Returns:
        str: The main relative URI if found, otherwise None.
    """
    g = Graph()
    g.parse(ttl_file, format="ttl")

    # Define namespace prefixes
    dcatapit = Namespace("http://dati.gov.it/onto/dcatapit#")

    main_uri = None

    for s, p, o in g:
        if (s, RDF.type, OWL.Ontology) in g and "onto" in root_dir.lower():
            main_uri = s
            break
        elif p == RDF.type and o == dcatapit.Dataset:
            main_uri = s
            break
        # elif (s, RDF.type, RDFS.Class) in g:
        #     main_uri = s
        #     break        
        elif (s, RDF.type, SKOS.ConceptScheme) in g:
            main_uri = s
            break        

    return main_uri

def check_filename_match_uri(root_dirs):
    """
    Checks whether the name of each TTL or oas3.yaml file matches the final part of its relative URI.

    Args:
        root_dirs (list): List of directories to search for TTL files.

    Returns:
        list: List of tuples (file, uri) for TTL or oas3.yaml files that do not match the URI.
    """
    mismatches = []

    for root_dir in root_dirs:
        for file_path in Path(root_dir).rglob("*.ttl"):
            filename = file_path.stem  # File name without extension
            uri = extract_main_uri(str(file_path), root_dir)  # Main relative URI of the file

            if uri:
                # Extract the final part of the URI
                uri_parts = str(uri).split("/")
                last_uri_part = uri_parts[-1]
                if last_uri_part == '':
                    last_uri_part = uri_parts[-2]                

                # Check if the root directory contains "schema"
                if "schema" in root_dir.lower():
                    # Check if the file with .oas3.yaml extension exists
                    oas3_yaml_file = Path(file_path.parent, f"{last_uri_part}")
                    if not oas3_yaml_file.exists():
                        mismatches.append((str(oas3_yaml_file), str(uri)))
                else:
                    # Compare the file name with the last part of the URI
                    if filename != last_uri_part:
                        mismatches.append((str(file_path), str(uri)))
            else:
                print(f"Warning: No main relative URI found for file {file_path}")

    return mismatches

def check_directory_existence(root_dirs):
    existing_dirs = [root_dir for root_dir in root_dirs if os.path.exists(root_dir)]
    if not existing_dirs:
        print("(no files to check)Skipped")
        return False

    for root_dir in existing_dirs:
        print(f"WARNING: {root_dir} does not exist")
    return True

def main():
    root_dirs = sys.argv[1:] 

    if not root_dirs:
        print("No root directories provided.")
        exit(1)
        
    if not check_directory_existence(root_dirs):
        exit(0)

    mismatches = check_filename_match_uri(root_dirs)

    if mismatches:
        print("Error: The following files do not match their relative URI:")
        for file_path, uri in mismatches:
            print(f"- File: {file_path}, URI: {uri}")
        exit(1)
    else:
        print("All files match their relative URI.")

if __name__ == "__main__":
    main()

