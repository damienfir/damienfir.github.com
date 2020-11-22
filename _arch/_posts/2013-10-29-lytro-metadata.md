---
layout: template
title: Information about Lytro .lfp metadata files
date: 2013-10-29
categories: lightfield
---

With each picture taken with the Lytro comes a JSON metadata file. It provides information about the exposure parameters, calibration data, RAW format and more.

The file is divided into two main sections, `image` and `device`. The former is about RAW output format, and the latter is about the exposure parameters and calibration data.


### Devices

In the `device` section, important non self-explanatory fields are:

- `sensor.pixelPitch`: pixel separation
- `lens.infinityLambda`: distance ahead of the micro lens array that is in focus at infinity
- `mla.lensPitch`: micro lens separation
- `mla.rotation`: sensor rotation with respect to the micro lens array, as viewed from in front of the camera
- `mla.sensorOffset`: amount of (x,y,z) displacement of the sensor with respect to the micro lens array


### Image

Most fields in the `image` section are self-explanatory. What is worth mentioning is the `representation` field with value `rawPacked`, and the `pixelPacking.bitsPerPixel` with value `12`. Meaning that in the RAW binary image, pixels are packed together, represented by values of 16 bits.
