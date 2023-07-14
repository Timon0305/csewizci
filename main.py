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
    print(result)
    if result.strip() == "-bash: /usr/local/bin/wizcli: No such file or directory":
        process = subprocess.Popen('curl -o wizcli https://wizcli.app.wiz.io/wizcli', shell=True,
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

        process = subprocess.Popen(f'''wizcli auth --id {ID} --secret {VALUE}''', shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        result = process.communicate()[0]
        res_string = result
        substring = "required flag(s)"
        
        if substring in res_string:
            print(result)
        else:
            print("Hurray Wizcli is ready to scan Misconfiguration in Terraform, Docker , Kubernetes")


def main():
    try:
        parser = OptionParser()
        parser.add_option("-t", "--type", action="store", type="string", dest="type",
                          help="Command Type:  1) Setup 2) auth 3) azure 4) gcp 5) docker")
        parser.add_option("-p", "--path", action="store", type="string", dest="path", help="Source path..")
        (options, args) = parser.parse_args()

        if options.type == "Setup":
            checkPrePackages()
            print()
        elif options.type == "auth":
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
        elif options.type == "azure" and options.path == "":
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
                process = subprocess.Popen('wizcli iac scan --policy "THD-Azure-TF-IaC" --path .', shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                result = process.communicate()[0]
                print(result)
            else:
                print("Did not found appropriate files to scan")

        elif options.type == "azure" and options.path != "":
            print(options.path)
            current_directory = options.path
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
                process = subprocess.Popen(f'''wizcli iac scan --policy "THD-Azure-TF-IaC" --path {options.path}''',
                                           shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                result = process.communicate()[0]
                print(result)
            else:
                print("Did not found appropriate files to scan")

        # Gcp
        elif options.type == "gcp" and options.path == "":

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
                process = subprocess.Popen('wizcli iac scan --policy "THD-GCP-TF-IaC" --path .', shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                result = process.communicate()[0]
                print(result)
            else:
                print("Did not found appropriate files to scan")

        elif options.type == "gcp"  and options.path != "":

            current_directory = options.path
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
                process = subprocess.Popen(f'''wizcli iac scan --policy "THD-GCP-TF-IaC" --path {options.path}''',
                                           shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                result = process.communicate()[0]
                print(result)
            else:
                print("Did not found appropriate files to scan")

        # Docker
        elif options.type == "docker" and options.path == "":

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
                process = subprocess.Popen('wizcli iac scan --policy "THD-Docker-IaC" --path .', shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                result = process.communicate()[0]
                print(result)
            else:
                print("Did not found appropriate files to scan")

        elif options.type == "docker"  and options.path != "":

            current_directory = options.path
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
                process = subprocess.Popen(f'''wizcli iac scan --policy "THD-Docker-IaC" --path {options.path}''',
                                           shell=True,
                                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                           universal_newlines=True)
                result = process.communicate()[0]
                print(result)
            else:
                print("Did not found appropriate files to scan")
        else:
            checkPrePackages()

    except Exception as e:
        print(e)
        print("here")


main()

