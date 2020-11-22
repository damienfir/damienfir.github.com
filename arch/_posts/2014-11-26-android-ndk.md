---
layout: template
title: Native computer vision on Android using the NDK
date: 2014-11-26
categories: android
---

During my work on the project [eFacsimile](http://lcav.epfl.ch/research/eFacsimile), I ported an implementation of [PTAM](http://www.robots.ox.ac.uk/~gk/PTAM/) on Android using the NDK. This page reflects the challenges I encountered while developing native code on Android.

The source code can be explored on [github](https://github.com/damienfir/android-ptam).

### OpenGL

The user interface of the project relies on OpenGL, which implies that a good knowledge of the graphic stack on Android is essential to be efficient. [This guide](https://source.android.com/devices/graphics/architecture.html) on the Android documentation page provides a very extensive overview of the graphics architecture.

[Grafika](https://github.com/google/grafika) by Google is a great source for code samples and examples for everything relating to graphics development on Android.

Android platforms support only OpenGL ES, which is good to keep in mind while porting pure OpenGL applications. You must provide an interface for the app's OpenGL call so that they are recognized by the Android platform.


### JNI

JNI is the Java Native Interface, and allows one to write functions in C/C++ that are callable from the JVM using Java code in a Android application.
