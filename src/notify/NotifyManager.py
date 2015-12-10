
class Notifyer:
	
	classes = []
	current = ''
	
	@classmethod
	def setupNewClass(cls, className):
		if className not in cls.classes:
			cls.classes.append(className)
		else:
			return None
		
		cls.current = className
		return cls
	
	@classmethod
	def newNotify(cls, mode, text):
		if cls.current in cls.classes:
			print ("%s:: %s: %s" % (cls.current, mode, text))
		else:
			return None
		
