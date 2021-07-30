# This list it's based in a pokemon type chart 
atack_rules = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 0, 1, 1, .5, 0]        ,           
    [1, .5, .5, 2, 1, 2, 1, 1, 1, 1, 1, 2, .5, 1, .5, 1, 2, 1]      ,         
    [1, 2, .5, .5, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, .5, 1, 1, 1]       ,          
    [1, .5, 2, .5, 1, 1, 1, .5, 2, .5, 1, .5, 2, 1, .5, 1, .5, 1]   ,   
    [1, 1, 2, .5, .5, 1, 1, 1, 0, 2, 1, 1, 1, 1, .5, 1, 1, 1]       ,          
    [1, .5, .5, 2, 1, .5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, .5, 1]      ,         
    [2, 1, 1, 1, 1, 2, 1, .5, 1, .5, .5, .5, 2, 0, 1, 2, 2, .5]     ,        
    [1, 1, 1, 2, 1, 1, 1, .5, .5, 1, 1, 1, .5, .5, 1, 1, 0, 2]      ,         
    [1, 2, 1, .5, 2, 1, 1, 2, 1, 0, 1, .5, 2, 1, 1, 1, 2, 1]        ,           
    [1, 1, 1, 2, .5, 1, 2, 1, 1, 1, 1, 2, .5, 1, 1, 1, .5, 1]       ,          
    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, .5, 1, 1, 1, 1, 0, .5, 1]        ,           
    [1, .5, 1, 2, 1, 1, .5, .5, 1, .5, 2, 1, 1, .5, 1, 2, .5, .5]   ,      
    [1, 2, 1, 1, 1, 2, .5, 1, .5, 2, 1, 2, 1, 1, 1, 1, .5, 1]       ,           
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, 1]         ,            
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, .5, 0]         ,            
    [1, 1, 1, 1, 1, 1, .5, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, .5]       ,          
    [1, .5, .5, 1, .5, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, .5, 2]      ,         
    [1, .5, 1, 1, 1, 1, 2, .5, 1, 1, 1, 1, 1, 1, 2, 2, .5, 1]           
]

#This dict it's about the atacker types
atack_types = {
    'normal':    0,
    'fire':      1,
    'water':     2,
    'grass':     3,
    'electric':  4,
    'ice':       5,
    'fighting':  6,
    'poison':    7, 
    'ground':    8,
    'flying':    9,
    'psychic':   10,
    'bug':       11,
    'rock':      12,
    'ghost':     13,
    'dragon':    14,
    'dark':      15,
    'steel':     16,
    'fairy':     17
}

#This function receives the atacker and the damaged pokemon types 
#And searchs in the atack_rules chart the intensity of the atack
def get_damage(atacker, demaged):
    row      = atack_types[atacker]
    column   = atack_types[demaged]
    return atack_rules[row][column]


# Capture rules to capture in each area with each pokeball type
capture_rules = [
    [	60	,	90	,	100	,	100	]	,
    [	55	,	80	,	95	,	100	]	,
    [	50	,	75	,	90	,	100	]	,
    [	45	,	70	,	90	,	100	]	,
    [	35	,	50	,	75	,	100	]	,
    [	25	,	40	,	70	,	100	]	,
    [	10	,	35	,	65	,	100	]	,
    [	5	,	10	,	65	,	90	]	,
    [	0	,	5	,	50	,	90	]	,
    [	0	,	0	,	10	,	75	]	
]

# Areas to use as row
capture_zones = {
    'object_forest'	:	0	,
    'object_mount'	:	1	,
    'object_cave'	:	2	,
    'object_tunnel'	:	3	,
    'object_safari'	:	4	,
    'object_islands':	5	,
    'object_road' 	:	6	,
    'object_trees'	:	7	,
    'object_valley'	:	8	,
    'object_center'	:	9	,
}

# Pokeball types to use as column
capture_methods = {
    '1'  : 0, # pokeballs
    '2'  : 1, # greatballs
    '3'  : 2, # ultraballs
    '4'  : 3, # masterballs
}

# Function that returns the correct chance to capture in each area with each pokeball type
def get_chance(zone, methods):
    row     = capture_zones[zone]
    column  = capture_methods[methods]
    return capture_rules[row][column]

evolution = {
1	:	[	50	,	20	]	,
2	:	[	75	,	22	]	,
3	:	[	113	,	24	]	,
4	:	[	169	,	26	]	,
5	:	[	253	,	29	]	,
6	:	[	380	,	31	]	,
7	:	[	456	,	33	]	,
8	:	[	547	,	35	]	,
9	:	[	656	,	37	]	,
10	:	[	787	,	41	]	,
11	:	[	945	,	44	]	,
12	:	[	1134	,	47	]	,
13	:	[	1360	,	50	]	,
14	:	[	1633	,	53	]	,
15	:	[	1959	,	57	]	,
16	:	[	2351	,	60	]	,
17	:	[	2821	,	63	]	,
18	:	[	3385	,	66	]	,
19	:	[	4062	,	69	]	,
20	:	[	4875	,	74	]	,
21	:	[	5362	,	77	]	,
22	:	[	5899	,	80	]	,
23	:	[	6488	,	83	]	,
24	:	[	7137	,	86	]	,
25	:	[	7851	,	90	]	,
26	:	[	8636	,	93	]	,
27	:	[	9500	,	96	]	,
28	:	[	10450	,	99	]	,
29	:	[	11495	,	102	]	,
30	:	[	12644	,	107	]	,
31	:	[	13909	,	111	]	,
32	:	[	15299	,	115	]	,
33	:	[	16829	,	119	]	,
34	:	[	18512	,	123	]	,
35	:	[	20364	,	128	]	,
36	:	[	22400	,	132	]	,
37	:	[	24640	,	136	]	,
38	:	[	27104	,	140	]	,
39	:	[	29814	,	144	]	,
40	:	[	32796	,	150	]	,
41	:	[	36075	,	154	]	,
42	:	[	39683	,	158	]	,
43	:	[	43651	,	162	]	,
44	:	[	48016	,	166	]	,
45	:	[	52818	,	171	]	,
46	:	[	58100	,	175	]	,
47	:	[	63910	,	179	]	,
48	:	[	70301	,	183	]	,
49	:	[	77331	,	187	]	,
50	:	[	85064	,	193	]	,
51	:	[	93570	,	197	]	,
52	:	[	102927	,	201	]	,
53	:	[	113220	,	205	]	,
54	:	[	124542	,	209	]	,
55	:	[	136996	,	214	]	,
56	:	[	150696	,	218	]	,
57	:	[	165765	,	222	]	,
58	:	[	182342	,	226	]	,
59	:	[	200576	,	230	]	,
60	:	[	210605	,	236	]	,
61	:	[	221135	,	241	]	,
62	:	[	232192	,	246	]	,
63	:	[	243801	,	251	]	,
64	:	[	255991	,	256	]	,
65	:	[	268791	,	262	]	,
66	:	[	282230	,	267	]	,
67	:	[	296342	,	272	]	,
68	:	[	311159	,	277	]	,
69	:	[	326717	,	282	]	,
70	:	[	343053	,	289	]	,
71	:	[	360205	,	294	]	,
72	:	[	378216	,	299	]	,
73	:	[	397126	,	304	]	,
74	:	[	416983	,	309	]	,
75	:	[	437832	,	315	]	,
76	:	[	459723	,	320	]	,
77	:	[	482710	,	325	]	,
78	:	[	506845	,	330	]	,
79	:	[	532187	,	335	]	,
80	:	[	558797	,	342	]	,
81	:	[	586736	,	347	]	,
82	:	[	616073	,	352	]	,
83	:	[	646877	,	357	]	,
84	:	[	679221	,	362	]	,
85	:	[	713182	,	368	]	,
86	:	[	748841	,	373	]	,
87	:	[	767562	,	378	]	,
88	:	[	786751	,	383	]	,
89	:	[	806420	,	388	]	,
90	:	[	826580	,	395	]	,
91	:	[	847245	,	403	]	,
92	:	[	868426	,	411	]	,
93	:	[	890136	,	419	]	,
94	:	[	912390	,	427	]	,
95	:	[	935200	,	437	]	,
96	:	[	958580	,	445	]	,
97	:	[	982544	,	453	]	,
98	:	[	1007108	,	461	]	,
99	:	[	1032285	,	471	]	,
    }
    
