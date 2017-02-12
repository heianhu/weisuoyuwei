# -*- coding: utf-8 -*-
import sqlite3, Queue, json
db = sqlite3.connect("chengyu.db")
cur = db.cursor()
cur.execute("SELECT * FROM cy")
list = cur.fetchall()
dict = []
cnt = 0
graph = {}
for i in list:
	if i[1][3] not in graph: graph[i[1][3]] = []
	graph[i[1][3]] += [(i[1][0], cnt)]
	dict.append(i[1])
	cnt += 1
open("dict.js","w+").write("var dict = " + json.dumps(dict))

for target, pinyin in [(u"为", "wei"), (u"忍", "ren"), (u"防", "fang")]:
	next = {}
	dist = {}
	q = Queue.Queue()
	q.put(target)
	dist[target] = 0
	while not q.empty():
		cur = q.get()
		if cur in graph:
			for i in graph[cur]:
				if i[0] not in dist:
					q.put(i[0])
					dist[i[0]] = dist[cur] + 1
					next[i[0]] = i[1]
	open("next_" + pinyin + ".js","w+").write("var next = " + json.dumps(next))
