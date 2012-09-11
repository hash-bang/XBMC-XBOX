Matts little XBMC/XBOX controller config
========================================

Installation
------------

Simply extract all files from this archive into your .xbmc directory.

Alternatively save (Keymap.xml)[https://github.com/hash-bang/XBMC-XBOX/blob/master/userdata/keymaps/Keymap.xml] into your XBOX `userdata/keymaps` folder which is found in your main XBMC user directory.


Controls
--------
<table>
	<tr>
		<th>Button</th>
		<th>Function</th>
	</tr>
	<tr>
		<td>A</td>
		<td>Select / Pause</td>
	</tr>
	<tr>
		<td>B</td>
		<td>Back /  Stop / Undo / Close</td>
	</tr>
	<tr>
		<td>Y</td>
		<td>Fullscreen toggle - i.e. show whats playing</td>
	</tr>
	<tr>
		<td>X</td>
		<td>Info / Parent directory</td>
	</tr>
	<tr>
		<td>Start</td>
		<td>Context Menu / OSD</td>
	</tr>
	<tr>
		<td>Back</td>
		<td>(Same as B)</td>
	</tr>
	<tr>
		<td>XBOX button</td>
		<td>Home</td>
	</tr>
	<tr>
		<td>D-Pad</td>
		<td>Left, right, up, down navigation / Seek + Volume</td>
	</tr>
	<tr>
		<td>Left / Right Sticks</td>
		<td>Same as D-Pad</td>
	</tr>
	<tr>
		<td>Left / Right Stick Press</td>
		<td>Context Menu</td>
	</tr>
	<tr>
		<td>Front Shoulders</td>
		<td>Volume</td>
	</tr>
	<tr>
		<td>Back Bumpers</td>
		<td>Seek</td>
	</tr>
</table>


Use with XBoxDrv (Linux)
------------------------
The [XBoxDrv](http://pingus.seul.org/~grumbel/xboxdrv/) driver is recommended with Linux as it provides a nice and easyily configurable Linux Joystick device.

The following launch method is recommended:

	sudo xboxdrv --dpad-as-button --trigger-as-button --deadzone 12000 --led 9 -D -s


Shoudl you wish to configure the config the following button reference may be useful.

<table>
	<tr>
		<th>Button</th>
		<th>Button ID</th>
	</tr>
	<tr>
		<td>A</td>
		<td>5</td>
	</tr>
	<tr>
		<td>B</td>
		<td>6</td>
	</tr>
	<tr>
		<td>Y</td>
		<td>8</td>
	</tr>
	<tr>
		<td>X</td>
		<td>7</td>
	</tr>
	<tr>
		<td>Back</td>
		<td>13</td>
	</tr>
	<tr>
		<td>XBox</td>
		<td>15</td>
	</tr>
	<tr>
		<td>Start</td>
		<td>14</td>
	</tr>
	<tr>
		<td>Back Shoulder Left</td>
		<td>11</td>
	</tr>
	<tr>
		<td>Front Shoulder Left</td>
		<td>9</td>
	</tr>
	<tr>
		<td>Back Shoulder Right</td>
		<td>12</td>
	</tr>
	<tr>
		<td>Front Shoulder Left</td>
		<td>10</td>
	</tr>
	<tr>
		<td>Left Joystick Press</td>
		<td>16</td>
	</tr>
	<tr>
		<td>Left Joystick Axis Up/Down</td>
		<td>A2</td>
	</tr>
	<tr>
		<td>Left Joystick Axis Left/Right</td>
		<td>A1</td>
	</tr>
	<tr>
		<td>Right Joystick Press</td>
		<td>17</td>
	</tr>
	<tr>
		<td>Right Joystick Axis Up/Down</td>
		<td>A4</td>
	</tr>
	<tr>
		<td>Right Joystick Axis Left/Right</td>
		<td>A3</td>
	</tr>
	<tr>
		<td></td>
		<td>D-pad Up - 1</td>
	</tr>
	<tr>
		<td></td>
		<td>D-pad Down - 2</td>
	</tr>
	<tr>
		<td></td>
		<td>D-pad Left - 3</td>
	</tr>
	<tr>
		<td></td>
		<td>D-pad Right- 4</td>
	</tr>
</table>
