import platform
from typing import Any
from os.path import dirname, abspath


def getcwebp(bin_path: Any) -> Any:
    if bin_path is None:
        if platform.system() == 'Linux':
            return dirname(
                dirname(abspath(__file__))) + '/lib/libwebp_linux/bin/cwebp'
        elif platform.system() == 'Windows':
            arch = platform.architecture()
            if arch[0] == '64bit':
                return dirname(dirname(
                    abspath(__file__))) + '/lib/libwebp_win64/bin/cwebp.exe'
            elif arch[0] in ('32bit', '86bit'):
                print('Unsupported platform:', platform.system(),
                      platform.architecture())
        elif platform.system() == 'Darwin':
            return dirname(
                dirname(abspath(__file__))) + '/lib/libwebp_osx/bin/cwebp'
        else:
            print('Unsupported platform:', platform.system(),
                  platform.architecture())
    else:
        return bin_path


def getdwebp(bin_path: Any) -> Any:
    if bin_path is None:
        if platform.system() == 'Linux':
            return dirname(
                dirname(abspath(__file__))) + '/lib/libwebp_linux/bin/dwebp'
        elif platform.system() == 'Windows':
            arch = platform.architecture()
            if arch[0] == '64bit':
                return dirname(dirname(
                    abspath(__file__))) + '/lib/libwebp_win64/bin/dwebp.exe'
            elif arch[0] == '32bit' and arch[0] == '86bit':
                print('Unsupported platform:', platform.system(),
                      platform.architecture())
        elif platform.system() == 'Darwin':
            return dirname(
                dirname(abspath(__file__))) + '/lib/libwebp_osx/bin/dwebp'
        else:
            print('Unsupported platform:', platform.system(),
                  platform.architecture())
    else:
        return bin_path


def getgifwebp(bin_path: Any) -> Any:
    if bin_path is None:
        if platform.system() == 'Linux':
            return dirname(
                dirname(abspath(__file__))) + '/lib/libwebp_linux/bin/gif2webp'
        elif platform.system() == 'Windows':
            arch = platform.architecture()
            if arch[0] == '64bit':
                return dirname(dirname(
                    abspath(__file__))) + '/lib/libwebp_win64/bin/gif2webp.exe'
            elif arch[0] in ('32bit', '86bit'):
                print('Unsupported platform:', platform.system(),
                      platform.architecture())
        elif platform.system() == 'Darwin':
            return dirname(
                dirname(abspath(__file__))) + '/lib/libwebp_osx/bin/gif2webp'
        else:
            print('Unsupported platform:', platform.system(),
                  platform.architecture())
    else:
        return bin_path


def getwebpmux(bin_path: Any) -> Any:
    if bin_path is None:
        if platform.system() == 'Linux':
            return dirname(
                dirname(abspath(__file__))) + '/lib/libwebp_linux/bin/webpmux'
        elif platform.system() == 'Windows':
            arch = platform.architecture()
            if arch[0] == '64bit':
                return dirname(dirname(
                    abspath(__file__))) + '/lib/libwebp_win64/bin/webpmux.exe'
            elif arch[0] in ('32bit', '86bit'):
                print('Unsupported platform:', platform.system(),
                      platform.architecture())
        elif platform.system() == 'Darwin':
            return dirname(
                dirname(abspath(__file__))) + '/lib/libwebp_osx/bin/webpmux'
        else:
            print('Unsupported platform:', platform.system(),
                  platform.architecture())
    else:
        return bin_path
