import abc

class BaseWSGIContainer(object):
	__metaclass__ = abc.ABCMeta

	DESCRIPTION = abc.abstractproperty

	@abc.abstractproperty
	def name(self):
		pass

	@abc.abstractmethod
	def send_request(self):
		"""Should be implemented by subclasses"""