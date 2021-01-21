from cv2 import cv2
import numpy
import os


HEIGHT = 35
WIDTH = 120
MAXNUMBER8BITCOLOR = 255


def main():
    setWindowDimension(HEIGHT, WIDTH)
    captureAndDisplayASCIICamera()


def setWindowDimension(height, width):
    os.system(f"mode con cols={width} lines={height}")


def captureAndDisplayASCIICamera():
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while camera.isOpened():
        _, frame = camera.read()
        frame = frameToGray(frame)
        print(resizeFrameAndConvertToASCII(frame, WIDTH, HEIGHT))


def frameToGray(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame


def resizeFrameAndConvertToASCII(frame, cols, rows):
    result = ""
    frameHeight, frameWidth = frame.shape
    cellWidth,  cellHeight = frameWidth / cols, frameHeight / rows

    for i in range(rows):
        for j in range(cols):
            iniPixelX = int(i * cellHeight)
            finPixelX = min(int((i + 1) * cellHeight), frameHeight)
            iniPixelY = int(j * cellWidth)
            finPixelY = min(int((j + 1) * cellWidth), frameWidth)

            setOfPixels = frame[iniPixelX:finPixelX, iniPixelY: finPixelY]

            finalPixel = numpy.mean(setOfPixels)

            result += PixelToChar(finalPixel)
        # result += "\n"

    return result


def PixelToChar(PixelColor):
    CHAR_LIST = ' .:-=+*#%@'
    charListLen = len(CHAR_LIST)
    charIndex = int(PixelColor * charListLen / MAXNUMBER8BITCOLOR)
    charIndex = min(charIndex, charListLen - 1)
    return CHAR_LIST[charIndex]


if __name__ == '__main__':
    main()
