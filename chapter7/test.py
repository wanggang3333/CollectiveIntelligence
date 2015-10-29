import treepredict
import zillow
#tree = treepredict.buildtree(treepredict.my_data)
#treepredict.printtree(tree)
#treepredict.drawtree(tree, jpeg = 'treeview.jpg')
#print treepredict.classify(['(direct)', 'USA', 'yes', 5], tree)
#treepredict.prune(tree, 1)
#treepredict.printtree(tree)
#print treepredict.mdclassify(['google', 'None', 'yes', None], tree)
housedata = zillow.getpricelist()
housetree = treepredict.buildtree(housedata,scoref = treepredict.variance)
treepredict.drawtree(housetree, jpeg = 'housetree.jpg')