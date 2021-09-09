[Webptools v0.0.7](https://pypi.org/project/webptools/)

webptools is a Webp image conversion package for the python.

Convert JPG,PNG.. images to webp image format

This library uses precompiled executables of WebP(v1.1.0) for more info
visit [WebP](https://developers.google.com/speed/webp)

For converting other image formats to webp, please read this
documentation  [cwebp Encoder](https://developers.google.com/speed/webp/docs/cwebp)

For converting webp image to other image format, please read this
documentation  [dwebp Encoder](https://developers.google.com/speed/webp/docs/dwebp)

For converting gif image to webp, please read this
documentation [gif2webp Converter](https://developers.google.com/speed/webp/docs/gif2webp)

For creating animated webp image using webp images, please read this
documentation [webpmux Muxer](https://developers.google.com/speed/webp/docs/webpmux)


# How to use

## Installation

```shell
$ pip install webptools
```

## Fix Permission Issue (if not using external executables)

```python

from webptools import grant_permission

# this will grant 755 permission to webp executables
grant_permission()

```

### Using External executables

```python

bin_path="libwebp_linux/bin/cwebp"

```

# cwebp

## Convert other image format to webp

```python

from webptools import cwebp

# pass input_image(.jpeg,.pnp .....) path ,
# output_image(give path where to save and image file name with .webp file type extension)
print(cwebp(input_image="python_logo.jpg", output_image="python_logo.webp",
            option="-q 80", logging="-v"))


```

## Convert base64 image to webp base64

```python

from webptools import base64str2webp_base64str

# pass base64 image, image type, webp options,
# for the conversion temp location need 

# use the default temp path for conversion
print(
    base64str2webp_base64str(base64str="", image_type="jpg", option="-q 80",
                             logging="-v"))
# use the custom temp path for conversion
print(base64str2webp_base64str(base64str="", image_type="jpg", option="-q 80",
                               temp_path="./temp",
                               logging="-v"))

```

# dwebp

## Convert webp image to other image format

```python

from webptools import dwebp

# pass input_image(.webp image) path ,output_image(.jpeg,.pnp .....)
print(dwebp(input_image="python_logo.webp", output_image="python_logo.jpg",
            option="-o", logging="-v"))

```

# gif2webp

## Convert gif image to webp

```python
from webptools import gifwebp

# pass input_image(.gif) path ,output_image(give path where to save and image file name with .webp file type extension)
print(gifwebp(input_image="linux_logo.gif", output_image="linux_logo.webp",
              option="-q 80", logging="-v"))
```

# webpmux

## Add ICC profile,XMP metadata and EXIF metadata

```python
from webptools import webpmux_add

# pass input_image(.webp image) path,output_image,set options(icc image profile,XMP metadata or EXIF metadata) and file.
# for options use keywords as below
# for ICC: icc
# for XMP metadata: xmp
# for EXIF metadata: exif
print(webpmux_add(input_image="in.webp", output_image="icc_container.webp",
                  icc_profile="image_profile.icc", option="icc", logging="-v"))
```

## Extract ICC profile,XMP metadata and EXIF metadata

```python

from webptools import webpmux_extract

# pass input_image(.webp image) path,output_image,set options(icc image profile,XMP metadata or EXIF metadata) and file.
# for options use keywords as below
# for ICC: icc
# for XMP metadata: xmp
# for EXIF metadata: exif
print(webpmux_extract(input_image="anim_container.webp",
                      icc_profile="image_profile.icc", option="icc",
                      logging="-v"))
```

## Strip ICC profile,XMP metadata and EXIF metadata

```python

from webptools import webpmux_strip

# pass input_image(.webp image) path,output_image,set options(icc image profile,XMP metadata or EXIF metadata) and file.
# for options use keywords as below
# for ICC: icc
# for XMP metadata: xmp
# for EXIF metadata: exif
print(webpmux_strip(input_image="icc_container.webp",
                    output_image="without_icc.webp", option="icc",
                    logging="-v"))


```

## Create an animated WebP file from Webp images

```python

from webptools import webpmux_animate

# pass input_images(.webp image) path with FRAME_OPTIONS, as array,ouput image will be animated .webp image

# https://developers.google.com/speed/webp/docs/webpmux
# FRAME_OPTIONS

# -file_i +di[+xi+yi[+mi[bi]]]

# e.g -frame one.webp +100 -frame two.webp +100+50+50 -frame three.webp +100+50+50+1+b

# Where: file_i is the i'th frame (WebP format), xi,yi specify the image offset for this frame,
# di is the pause duration before next frame, mi is the dispose method for this frame (0 for NONE or 1 for BACKGROUND)
# and bi is the blending method for this frame (+b for BLEND or -b for NO_BLEND).
# Argument bi can be omitted and will default to +b (BLEND). Also, mi can be omitted if bi is omitted and
# will default to 0 (NONE). Finally,
# if mi and bi are omitted then xi and yi can be omitted and will default to +0+0.

# -loop n

# e.g 10

# Loop the frames n number of times. 0 indicates the frames should loop forever.
# Valid range is 0 to 65535 [Default: 0 (infinite)].

# -bgcolor A,R,G,B

# e.g 255,255,255,255

# Background color of the canvas. Where: A, R, G and B are integers in the range 0 to 255 specifying
# the Alpha, Red, Green and Blue component values respectively [Default: 255,255,255,255].

input = ["./frames/tmp-0.webp +100", "./frames/tmp-1.webp +100",
         "./frames/tmp-2.webp +100"]
print(webpmux_animate(input_images=input, output_image="anim_container.webp",
                      loop="10", bgcolor="255,255,255,255", logging="-v"))

```

## Get a frame from an animated WebP file

```python

from webptools import webpmux_getframe

# pass input_image(.webp image) path ,output_image and frame number
print(webpmux_getframe(input_image="anim_container.webp",
                       output_image="frame_2.webp", frame_number="2",
                       logging="-v"))


```
