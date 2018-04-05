import os
import numpy
import time

quote1 = (
'\n\n\n\n\n\n\n\n\n'
'          *\n'
'         * *\n'
'          *\n'
'\n\n\n\n\n\n\n\n\n')

quote2 = (
'\n\n\n\n\n\n\n\n'
'          *\n'
'\n'
'        *   *\n'
'\n'
'          *\n'
'\n\n\n\n\n\n\n\n')

quote3 = (
'\n\n\n\n\n\n\n'
'          *\n'
'\n\n'
'       *     *\n'
'\n\n'
'          *\n'
'\n\n\n\n\n\n\n')

quote4 = (
'\n\n\n\n\n\n'
'          *\n'
'\n\n\n'
'      *       *\n'
'\n\n\n'
'          *\n'
'\n\n\n\n\n\n')

quote5 = (
'\n\n\n\n\n'
'          *\n'
'\n\n\n\n'
'     *         *\n'
'\n\n\n\n'
'          *\n'
'\n\n\n\n\n')

quote6 = (
'\n\n\n\n'
'          *\n'
'\n\n\n\n\n'
'    *           *\n'
'\n\n\n\n\n'
'          *\n'
'\n\n\n\n')

quote7 = (
'\n\n\n'
'          *\n'
'\n\n\n\n\n\n'
'   *             *\n'
'\n\n\n\n\n\n'
'          *\n'
'\n\n\n')

quote8 = (
'\n\n'
'          *\n'
'\n\n\n\n\n\n\n'
'  *               *\n'
'\n\n\n\n\n\n\n'
'          *\n'
'\n\n')

quote9 = (
'\n'
'          *\n'
'\n\n\n\n\n\n\n\n'
' *                 *\n'
'\n\n\n\n\n\n\n\n'
'          *\n'
'\n')

quote10 = (
'          *\n'
'\n\n\n\n\n\n\n\n'
'  * * * * * * * * * \n'
'* Live with a smile *\n'
'   * * * * * * * *\n'
'\n\n\n\n\n\n\n\n'
'          *\n')

quote11 = (
'          *\n'
'\n\n\n\n\n\n\n\n'
'   * * * * * * * *\n'
'* Live with a smile *\n'
'  * * * * * * * * * \n'
'\n\n\n\n\n\n\n\n'
'          *\n')
array = []
array.append(quote1)
array.append(quote2)
array.append(quote3)
array.append(quote4)
array.append(quote5)
array.append(quote6)
array.append(quote7)
array.append(quote8)
array.append(quote9)
array.append(quote10)
array.append(quote11)
array.append(quote10)
array.append(quote11)
array.append(quote10)
array.append(quote11)
count = 0
os.system('cls')
while True:
    print(array[count], end='\r')
    time.sleep(0.2)
    count = (count + 1) % 15
