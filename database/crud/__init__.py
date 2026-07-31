from .customer import (
    create_customer,
    get_customer,
    get_all_customers,
    update_customer,
    delete_customer,
)

from .vehicle import (
    create_vehicle,
    get_vehicle,
    get_all_vehicles,
    update_vehicle,
    delete_vehicle,
)

from .policy import (
    create_policy,
    get_policy,
    get_policy_by_number,
    get_all_policies,
    update_policy,
    delete_policy,
)
from .claim import (
    create_claim,
    get_claim,
    get_all_claims,
    get_claims_by_customer,
    get_claims_by_policy,
    update_claim,
    delete_claim,
)
from .ai_decision import (
    create_ai_decision,
    get_ai_decision,
    get_ai_decision_by_claim,
    get_all_ai_decisions,
    update_ai_decision,
    delete_ai_decision,
)