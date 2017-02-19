from abc import ABCMeta, abstractmethod, abstractproperty

class Base(object):
	__metaclass__ = ABCMeta

	DESCRIPTION = abstractproperty
	NAME = NotImplemented

	@abstractproperty
	def definethisproperty(self):
		"""Nothing Required Here"""

	@property
	def definedproperty(self):
		return "This is a property"

	@abstractmethod
	def definethismethod(self):
		pass

	def definedmethod(self):
		return "This is a method"


class SubClass(Base):
	DESCRIPTION = 'No longer abstract'

	def definethisproperty(self):
		return 'No longer abstract property'

	def definethismethod(self):
		return 'No longer abstract method'

def main():
	try:
		b = Base() # Will throw a TypeError as trying to instantiate an abstract class
	except TypeError:
		s = SubClass()
		assert s.NAME is NotImplemented

if __name__ == '__main__':
	main()