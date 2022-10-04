#!/usr/bin/env python3

import oaktree

from oaktree.common import UniversalWriter

class BraketProxy() :
	def __init__(self, indent='\t') :
		self.indent = indent

	def save(self, tree, output=None) :
		uw = UniversalWriter(output)
		with uw as (u, w) :
			self.compose(tree, w)
		return uw.output

	def compose(self, n, w, d=0) :
		self._compose_header(n, w, d)
		for k in n.sub :
			if isinstance(k, oaktree.Leaf) :
				self.compose(k, w, d+1)
			elif isinstance(k, str) :
				txt = k.replace('\t', '\\t').replace('\n', '\\n')
				w(f'{self.indent * (d+1)}{repr(txt)}\n')
			else :
				w(f'!!! {k}')
				#raise ValueError(f'{k} {type(k)}')
		w(f'{self.indent * d}>\n')

	def _compose_header(self, n, w, d) :
		stack = list()
		stack.append(f'{self._compose_header_space(n)}{n.tag}{self._compose_header_ident(n)}')
		for k in n.pos :
			stack.append(f'{{{k}}}')
		for k in sorted(n.nam) :
			stack.append(f'{k}{{{n.nam[k]}}}')
		for k in n.flag :
			stack.append(f'!{k}')
		for k in n.style :
			stack.append(f'@{k}')
		w(f'{self.indent * d}<{" ".join(stack)}|\n')

	def _compose_header_space(self, n) :
		if n.space is None :
			return ''
		else :
			return f'{n.space}.'

	def _compose_header_ident(self, n) :
		if n.ident is None :
			return ''
		else :
			return f'#{n.ident}'
