extends Control

var hitbox = Rect2(0,0,0,0)


func _draw():
	draw_rect(hitbox, Color.blue, false, 3, false)
	
	
func _process(delta):
	update()
