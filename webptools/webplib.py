import subprocess
from typing import Dict,List
from .webpbin import getcwebp, getdwebp, getgifwebp, getwebpmux


# ****************** cwebp *********************** #

# now convert image to .webp format

# input_image: input image(.jpeg, .pnp ....)
# output_image: output image .webp
# option: options and quality,it should be given between 0 to 100
def cwebp(input_image: str, output_image: str, option: str) -> Dict:
    cmd = f"{getcwebp()} {option} {input_image} -o {output_image}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


# ****************** dwebp *********************** #

# now convert .webp to other image format

# input_image: input image .webp
# output_image: output image(.jpeg, .pnp ....)
# option: options and quality,it should be given between 0 to 100
def dwebp(input_image: str, output_image: str, option: str) -> Dict:
    cmd = f'"{getdwebp()}" "{input_image}" "{option}" "{output_image}"'
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


# ****************** gif2webp *********************** #

# now convert .gif image to .webp format

# input_image: input image(.jpeg, .pnp ....)
# output_image: /output image .webp
# option: options and quality,it should be given between 0 to 100
def gifwebp(input_image: str, output_image: str, option: str) -> Dict:
    cmd = f"{getgifwebp()} {option} {input_image} -o {output_image}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


# ****************** webpmux *********************** #

# Add ICC profile,XMP metadata and EXIF metadata #

# input_image: input image(.webp)
# output_image: output image .webp
# icc_profile: icc profile
# option: get or set option (icc,xmp,exif)
def webpmux_add(input_image: str, output_image: str, icc_profile: str,
                option: str) -> Dict:
    cmd = f"{getwebpmux()} -set {option} {icc_profile} {input_image} -o {output_image}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


# Extract ICC profile,XMP metadata and EXIF metadata

# input_image: input image(.webp)
# icc_profile: icc profile
def webpmux_extract(input_image: str, icc_profile: str, option: str) -> Dict:
    cmd = f"{getwebpmux()} -get {option} {input_image} -o {icc_profile}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


# Strip ICC profile,XMP metadata and EXIF metadata

# input_image: input image(.webp)
# output_image: output image .webp
def webpmux_strip(input_image: str, output_image: str, option: str) -> Dict:
    cmd = f"{getwebpmux()} -strip {option} {input_image} -o {output_image}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


# Create an animated WebP file from Webp images

# input_images: array of image(.webp)
# output_image: animatedimage .webp
# loop:Loop the frames n number of times
# bgcolor: Background color of the canvas
def webpmux_animate(input_images: List, output_image: str, loop: str,
                    bgcolor: str) -> Dict:
    files = ""
    for frame in input_images:
        files += f" -frame {frame}"

    cmd = f"{getwebpmux()} {files} -loop {loop} bgcolor {bgcolor} -o {output_image}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result


# Get the a frame from an animated WebP file

# input_image: input image(.webp)
# output_image: output image .webp
# frame_number: frame number
def webpmux_getframe(input_image: str, output_image: str,
                     frame_number: str) -> Dict:
    cmd = f"{getwebpmux()} -get frame {frame_number} {input_image} -o {output_image}"
    p = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (stdout, stderr) = p.communicate()
    result = {'exit_code': p.returncode, 'stdout': stdout, 'stderr': stderr,
              'command': cmd}
    return result
