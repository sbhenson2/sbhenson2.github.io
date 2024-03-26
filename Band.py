import random

Adj = "attractive"," bald"," beautiful"," chubby"," clean"," dazzling"," drab"," elegant"," fancy"," fit"," flabby"," glamorous"," gorgeous"," handsome"," long"," magnificent"," muscular"," plain"," plump"," quaint"," scruffy"," shapely"," short"," skinny"," stocky"," ugly"," unkempt"," unsightly"," aggressive"," agreeable"," ambitious"," brave"," calm"," delightful"," eager"," faithful"," gentle"," happy"," jolly"," kind"," lively"," nice"," obedient"," polite"," proud"," silly"," thankful"," victorious"," witty"," wonderful"," zealous"," angry"," bewildered"," clumsy"," defeated"," embarrassed"," fierce"," grumpy"," helpless"," itchy"," jealous"," lazy"," mysterious"," nervous"," obnoxious"," panicky"," pitiful"," repulsive"," scary"," thoughtless"," uptight"," worried"," broad"," chubby"," crooked"," curved"," deep"," flat"," high"," hollow"," low"," narrow"," refined"," shallow"," skinny"," square"," steep"," straight"," wide"
Noun = "truth"," faith"," affordable"," joy"," wonder"," pleasure"," friendly"," despair"," cheap"," jadedness"," hatred"," dislike"," crony person"," animal"," vehicle"," guest"," house"," building"," colleague woman"," man"," child"," teacher"," home"," school"," hospital"," park"," table"," chair"," car"," computer"," love"," anger"," happiness"," fear book"," table"," chair"," car"," tree"

Adj_len = len(Adj)
Adj_index = random.randint(0, Adj_len-1)
print(Adj[Adj_index])

N_len = len(Noun)
N_index = random.randint(0, N_len-1)
print(Noun[N_index])