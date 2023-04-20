def even_odd_filter(**kwargs):
    if 'odd' in kwargs.keys():
        kwargs['odd'] = [n for n in kwargs['odd'] if int(n) % 2 == 1]
    if 'even' in kwargs.keys():
        kwargs['even'] = [n for n in kwargs['even'] if int(n) % 2 == 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
