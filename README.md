# EMG Drums

## Description
<img src="https://upload.orthobullets.com/topic/1052/images/transradial.jpg" alt="transradial amputation" width="200"/>
People who go through a transradial amputation lose the ability to play instruments with their hands. 

In order to give people who undergo that trauma support in getting back to everyday life, we developed an application that allows users to band drums on a drum set through movement in their muscles.

The application: 
- Is a [PYQT6 application](https://www.riverbankcomputing.com/static/Docs/PyQt6/) to make it as accessible as possible. It can run on Android, iOS, MacOS, and Windows devices.
- Uses EMG signals picked up with (Delsys Avanti)[https://delsys.com/trigno-avanti/] sensors placed on a persons arm to detect speed and location in space.
- Communicates through TCP to register EMG signals.
- Converts EMG signals into MIDI Messages that can be played using different sound sets.
- Displays the drums available with animations based on how the user plays.

## Installation and Running the App (MacOS and Windows)

1. Install the (Delsys SDK)[https://delsys.com/sdk/] and connect Delsys Avanti devices you intend to pick up signals for.
2. Open Terminal or Command Line.
3. Install PYQT6 with `pip install PyQt6`.
4. Navigate to project directory.
5. Install dependencies using `python -m pip install -r requirements.txt`.
6. Run the app with `python app.py`.

## Using the App

Video coming soon.

## Contributors

- [Maximilian Carvajal](https://www.linkedin.com/in/maximilian-carvajal/)
- [Maggie]()
- [Pouyan Firouzabadi](https://www.linkedin.com/in/pouyan-firouzabadi/)
- [Samat Kadyrov](https://www.linkedin.com/in/skadyrov/)
- [Lukas Carvajal](https://lcarvajal.github.io)


## License

MIT License

Copyright (c) 2023 Max Carvajal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.