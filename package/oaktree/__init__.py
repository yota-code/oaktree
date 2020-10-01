#!/usr/bin/env python3

def _walk_limit(start=None, stop=None, _depth=0) :
        return (
                (start is None or _depth >= start) and
                (stop is None or _depth < stop)
        )

class Leaf() :

	def __init__(self, tag=None, ident=None, space=None, pos=None, nam=None, flag=None, style=None) :

		self.tag = tag
		self.ident = ident
		self.space = space

		if isinstance(flag, str) :
			flag = [flag,]

		if isinstance(style, str) :
			style = [style,]

		self.pos = list(pos) if pos else list()
		self.nam = dict(nam) if nam else dict()
		self.flag = set(flag) if flag else set()
		self.style = set(style) if style else set()

		self.sub = list()
		self.parent = None

	def parent_n(self, n=1) :
		if n == 1 :
			return self.parent
		else :
			return self.parent.parent_n(n-1)
		
	def __str__(self) :
		return f"<{self.tag}>"
		
	def __repr__(self) :
		return f"<{self.tag}>"

	def iterleaf(self) :
		""" iter in sub-Leaf only """
		return (i for i in self.sub if isinstance(i, Leaf))

	# __iter__ == self.iterleaf

	@property
	def root(self) :
		root = self
		while root.parent is not None :
			root = root.parent
		return root

	@property
	def is_root(self) :
		return self.parent is None

	def down_to(self, tag, ident=None) :
		""" return the first leaf in sub, matching the tag, or the tag and the ident 
		TODO: replace all calls to pick_tag_ident et pick_tag par down
		"""
		for n_sub in self :
			if n_sub.tag == tag :
				if ident is None :
					return n_sub
				else :
					if n_sub.ident == ident :
						return n_sub
		raise KeyError("no ident={0}{1} in {2}".format(type(ident), ident,
			", ".join("{0}{1}".format(type(n.ident), repr(n.ident)) for n in self))
		)

	def attach(self, * other_list) :
		""" attach either a Leaf, or something else """
		for other in other_list :
			if isinstance(other, Leaf) :
				other.parent = self
				self.sub.append(other)
			else :
				self.sub.append(other)
		return other_list[0]

	def grow(self, tag=None, ident=None, space=None, pos=None, nam=None, flag=None, style=None, cls=None) :
		""" make a new Leaf and append it, if you want to subclass use _cls """
		
		if cls is None :
			cls = Leaf
			if space is None :
				space = self.space

		n_leaf = cls(tag, ident, space, pos, nam, flag, style)
		self.attach(n_leaf)
		return n_leaf

	def walk(self, mode="depth") :
		if mode == "depth" :
			fn = self.walk_depth
		elif mode == "breadth" :
			fn = self.walk_breadth
		else :
			raise ValueError
		yield from fn()

	def walk_depth(self, start=None, stop=None, _depth=0) :
		if _walk_limit(start, stop, _depth) :
			yield self
		for child in self.iterleaf() :
			yield from child.walk_depth(start, stop, _depth+1)

	def walk_breadth(self, start=None, stop=None, _depth=0) :
		if _depth == 0 and _walk_limit(start, stop, _depth) :
			yield self
		for n_sub in self.iterleaf() :
			if _walk_limit(start, stop, _depth+1) :
				yield n_sub
		for n_sub in self.iterleaf() :
			yield from n_sub.walk_breadth(start, stop, _depth+1)
			
	def walk_into(self, depth=0) :
		for n_sub in self.sub :
			yield depth, n_sub
			if isinstance(n_sub, Leaf) :
				yield from n_sub.walk_into(depth+1)
			
	def add_text(self, txt) :
		""" append a string to the Leaf, return self """
		if isinstance(txt, str) :
			#if txt.strip() != '' :
			self.sub.append(txt)
		else :
			raise ValueError("append(): first argument must be a string")
		return self

	def set_text(self, txt) :
		""" existing children are cleared, the only child is a text """
		self.sub = [str(txt),]
		return self

	def find_ident(self, ident, walk_mode="depth") :
		""" return the first leaf whose ident match """
		for n in self.walk_depth() :
			if not isinstance(n, Leaf) :
				continue
			if n.ident == ident :
				return n

	@property
	def ancestor_lst(self) :
		""" return a list of all ancestors up to the root """
		a_lst = list()
		u = self

		a_lst.append(u)
		while u.parent is not None :
			u = u.parent
			a_lst.append(u)

		return a_lst[::-1]

	def ancestor(self, depth) :
		""" if depth is negatives is pick up """
		pass