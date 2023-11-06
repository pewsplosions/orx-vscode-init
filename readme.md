# ORX Project Starter

This is a simple script for generating an ORX project with VS Code tasks for building and running the project with the Microsoft C++ toolchain.

## Purpose

I created this because I like VS Code a lot better than full Visual Studio. This will also make it a little easier to use the ORX init command I think and take care of other setup steps like initializing a git repo, making a readme, making the initial commit, etc...

## Usage

1. Pre-requisites. On Windows, highly recommend using [Scoop](https://scoop.sh/) when possible.
    - Must install [Visual Studio and Visual Studio Code](https://visualstudio.microsoft.com/downloads/). There is a way to install the VS toolchain without installing Visual Studio but I have not tried that way yet and it doesn't hurt to have Visual Studio around just in case.
    - Must also have [git](https://git-scm.com) installed. Also set up [git-lfs](https://git-lfs.com/) recommended.
    - Must have [ORX](https://orx-project.org/) set up somewhere and built.

2. Edit the generate.py file. There are a handful of configuration variables at the top to point it to ORX, target location, project name, etc... This seems just as easy (or easier) than requiring a bunch of command line options.

3. Navigate to the new project directory and open it in VS Code. (Should be able to right click, Open VS Code Here if you installed that option. If you installed VS Code with scoop, there is a registry command to add it, check scoop install again.)

4. Run the build task and then run the rundebug task to launch the initial ORX demo. I have made these shortcuts Ctrl+F5 and F5 so I can quickly build and launch the game. Pretty sure you can set any shortcut to them.

5. Enjoy building your new game! Note, this is just to get up and running. To do releases and such later it may be a more involved process. Also, the init tool only seems to add the build options for the current system (e.g. Windows) so if you want to update your project to have other platform build options, that'll require extra work for now (may try to update this later for Linux and Mac but currently just working on Windows so I have no way to really test that.)

6. EXTRA - Added code snippets to quickly generate boilerplate Scroll Objects header and cpp content. The files will still need to be created manually and added to the .vcxproj file but this will save some typing and copy/pasta maybe.

Note, when adding new headers and code files, they need to be manually aded to the .vcxproj file.

#### Cross Compile WSL

There is a third task that allows cross compiling for Linux. This has some pre-requisites of its own. First you have to set up [WSL](https://learn.microsoft.com/en-us/windows/wsl/install). This may be as simple as `wsl --install` for most people. This task was tested specifically with Ubuntu as the distro. Others may work too, would just need to update the task for your specific use case.

After WSL is all set up, you will need to clone, setup, and build ORX on the WSL instance. This will require `sudo apt-get install build-essential` to set up the compiler. Otherwise, this is no different than is already documented in the ORX learning material and should set an ORX environment variable in your linux environment.

With build-essential, ORX, and WSL all set up now, you can assign a hotkey or run the new task from the command palette. It should build all the objects and end up with the .so libraries and an executable file in the bin (these are fine to live alongside the Windows build also.)

Note, you may need to create a project on linux with ORX init tool to get the linux build folder. You can then just copy this folder to your project.

Also note, just like developing for Windows requires adding new H and C/CPP files to vcxproj, any new H and C/CPP files will need to be added to the .make file in the build/linux/gmake folder.
