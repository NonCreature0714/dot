# D.O.T. (DevOps Tool)
# One tool to rule them all, one tool to find them,
# One tool to bring them all and in the darkness bind them ...

# Developed by: William Brubaker



# One string to make sure multithreading never interrupts the message.
basic_use_message = "Usage of D.O.T. (DevOps Tool) is:\n\ndot <command>\n\nor \n\ndot <service> <command> <arguments> <options> \n\n\tcommands:\n\t\tstatus 		:\n\t\tservice		:\n\t\tservices	:\n\t\tps\t\t:\n\t\tnetwork\t\t:\n\t\tsystem	\t:\n\t\tos\t\t:\n\t\tall\t\t: issues next command to all specified targets\n\n\tservice:\n\t\taws : \n\t\tsalt\t:"

def usage(message):
	print(message)



# usage(use_message)
