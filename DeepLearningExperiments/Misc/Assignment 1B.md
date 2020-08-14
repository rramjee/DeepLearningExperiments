#### Extensive Vision for AI

### Name: Ramjee R

### W6

### Email - rramjee@gmail.com

### Assignment 1B

### 1. What are Kernels and Channels according to EVA.?

## Response: 

Kernels are filters to detect a specific feature(s) in an image. One can use as many kernels to detect different features in an image. Also, kernels can be used in various layers of the the neural network. Deeper we go in an neural network, more advanced or sophisticated features can be detected with kernels.



Channels are referred to as a feature map that encodes the presence or absence of a specific feature. It is usually the convolution of the input pixel values and the kernel values. 



### 2. Why should we only (mostly) use 3*3 kernel ?

## Response

The reason for using 3*3 kernel is primarily to detect the optimum features in the input image. The size 3*3 is not too low to keep the high dimensionality and also not too high to miss significant features that are small.



### 3. How many times do we need to perfrom 3*3 convolutions operation to reach 1*1 from 199*199

## Response

It is 99 times. 

Input	Kernel	Output	Step Count
199*199	3*3	197*197	1
197*197	3*3	195*195	2
195*195	3*3	193*193	3
193*193	3*3	191*191	4
191*191	3*3	189*189	5
189*189	3*3	187*187	6
187*187	3*3	185*185	7
185*185	3*3	183*183	8
183*183	3*3	181*181	9
181*181	3*3	179*179	10
179*179	3*3	177*177	11
177*177	3*3	175*175	12
175*175	3*3	173*173	13
173*173	3*3	171*171	14
171*171	3*3	169*169	15
169*169	3*3	167*167	16
167*167	3*3	165*165	17
165*165	3*3	163*163	18
163*163	3*3	161*161	19
161*161	3*3	159*159	20
159*159	3*3	157*157	21
157*157	3*3	155*155	22
155*155	3*3	153*153	23
153*153	3*3	151*151	24
151*151	3*3	149*149	25
149*149	3*3	147*147	26
147*147	3*3	145*145	27
145*145	3*3	143*143	28
143*143	3*3	141*141	29
141*141	3*3	139*139	30
139*139	3*3	137*137	31
137*137	3*3	135*135	32
135*135	3*3	133*133	33
133*133	3*3	131*131	34
131*131	3*3	129*129	35
129*129	3*3	127*127	36
127*127	3*3	125*125	37
125*125	3*3	123*123	38
123*123	3*3	121*121	39
121*121	3*3	119*119	40
119*119	3*3	117*117	41
117*117	3*3	115*115	42
115*115	3*3	113*113	43
113*113	3*3	111*111	44
111*111	3*3	109*109	45
109*109	3*3	107*107	46
107*107	3*3	105*105	47
105*105	3*3	103*103	48
103*103	3*3	101*101	49
101*101	3*3	99*99	50
99*99	3*3	97*97	51
97*97	3*3	95*95	52
95*95	3*3	93*93	53
93*93	3*3	91*91	54
91*91	3*3	89*89	55
89*89	3*3	87*87	56
87*87	3*3	85*85	57
85*85	3*3	83*83	58
83*83	3*3	81*81	59
81*81	3*3	79*79	60
79*79	3*3	77*77	61
77*77	3*3	75*75	62
75*75	3*3	73*73	63
73*73	3*3	71*71	64
71*71	3*3	69*69	65
69*69	3*3	67*67	66
67*67	3*3	65*65	67
65*65	3*3	63*63	68
63*63	3*3	61*61	69
61*61	3*3	59*59	70
59*59	3*3	57*57	71
57*57	3*3	55*55	72
55*55	3*3	53*53	73
53*53	3*3	51*51	74
51*51	3*3	49*49	75
49*49	3*3	47*47	76
47*47	3*3	45*45	77
45*45	3*3	43*43	78
43*43	3*3	41*41	79
41*41	3*3	39*39	80
39*39	3*3	37*37	81
37*37	3*3	35*35	82
35*35	3*3	33*33	83
33*33	3*3	31*31	84
31*31	3*3	29*29	85
29*29	3*3	27*27	86
27*27	3*3	25*25	87
25*25	3*3	23*23	88
23*23	3*3	21*21	89
21*21	3*3	19*19	90
19*19	3*3	17*17	91
17*17	3*3	15*15	92
15*15	3*3	13*13	93
13*13	3*3	11*11	94
11*11	3*3	9*9		95
9*9		3*3	7*7		96
7*7		3*3	5*5		97
5*5		3*3	3*3		98
3*3		3*3	1*1		99


