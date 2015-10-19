import searchengine
#crawler = searchengine.crawler('searchindex.db')
#crawler.createindextables()

#pages = ['https://github.com/']
#crawler.crawl(pages)
e = searchengine.searcher('searchindex.db')
#e.getmatchrows('github help')
e.query('github  help')

#crawler.calculatepagerank()
#cur = crawler.con.execute('select * from pagerank order by score desc')
#for i in range(3):
#	print cur.next()
#print e.geturlname(1)
