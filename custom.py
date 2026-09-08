# Оптимизация размера исполняемого файла
optimize = "size"
debug_symbols = "no"

# Отключаем 3D подсистему и тяжелые модули
disable_3d = "yes"
#disable_advanced_gui = "yes"

# Отключаем модули, которые не нужны в 2D игре
#module_basis_universal_enabled = "no"
#module_msdfgen_enabled = "no"  # если не используете MSDF шрифты
module_openxr_enabled = "no"
module_webxr_enabled = "no"
module_mobile_vr_enabled = "no"
module_camera_enabled = "no"
module_lightmapper_rd_enabled = "no"
module_navigation_enabled = "no" # если не нужен поиск путей
