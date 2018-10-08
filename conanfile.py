#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools


class CmakemodulesConan(ConanFile):
    name        = 'cmake-modules'
    version     = '1.0'
    license     = 'MIT'
    url         = 'https://github.com/kheaactua/conan-cmake-modules'
    description = 'Import CMake modules from https://github.com/rpavlik/cmake-modules'

    def source(self):
        self.run('git clone https://github.com/rpavlik/cmake-modules.git %s'%self.name)

    def package(self):
        self.copy('*', src='cmake-modules')

    def package_info(self):
        self.env_info.CMAKE_PREFIX_PATH.append(self.cpp_info.resdirs[0])

# vim: ts=4 sw=4 expandtab ffs=unix ft=python foldmethod=marker :
