from os import sep
from pathlib import Path
import base64
from webptools import cwebp, dwebp, gifwebp, webpmux_add, webpmux_extract
from webptools import webpmux_strip, webpmux_animate, webpmux_getframe
from webptools import base64str2webp_base64str, grant_permission

grant_permission()
# *************** cwebp ************** #

# pass input_image(.jpeg,.pnp .....) path ,
# output_image(give path where to save and image file name with .webp
# file type extension)
# print(cwebp(
#     f"{str(Path(__file__).parent.parent)}{sep}extras{sep}python_logo.jpg",
#     f"{str(Path(__file__).parent.parent)}{sep}extras{sep}python_logo.webp",
#     "-q 80",logging="-v",bin_path="/home/sky/Desktop/webp/lib/libwebp_linux/bin/cwebp"))

# ******* dwebp ************ #

# pass input_image(.webp image) path ,output_image(.jpeg,.pnp .....)
print(dwebp(
    f"{str(Path(__file__).parent.parent)}{sep}extras{sep}python_logo.webp",
    f"{str(Path(__file__).parent.parent)}{sep}extras{sep}python_logo.jpg",
    "-o",logging="-v",bin_path="/home/sky/Desktop/webp/lib/libwebp_linux/bin/dwebp"))

# ***************** gif2webp *********************** #

# pass input_image(.gif) path ,output_image(give path where to save and
# image file name with .webp file type extension)
# print(gifwebp(
#     f"{str(Path(__file__).parent.parent)}{sep}extras{sep}linux_logo.gif",
#     f"{str(Path(__file__).parent.parent)}{sep}extras{sep}linux_logo.webp",
#     "-q 80"))

# *************** webpmux ********************* #

# %%%%%%%%%%%%%%%%%% Add ICC profile,XMP metadata and EXIF metadata

# pass input_image(.webp image) path,output_image,set
# options(icc image profile,XMP metadata or EXIF metadata) and file.
# for options use keywords as below
# for ICC: icc
# for XMP metadata: xmp
# for EXIF metadata: exif
# print(webpmux_add("in.webp", "icc_container.webp", "image_profile.icc", "icc"))

# %%%%%%%%%%%%%%%% Extract ICC profile,XMP metadata and EXIF metadata

# pass input_image(.webp image) path,output_image,set
# options(icc image profile,XMP metadata or EXIF metadata) and file.
# for options use keywords as below
# for ICC: icc
# for XMP metadata: xmp
# for EXIF metadata: exif
# print(webpmux_extract("anim_container.webp", "image_profile.icc", "icc"))

# %%%%%%%%%%%%%%%%%%%%% Strip ICC profile,XMP metadata and EXIF metadata

# pass input_image(.webp image) path,output_image,set
# options(icc image profile,XMP metadata or EXIF metadata) and file.
# for options use keywords as below
# for ICC: icc
# for XMP metadata: xmp
# for EXIF metadata: exif
# print(webpmux_strip("icc_container.webp", "without_icc.webp", "icc"))

# %%%%%%%%%%%%%%%%%%% Create an animated WebP file from Webp images

# pass input_images(.webp image) path with FRAME_OPTIONS,
# as array,ouput image will be animated .webp image

# https://developers.google.com/speed/webp/docs/webpmux
# FRAME_OPTIONS

# -file_i +di[+xi+yi[+mi[bi]]]

# e.g -frame one.webp +100 -frame two.webp +100+50+50 -frame three.webp
# +100+50+50+1+b

# Where: file_i is the i'th frame (WebP format), xi,yi specify the image
# offset for this frame,
# di is the pause duration before next frame, mi is the dispose method for
# this frame (0 for NONE or 1 for BACKGROUND)
# and bi is the blending method for this frame
# (+b for BLEND or -b for NO_BLEND).
# Argument bi can be omitted and will default to +b (BLEND).
# Also, mi can be omitted if bi is omitted and
# will default to 0 (NONE). Finally,
# if mi and bi are omitted then xi and yi can be omitted and will default
# to +0+0.

# -loop n

# e.g 10

# Loop the frames n number of times. 0 indicates
# the frames should loop forever.
# Valid range is 0 to 65535 [Default: 0 (infinite)].

# -bgcolor A,R,G,B

# e.g 255,255,255,255

# Background color of the canvas. Where: A, R, G and B are integers
# in the range 0 to 255 specifying
# the Alpha, Red, Green and Blue component values respectively
# [Default: 255,255,255,255].

# input = ["./frames/tmp-0.webp +100", "./frames/tmp-1.webp +100",
#          "./frames/tmp-2.webp +100"]
# print(webpmux_animate(input, "anim_container.webp", "10", "255,255,255,255"))

# %%%%%%%%%%%%%%%%%%%%% Get the a frame from an animated WebP file

# pass input_image(.webp image) path ,output_image and frame number
# print(webpmux_getframe("anim_container.webp", "frame_2.webp", "2"))

# *************** base64 to webp base64 ************** #

# with open(
#         r"C:\Users\user\python_logo.jpg",
#         "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read())
# base64_image = encoded_string.decode('utf-8')
#
# print(str2webpstr(base64str=base64_image, image_type="jpg",
#                   option="-q 80", logging="-v"))
