from conans.model import Generator
from conans.paths import BUILD_INFO
from conans import ConanFile

from collections import OrderedDict

import json

class VSCodeProperties(Generator):

    def _makeConfigEntry(self, config_name, default_include_path, deps_include_path):
        entry = OrderedDict()
        entry["name"] = config_name
        entry["includePath"] = [default_include_path]
        entry["includePath"].extend(deps_include_path)

        browse = OrderedDict()
        browse["limitSymbolsToIncludedHeaders"] = True
        browse["databaseFilename"] = ""
        entry["browse"] = browse

        return entry

    @property
    def filename(self):
        return ".vscode/c_cpp_properties.json"

    @property
    def content(self):
        configurations = []
        configurations.append(self._makeConfigEntry("Mac", "/usr/include", self.deps_build_info.include_paths))
        configurations.append(self._makeConfigEntry("Linux", "/usr/include", self.deps_build_info.include_paths))
        configurations.append(self._makeConfigEntry("Win32", "/usr/include", self.deps_build_info.include_paths))

        config = {"configurations": configurations}
        config["configurations"] = configurations
        return json.dumps(config, indent = 4)

class VisualStuioCodePropertiesGenerator(ConanFile):
    name = "vscodepropertiesgen"
    version = "0.1"
    description = "Simple visual studio code C/C++ extension property generator"
    url = "https://github.com/mkovalchik/conan-vscodepropertiesgen"
    license = "MIT"

    def build(self):
        pass
    
    def package_info(self):
        self.cpp_info.includedirs = []
        self.cpp_info.libdirs = []
        self.cpp_info.bindirs = []
