---
layout: post
title: Decoding light field from Lytro lenselet images
---


### Decoding Lytro files

_Information given here were first published by [Nirav Patel][http://eclecti.cc/computervision/reverse-engineering-the-lytro-lfp-file-format]._

Most of the metadata needed to decode a raw Lytro image is included in the `.lfp` container that is obtainable by exporting the image from the Lytro desktop software.

Using `lfpsplitter` from [lfptools](https://github.com/nrpatel/lfptools) on the exported `.lfp` file, you get 3 files:

- `{filename}_imageRef0.raw`
- `{filename}_metadataRef0.json`
- `{filename}_table.json`

The first file is the raw data. Given that the raw size of a Lytro image is 3280x3280, you can decode it to a TIFF format by using `raw2tiff` as follows:

```raw2tiff -w 3280 -l 3280 -d short input.raw output.tif```

The second file contains metadata from the image. It includes information about the Bayer color filter pattern, the focal length and zoom position of the main lens, the calibration data related to the micro lens array such as offset and rotation, and other metadata about various components of the camera.

The third file contains information about the device and the two previous files.


### Calibration data

Most calibration data is included in the `{filename}_metadataRef0.json` file but not all. Some extra data are contained in the backup files that the Lytro desktop software imports when the camera is first connected to the computer. Those files are usually found in `/Users/{username}/AppData/Local/Lytro` under the name `data.C.#`.

Those files can be decoded using `lfpsplitter` or [python-lfp-reader](http://code.behnam.es/python-lfp-reader/) (I recommend the latter for this part, as the output filenames are clearer). The interesting file in the list is called `data.C.3.__C__T1CALIB__MLACALIBRATION.TXT` and contains calibration data for the micro lens array as a function of zoom and focus motor positions.

The most interesting of those numbers are the coordinates of the center of the central micro lens (`xDiskOriginPixels` and `yDiskOriginPixels`) and the components of the two vectors forming the basis of the hexagonal lattice on which the micro lenses are positioned (`xDiskStepPixelsX` and `xDiskStepPixelsY` for the first vector, and `yDiskStepPixelsX` and `yDiskStepPixelsY` for the second).


### Extracting the light field from the raw image

Given that micro lens sampling grid is hexagonal, we cannot sampling the light field using a orthogonal grid as it would be done for a conventional image. Instead we need to use the metadata extracted earlier to build a hexagonal grid.

The first step is to find the centers of every micro image (which are the images of each micro lens on the sensor). The coordinates for the center of the image extracted earlier gives the origin of the hexagonal lattice. From that point, all we have to use are the basis vectors. We can get the centers of each micro image by bulding the grid from those basis vectors, with coordinates that cover the whole image.

Once we extract the centers of each micro image, we can directly build a 11x11 grid (from -5 to +5 for x and y directions) for each of them, which will give us the relative coordinates of each pixel within each micro image.



