# D.O.T. - DevOps Tool
## One tool to rule them all, one tool to find them,
## One tool to bring them all and in the darkness bind them ...

### Developed by: William Brubaker (noncreature0714@gmail.com)
### Github: https://github.com/NonCreature0714/dot

## What is D.O.T.?

D.O.T. (or dot) is my response to the bredth of tools and services out there for DevOps, configuration management, security, and troubleshooting. It is an abstraction on top of many other tools, and intelligently incorporates necessary packages by "unlocking" them when they are called. This means D.O.T. starts "locked," and must be unlocked, like a dungeon.

Put plainly, D.O.T. is a domain specific (only the realm of DevOps) package manager and doctor; and may be thought of as a way to alias normally very long commands for pipelining, administratrion, and _troubleshooting_.

## Who is this for?
***Everyone!*** Everyone, that is, who is trying to practice DevOps or just wants less of a headache getting a project off the ground and running smoothly. So this is for system administrators, developers, network engineers, configuration managers, Site Reliability Engineers... Really, it's for anyone who is trying to run their team more efficiently.

# How is this code organized?

This is organized like so:

 - main.py : program entry point
 - under `lib/`
 	- dev/ : dev directory, for dev related tools, services, etc.
	- ops/ : ops directory, for ops related tools, services, etc.
 	- devops/ : a directory for things which don't quite fit cleanly into dev or ops, like configuration management.

## So, what are "dev" things?

Dev things are those "things" which a developer would do on any given day, like:
 - Use Git
 - install a package/library/module

Ops things are closer to the realm of:
 - System administration
 - Networking
 - User management

DevOps things are more like: 
 - enforcing or defining a branching plan
 - AWS configuration / managementment
