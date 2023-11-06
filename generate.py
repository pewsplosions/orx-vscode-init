import os
import shutil
import glob

# TODO - Configure the project with the variables before generating.
# This is done to not have to enter it all on command line arguments.

orx_location = os.environ["ORX"] + "\.."
print (orx_location)
orx_init_cmd = "init.bat"
orx_options  = [
  # bundle: orxBundle support (resources can be automatically packaged and encrypted)=[no], optional
  # c++: Create a C++ project instead of C=[yes], optional
  # imgui: Dear ImGui support (https://github.com/ocornut/imgui)=[no], triggers [+c++], optional
  # mod: MOD (ProTracker) decoding support=[no], optional
  # movie: Movie (MPEG-1) decoding support=[no], optional
  # nuklear: Nuklear support (https://github.com/immediate-mode-ui/nuklear)=[no], optional
  # remote: orxRemote support (resources can be stored on a web server, HTTP-only)=[no], optional
  # scroll: C++ convenience layer with config-object binding=[no], triggers [+c++], optional

  # "+c++",
  # "-c++",
  "+scroll",
  "+remote",
  "+bundle",
  # "+imgui",
  "+mod",
  "+movie",
  # "+nuklear"
]

target_location = r"<Full path to new project directory>"
project_name = "Sandbox"
new_project = target_location + "/" + project_name

original_location = os.getcwd()


class colors:
  """ Colors for terminal output. """
  END = "\033[0m"
  GO = "\033[1;32m"
  TASK = "\033[1;94m"
  ALERT = "\033[1;31m"

def orx_init():
  os.chdir(orx_location)
  final_command = "{} {}".format(orx_init_cmd, new_project)
  for item in orx_options:
    final_command = final_command + " " + item
  os.system(final_command)
  os.chdir(original_location)

def copy_vscode():
  os.chdir(original_location)
  shutil.copytree(original_location + "/.vscode", new_project + "/.vscode")

def clean_up():
  os.chdir(new_project)
  for f in glob.glob("*.sublime-project"):
    os.remove(f)
  # TODO - Consider also removing the initial orx assets?

def git_init():
  os.chdir(new_project)
  with open("readme.md", "w") as fp:
    fp.write("# " + project_name)
  with open(".gitignore", "w") as fp:
    fp.write(".vscode\n")
    fp.write("bin\n")
    fp.write("build/**/obj\n")
  os.system("git init .")
  os.system("git lfs track \"data/sound/**\"")
  os.system("git lfs track \"data/texture/**\"")
  os.system("git add --all")
  os.system("git commit -m \"Project Generated!\"")


print(colors.GO + "Generating ORX Project")
print(colors.GO + "  - {} at {}".format(project_name, target_location))

print(colors.TASK + "Running ORX Init Command" + colors.END)
orx_init()

print(colors.TASK + "Copying VS Code Settings" + colors.END)
copy_vscode()

print(colors.TASK + "Cleaning Up!" + colors.END)
clean_up()

print(colors.TASK + "Initialize Git Repository" + colors.END)
git_init()

print(colors.GO + "Finished Creating " + project_name + colors.END)
