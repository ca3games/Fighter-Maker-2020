extends Node2D

onready var ROOT = $"../../../../../../../../"

var move = false
var speed_drag = 1
var move_camera = false
var root_click = Vector2.ZERO
var mousepos = Vector2.ZERO

func _input(event):
	if move:
		if event is InputEventMouseMotion:
			if Input.is_action_pressed("MOUSE DRAG"):
				var speed = (event.relative.normalized() * speed_drag)
				$Sprite.position += speed
				Variables.sprite_data.sprites[ROOT.sprite_id].pos += speed
				var pos = $Sprite.position
				ROOT.YLabel.text = str(int(pos.y))
				ROOT.XLabel.text = str(int(pos.x))
	
	if event is InputEventMouseMotion:
			if Input.is_action_pressed("MOUSE DRAG"):
				$Camera/BODY.hitbox = Rect2(root_click, mousepos - root_click)
				print($Camera/BODY.hitbox)
	
	if move_camera:
		if event is InputEventMouseMotion:
			if Input.is_action_pressed("MOUSE DRAG"):
				$Camera.position += event.relative.normalized() * speed_drag


func _on_MOVE_pressed():
	move = !move
	move_camera = false
	ROOT.camera_check.pressed = false

func _on_MOVECAMERA_pressed():
	move_camera = !move_camera
	move = false
	ROOT.sprite_move.pressed = false


func _on_MouseClick_button_down():
	root_click = mousepos
