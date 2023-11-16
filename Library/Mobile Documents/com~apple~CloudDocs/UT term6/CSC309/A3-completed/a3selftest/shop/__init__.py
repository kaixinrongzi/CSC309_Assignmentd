from .add import test_add_item
from .update import test_update_item
from .adjust import test_decrease_increase
from .delete import test_delete_item
from .total import test_total

tests = (test_add_item, test_update_item, test_decrease_increase,
         test_delete_item, test_total)