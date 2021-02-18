# Pysheng3

A simple port of https://github.com/pysheng/pysheng for python3

Download books from Google Books as PNG images. It can be run either from the command-line or using a simple GUI (graphical interface). It should work out-of-the box for Unix systems (GNU/Linux, BSD) and (hopefully) for Windows.


Install
=======

### Install dependencies:

```
$ sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0
```

### Install Pysheng

For UNIX systems:

```
$ git clone https://github.com/D-Brox/pysheng/
$ pip3 install -r requirements.txt
```
To install locally:

```
$ python3 setup.py install --user
```

To install system-wide:

```
$ sudo python3 setup.py install
```

Usage
=====

### Using the GUI


Note that in order to save a PDF you need [ReportLab](http://www.reportlab.com/software/opensource/) installed.

```
$ pysheng-gui
```

http://pysheng.googlecode.com/svn/wiki/screenshot1.png

### Command line


 * Download a whole book:

```
$ pysheng "http://books.google.com/books?id=m5w5PRj5Nj4C"
```

 * Download a whole book using the command-line and convert the images into a single PDF (requires [Imagemagick](http://www.imagemagick.org/script/index.php)). Notice that you can use the Book ID only.

```
$ convert $(pysheng "m5w5PRj5Nj4C") book.pdf
```
