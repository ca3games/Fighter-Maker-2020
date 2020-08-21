extends HBoxContainer

func _ready():
	$Direction.add_item("Neutral")
	$Direction.add_item("Left")
	$Direction.add_item("DownLeft")
	$Direction.add_item("Down")
	$Direction.add_item("DownRight")
	$Direction.add_item("Right")
	$Direction.add_item("UpRight")
	$Direction.add_item("Up")
	$Direction.add_item("UpLeft")
