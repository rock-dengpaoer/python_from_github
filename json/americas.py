import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Center, and South America'

wm.add('North America', {'ca': 34126000, 'mx': 309349000, 'us': 1234234566})
wm.add('Center America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('na_populations.svg')
