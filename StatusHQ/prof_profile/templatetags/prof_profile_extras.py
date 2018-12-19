# -*- coding: utf-8 -*-
# @Author: Charlie Gallentine
# @Date:   2018-12-18 21:55:43
# @Last Modified by:   Charlie Gallentine
# @Last Modified time: 2018-12-18 22:11:00
from django import template

register = template.Library()

@register.filter
def top_num(section, num):
	# int(num) -= 1
	return list(section.profileentry_set.all())[:int(num)]