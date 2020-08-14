**FORMULA FOR CALCULATING RF**

Rout = Rin + (k-1)*Jin

k = kernel size

Jin = Input jump size.

Jout = Jin*Stride

------

#### 1. 5*5 in grouped convolutions, Final receptive field = 907

| Input Kernel and Stride                    | Rin                | Jin  | Jout    |
| ------------------------------------------ | ------------------ | ---- | ------- |
| Input                                      | 1                  | 1    | 1       |
| 7*7,2                                      | 1+(7-1)*1=7        | 1    | 1*2 = 2 |
| 3*3,2                                      | 7+(3-1)*2=11       | 2    | 2*2=4   |
| 3*3,1                                      | 11+(3-1)*4=19      | 4    | 4*1=4   |
| 3*3,2                                      | 19+(3-1)*4=27      | 4    | 4*2=8   |
| Inception(taking the size of maximum)5*5,1 | 27+(5-1)*8=59      | 8    | 8*1=8   |
| Inception(taking the size of maximum)5*5,1 | 59+(5-1)*8=91      | 8    | 8*1=8   |
| 3*3,2                                      | 91+(3-1)*8=107     | 8    | 8*2=16  |
| Inception(taking the size of maximum)5*5,1 | 107+(5-1)*16=171   | 16   | 16*1=16 |
| Inception(taking the size of maximum)5*5,1 | 171+(5-1)*16=235   | 16   | 16*1=16 |
| Inception(taking the size of maximum)5*5,1 | 235+(5-1)*16=299   | 16   | 16*1=16 |
| Inception(taking the size of maximum)5*5,1 | 299+(5-1)*16=363   | 16   | 16*1=16 |
| Inception(taking the size of maximum)5*5,1 | 363+(5-1)*16=427   | 16   | 16*1=16 |
| 3*3,2                                      | 427+(3-1)*16=459   | 16   | 16*2=32 |
| Inception(taking the size of maximum)5*5,1 | 459+(5-1)*32=587   | 32   | 32*1=32 |
| Inception(taking the size of maximum)5*5,1 | 587+(5-1)*32=715   | 32   | 32*1=32 |
| 7*7,1                                      | 715+(7-1)*32 = 907 | 32   | 32*1=32 |
|                                            |                    |      |         |
|                                            |                    |      |         |

#### 2. 3*3 in grouped convolutions, Final receptive field = 587

|       Input Kernel and Stride        |        Rin         | Jin  | Jout    |
| :----------------------------------: | :----------------: | :--: | ------- |
|                Input                 |         1          |  1   | 1*1=1   |
|                7*7,2                 |   1+(7-1)*7 = 7    |  1   | 1*2=2   |
|                3*3,2                 |   7+(3-1)*2 = 11   |  2   | 2*2=4   |
|                3*3,1                 |  11+(3-1)*4 = 19   |  4   | 4*1=4   |
|                3*3,2                 |  19+(3-1)*4 = 27   |  4   | 4*2=8   |
| Inception(taking the size of 3)3*3,1 |  27+(3-1)*8 = 43   |  8   | 8*1=8   |
| Inception(taking the size of 3)3*3,1 |  43+(3-1)*8 = 59   |  8   | 8*1=8   |
|                3*3,2                 |  59+(3-1)*8 = 75   |  8   | 8*2=16  |
| Inception(taking the size of 3)3*3,1 | 75+(3-1)*16 = 107  |  16  | 16*1=16 |
| Inception(taking the size of 3)3*3,1 | 107+(3-1)*16 = 139 |  16  | 16*1=16 |
| Inception(taking the size of 3)3*3,1 | 139+(3-1)*16 = 171 |  16  | 16*1=16 |
| Inception(taking the size of 3)3*3,1 | 171+(3-1)*16 = 203 |  16  | 16*1=16 |
| Inception(taking the size of 3)3*3,1 | 203+(3-1)*16 = 235 |  16  | 16*1=16 |
|                3*3,2                 | 235+(3-1)*16 = 267 |  16  | 16*2=32 |
| Inception(taking the size of 3)3*3,1 | 267+(3-1)*32 = 331 |  32  | 32*1=32 |
| Inception(taking the size of 3)3*3,1 | 331+(3-1)*32 = 395 |  32  | 32*1=32 |
|                7*7,1                 | 395+(7-1)*32 = 587 |  32  | 32*1=32 |

------

#### 3. 1*1 in grouped convolutions, Final receptive field = 267

|       Input Kernel and Stride        |        Rin        | Jin  | Jout    |
| :----------------------------------: | :---------------: | :--: | ------- |
|                Input                 |         1         |  1   | 1*1=1   |
|                7*7,2                 |   1+(7-1)*7 = 7   |  1   | 1*2=2   |
|                3*3,2                 |  7+(3-1)*2 = 11   |  2   | 2*2=4   |
|                3*3,1                 |  11+(3-1)*4 = 19  |  4   | 4*1=4   |
|                3*3,2                 |  19+(3-1)*4 = 27  |  4   | 4*2=8   |
| Inception(taking the size of 1)1*1,1 |  27+(1-1)*8 = 27  |  8   | 8*1=8   |
| Inception(taking the size of 1)1*1,1 |  27+(1-1)*8 = 27  |  8   | 8*1=8   |
|                3*3,2                 |  27+(3-1)*8 = 43  |  8   | 8*2=16  |
| Inception(taking the size of 1)1*1,1 | 43+(1-1)*16 = 43  |  16  | 16*1=16 |
| Inception(taking the size of 1)1*1,1 | 43+(1-1)*16 = 43  |  16  | 16*1=16 |
| Inception(taking the size of 1)1*1,1 | 43+(1-1)*16 = 43  |  16  | 16*1=16 |
| Inception(taking the size of 1)1*1,1 | 43+(1-1)*16 = 43  |  16  | 16*1=16 |
| Inception(taking the size of 1)1*1,1 | 43+(1-1)*16 = 43  |  16  | 16*1=16 |
|                3*3,2                 | 43+(3-1)*16 = 75  |  16  | 16*2=32 |
| Inception(taking the size of 1)1*1,1 | 75+(1-1)*32 = 75  |  32  | 32*1=32 |
| Inception(taking the size of 1)1*1,1 | 75+(1-1)*32 = 75  |  32  | 32*1=32 |
|                7*7,1                 | 75+(7-1)*32 = 267 |  32  | 32*1=32 |