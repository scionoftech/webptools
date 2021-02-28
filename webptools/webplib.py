import subprocess
from pathlib import Path
import os
import uuid
import base64
from typing import Tuple
from typing import Dict, List
from .webpbin import getcwebp, getdwebp, getgifwebp, getwebpmux


def grant_permission():
    """
    Change permission of webp executables to 755
    :return:
    """
    files = [getcwebp(), getdwebp(), getgifwebp(), getwebpmux()]
    for file in files:
        os.chmod(file, 0o755)


def temp_file_path() -> str:
    """
    Get Temp folder path
    :return:
    """
    return f"{get_project_path()}{os.sep}temp{os.sep}"


# get project root path
def get_project_path() -> str:
    """
    Get root folder path
    :return:
    """
    return str(
        Path(__file__).parent.parent)


def base64str2webp_base64str(base64str: str, image_type: str, option: str,
                             temp_path: str = None,
                             logging: str = "-v") -> Tuple:
    """
    Convert bas64 image to webp base64
    :param base64str:
    :param image_type:
    :param option:
    :param temp_path:
    :param logging:
    :return:
    """
    if not temp_path:
        temp_path = temp_file_path()

    filename = uuid.uuid4().hex

    input_file = f"{temp_path}{filename}.{image_type}"
    output_file = f"{temp_path}{filename}.webp"

    imgdata = base64.b64decode(base64str)

    with open(input_file, 'wb') as f:
        f.write(imgdata)

    results = cwebp(input_image=input_file, output_image=output_file,
                    option=option, logging=logging)

    if results["exit_code"] == 0:
        with open(output_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        for fpath in [input_file, output_file]:
            file_to_rem = Path(fpath)
            if file_to_rem.exists():
                file_to_rem.unlink()
        return encoded_string.decode('utf-8'), results
    else:
        return None, results


# ****************** cwebp *********************** #

def cwebp(input_image: str, output_image: str, option: str,
          logging: str = "-v") -> Dict:
    """
    now convert image to .webp format

    input_image: input image(.jpeg, .pnp ....)
    output_image: output image .webp
    option: options and quality,it should be given between 0 to 100

    :param input_image:
    :param output_image:
    :param option:
    :param logging:
    :return:
    """
    cmd = f"{getcwebp()} {option} {input_image} -o {output_image} {logging}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


# ****************** dwebp *********************** #

def dwebp(input_image: str, output_image: str, option: str,
          logging: str = "-v") -> Dict:
    """
    now convert .webp to other image format

    input_image: input image .webp
    output_image: output image(.jpeg, .pnp ....)
    option: options and quality,it should be given between 0 to 100
    :param input_image:
    :param output_image:
    :param option:
    :param logging:
    :return:
    """
    cmd = f"{getdwebp()} {input_image} {option} {output_image} {logging}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


# ****************** gif2webp *********************** #

def gifwebp(input_image: str, output_image: str, option: str,
            logging: str = "-v") -> Dict:
    """
    now convert .gif image to .webp format

    input_image: input image(.jpeg, .pnp ....)
    output_image: /output image .webp
    option: options and quality,it should be given between 0 to 100
    :param input_image:
    :param output_image:
    :param option:
    :param logging:
    :return:
    """
    cmd = f"{getgifwebp()} {option} {input_image} -o {output_image} {logging}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


# ****************** webpmux *********************** #

def webpmux_add(input_image: str, output_image: str, icc_profile: str,
                option: str, logging: str = "-v") -> Dict:
    """
    Add ICC profile,XMP metadata and EXIF metadata #

    input_image: input image(.webp)
    output_image: output image .webp
    icc_profile: icc profile
    option: get or set option (icc,xmp,exif)
    :param input_image:
    :param output_image:
    :param icc_profile:
    :param option:
    :param logging:
    :return:
    """
    cmd = f"{getwebpmux()} -set {option} {icc_profile} {input_image} -o {output_image} {logging}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


def webpmux_extract(input_image: str, icc_profile: str, option: str,
                    logging: str = "-v") -> Dict:
    """
    Extract ICC profile,XMP metadata and EXIF metadata

    input_image: input image(.webp)
    icc_profile: icc profile
    :param input_image:
    :param icc_profile:
    :param option:
    :param logging:
    :return:
    """
    cmd = f"{getwebpmux()} -get {option} {input_image} -o {icc_profile} {logging}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


def webpmux_strip(input_image: str, output_image: str, option: str,
                  logging: str = "-v") -> Dict:
    """
    Strip ICC profile,XMP metadata and EXIF metadata

    input_image: input image(.webp)
    output_image: output image .webp
    :param input_image:
    :param output_image:
    :param option:
    :param logging:
    :return:
    """
    cmd = f"{getwebpmux()} -strip {option} {input_image} -o {output_image} {logging}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


def webpmux_animate(input_images: List, output_image: str, loop: str,
                    bgcolor: str, logging: str = "-v") -> Dict:
    """
    Create an animated WebP file from Webp images

    input_images: array of image(.webp)
    output_image: animatedimage .webp
    loop:Loop the frames n number of times
    bgcolor: Background color of the canvas
    :param input_images:
    :param output_image:
    :param loop:
    :param bgcolor:
    :param logging:
    :return:
    """
    files = ""
    for frame in input_images:
        files += f" -frame {frame}"

    cmd = f"{getwebpmux()} {files} -loop {loop} bgcolor {bgcolor} -o {output_image} {logging}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


def webpmux_getframe(input_image: str, output_image: str,
                     frame_number: str, logging: str = "-v") -> Dict:
    """
    Get the a frame from an animated WebP file

    input_image: input image(.webp)
    output_image: output image .webp
    frame_number: frame number
    :param input_image:
    :param output_image:
    :param frame_number:
    :param logging:
    :return:
    """
    cmd = f"{getwebpmux()} -get frame {frame_number} {input_image} -o {output_image} {logging}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result
