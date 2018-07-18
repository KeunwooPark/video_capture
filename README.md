# Video Capture
Simple python script for capturing video.
It uses OpenCV.

## How to use
1. Do not record, but show live images
<pre><code>$ python record.py
</code></pre>

1. Open camera setting panel.
<pre><code>$ python record.py --setting
</code></pre>

1. Save images to directory. All the streaming images will be saved automatically
<pre><code>$ python record.py --save dir/to/save --mode a
</code></pre>

1. Save images to directory. All the streaming images will be saved manually. If you press 'space' button, it will save an image.
<pre><code>$ python record.py --save dir/to/save --mode m
</code></pre>

## Help
<pre><code>$ python record.py --help
</code></pre>
