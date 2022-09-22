links = {"LinkedIn" : "https://linkedin.com/in/bhavya-muni/", "GitHub" : "https://github.com/BhavyaMuni/", "Website": "http://bhavyamuni.com/ "}
import subprocess
if __name__ == "__main__":
    for i in links.keys():
        with open (i + ".command", "w") as f:
            f.write("#!/usr/bin/env bash" + "\n")
            f.write(f'python3 -c "import subprocess; subprocess.run(\'pbcopy\', universal_newlines=True, input=\'{links[i]}\')"')
            subprocess.call(['chmod', '0555', '/Users/bhavya/projects/ez-copy/'+i+".command"])