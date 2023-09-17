site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {product} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {product}',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def site_constructor(site, counter, site_quantity):
    if counter < site_quantity:
        product_name = input('Введите название продукта для нового сайта: ')
        site['html']['head']['title'] = 'Куплю/продам {product} недорого'.format(product=product_name)
        site['html']['body']['h2'] = 'У нас самая низкая цена на {product}'.format(product=product_name)
        counter += 1
        print(f'Сайт для {product_name}:')
        print('site =', site)
        site_constructor(site, counter, site_quantity)


site_quantity = int(input('Сколько сайтов: '))
counter = 0
site_constructor(site, counter, site_quantity)
