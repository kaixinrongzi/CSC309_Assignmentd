from .first import test_first_page
from .like import test_like_simple, test_like_hard
from .all import test_all_pages
from .last import test_no_more_pages

tests = ( 
    test_first_page, test_like_simple, test_all_pages, test_no_more_pages,
    test_like_hard,
)