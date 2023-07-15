import os
import re
import sys
import subprocess
from optparse import OptionParser

ID = ""
VALUE = ""


def checkPrePackages():
    # check and install wizcli if not pre-installed
    process = subprocess.Popen('wizcli version', shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    result = process.communicate()[0]
    #result = process.returncode
    #print(result)
    if result != 00:
        process = subprocess.Popen('rm -f /usr/local/bin/wizcli', shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        process = subprocess.Popen('curl --silent -o wizcli https://wizcli.app.wiz.io/wizcli', shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        result = process.communicate()[0]
        print(result)

        process = subprocess.Popen('chmod +x wizcli', shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        result = process.communicate()[0]
        print(result)

        process = subprocess.Popen('mv wizcli /usr/local/bin', shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        result = process.communicate()[0]
        print(result)

        process = subprocess.Popen('wizcli version', shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        result = process.communicate()[0]
        print(result)

        #process = subprocess.Popen(f'''wizcli auth --id {ID} --secret {VALUE}''', shell=True,
        #                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        #result = process.communicate()[0]
        #res_string = result
        #substring = "required flag(s)"
        
        #if substring in res_string:
        #    print(result)
        #else:
        #    print("Hurray Wizcli is ready to scan Misconfiguration in Terraform, Docker , Kubernetes")


def main():
    try:
        #parser = OptionParser()
        #parser.add_option("-t", "--type", action="store", type="string", dest="type",
        #                  help="Command Type:  1) Setup 2) auth 3) azure 4) gcp 5) docker")
        #parser.add_option("-p", "--path", action="store", type="string", dest="path", help="Source path..")
        #(options, args) = parser.parse_args()
        #if sys.argv[1]
        #if options.type == "Setup":
        if sys.argv[1] == "setup":
            checkPrePackages()
            print()
        elif sys.argv[1] == "upgrade":
            checkPrePackages()
            print()
        #elif options.type == "auth":
        elif sys.argv[1] == "auth":
            process = subprocess.Popen(f'''wizcli auth --id {ID} --secret {VALUE}''', shell=True,
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
            result = process.communicate()[0]
            
            res_string = result
            substring = "required flag(s)"
            
            if substring in res_string:
                print(result)
            else:
                print("Hurray Wizcli is ready to scan Misconfiguration in Terraform, Docker , Kubernetes")
        # Azure
        #elif options.type == "azure" and options.path == "":
        elif sys.argv[1] == "terraform":
            if sys.argv[2] == "azure":
                if len(sys.argv) == 6:
                    current_directory = os.getcwd()
                    # Check for files with .tf or .json extensions
                    matching_files = [filename for filename in os.listdir(current_directory) if
                              filename.endswith((".tf", ".json"))]

                    # Display the matching file names or "No files exist"
                    if matching_files:
                        print("Matching files:")
                        for filename in matching_files:
                            print(filename)
                        print()
                        print()
                        print("Started Scanning Azure Terraform Misconfiguration")
                        print()
                        process = subprocess.Popen(f'''wizcli iac scan --policy "AZURE TFE" --path ./ --name {sys.argv[4]} --project {sys.argv[5]}''', shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                        result = process.communicate()[0]
                        print(result)
                    else:
                        print("Did not found appropriate files to scan")
                elif len(sys.argv) == 7:

        #elif options.type == "azure" and options.path != "":
                    #print(options.path)
                    current_directory = sys.argv[4]
                    # Check for files with .tf or .json extensions
                    matching_files = [filename for filename in os.listdir(current_directory) if
                              filename.endswith((".tf", ".json"))]

                    # Display the matching file names or "No files exist"
                    if matching_files:
                        print("Matching files:")
                        for filename in matching_files:
                            print(filename)
                        print()
                        print()
                        print("Started Scanning Azure Terraform Misconfiguration")
                        print()
                        process = subprocess.Popen(f'''wizcli iac scan --policy "AZURE TFE" --path {sys.argv[4]}/ --name {sys.argv[5]} --project {sys.argv[6]}''',
                                           shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                        result = process.communicate()[0]
                        print(result)
                    else:
                        print("Did not found appropriate files to scan")

        # Gcp
        #elif options.type == "gcp" and options.path == "":
            elif sys.argv[2] == "gcp":
                if len(sys.argv) == 6:
                    current_directory = os.getcwd()
                    # Check for files with .tf or .json extensions
                    matching_files = [filename for filename in os.listdir(current_directory) if
                              filename.endswith((".tf", ".json"))]

                    # Display the matching file names or "No files exist"
                    if matching_files:
                        print("Matching files:")
                        for filename in matching_files:
                            print(filename)
                        print()
                        print()
                        print("Started Scanning Google Terraform Misconfiguration")
                        print()
                        process = subprocess.Popen(f'''wizcli iac scan --policy "GCP TFE" --path ./ --name {sys.argv[4]} --project {sys.argv[5]}''', shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                        result = process.communicate()[0]
                        print(result)
                    else:
                        print("Did not found appropriate files to scan")

        #elif options.type == "gcp"  and options.path != "":
                elif len(sys.argv) == 7:
                    current_directory = sys.argv[4]
                    # Check for files with .tf or .json extensions
                    matching_files = [filename for filename in os.listdir(current_directory) if
                              filename.endswith((".tf", ".json"))]

                    # Display the matching file names or "No files exist"
                    if matching_files:
                        print("Matching files:")
                        for filename in matching_files:
                            print(filename)
                        print()
                        print()
                        print("Started Scanning Google Terraform Misconfiguration")
                        print()
                        process = subprocess.Popen(f'''wizcli iac scan --policy "GCP TFE" --path {sys.argv[4]}/ --name {sys.argv[5]} --project {sys.argv[6]}''',
                                           shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                        result = process.communicate()[0]
                        print(result)
                    else:
                        print("Did not found appropriate files to scan")

        # Docker
        elif sys.argv[1] == "docker":
            if len(sys.argv) == 5:

        #elif options.type == "docker" and options.path == "":

                current_directory = os.getcwd()
                # Check for files with .tf or .json extensions
                matching_files = [filename for filename in os.listdir(current_directory) if
                              filename.endswith((".yml", ".yaml"))]

                # Display the matching file names or "No files exist"
                if matching_files:
                    print("Matching files:")
                    for filename in matching_files:
                        print(filename)
                    print()
                    print()
                    print("Started Scanning Dockerfile Misconfiguration")
                    print()
                    process = subprocess.Popen(f'''wizcli iac scan --policy "THD-Docker-IaC" --path ./ --name {sys.argv[3]} --project {sys.argv[4]}''', shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                    result = process.communicate()[0]
                    print(result)
                else:
                    print("Did not found appropriate files to scan")

        #elif options.type == "docker"  and options.path != "":
            if len(sys.argv) == 6:
                current_directory = sys.argv[3]
                # Check for files with .tf or .json extensions
                matching_files = [filename for filename in os.listdir(current_directory) if
                              filename.endswith((".yml", ".yaml"))]

                # Display the matching file names or "No files exist"
                if matching_files:
                    print("Matching files:")
                    for filename in matching_files:
                        print(filename)
                    print()
                    print()
                    print("Started Scanning Dockerfile Misconfiguration")
                    print()
                    process = subprocess.Popen(f'''wizcli iac scan --policy "THD-Docker-IaC" --path {sys.argv[3]}/ --name {sys.argv[4]} --project {sys.argv[5]}''',
                                           shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                    result = process.communicate()[0]
                    print(result)
                else:
                    print("Did not found appropriate files to scan")
        elif sys.argv[1] == "kubernetes":
            if len(sys.argv) == 5:

        #elif options.type == "docker" and options.path == "":

                current_directory = os.getcwd()
                # Check for files with .tf or .json extensions
                matching_files = [filename for filename in os.listdir(current_directory) if
                              filename.endswith((".yml", ".yaml"))]

                # Display the matching file names or "No files exist"
                if matching_files:
                    print("Matching files:")
                    for filename in matching_files:
                        print(filename)
                    print()
                    print()
                    print("Started Scanning Kubernetes Misconfiguration")
                    print()
                    process = subprocess.Popen(f'''wizcli iac scan --policy "THD-Docker-IaC" --path ./ --name {sys.argv[3]} --project {sys.argv[4]}''', shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                    result = process.communicate()[0]
                    print(result)
                else:
                    print("Did not found appropriate files to scan")

        #elif options.type == "docker"  and options.path != "":
            if len(sys.argv) == 6:
                current_directory = sys.argv[3]
                # Check for files with .tf or .json extensions
                matching_files = [filename for filename in os.listdir(current_directory) if
                              filename.endswith((".yml", ".yaml"))]

                # Display the matching file names or "No files exist"
                if matching_files:
                    print("Matching files:")
                    for filename in matching_files:
                        print(filename)
                    print()
                    print()
                    print("Started Scanning Kubernetes Misconfiguration")
                    print()
                    process = subprocess.Popen(f'''wizcli iac scan --policy "THD-Docker-IaC" --path {sys.argv[3]}/ --name {sys.argv[4]} --project {sys.argv[5]}''',
                                           shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                    result = process.communicate()[0]
                    print(result)
                else:
                    print("Did not found appropriate files to scan")
        
        elif sys.argv[1] == "image":
            if len(sys.argv) == 6:
                print()
                print()
                print("Started Image Scanning For Vunlnerabilities")
                print()
                process = subprocess.Popen(f'''wizcli docker scan -i {sys.argv[5]}''',
                                           shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                result = process.communicate()[0]
                print(result)
        else:
            checkPrePackages()

    except Exception as e:
        print(e)
        print("here")


main()

