webptools is a Webp image conversion package for python.

Convert JPG,PNG.. images to webp image format

This library uses precompiled executables of WebP for more info visit [WebP](https://developers.google.com/speed/webp)

For converting other image formats to webp, please read this documentation  [cwebp Encoder](https://developers.google.com/speed/webp/docs/cwebp)

For converting webp image to other image format, please read this documentation  [dwebp Encoder](https://developers.google.com/speed/webp/docs/dwebp)

For converting gif image to webp, please read this documentation [gif2webp Converter](https://developers.google.com/speed/webp/docs/gif2webp)

For creating animated webp image using webp images, please read this documentation [webpmux Muxer](https://developers.google.com/speed/webp/docs/webpmux)


# How to use

# cwebp

## Convert other image format to webp

```python

from webptools import webplib as webp

# pass input_image(.jpeg,.pnp .....) path ,
# output_image(give path where to save and image file name with .webp file type extension)
print(webp.cwebp("python_logo.jpg", "python_logo.webp", "-q 80"))


```

# dwebp

## Convert webp image to other image format

```python

from webptools import webplib as webp

# pass input_image(.webp image) path ,output_image(.jpeg,.pnp .....)
print(webp.dwebp("python_logo.webp","python_logo.jpg","-o"))

```

# gif2webp

## Convert gif image to webp

```python
from webptools import webplib as webp

# pass input_image(.gif) path ,output_image(give path where to save and image file name with .webp file type extension)
print(webp.gifwebp("linux_logo.gif","linux_logo.webp","-q 80"))
```

# webpmux

## Add ICC profile,XMP metadata and EXIF metadata

```python
from webptools import webplib as webp

# pass input_image(.webp image) path,output_image,set options(icc image profile,XMP metadata or EXIF metadata) and file.
# for options use keywords as below
# for ICC: icc
# for XMP metadata: xmp
# for EXIF metadata: exif
print(webp.webpmux_add("in.webp","icc_container.webp","image_profile.icc","icc"))
```

## Extract ICC profile,XMP metadata and EXIF metadata

```python

from webptools import webplib as webp

# pass input_image(.webp image) path,output_image,set options(icc image profile,XMP metadata or EXIF metadata) and file.
# for options use keywords as below
# for ICC: icc
# for XMP metadata: xmp
# for EXIF metadata: exif
print(webp.webpmux_extract("anim_container.webp","image_profile.icc","icc"))
```

## Strip ICC profile,XMP metadata and EXIF metadata

```python

from webptools import webplib as webp

# pass input_image(.webp image) path,output_image,set options(icc image profile,XMP metadata or EXIF metadata) and file.
# for options use keywords as below
# for ICC: icc
# for XMP metadata: xmp
# for EXIF metadata: exif
print(webp.webpmux_strip("icc_container.webp","without_icc.webp","icc"))


```

## Create an animated WebP file from Webp images

```python

from webptools import webplib as webp

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

input=["./frames/tmp-0.webp +100","./frames/tmp-1.webp +100","./frames/tmp-2.webp +100"]
print(webp.webpmux_animate(input,"anim_container.webp","10","255,255,255,255"))

```

## Get a frame from an animated WebP file

```python

from webptools import webplib as webp

# pass input_image(.webp image) path ,output_image and frame number
print(webp.webpmux_getframe("anim_container.webp","frame_2.webp","2"))


```

## Installation

```shell
$ pip install webptools
```

## License

  [MIT](LICENSE)
