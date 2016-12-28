# conan-vscodeproperties
![Build Status](https://img.shields.io/badge/status-works%20for%20me-lightgrey.svg)

A [conan](https://conan.io) generator for [microsoft's visual studio code C/C++ extension]
(https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) property file

Generates a .vscode/c_cpp_properties.json file for the default configurations using
the default properties with the include paths used by conan appended to the default include paths

# Using
This generator is not currently published to a public conan server so you will have to export it
into your local conan cache:

Clone this repository: '`git clone https://github.com/mkovalchik/conan-vscodepropertiesgen.git`'

Export the generator into your local conan cache: '`cd conan-vscodepropertiesgen; conan export conan-vscodepropertiesgen/0.1@mkovalchik/stable`'

Include the generator in your `conanfile.txt`
```
[requires]
vscodepropertiesgen/0.1@mkovalchik/stable

[generators]
VSCodeProperties
```

# Todo
- [ ] Publish on a public conan server
- [ ] Specify the file path to write the properties to
- [ ] Merge/Append conan include directories to vscode includePaths property instead of replacing the whole file
- [ ] Allow/Handle definition of specific configuration names
