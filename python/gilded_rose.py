# -*- coding: utf-8 -*-

def minmax(low, high, value):
	min(max(low, value), high)

class GildedRose(object):
	self.special_items = ["Sulfuras, Hand of Ragnaros"]
	self.aging_items = ["Aged Brie", "Backstage passes"]

	def __init__(self, items):
		self.items = items

	def update_quality(self):
		for item in self.items:
    		if item.name in self.special_items:
				self.update_special_item(item)
			elif [1 for aging_item in self.aging_items if item in aging_item]:
				self.update_aging_item(item)
			else:
				self.update_normal_item(item)
	#     if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
	#         if item.quality > 0:
	#             if item.name != "Sulfuras, Hand of Ragnaros":
	#                 item.quality = item.quality - 1
	#     else:
	#         if item.quality < 50:
	#             item.quality = item.quality + 1
	#             if item.name == "Backstage passes to a TAFKAL80ETC concert":
	#                 if item.sell_in < 11:
	#                     if item.quality < 50:
	#                         item.quality = item.quality + 1
	#                 if item.sell_in < 6:
	#                     if item.quality < 50:
	#                         item.quality = item.quality + 1
	#     if item.name != "Sulfuras, Hand of Ragnaros":
	#         item.sell_in = item.sell_in - 1
	#     if item.sell_in < 0:
	#         if item.name != "Aged Brie":
	#             if item.name != "Backstage passes to a TAFKAL80ETC concert":
	#                 if item.quality > 0:
	#                     if item.name != "Sulfuras, Hand of Ragnaros":
	#                         item.quality = item.quality - 1
	#             else:
	#                 item.quality = item.quality - item.quality
	#         else:
	#             if item.quality < 50:
	#                 item.quality = item.quality + 1

	def update_special_item(self, item):
		if item.name == "Sufuras, Hand of Ragnaros":
			item.quality = 80
			pass
	def update_aging_item(self, item):
		conjured = 1 + "conjured" in item.name.lower()
		expired = 1 + item.sell_in <= 0
		if "Aged Brie" in item.name:
			item.quality += conjured * expired * 1
			item.quality  = minmax(0, 50, item.quality)
			item.sell_in -= 1

		elif "Backstage passes" in item.name:
			if sell_in  > 10:
				increaseby = 1
			elif sell_in > 3:
				increaseby = 2
			elif sellin > 0:
				increaseby = 3
			if sellin <= 0:
				item.quality = 0
				sellin -= 1
				return

			# handle the increases here
			sellin -= 1
			pass
		pass
	def update_normal_item(self, item):
		pass
class Item:
    def __init__(self, name, sell_in, quality):
	self.name = name
	self.sell_in = sell_in
	self.quality = quality

    def __repr__(self):
	return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
