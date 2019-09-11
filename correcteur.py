import sys
import getopt

class Correction():
	"""docstring for Correction"""
	def __init__(self, chemin):
		self.chemin = chemin
		self.p_init = [] # phrases avec \n sans tenir compte des points
		self.p_bon = [] # phrases en tenant compte de tout
		self.p_corrigee = []
		self.phr_avec_err = 0
		self.phrases()
		self.correct = self.corriger()

	def phrases(self):
		with open(self.chemin, "r") as ch:
			self.p_init = ch.readlines()

		for p in self.p_init:
			self.p_bon.extend(p.split("."))

	def corriger(self):
		pos = 0
		correct = [] # nouvelle liste des phrases corrigées
		while pos < len(self.p_bon):#itération par phrase
			phrase = self.p_bon[pos]
			# 2 variables pour collecter les position des parentheses
			# un pour les paratheses ouvrantes l'autre les fermentes
			pos_err_ferm, pos_err_ouvr = [], [] 
			for i, char in enumerate(phrase):#iteration par caractere
				if char == "(":
					#par defaut une parenthese ouvrante est un erreur
					pos_err_ouvr.append(i)

				if char == ")" :
					# si on retrouve un femente c'est qu'elle ferme la derniere
					# ouvrante. Ainsi la derniere dans la liste des ouvrantes
					# ainsi cette ouvrante est retirée de la liste des érronées. 

					# Si tel n'est pas les cas, la fermente ne ferme rien, donc
					# c'est elle l'erreur. elle mise dans les fermantes erronée
					if pos_err_ouvr:
						pos_err_ouvr.pop()
					else:
						pos_err_ferm.append(i)
			# la liste des fermantes qui ne ferment rien tout comme celle
			# des ouvrantes non fermées sont fussionées dans la liste des 
			# positions contenant les erreurs nomée "pos_err"
			pos_err = pos_err_ferm + pos_err_ouvr
			if(pos_err):
				self.phr_avec_err+=1
				# transormation de la phrase qui vient d'etre traité en
				# en list de chars. pour remplacer tout ses positions
				# contenants les erreurs par le mot "!erreur ".
				# en fin la liste des char est retransformée en string
				list_char = [x for x in phrase]
				for x in pos_err:
					list_char[x] = "!erreur "
				phrase = "".join(list_char)
			correct.append(phrase)
			pos+=1
		return correct

	def __str__(self):
		a=f"nombre de phrases {len(self.p_bon)}\n\
nombre de phrases contenant des erreurs {self.phr_avec_err}\n\n"
		for x in self.correct:
			# si l'element courant est se termin par un saut de ligne
			# on l'ajouter automatiquement, sinon on ajoute un point
			if x[-1] == "\n":
				a+=x
			else:
				a = a+x+"."
		return a

if __name__ == '__main__':
	chemin, chemout = '',''
	try:
		opts, args = getopt.getopt(sys.argv[1:], "i:o:", ["input=", "output="])
		for opt, arg in opts:
			if opt in ["-i", "--input"]:
				chemin = arg
			elif opt in ["-o", "--output"]:
				chemout = arg
	except:
		print("la systaxe est:\ncorrecteur.py -i input_file.txt -o output_file.txt")
		sys.exit(0)
	else:
		correction = Correction(chemin)
		# print(correction, file=chemout)
		with open(chemout, "w") as out:
			out.write(str(correction))
