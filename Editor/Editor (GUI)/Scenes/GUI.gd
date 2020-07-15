extends Node2D

onready var camera_check = $Panel/Game/TabContainer/SPRITES/Sprites/Title/MOVECAMERA
onready var sprite_move = $Panel/Game/TabContainer/SPRITES/Sprites/Title/MOVE

onready var XLabel = $Panel/Game/TabContainer/SPRITES/Sprites/Info/Xpos
onready var YLabel = $Panel/Game/TabContainer/SPRITES/Sprites/Info/Ypos
onready var SpriteNode = $Panel/Game/TabContainer/SPRITES/Sprites/SpriteViewport/Viewport/Picture
onready var FrameID = $Panel/Game/TabContainer/SPRITES/Sprites/Frames/FrameID

onready var FrameData = load("res://Code/Data.gd")

var sprite_id = 0

func _ready():
	FrameID.text = "000"



func _on_LOADSPRITE_pressed():
	$SpriteImport.show()


func _on_SpriteImport_files_selected(paths):
	for id in len(paths):
		var image = ImageTexture.new()
		var frame_data = FrameData.new()
		image.load(paths[id])
		SpriteNode.get_node("Sprite").frames.add_frame("frames", image)
		var size = SpriteNode.get_node("Sprite").frames.get_frame_count("frames")
		frame_data.filename = paths[id].get_file()
		var sprite_size = SpriteNode.get_node("Sprite").frames.get_frame("frames", size-1).get_size()
		sprite_size = Vector2(0, -sprite_size.y/2)
		frame_data.pos = sprite_size
		Variables.sprite_data.sprites.append(frame_data)
	ResetSpriteView(0)

func ResetSpriteView(id):
	SpriteNode.get_node("Sprite").frame = id
	var pos = Variables.sprite_data.sprites[id].pos
	SpriteNode.get_node("Sprite").position = pos
	FrameID.text = str(id)
	XLabel.text = str(pos.x)
	YLabel.text = str(pos.y)

func _on_NextFrame_pressed():
	var size = SpriteNode.get_node("Sprite").frames.get_frame_count("frames")
	if sprite_id + 1 < size:
		sprite_id += 1
		ResetSpriteView(sprite_id)


func _on_LastFrame_pressed():
	if sprite_id > 0:
		sprite_id -= 1
		ResetSpriteView(sprite_id)
