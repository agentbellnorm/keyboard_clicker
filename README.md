# keyboard_clicker

![](demo.gif)

Click anything on screen in any application using only five keyboard keys.

The item to click is located visually using a two dimensional divide and conquer approach.

[Background and motivation (blog post).](https://morganbentell.wordpress.com/2019/01/29/moving-away-from-the-mouse-part-2/)

Note: Currently only working on Mac.

### Install
Make sure you have python 3.X installed.
```bash
python --version
Python 3.7.2
```
or in some cases
```bash
python3 --version
Python 3.7.2
```
If `python3` works for you, you should use it insted of `python` below. Also use `pip3` insted of `pip`.

If you have Python 3 installed then go ahead and:
```bash
# download the code
git clone https://github.com/agentbellnorm/keyboard_clicker.git
cd keyboard_clicker

# install dependencies
pip install -r requirements.txt

# start the app
python src/run.py
```


### Usage
* Go to the application that you want to click in.
* Tab to the python app icon in the OS.
* Select quadrant with he keyboard keys I, J, F, E (for quadrant 1, 2, 3, 4).
* When the element to click is at the origin (at the cross formed by the four quadrants), press space to click.
* To click again, tab back to the python app.
* To start over when in localization mode, press `shift + r`

### Libraries used
```
wxPython
PyAutoGUI
```

