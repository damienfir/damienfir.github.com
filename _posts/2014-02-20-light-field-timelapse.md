---
layout: post
title: Parallax timelapse photography with static light field capture
date: 2014-02-20
category: light-field
---

Timelapse photography can be greatly enhanced by adding a parallax effect during the shooting. [This video](http://vimeo.com/80836225) is a good example of what can be achieved using a motorized devices to move the camera gradually over a long period of time. This method requires additional equipement, and is complex to setup. Due to its mechanical nature, it is prone to failure and can be slow. These limitations can be partially removed by using a light field camera, where the point of view can be changed slightly after the exposure.

When capturing an image, a light field camera allows to capture light while keeping the directional information of light rays available in the raw image. From this data, one can computationally change the point of view of the scene, thus rendering multiple views of the scene in a single exposure. This effect can be used for timelapse photography, where multiples exposures can be taken during a period of time, with a static light field camera. In post processing, the point of view of the multiple exposures can be changed gradually to produce a parallax effect.
