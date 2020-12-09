# given a list of items, return a list where the first item of the original is removed and newitem is appended
def append_to_buffer(old_list, newitem):
    return_list = old_list[1:]
    return_list.append(newitem)
    return return_list

# given a number and a buffer of other numbers, determine if number can be made as a sum of any two numbers in the buffer
def is_number_sum_from_list(number, buffer):
    for num1 in buffer:
        for num2 in buffer:
            if num1 == num2:
                continue

            if num1 + num2 == number:
                return True
    return False

# find a contiguous set of numbers in list that adds up to number
def find_contiguous_sum(list, number):
    position = 0
    while position < len(list):

      set_length = 1
      current_set = []
      while sum(current_set) <= number:
          current_set = list[position:set_length]
          if sum(current_set) == number:
              return current_set

          set_length = set_length + 1

      position = position + 1

    return None


if __name__ == '__main__':
    data = '''
33
18
22
44
49
15
12
38
41
46
3
42
37
19
13
7
21
29
34
40
39
35
27
25
48
87
10
16
17
45
18
30
20
22
23
73
24
26
28
53
31
37
51
32
33
34
36
35
54
27
38
39
40
74
70
41
93
144
45
63
87
66
65
55
58
62
72
105
59
76
61
67
68
77
106
78
79
183
86
117
96
100
108
104
123
113
114
116
129
119
178
120
196
126
177
184
135
182
192
201
174
360
186
190
210
248
214
282
217
227
229
304
235
370
308
261
302
300
542
376
309
317
356
364
375
407
396
400
404
585
599
514
444
907
456
633
687
496
665
561
563
832
1056
626
673
681
720
731
840
819
796
800
1033
1117
900
958
940
952
1017
1019
1748
1177
1422
1124
1578
1189
1299
1678
1307
1354
2702
2476
1689
3775
1740
2813
2706
1977
1898
1840
2630
2864
1971
2439
2143
2932
2301
2313
2423
2488
2496
3194
2661
2996
3043
4416
3429
3529
3580
3638
3738
3983
4830
3811
4114
4724
5782
4394
4444
7143
6623
6882
7267
5149
7823
5855
5657
5704
6425
7026
6958
9666
7109
7218
10249
8535
7794
11512
14327
9969
15906
8838
10101
9593
12082
10806
10853
13451
17489
13073
11361
12129
17210
13383
13984
30562
16329
14903
15753
19306
16632
23920
26456
26113
18431
27032
19644
27882
20399
37885
21659
27976
24812
23490
24744
25345
25512
42785
27367
29737
30656
45579
31535
32385
35063
52788
38075
38830
44544
40090
40043
55249
57897
42058
45149
52712
48234
48302
72946
50089
64342
52879
103551
57104
72428
62191
79837
63920
71215
73138
80133
84587
82148
156430
90132
152323
113146
90360
197733
100946
105591
101113
98391
288093
154280
109983
204497
164424
152975
137058
126111
191473
181079
144353
153271
170265
166735
183261
180492
188523
236094
235449
188751
202059
262815
305610
199504
208374
247041
312042
254336
440591
353175
442859
263169
270464
616344
297624
311088
320006
402829
377274
363753
369015
501377
388255
390810
397125
401563
407878
446545
455415
471543
732768
524800
751679
1043856
533633
626922
568088
581552
608712
699343
631094
697280
779065
926958
921925
868668
785380
969651
856978
798688
809441
989430
901960
1036967
996343
1285312
1133512
1101721
1195010
1115185
1149640
1330437
1911355
1239806
1328374
1912577
1476345
3239729
1654048
1655666
1594821
1584068
1608129
1758938
1700648
1711401
2365341
1898303
2895658
2098064
2216906
4654596
3293074
2769233
2354991
3039775
2834627
3238116
3810880
3132011
3060413
3178889
3284716
3192197
3202950
3295469
4253294
3928307
3412049
4720332
4993722
4867297
3996367
4571897
8152013
4986139
5124224
5189618
6472462
5394766
5874402
5895040
7003077
6192424
7385305
8181601
6476913
6395147
6487666
8716699
6707518
7408416
8398188
7983946
8568264
8863664
8982506
9120591
13184431
10860541
10110363
10313842
10584384
11289806
15470172
11769442
12382706
16579789
15056088
12872060
13896082
12964579
13102665
25185888
24474237
14115934
20633106
16382134
16552210
23098440
19092869
18103097
24209924
24392471
27842016
24254385
28687481
24152148
23059248
38150467
24641502
25347285
25836639
42357482
36023827
26067244
27080513
35645079
49033973
30498068
39463219
42619454
32934344
34655307
29221323
37195966
60665329
62725592
47313633
50901264
47211396
82958712
47700750
48406533
49988787
50708746
51183924
51903883
53147757
88497192
77789259
56301836
86546343
67694034
59719391
70130310
81340877
101892670
63876630
66417289
84407362
96107283
94525029
146096070
94912146
95617929
103087807
101554290
180025291
103136544
102612629
110903315
105051640
109449593
116021227
120178466
122719125
178932391
197661573
123596021
167971579
130293919
283113098
199576669
245349680
199243827
189437175
213515944
190530075
196466436
197172219
233045614
390106744
223315010
225331754
207664269
214501233
396748888
225470820
291567600
312156300
478395294
343809863
253889940
298265498
509328519
319731094
472550273
379967250
385903611
386609394
479221694
711440908
545201914
393638655
629794502
422165502
439972053
680214542
461554209
433135089
468391173
1024423608
479360760
545457540
552155438
854294784
573621034
617996592
678232748
705634705
699698344
938840569
773605905
772513005
780248049
815804157
1170152030
826773744
855192864
1418201329
862137555
1794033433
1024818300
894689298
1051131681
1163454132
1031516198
1052981794
1119078574
1125776472
1191617626
1450745753
1485882754
1377931092
1405333049
1472211349
2266130803
1546118910
1552761054
2576522225
1642577901
1717330419
1681966608
1749882162
2300022347
1886955855
2216435926
1919507598
2242749307
2084497992
2150594772
2157292670
2172060368
2244855046
2317394098
2569548718
2891215803
2783264141
2850142441
2877544398
3762554836
3098879964
4533830024
3195338955
4384520339
5066578367
3399297027
3568922463
3636838017
8170668041
6514382415
4373728596
4467988870
4322655140
6446466861
4307887442
5674479944
4416915414
7406767406
5100658239
5352812859
5978603096
7105919281
6498176991
8669580702
6294218919
6735717981
11048212439
8021358356
6968219490
11573908151
7036135044
7205760480
7944725459
9423313379
8630542582
8790644010
17868127070
8724802856
9408545681
9982367386
10453471098
9517573653
11079261335
12792395910
18253972919
12272822015
13400138200
13233894972
13029936900
13262438409
14912944949
14004354534
27677286298
17188127866
20436273244
14241895524
21790395668
20502574714
17421186592
19499941039
17515446866
25912930722
23687366070
18926119334
20435838484
25672960215
24109198235
44865414164
25065217925
25302758915
25506716987
26263831872
30683625001
27034291434
27504333933
28246250058
31192482400
48104811593
36921127631
33168014858
31663082116
42486404517
34936633458
43188407081
50683461724
36441566200
43991337259
81786541795
39361957818
44545036719
49174416160
49411957150
61876107401
50367976840
53549008973
51770548859
53298123306
54538625367
55280541492
59909332174
84348590608
87706640225
64831096974
82346543840
71025039934
66599715574
71378199658
126331578514
75803524018
121746176498
93956993869
115923236377
89729934658
83906994537
93719452879
143131410029
99779933990
102138525699
136119139467
125563665301
106309174226
107836748673
109819166859
115189873666
126509047748
185622690877
147177640814
131430812548
287761216576
137624755508
192931294088
165533458676
159710518555
177626447416
201793742542
173636929195
183449387537
183686928527
186045520236
193499386869
206089108216
217655915532
208447699925
407882850758
423745023748
232818221974
239267561221
300145976943
241698921414
314880200085
269055568056
330627028351
291141331103
353209905424
343159906092
392134628452
325243977231
351263376611
363671967652
357086316732
416505150501
367136316064
399588495085
394493220161
745756596772
414536808141
426103615457
441265921899
472085783195
584858827506
474517143388
592477466645
709373420246
510754489470
783641466565
560196899159
841653459452
616385308334
694423282703
719737197392
676507353842
886622591336
720758284384
724222632796
1071000574003
810998370662
1010962442963
794081715246
1208618523387
1150639342145
1001462821058
867369537356
915783065287
946602926583
985271632858
1034714042547
1176582207493
1070951388629
1127139797804
1587106734748
1812461191720
2502889800035
1292892662176
1370930636545
1396244551234
1607380875720
3537603842582
1444980917180
1795174021425
1938370111359
1661451252602
1709864780533
2086974377422
1950497107834
1813972463939
1783152602643
2105665431176
1986734453916
1931874559441
2019985675405
3108456766934
2198091186433
2788591050406
2420032459980
2689137213410
3769887056559
4136461297792
2663823298721
2767175187779
3003625426954
4056162539010
3106432169782
3228133519823
3371316033135
3733649710477
4887228399843
3493017383176
3597125066582
5109290858130
3803138278048
5917270733233
4125651106581
3951860234846
4129965745874
4218076861838
4618123646413
4861914485154
5109169673390
7773114156851
6156840681897
6840081880259
5430998486500
5667448725675
6500824898256
6110057596736
6721150902999
10235708703317
7446210381661
6968441099717
7090142449758
8743774752994
7296155661224
7400263344630
8912307951438
8665052763202
8077511341427
8081825980720
9079991346992
15069148633335
10374917543735
13510320941366
9971084158544
11219227270126
14917593221686
12271080366759
11098447212175
12168273623931
11777506322411
12610882494992
12831208499735
13689592002716
14058583549475
14264596760941
14368704444347
14386298110982
14696419005854
23369527578934
20231471844365
16159337322147
24824390085349
25915646275980
26997180605974
25678594565297
22242164525303
22802292658279
22139357782475
21069531370719
22317674482301
22875953534586
25442090994727
28961015766795
25836089871886
26042103083352
26300474497708
40284350720327
28755002555329
28323180310416
35334128131660
51203180292098
36525655893457
45044457183582
45193628016887
36390809166512
42074983598127
48153764354187
43311695896022
49176428032294
43208889153194
43387205853020
43871824028998
44457032264776
73989854226073
47759765477028
48318044529313
51278180866613
54591092427215
69044979025080
52342577581060
54623654808124
57078182865745
76082945787444
92610796618963
71724937298172
72916465059969
78465792764639
79599698319706
81584437183399
79702505062534
122092893092263
86596095006214
86520585049216
87080713182192
96799609845836
87259029882018
99080687072900
'''
    lines = [int(line.strip()) for line in data.split("\n") if len(line) > 0]
    buffer = lines[0:25]
    position = 25
    while position < len(lines):
        current = lines[position]
        if not is_number_sum_from_list(current, buffer):
            found_answer = current
            break

        buffer = append_to_buffer(buffer, current)
        position = position + 1

    answer = find_contiguous_sum(lines, found_answer)
    print(min(answer) + max(answer))
