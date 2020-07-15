extends TextureButton

func _process(delta):
	$"../../".mousepos = get_local_mouse_position()
