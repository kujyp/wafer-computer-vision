from models.line import Line
from utils.consts import VIDEO_RESOLUTION
from utils.logging_ import logger

MINIMUM_POINTS_FOR_LINE = 3
NUM_OF_DIRECTIONS = 2000
INF = 100000
# VIDEO_RESOLUTION = {
#     'y':1080,
#     'x':1920,
#     'color':3
# }
HORIZONTAL_DIRACTION = (1.0, 0.0)
LINE_LIMITLENGTH = VIDEO_RESOLUTION['x'] / 40

def detectContourLine(image):
    # mask, mainline = detectHoughLines(image)
    # WindowManager.getInstance().imgshow(mask, 'surf')
    # lines = findMainLines(mask, mainDirection)
    # mask = Line.drawLines(image, lines)

    return mask

def findMainLines(lines, maindirectionline):
    lineLengths = dict()
    lineAsclass = dict()
    lineCnt = dict()
    maindir = maindirectionline.direction
    for idx, line in enumerate(lines):
        x1, y1, x2, y2 = line[0]
        line_ = Line((x1, y1), (x2, y2))
        if maindir == line_.direction:
            baseorigin = line_.baseorigin
            length = line_.length
            if line_.isBoundary:
                logger.debug("LIMITED ISBOUNDARY baseorigin={}, length={}".format(baseorigin, length))
                continue
            # if length > LINE_LIMITLENGTH:
            #     logger.debug("LIMITED LENGTH baseorigin={}, length={}".format(baseorigin, length))
            else:
                if baseorigin in lineLengths:
                    lineLengths[baseorigin] += length
                    lineCnt[baseorigin] += 1
                else:
                    lineLengths[baseorigin] = length
                    lineAsclass[baseorigin] = line_
                    lineCnt[baseorigin] = 1
        else:
            pass

    maxlength = -INF
    mainline = None
    for key, length in lineLengths.items():
        if length > maxlength:
            maxlength = length
            mainline = lineAsclass[key]

    return mainline

# def findMainLines(image, direction):
#     img = np.copy(image)
#     if len(img.shape) == 3:
#         img = img.astype(np.float32)
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     lines = []
#     cnts = []
#     length = img.shape[0]
#     xlim, ylim = img.shape[0], img.shape[1]
#     for i in range(length):
#         j=0
#         cnt = 0
#         x1, y1 = i,0
#         x, y = x1,y1
#         while True:
#             def isValidAxis(x,y,xlim,ylim):
#                 result = True
#                 if not(x >= 0 and x < xlim):
#                     result = False
#                 if not(y >= 0 and y < ylim):
#                     result = False
#                 return result
#
#             def onNextAxis(x,y,direction):
#                 if direction == 1:
#                     return x, y+1
#                 else:
#                     return x+1, y+tan(asin(direction))
#
#             if not isValidAxis(x, y, xlim, ylim):
#                 break
#
#             axisx,axisy = x,int(y)
#             # logger.debug("img[{},{}]={}".format(axisx,axisy,img[axisx, axisy]))
#             if img[axisx,axisy] > 0:
#                 cnt+=1
#             x2, y2 = axisx,axisy
#             x, y = onNextAxis(x, y, direction)
#         lines.append([[x1,y1,x2,y2]])
#         cnts.append(cnt)
#
#     _, max_idx = findMax(cnts)
#     return [lines[max_idx]]


def findMainDirectionByLines(lines):
    lineLengths = dict()
    lineAsclass = dict()
    for idx, line in enumerate(lines):
        x1, y1, x2, y2 = line[0]
        line_ = Line((x1,y1), (x2,y2))
        direction = line_.direction
        if direction in lineLengths:
            lineLengths[direction] += line_.length
        else:
            lineLengths[direction] = line_.length
            lineAsclass[direction] = line_

    maxlength = -INF
    mainline = None
    for direction, length in lineLengths.items():
        if direction == HORIZONTAL_DIRACTION:
            logger.debug("skip HORIZONTAL_DIRACTION")
            continue

        if length > maxlength:
            maxlength = length
            mainline = lineAsclass[direction]

    # hist, bin_edges = np.histogram(sins, bins=NUM_OF_DIRECTIONS)
    # hist, bin_edges= list(hist), list(bin_edges)
    # if bin_edges[0] == -1.0:
    #     if bin_edges[-1] == 1.0:
    #         hist[-1] += hist[0]
    #     else:
    #         hist.append(hist[0])
    #         bin_edges.append(1.0)
    #     bin_edges.__delitem__(0)
    #     hist.__delitem__(0)

    # logger.debug("hist={}".format(hist))
    # logger.debug("bin_edges={}".format(bin_edges))
    # maximum, idx = findMax(hist)
    # logger.debug("Main direction sin={}-{}, maximum={}, idx={}".format(bin_edges[idx], bin_edges[idx+1], maximum, idx))
    # mainDirection = bin_edges[idx+1]
    # import matplotlib.pyplot as plt
    # plt.hist(hist,bin_edges)  # plt.hist passes it's arguments to np.histogram
    # plt.title("Histogram with 'auto' bins")
    # plt.show()

    return mainline

def findMax(arr):
    max = -INF
    max_idx = -1
    for idx, item in enumerate(arr):
        if item > max:
            max = item
            max_idx = idx

    return max, max_idx