# *****************************************************************************

	# This program is free software: you can redistribute it and/or modify
	# it under the terms of the GNU General Public License as published by
	# the Free Software Foundation, either version 3 of the License, or
	# (at your option) any later version.

	# This program is distributed in the hope that it will be useful,
	# but WITHOUT ANY WARRANTY; without even the implied warranty of
	# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	# GNU General Public License for more details.

	# You should have received a copy of the GNU General Public License
	# along with this program.  If not, see <http://www.gnu.org/licenses/>.
	
# *****************************************************************************

import Image
import sys
if len(sys.argv) < 3:
	print('\n	Please open a console and entire the Input and Output files\n	Example: FE6_WMC.py C:/path/to/Input.bmp C:/path/to/output.bmp\n	Fire Emblem 6 World Map Converter by Seinu Fireflower')
	sys.exit()

try:
	image = Image.open(sys.argv[1])
except:
	print('\n	Please make sure the input path is correct!')
	sys.exit()
print('\n	Fire Emblem 6 World Map Converter by Seinu Fireflower')
width = image.size[0]
height = image.size[1]
width_ = width / 8
size = 256, 152
FMTimage = Image.new('RGB', size)
FMTwidth = FMTimage.size[0]
FMTwidth_ = FMTwidth / 8
FMTheight = FMTimage.size[1]
FMTheight_ = FMTheight / 8
y = 0
x = 0
for a in range(0, FMTheight_):
	for b in range(0, FMTwidth_):
		pasteStartH = a * 8
		for c in range(pasteStartH, pasteStartH+8):
			pasteStartW = b * 8
			copyStart = x
			box = (copyStart, y, copyStart + 8, y + 1)
			region = image.crop(box)
			FMTbox = (pasteStartW, c, pasteStartW+8 , c + 1)
			width_ = width_ + 1
			FMTimage.paste(region, FMTbox)
			width_ = width_ + 1
			x = x + 8
			if x == width:
				y = y + 1
				x = 0
FMTimage.save(sys.argv[2])
print('Done')
				