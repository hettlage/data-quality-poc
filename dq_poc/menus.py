from dq_poc.errors import NotFoundException

# secondary menus
#
# Each menu is described by a list of tuples containing the title to use in the menu, the slug to use in the URL
# and the module for the page content.

_telescope_menu = (
    ('Weather', 'weather', 'content.telescope.weather'),
    ('Seeing', 'seeing', 'content.telescope.seeing')
)

_salticam_menu = (
    ('Bias Levels', 'bias', 'content.salticam.bias'),
    ('Throughput', 'throughput', 'content.salticam.throughput')
)

_rss_menu = (
    ('Bias Levels', 'bias', 'content.rss.bias'),
    ('Throughput', 'throughput', 'content.rss.throughput')
)

# primary menu
#
# Each list item is a tuple of the title to use in the menu, the slug for the URL and the secondary menu

_primary_menu = (
    ('Telescope', 'telescope', _telescope_menu),
    ('Salticam', 'salticam', _salticam_menu),
    ('RSS', 'rss', _rss_menu)
)


def primary_menu():
    return _primary_menu


def primary_menu_item(url):
    slugs = url.split('/')
    if len(slugs) == 0 or not slugs[0]:
        return _primary_menu[0]
    slug = slugs[0]

    menu_item = next(filter(lambda item: item[1] == slug, _primary_menu), None)

    if menu_item is None:
        raise NotFoundException('The requested primary menu item does not exist')

    return menu_item


def secondary_menu(primary_menu_item):
    pass
