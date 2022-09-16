from .auth import authUrls
from .category import categoryURL
from .airline import airlineURL
from .status import statusURL
from .cargo import cargoURL
from .booking import bookingURL
from .car import carURL
from .cancel import cancelURL
from .branch import branchURL

urlpatterns=authUrls+categoryURL+airlineURL+statusURL+cargoURL+bookingURL+carURL+cancelURL+branchURL