# Code generated by Lark OpenAPI.

from typing import Callable, Type

from lark_oapi.event.processor import IEventProcessor
from .model.p2_corehr_contract_created_v1 import P2CorehrContractCreatedV1
from .model.p2_corehr_department_created_v1 import P2CorehrDepartmentCreatedV1
from .model.p2_corehr_department_deleted_v1 import P2CorehrDepartmentDeletedV1
from .model.p2_corehr_department_updated_v1 import P2CorehrDepartmentUpdatedV1
from .model.p2_corehr_employment_converted_v1 import P2CorehrEmploymentConvertedV1
from .model.p2_corehr_employment_created_v1 import P2CorehrEmploymentCreatedV1
from .model.p2_corehr_employment_deleted_v1 import P2CorehrEmploymentDeletedV1
from .model.p2_corehr_employment_resigned_v1 import P2CorehrEmploymentResignedV1
from .model.p2_corehr_employment_updated_v1 import P2CorehrEmploymentUpdatedV1
from .model.p2_corehr_job_change_updated_v1 import P2CorehrJobChangeUpdatedV1
from .model.p2_corehr_job_data_changed_v1 import P2CorehrJobDataChangedV1
from .model.p2_corehr_job_data_employed_v1 import P2CorehrJobDataEmployedV1
from .model.p2_corehr_offboarding_updated_v1 import P2CorehrOffboardingUpdatedV1
from .model.p2_corehr_org_role_authorization_updated_v1 import P2CorehrOrgRoleAuthorizationUpdatedV1
from .model.p2_corehr_person_created_v1 import P2CorehrPersonCreatedV1
from .model.p2_corehr_person_deleted_v1 import P2CorehrPersonDeletedV1
from .model.p2_corehr_person_updated_v1 import P2CorehrPersonUpdatedV1
from .model.p2_corehr_pre_hire_updated_v1 import P2CorehrPreHireUpdatedV1


class P2CorehrContractCreatedV1Processor(IEventProcessor[P2CorehrContractCreatedV1]):
    def __init__(self, f: Callable[[P2CorehrContractCreatedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrContractCreatedV1]:
        return P2CorehrContractCreatedV1

    def do(self, data: P2CorehrContractCreatedV1) -> None:
        self.f(data)


class P2CorehrDepartmentCreatedV1Processor(IEventProcessor[P2CorehrDepartmentCreatedV1]):
    def __init__(self, f: Callable[[P2CorehrDepartmentCreatedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrDepartmentCreatedV1]:
        return P2CorehrDepartmentCreatedV1

    def do(self, data: P2CorehrDepartmentCreatedV1) -> None:
        self.f(data)


class P2CorehrDepartmentDeletedV1Processor(IEventProcessor[P2CorehrDepartmentDeletedV1]):
    def __init__(self, f: Callable[[P2CorehrDepartmentDeletedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrDepartmentDeletedV1]:
        return P2CorehrDepartmentDeletedV1

    def do(self, data: P2CorehrDepartmentDeletedV1) -> None:
        self.f(data)


class P2CorehrDepartmentUpdatedV1Processor(IEventProcessor[P2CorehrDepartmentUpdatedV1]):
    def __init__(self, f: Callable[[P2CorehrDepartmentUpdatedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrDepartmentUpdatedV1]:
        return P2CorehrDepartmentUpdatedV1

    def do(self, data: P2CorehrDepartmentUpdatedV1) -> None:
        self.f(data)


class P2CorehrEmploymentConvertedV1Processor(IEventProcessor[P2CorehrEmploymentConvertedV1]):
    def __init__(self, f: Callable[[P2CorehrEmploymentConvertedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrEmploymentConvertedV1]:
        return P2CorehrEmploymentConvertedV1

    def do(self, data: P2CorehrEmploymentConvertedV1) -> None:
        self.f(data)


class P2CorehrEmploymentCreatedV1Processor(IEventProcessor[P2CorehrEmploymentCreatedV1]):
    def __init__(self, f: Callable[[P2CorehrEmploymentCreatedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrEmploymentCreatedV1]:
        return P2CorehrEmploymentCreatedV1

    def do(self, data: P2CorehrEmploymentCreatedV1) -> None:
        self.f(data)


class P2CorehrEmploymentDeletedV1Processor(IEventProcessor[P2CorehrEmploymentDeletedV1]):
    def __init__(self, f: Callable[[P2CorehrEmploymentDeletedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrEmploymentDeletedV1]:
        return P2CorehrEmploymentDeletedV1

    def do(self, data: P2CorehrEmploymentDeletedV1) -> None:
        self.f(data)


class P2CorehrEmploymentResignedV1Processor(IEventProcessor[P2CorehrEmploymentResignedV1]):
    def __init__(self, f: Callable[[P2CorehrEmploymentResignedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrEmploymentResignedV1]:
        return P2CorehrEmploymentResignedV1

    def do(self, data: P2CorehrEmploymentResignedV1) -> None:
        self.f(data)


class P2CorehrEmploymentUpdatedV1Processor(IEventProcessor[P2CorehrEmploymentUpdatedV1]):
    def __init__(self, f: Callable[[P2CorehrEmploymentUpdatedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrEmploymentUpdatedV1]:
        return P2CorehrEmploymentUpdatedV1

    def do(self, data: P2CorehrEmploymentUpdatedV1) -> None:
        self.f(data)


class P2CorehrJobChangeUpdatedV1Processor(IEventProcessor[P2CorehrJobChangeUpdatedV1]):
    def __init__(self, f: Callable[[P2CorehrJobChangeUpdatedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrJobChangeUpdatedV1]:
        return P2CorehrJobChangeUpdatedV1

    def do(self, data: P2CorehrJobChangeUpdatedV1) -> None:
        self.f(data)


class P2CorehrJobDataChangedV1Processor(IEventProcessor[P2CorehrJobDataChangedV1]):
    def __init__(self, f: Callable[[P2CorehrJobDataChangedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrJobDataChangedV1]:
        return P2CorehrJobDataChangedV1

    def do(self, data: P2CorehrJobDataChangedV1) -> None:
        self.f(data)


class P2CorehrJobDataEmployedV1Processor(IEventProcessor[P2CorehrJobDataEmployedV1]):
    def __init__(self, f: Callable[[P2CorehrJobDataEmployedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrJobDataEmployedV1]:
        return P2CorehrJobDataEmployedV1

    def do(self, data: P2CorehrJobDataEmployedV1) -> None:
        self.f(data)


class P2CorehrOffboardingUpdatedV1Processor(IEventProcessor[P2CorehrOffboardingUpdatedV1]):
    def __init__(self, f: Callable[[P2CorehrOffboardingUpdatedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrOffboardingUpdatedV1]:
        return P2CorehrOffboardingUpdatedV1

    def do(self, data: P2CorehrOffboardingUpdatedV1) -> None:
        self.f(data)


class P2CorehrOrgRoleAuthorizationUpdatedV1Processor(IEventProcessor[P2CorehrOrgRoleAuthorizationUpdatedV1]):
    def __init__(self, f: Callable[[P2CorehrOrgRoleAuthorizationUpdatedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrOrgRoleAuthorizationUpdatedV1]:
        return P2CorehrOrgRoleAuthorizationUpdatedV1

    def do(self, data: P2CorehrOrgRoleAuthorizationUpdatedV1) -> None:
        self.f(data)


class P2CorehrPersonCreatedV1Processor(IEventProcessor[P2CorehrPersonCreatedV1]):
    def __init__(self, f: Callable[[P2CorehrPersonCreatedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrPersonCreatedV1]:
        return P2CorehrPersonCreatedV1

    def do(self, data: P2CorehrPersonCreatedV1) -> None:
        self.f(data)


class P2CorehrPersonDeletedV1Processor(IEventProcessor[P2CorehrPersonDeletedV1]):
    def __init__(self, f: Callable[[P2CorehrPersonDeletedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrPersonDeletedV1]:
        return P2CorehrPersonDeletedV1

    def do(self, data: P2CorehrPersonDeletedV1) -> None:
        self.f(data)


class P2CorehrPersonUpdatedV1Processor(IEventProcessor[P2CorehrPersonUpdatedV1]):
    def __init__(self, f: Callable[[P2CorehrPersonUpdatedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrPersonUpdatedV1]:
        return P2CorehrPersonUpdatedV1

    def do(self, data: P2CorehrPersonUpdatedV1) -> None:
        self.f(data)


class P2CorehrPreHireUpdatedV1Processor(IEventProcessor[P2CorehrPreHireUpdatedV1]):
    def __init__(self, f: Callable[[P2CorehrPreHireUpdatedV1], None]):
        self.f = f

    def type(self) -> Type[P2CorehrPreHireUpdatedV1]:
        return P2CorehrPreHireUpdatedV1

    def do(self, data: P2CorehrPreHireUpdatedV1) -> None:
        self.f(data)
