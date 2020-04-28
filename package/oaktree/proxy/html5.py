#!/usr/bin/env pyton3

from oaktree.common import UniversalWriter

class XmlProxy() :
	def __init__(self, indent='\t', standalone="no", fragment=False, stylesheet=None) :
		self.indent = indent
		self.standalone = standalone
		self.fragment = fragment
		self.stylesheet = None

		self.fid = None

	def save(self, tree, output=None) :
		self.uwriter = UniversalWriter(output)
		w = self.uwriter.open()
		if not self.fragment :
			w(f'<?xml version="1.0" encoding="UTF-8" standalone="{self.standalone}"?>\n')
		self._compose(tree, w, self.indent)
		return self.uwriter.close()

	def _compose(self, node, w, indent, depth=0) :
		s = list()
		# tag
		t = f"{node.space}:" if node.space else ''
		t += f"{node.tag}"
		s.append(t)
		# ident
		if node.ident :
			s.append(f'id="{node.ident}"')
		# style
		if node.style :
			s.append('class="{0}"'.format(','.join(node.style)))
		# pos is not used in xml
		# nam
		for k in node.nam :
			s.append(f'{k}="{node.nam[k]}"')
		# flag
		for k in node.flag :
			v = 'false' if k.endswith('~') else 'true'
			s.append(f'{k}="{v}"')

		i = (self.indent * (depth)) if self.indent else ''
		n = '\n' if self.indent else ''

		w(i + '<' + ' '.join(s) + ('>' if node.sub else ' />') + n)

		for k in node.sub :
			if isinstance(k, str) :
				w(k + n)
			else :
				self._compose(k, w, indent, depth+1)
		if node.sub :
			w(f'{i}</{t}>{n}')


if __name__ == '__main__' :
	import oaktree

	u = oaktree.Leaf('tutu', nam={'vache': "meuh", 'canard':"coincoin"}, style="animal")
	g = u.grow('toto', flag="eurhm")
	g.add_text("bizarre")
	g.grow('tata')
	g.add_text("vouzavé dit bizarre")

	x = XmlProxy()
	print(x.save(u))
