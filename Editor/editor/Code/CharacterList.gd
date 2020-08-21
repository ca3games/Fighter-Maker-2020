extends HBoxContainer

func _ready():
	Test()

func Test():
	for x in range(100):
		$VBoxContainer2/ItemList.add_item("Character " + str(x), null, true)
