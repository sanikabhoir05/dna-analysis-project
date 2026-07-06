import matplotlib.pyplot as plt
genes=["Gene1","Gene2","Gene3","Gene4"]
expression=[12,20,18,30]
plt.bar(genes,expression)
plt.title("Gene Expression")
plt.show()

import matplotlib.pyplot as plt 
genes=["BRCA1","TP53","EFGR","MYC","KRAS"]
expression=[45,60,25,70,40]
plt.plot(genes,expression,marker="o")
plt.title("Cancer Gene Expression")
plt.xlabel("Genes")
plt.ylabel("Expression Level")
plt.grid()
plt.show()

import matplotlib.pyplot as plt 
genes=["A","B","C","D","E"]
healthy=[15,20,18,25,22]
treated=[12,17,15,20,18]
plt.plot(genes,healthy,marker="o",label="Healthy")
plt.plot(genes,treated,marker="s",label="Drug Treated")
plt.title("Drug Effect on Gene Expression")
plt.xlabel("Genes")
plt.ylabel("Expression")
plt.legend()
plt.grid()
plt.show()

import matplotlib.pyplot as plt 
genes=["GeneA","GeneB","GeneC","GeneD","GeneE"]
expression=[22,15,35,18,28]
plt.plot(genes,expression,marker="o")
plt.title("Graph")
plt.xlabel("Genes")
plt.ylabel("Expression")
plt.grid()
plt.show()

import matplotlib.pyplot as plt 
genes=["TP53","BRCA1","MYC","EFGR","KRAS"]
expression=[50,40,65,30,55]
plt.title("BAR")
plt.xlabel("Genes")
plt.ylabel("Expression")
plt.bar(genes,expression)
plt.show()