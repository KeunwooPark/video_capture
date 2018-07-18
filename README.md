# Video Capture
Simple python script for capturing video.
It uses OpenCV.

## How to use
1. Do not record, but show live images
```console
$ python record.py
```

2. Open camera setting panel.
```console
$ python record.py --setting
```

3. Save images to directory. All the streaming images will be saved automatically
```console
$ python record.py --save dir/to/save --mode a
```

4. Save images to directory. All the streaming images will be saved manually. If you press 'space' button, it will save an image.
```console
$ python record.py --save dir/to/save --mode m
```

## Help
```console
$ python record.py --help
```
