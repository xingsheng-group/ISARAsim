topo = []
#       层名称 层序号 输入图像高宽 输出图像高宽 卷积核高宽 输入输出通道 卷积步长 展开 最后层
#          \    \         \         |        /        /        /     /    /
#           \    \         \        |       /        /        /     /    /
#            \    \         |       |      /        /        /     /    /
#             \    \        |       |      |        |       /     /    /
#              \    \       |       |      |        |      /     /    /
#               |    \      |       |      |        |     /     /    |
#               |     \     |       |      |        |    /     /     |
#               |      |    |       |      |        |    |     |     |
#               |      |    |       |      |        |    |     |     |
#               |      |   / \     / \    / \      / \   |     |     |
topo.append(['Conv1 ', 0, 32, 32, 28, 28, 5, 5,   1,   6, 1, False, False, 4, 4, 4])
topo.append(['Conv2 ', 1, 14, 14, 10, 10, 5, 5,   6,  16, 1, False, False, 4, 4, 4])
topo.append(['FC1   ', 2,  5,  5,  1,  1, 1, 1,  16, 120, 1,  True, False, 4, 4, 4])
topo.append(['FC2   ', 3,  1,  1,  1,  1, 1, 1, 120,  84, 1, False, False, 4, 4, 4])
topo.append(['FC3   ', 4,  1,  1,  1,  1, 1, 1,  84,  10, 1, False,  True, 4, 4, 4])
lenet5_topo = topo

####################################################################################

topo = []
topo.append(['Conv1 ',  0, 224, 224, 112, 112, 7, 7,    3,   64, 1, False, False, 8, 8, 8])

size = 56
topo.append(['Conv2 ',  1, size, size, size, size, 3, 3,  64,  64, 1, False, False, 8, 8, 8])
topo.append(['Conv3 ',  2, size, size, size, size, 3, 3,  64,  64, 1, False, False, 8, 8, 8])
topo.append(['Conv4 ',  3, size, size, size, size, 3, 3,  64,  64, 1, False, False, 8, 8, 8])
topo.append(['Conv5 ',  4, size, size, size, size, 3, 3,  64,  64, 1, False, False, 8, 8, 8])

size = 28
topo.append(['Conv6 ',  5, size, size, size, size, 3, 3,  64, 128, 1, False, False, 8, 8, 8])
topo.append(['Conv7 ',  6, size, size, size, size, 3, 3, 128, 128, 1, False, False, 8, 8, 8])
topo.append(['Conv8 ',  7, size, size, size, size, 3, 3, 128, 128, 1, False, False, 8, 8, 8])
topo.append(['Conv9 ',  8, size, size, size, size, 3, 3, 128, 128, 1, False, False, 8, 8, 8])

size = 14
topo.append(['Conv10',  9, size, size, size, size, 3, 3, 128, 256, 1, False, False, 8, 8, 8])
topo.append(['Conv11', 10, size, size, size, size, 3, 3, 256, 256, 1, False, False, 8, 8, 8])
topo.append(['Conv12', 11, size, size, size, size, 3, 3, 256, 256, 1, False, False, 8, 8, 8])
topo.append(['Conv13', 12, size, size, size, size, 3, 3, 256, 256, 1, False, False, 8, 8, 8])

size = 7
topo.append(['Conv14', 13, size, size, size, size, 3, 3, 256, 512, 1, False, False, 8, 8, 8])
topo.append(['Conv15', 14, size, size, size, size, 3, 3, 512, 512, 1, False, False, 8, 8, 8])
topo.append(['Conv16', 15, size, size, size, size, 3, 3, 512, 512, 1, False, False, 8, 8, 8])
topo.append(['Conv17', 16, size, size, size, size, 3, 3, 512, 512, 1, False, False, 8, 8, 8])

topo.append(['FC    ', 17, 1, 1, 1, 1, 1, 1, 512, 1000, 1, False, True, 8, 8, 8])
ResNet18_8 = topo


topo = []
topo.append(['Conv1 ',  0, 224, 224, 112, 112, 7, 7,    3,   64, 1, False, False, 4, 4, 4])

size = 56
topo.append(['Conv2 ',  1, size, size, size, size, 3, 3,  64,  64, 1, False, False, 4, 4, 4])
topo.append(['Conv3 ',  2, size, size, size, size, 3, 3,  64,  64, 1, False, False, 4, 4, 4])
topo.append(['Conv4 ',  3, size, size, size, size, 3, 3,  64,  64, 1, False, False, 4, 4, 4])
topo.append(['Conv5 ',  4, size, size, size, size, 3, 3,  64,  64, 1, False, False, 4, 4, 4])

size = 28
topo.append(['Conv6 ',  5, size, size, size, size, 3, 3,  64, 128, 1, False, False, 4, 4, 4])
topo.append(['Conv7 ',  6, size, size, size, size, 3, 3, 128, 128, 1, False, False, 4, 4, 4])
topo.append(['Conv8 ',  7, size, size, size, size, 3, 3, 128, 128, 1, False, False, 4, 4, 4])
topo.append(['Conv9 ',  8, size, size, size, size, 3, 3, 128, 128, 1, False, False, 4, 4, 4])

size = 14
topo.append(['Conv10',  9, size, size, size, size, 3, 3, 128, 256, 1, False, False, 4, 4, 4])
topo.append(['Conv11', 10, size, size, size, size, 3, 3, 256, 256, 1, False, False, 4, 4, 4])
topo.append(['Conv12', 11, size, size, size, size, 3, 3, 256, 256, 1, False, False, 4, 4, 4])
topo.append(['Conv13', 12, size, size, size, size, 3, 3, 256, 256, 1, False, False, 4, 4, 4])

size = 7
topo.append(['Conv14', 13, size, size, size, size, 3, 3, 256, 512, 1, False, False, 4, 4, 4])
topo.append(['Conv15', 14, size, size, size, size, 3, 3, 512, 512, 1, False, False, 4, 4, 4])
topo.append(['Conv16', 15, size, size, size, size, 3, 3, 512, 512, 1, False, False, 4, 4, 4])
topo.append(['Conv17', 16, size, size, size, size, 3, 3, 512, 512, 1, False, False, 4, 4, 4])

topo.append(['FC    ', 17, 1, 1, 1, 1, 1, 1, 512, 1000, 1, False, True, 4, 4, 4])
ResNet18_4 = topo


topo = []
topo.append(['Conv1 ',  0, 224, 224, 112, 112, 7, 7,    3,   64, 1, False, False, 8, 8, 8])

size = 56
topo.append(['Conv2 ',  1, size, size, size, size, 3, 3,  64,  64, 1, False, False, 8, 8, 8])
topo.append(['Conv3 ',  2, size, size, size, size, 3, 3,  64,  64, 1, False, False, 8, 8, 8])
topo.append(['Conv4 ',  3, size, size, size, size, 3, 3,  64,  64, 1, False, False, 8, 8, 8])
topo.append(['Conv5 ',  4, size, size, size, size, 3, 3,  64,  64, 1, False, False, 8, 4, 4])

size = 28
topo.append(['Conv6 ',  5, size, size, size, size, 3, 3,  64, 128, 1, False, False, 4, 8, 8])
topo.append(['Conv7 ',  6, size, size, size, size, 3, 3, 128, 128, 1, False, False, 8, 8, 8])
topo.append(['Conv8 ',  7, size, size, size, size, 3, 3, 128, 128, 1, False, False, 8, 8, 8])
topo.append(['Conv9 ',  8, size, size, size, size, 3, 3, 128, 128, 1, False, False, 8, 4, 4])

size = 14
topo.append(['Conv10',  9, size, size, size, size, 3, 3, 128, 256, 1, False, False, 4, 8, 8])
topo.append(['Conv11', 10, size, size, size, size, 3, 3, 256, 256, 1, False, False, 8, 8, 8])
topo.append(['Conv12', 11, size, size, size, size, 3, 3, 256, 256, 1, False, False, 8, 4, 4])
topo.append(['Conv13', 12, size, size, size, size, 3, 3, 256, 256, 1, False, False, 4, 4, 4])

size = 7
topo.append(['Conv14', 13, size, size, size, size, 3, 3, 256, 512, 1, False, False, 4, 4, 4])
topo.append(['Conv15', 14, size, size, size, size, 3, 3, 512, 512, 1, False, False, 4, 4, 4])
topo.append(['Conv16', 15, size, size, size, size, 3, 3, 512, 512, 1, False, False, 4, 4, 4])
topo.append(['Conv17', 16, size, size, size, size, 3, 3, 512, 512, 1, False, False, 4, 4, 4])

topo.append(['FC    ', 17, 1, 1, 1, 1, 1, 1, 512, 1000, 1, False, True, 4, 8, 8])
ResNet18_bops = topo

######################################################################################################################

topo = []
topo.append(['Conv1 ',  0, 32, 32, 32, 32, 3, 3,    3,   16, 1, False, False, 8, 8, 8])

size = 32
topo.append(['Conv2 ',  1, size, size, size, size, 3, 3, 16, 16, 1, False, False, 8, 8, 8])
topo.append(['Conv3 ',  2, size, size, size, size, 3, 3, 16, 16, 1, False, False, 8, 8, 8])
topo.append(['Conv4 ',  3, size, size, size, size, 3, 3, 16, 16, 1, False, False, 8, 8, 8])
topo.append(['Conv5 ',  4, size, size, size, size, 3, 3, 16, 16, 1, False, False, 8, 8, 8])
topo.append(['Conv6 ',  3, size, size, size, size, 3, 3, 16, 16, 1, False, False, 8, 8, 8])
topo.append(['Conv7 ',  4, size, size, size, size, 3, 3, 16, 16, 1, False, False, 8, 8, 8])

size = 16
topo.append(['Conv8 ',  7, size, size, size, size, 3, 3, 16, 32, 1, False, False, 8, 8, 8])
topo.append(['Conv9 ',  8, size, size, size, size, 3, 3, 32, 32, 1, False, False, 8, 8, 8])
topo.append(['Conv10',  5, size, size, size, size, 3, 3, 32, 32, 1, False, False, 8, 8, 8])
topo.append(['Conv11',  6, size, size, size, size, 3, 3, 32, 32, 1, False, False, 8, 8, 8])
topo.append(['Conv12',  5, size, size, size, size, 3, 3, 32, 32, 1, False, False, 8, 8, 8])
topo.append(['Conv13',  6, size, size, size, size, 3, 3, 32, 32, 1, False, False, 8, 8, 8])

size = 8
topo.append(['Conv14',  9, size, size, size, size, 3, 3, 32, 64, 1, False, False, 8, 8, 8])
topo.append(['Conv15', 10, size, size, size, size, 3, 3, 64, 64, 1, False, False, 8, 8, 8])
topo.append(['Conv16', 11, size, size, size, size, 3, 3, 64, 64, 1, False, False, 8, 8, 8])
topo.append(['Conv17', 12, size, size, size, size, 3, 3, 64, 64, 1, False, False, 8, 8, 8])
topo.append(['Conv18', 11, size, size, size, size, 3, 3, 64, 64, 1, False, False, 8, 8, 8])
topo.append(['Conv19', 12, size, size, size, size, 3, 3, 64, 64, 1, False, False, 8, 8, 8])

topo.append(['FC    ', 17, 1, 1, 1, 1, 1, 1, 64, 10, 1, False, True, 8, 8, 8])
ResNet20_8 = topo

######################################################################################################################

bit_width = 1
topo = []
topo.append(['Conv1 ', 0, 32, 32, 28, 28, 5, 5,   1,   6, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv2 ', 1, 14, 14, 10, 10, 5, 5,   6,  16, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC1   ', 2,  5,  5,  1,  1, 1, 1,  16, 120, 1,  True, False, bit_width, bit_width, bit_width])
topo.append(['FC2   ', 3,  1,  1,  1,  1, 1, 1, 120,  84, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC3   ', 4,  1,  1,  1,  1, 1, 1,  84,  10, 1, False,  True, bit_width, bit_width, bit_width])
lenet5_11_topo = topo


bit_width = 4
topo = []
topo.append(['Conv1 ', 0, 32, 32, 28, 28, 5, 5,   1,   6, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv2 ', 1, 14, 14, 10, 10, 5, 5,   6,  16, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC1   ', 2,  5,  5,  1,  1, 1, 1,  16, 120, 1,  True, False, bit_width, bit_width, bit_width])
topo.append(['FC2   ', 3,  1,  1,  1,  1, 1, 1, 120,  84, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC3   ', 4,  1,  1,  1,  1, 1, 1,  84,  10, 1, False,  True, bit_width, bit_width, bit_width])
lenet5_44_topo = topo


bit_width = 8
topo = []
topo.append(['Conv1 ', 0, 32, 32, 28, 28, 5, 5,   1,   6, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv2 ', 1, 14, 14, 10, 10, 5, 5,   6,  16, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC1   ', 2,  5,  5,  1,  1, 1, 1,  16, 120, 1,  True, False, bit_width, bit_width, bit_width])
topo.append(['FC2   ', 3,  1,  1,  1,  1, 1, 1, 120,  84, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC3   ', 4,  1,  1,  1,  1, 1, 1,  84,  10, 1, False,  True, bit_width, bit_width, bit_width])
lenet5_88_topo = topo

######################################################################################################################

bit_width = 1
topo = []
topo.append(['FC1   ', 0,  1,  1,  1,  1, 1, 1,  784, 1024, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC2   ', 1,  1,  1,  1,  1, 1, 1, 1024,   64, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC3   ', 2,  1,  1,  1,  1, 1, 1,   64,   64, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC4   ', 3,  1,  1,  1,  1, 1, 1,   64,   10, 1, False,  True, bit_width, bit_width, bit_width])
MLP4_1 = topo


bit_width = 4
topo = []
topo.append(['FC1   ', 0,  1,  1,  1,  1, 1, 1,  784, 1024, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC2   ', 1,  1,  1,  1,  1, 1, 1, 1024,   64, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC3   ', 2,  1,  1,  1,  1, 1, 1,   64,   64, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC4   ', 3,  1,  1,  1,  1, 1, 1,   64,   10, 1, False,  True, bit_width, bit_width, bit_width])
MLP4_4 = topo


bit_width = 8
topo = []
topo.append(['FC1   ', 0,  1,  1,  1,  1, 1, 1,  784, 1024, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC2   ', 1,  1,  1,  1,  1, 1, 1, 1024,   64, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC3   ', 2,  1,  1,  1,  1, 1, 1,   64,   64, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC4   ', 3,  1,  1,  1,  1, 1, 1,   64,   10, 1, False,  True, bit_width, bit_width, bit_width])
MLP4_8 = topo

######################################################################################################################

bit_width = 1
topo = []
topo.append(['Conv1 ',  0, 224, 224, 224, 224, 3, 3,    3,   64, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv2 ',  1, 224, 224, 224, 224, 3, 3,   64,   64, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['Conv3 ',  2, 112, 112, 112, 112, 3, 3,   64,  128, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv4 ',  3, 112, 112, 112, 112, 3, 3,  128,  128, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['Conv5 ',  4,  56,  56,  56,  56, 3, 3,  128,  256, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv6 ',  5,  56,  56,  56,  56, 3, 3,  256,  256, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv7 ',  6,  56,  56,  56,  56, 3, 3,  256,  256, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['Conv8 ',  7,  28,  28,  28,  28, 3, 3,  256,  512, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv9 ',  8,  28,  28,  28,  28, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv10',  9,  28,  28,  28,  28, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['Conv11', 10,  14,  14,  14,  14, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv12', 11,  14,  14,  14,  14, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv13', 12,  14,  14,  14,  14, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['FC1   ', 13,   7,   7,   1,   1, 1, 1,  512, 4096, 1,  True, False, bit_width, bit_width, bit_width])
topo.append(['FC2   ', 14,   1,   1,   1,   1, 1, 1, 4096, 4096, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC3   ', 15,   1,   1,   1,   1, 1, 1, 4096, 1000, 1, False,  True, bit_width, bit_width, bit_width])
VGG16_1 = topo


bit_width = 4
topo = []
topo.append(['Conv1 ',  0, 224, 224, 224, 224, 3, 3,    3,   64, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv2 ',  1, 224, 224, 224, 224, 3, 3,   64,   64, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['Conv3 ',  2, 112, 112, 112, 112, 3, 3,   64,  128, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv4 ',  3, 112, 112, 112, 112, 3, 3,  128,  128, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['Conv5 ',  4,  56,  56,  56,  56, 3, 3,  128,  256, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv6 ',  5,  56,  56,  56,  56, 3, 3,  256,  256, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv7 ',  6,  56,  56,  56,  56, 3, 3,  256,  256, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['Conv8 ',  7,  28,  28,  28,  28, 3, 3,  256,  512, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv9 ',  8,  28,  28,  28,  28, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv10',  9,  28,  28,  28,  28, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['Conv11', 10,  14,  14,  14,  14, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv12', 11,  14,  14,  14,  14, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv13', 12,  14,  14,  14,  14, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['FC1   ', 13,   7,   7,   1,   1, 1, 1,  512, 4096, 1,  True, False, bit_width, bit_width, bit_width])
topo.append(['FC2   ', 14,   1,   1,   1,   1, 1, 1, 4096, 4096, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC3   ', 15,   1,   1,   1,   1, 1, 1, 4096, 1000, 1, False,  True, bit_width, bit_width, bit_width])
VGG16_4 = topo


bit_width = 8
topo = []
topo.append(['Conv1 ',  0, 224, 224, 224, 224, 3, 3,    3,   64, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv2 ',  1, 224, 224, 224, 224, 3, 3,   64,   64, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['Conv3 ',  2, 112, 112, 112, 112, 3, 3,   64,  128, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv4 ',  3, 112, 112, 112, 112, 3, 3,  128,  128, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['Conv5 ',  4,  56,  56,  56,  56, 3, 3,  128,  256, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv6 ',  5,  56,  56,  56,  56, 3, 3,  256,  256, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv7 ',  6,  56,  56,  56,  56, 3, 3,  256,  256, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['Conv8 ',  7,  28,  28,  28,  28, 3, 3,  256,  512, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv9 ',  8,  28,  28,  28,  28, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv10',  9,  28,  28,  28,  28, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['Conv11', 10,  14,  14,  14,  14, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv12', 11,  14,  14,  14,  14, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['Conv13', 12,  14,  14,  14,  14, 3, 3,  512,  512, 1, False, False, bit_width, bit_width, bit_width])

topo.append(['FC1   ', 13,   7,   7,   1,   1, 1, 1,  512, 4096, 1,  True, False, bit_width, bit_width, bit_width])
topo.append(['FC2   ', 14,   1,   1,   1,   1, 1, 1, 4096, 4096, 1, False, False, bit_width, bit_width, bit_width])
topo.append(['FC3   ', 15,   1,   1,   1,   1, 1, 1, 4096, 1000, 1, False,  True, bit_width, bit_width, bit_width])
VGG16_8 = topo

