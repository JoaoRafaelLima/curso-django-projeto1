from math import ceil


def make_pagination_range(
    page_range,
    qty_pages,
    current_page):
    middle_page = ceil(qty_pages/2)
    start_range = current_page - middle_page
    stop_range = current_page + middle_page
    start_range_offset = abs(start_range) if start_range < 0 else 0
    if start_range < 0:
        start_range = 0
        stop_range+= start_range_offset
    return page_range[start_range:stop_range]