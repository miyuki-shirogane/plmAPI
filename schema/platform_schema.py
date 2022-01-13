import sgqlc.types


platform_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AggregationFrame(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DAY', 'EVERY_DAY_RANGE', 'HOUR', 'MONTH', 'WEEK', 'WORKDAY')


class AlertStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ALERTING', 'FINISHED')


class AppKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ENTERPRISE', 'SELF', 'THIRD_PARTY')


class BomStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('IN_PROCESS', 'RELEASED', 'VERIFY')


Boolean = sgqlc.types.Boolean

class BorrowState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('IS_BORROWED', 'IS_RETURN', 'NOT_CONFIRMED')


class CalibrateMethod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('EXEMPTION', 'INSIDE', 'OUTSIDE', 'UNSET')


class CalibrateReason(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BORROWED', 'EXPIRED', 'LEASED', 'NEW', 'OTHER', 'REPAIR')


class CalibrateRepeatPeriod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('MONTH', 'YEAR')


class CalibrateResult(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BY_RESULT', 'QUALIFIED', 'UNQUALIFIED', 'UNSET')


class CalibrateState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CALIBRATING', 'DONE', 'UNSET')


class CardType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CARD', 'IMAGE', 'TAB', 'TEXT')


class CertificateState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NOT_RETURNED', 'RETURNED')


class ChangeBorrowOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'REJECT', 'SUBMIT')


class ChangeBorrowState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'NOT_PASS', 'PENDING', 'UNDER_REVIEW_BY_APPLY_FOR', 'UNDER_REVIEW_BY_BORROWED')


class ChangeBorrowTrigger(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'REJECT', 'SAVE', 'SUBMIT')


class CockpitKeyStatistic(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('AVG', 'LAST', 'SUM')


class CockpitKeyType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('REAL_TIME', 'STATISTIC')


class CombaDataType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FEE_RATE', 'FIRST_PASS_RATE', 'PRODUCTION', 'REPAIR', 'SMT', 'UNQUALIFIED')


class CombaDeviceStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('RUNNING', 'STANDBY')


class CombaGranularity(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DAILY', 'MONTHLY')


class DataType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BOOL', 'ENUM', 'FLOAT', 'INT', 'STRING')


class EamImportOption(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('INSERT_NORMAL', 'UPSERT_NORMAL')


class ElectricityPeriod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NORMAL', 'PEAK', 'SHARP', 'VALLEY')


class EmsImportOption(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('INSERT_NORMAL', 'UPSERT_NORMAL')


class EnergyTimeGranularity(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DAY', 'HOUR', 'MONTH')


class EnergyType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ELECTRICITY',)


Float = sgqlc.types.Float

class FuncType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('MAX', 'SUM')


class Granularity(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ANNUALLY', 'DAILY', 'FIVE_MINUTE', 'HOURLY', 'MINUTE', 'MONTHLY', 'WEEKLY')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class IssueAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CLOSE', 'DEAL', 'REMARK', 'REOPEN', 'TRANSFER')


class IssueCategory(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('EDUCTION', 'HELP', 'SYSTEM')


class IssueReason(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ABNORMAL_DATA', 'OTHER', 'SLOW_LOADING')


class IssueStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CLOSE', 'DEALING', 'READY')


class IssueType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ABNORMAL_DATA', 'OTHER', 'SLOW_LOADING')


class JSON(sgqlc.types.Scalar):
    __schema__ = platform_schema


class JSONString(sgqlc.types.Scalar):
    __schema__ = platform_schema


class JumpKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CURRENT_WINDOW', 'NEW_WINDOW')


class MarketAppType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ENERGY_SAVING', 'MAINTENANCE_SERVICE', 'MANUFACTURING', 'OPERATION_MANAGEMENT', 'QUALITY_CONTROL', 'RESEARCH_DESIGN', 'SAFETY_PRODUCTION', 'SUPPLY_CHAIN_MANAGEMENT', 'WAREHOUSE_AND_LOGISTICS')


class MarketConsultationType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APP', 'SOLUTION')


class MarketIssueAction(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'CLOSE', 'FOLLOW', 'REOPEN', 'TRANSFER')


class MarketIssueStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CLOSE', 'DEALING', 'READY')


class MarketSolutionType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ENERGY_SAVING', 'MAINTENANCE_SERVICE', 'MANUFACTURING', 'OPERATION_MANAGEMENT', 'QUALITY_CONTROL', 'RESEARCH_DESIGN', 'SAFETY_PRODUCTION', 'SUPPLY_CHAIN_MANAGEMENT', 'WAREHOUSE_AND_LOGISTICS')


class MaterialProperty(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BACTERIA', 'INTERMEDIATE', 'PRODUCT', 'RAW_MATERIAL')


class MeasurementObject(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY', 'ENVIRONMENTAL_PROTECTION', 'EQUIPMENT', 'FACTORY', 'INFRASTRUCTURE', 'OFFICE', 'WORKSHOP')


class NotificationKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APP', 'PLATFORM')


class OnState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ABANDONED', 'AVAILABLE', 'DEBUGGING', 'IN_USE', 'OTHER')


class OutsideCalibratePayStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PAID', 'UNDER_REVIEW')


class PermissionDataRange(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ALL', 'OWN')


class PermissionType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APP_MENU', 'FUNCTION', 'INTERFACE', 'PLATFORM_MENU')


class ProductProjectCategory(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CUSTOMIZATION', 'OPTIMIZATION', 'RESEARCH')


class ProductProjectDocumentPhase(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('PROJECT_INPUT', 'PROJECT_OUTPUT', 'TASK_OUTPUT')


class ProductProjectStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ENDED', 'IN_PROCESS', 'PENDING')


class RepeatPeriod(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DAY', 'MONTH', 'WEEK', 'YEAR')


class ResetPasswordScenario(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY_ADMIN', 'NORMAL_USER', 'PLATFORM_USER')


class ReturnState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NOT_RETURNED', 'RETURNED')


class RoleScope(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY_ADMIN', 'PLATFORM')


class RuleLevel(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('HIGH', 'LOW', 'MIDDLE')


class RuleOperator(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BETWEEN', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NEQ')


class SourceRegister(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('C', 'DB', 'I', 'M', 'Q', 'T', 'V')


class SourceType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BIT', 'BYTE', 'DWFLOAT', 'FLOAT', 'HEX', 'LONG', 'SHORT', 'STRING', 'UDWFLOAT', 'ULONG', 'USHORT', 'UWFLOAT', 'WFLOAT')


class SparePartOutboundKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('MAINTENANCE', 'OTHER', 'REPAIR')


class SparePartReceiptKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OTHER', 'PURCHASE', 'RETURN')


class SparePartWriteoffKind(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OUTBOUND', 'RECEIPT')


String = sgqlc.types.String

class TableFieldGroup(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CUSTOM', 'FIXED', 'SCROLLABLE')


class ThingBorrowOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'REJECT', 'SUBMIT')


class ThingBorrowState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'NOT_PASS', 'PENDING', 'UNDER_REVIEW_BY_APPLY_FOR', 'UNDER_REVIEW_BY_BORROWED')


class ThingBorrowTrigger(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('APPROVE', 'REJECT', 'SAVE', 'SUBMIT')


class ThingCalibrateOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'APPROVE', 'REJECT', 'SUBMIT', 'TURNTO')


class ThingCalibrateState(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CALIBRATING', 'FINISHED', 'PENDING', 'UNDER_REVIEW')


class ThingCalibrateTrigger(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'APPROVE', 'REJECT', 'SAVE', 'SUBMIT', 'TURNTO')


class ThingGroupAlterOperation(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ADD', 'REMOVE')


class ThingGroupType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DEPARTMENT', 'PERSONAL')


class ThingInspectionCreateType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BYHANDLE', 'BYSCHEDULE')


class ThingInspectionOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'FINISH', 'RESTART', 'TURNTO')


class ThingInspectionStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'INSPECTING', 'PENDING')


class ThingInspectionTrigger(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'FINISH', 'RESTART', 'SAVE', 'TURNTO')


class ThingMaintenanceCreateType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('BYHANDLE', 'BYSCHEDULE')


class ThingMaintenanceOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'APPLY_FOR_SPARE_PART', 'APPROVE', 'FINISH', 'PAUSE', 'REJECT', 'RESTART', 'TURNTO')


class ThingMaintenanceStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'MAINTAINING', 'PAUSED', 'PENDING', 'UNDER_REVIEW')


class ThingMaintenanceTrigger(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'APPROVE', 'FINISH', 'PAUSE', 'REJECT', 'RESTART', 'SAVE', 'TURNTO')


class ThingRateType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('OEE', 'OPERATION_RATE', 'PERFORMANCE_RATE', 'YIELD_RATE')


class ThingRepairOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'APPLY_FOR_SPARE_PART', 'APPROVE', 'FINISH', 'PAUSE', 'REJECT', 'RESTART', 'TURNTO')


class ThingRepairStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISHED', 'PAUSED', 'PENDING', 'REPAIRING', 'UNDER_REVIEW')


class ThingRepairTrigger(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPT', 'APPROVE', 'FINISH', 'PAUSE', 'REJECT', 'RESTART', 'SAVE', 'TURNTO')


class ThingRepairType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('NOREPAIR', 'REPAIR', 'REPAIROUTSOURCE')


class ThingStatusType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ALARM', 'OPERATION', 'SHUTDOWN', 'STANDBY')


class TicketType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('INSPECTION', 'MAINTENANCE')


class Timestamp(sgqlc.types.Scalar):
    __schema__ = platform_schema


class TypeCompaniesScenario(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY', 'CUSTOMER', 'MY_COMPANY', 'ROLE', 'SYSTEM_LOG', 'USER')


class UCCFieldType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('DATE', 'LABEL', 'MULTI_RADIO', 'RADIO', 'RANGE', 'RANGE_EXTREMUM', 'SELECT_BOX', 'SET', 'TEXT')


class UCCFiledValue(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FLOAT', 'TEXT')


class UCCScope(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY', 'PLATFORM')


class UpdateCompanyScenario(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('COMPANY', 'MY_COMPANY')


class UserOrigin(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ADDED', 'REGISTED')


class UserType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('CHANJIAO_SCHOOL_ADMIN', 'CHANJIAO_SYS_ADMIN', 'COMPANY_ADMIN', 'COMPANY_NORMAL', 'JIN_HUA_SCHOOL', 'PLATFORM_ADMIN')


class WorkerOrderOperatorType(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('FINISH', 'REMARK', 'TURN')


class WorkerOrderStatus(sgqlc.types.Enum):
    __schema__ = platform_schema
    __choices__ = ('ACCEPTING', 'FINISHED', 'UNCREATED')



########################################################################
# Input Objects
########################################################################
class ActivateUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class AdapterFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'thing_type_id')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')


class AdapterModelFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'thing_mechanism_model_code')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_mechanism_model_code = sgqlc.types.Field(String, graphql_name='thingMechanismModelCode')


class AddBomMaterialInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('bom', 'company', 'material')
    bom = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='bom')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    material = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput'))), graphql_name='material')


class AddCompanyAppsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app_ids', 'company_id')
    app_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='appIDs')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='companyID')


class AddProductTaskInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('project', 'task')
    project = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='project')
    task = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreateTaskInput'))), graphql_name='task')


class AddProjectDocumentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'phase', 'project', 'task')
    attachment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput'))), graphql_name='attachment')
    phase = sgqlc.types.Field(sgqlc.types.non_null(ProductProjectDocumentPhase), graphql_name='phase')
    project = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='project')
    task = sgqlc.types.Field('IntIDInput', graphql_name='task')


class AddProjectGroupMemberInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('member', 'project_group')
    member = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='member')
    project_group = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='projectGroup')


class AddThingBorrowDraftInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('add_sub_thing', 'code', 'company', 'department', 'expected_borrow_at', 'expected_return_at', 'thing')
    add_sub_thing = sgqlc.types.Field(Boolean, graphql_name='addSubThing')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    department = sgqlc.types.Field('IDInput', graphql_name='department')
    expected_borrow_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='expectedBorrowAt')
    expected_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='expectedReturnAt')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')


class AddThingChangeBorrowDraftInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('change_return_at', 'code', 'company', 'thing', 'thing_circulation')
    change_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='changeReturnAt')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')
    thing_circulation = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput'))), graphql_name='thingCirculation')


class AlertFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('companies', 'end_at', 'rule_level', 'search', 'start_at', 'status', 'worker_order_status')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='companies')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    rule_level = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RuleLevel)), graphql_name='ruleLevel')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AlertStatus)), graphql_name='status')
    worker_order_status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(WorkerOrderStatus)), graphql_name='workerOrderStatus')


class AlertLevelFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('companies', 'end_at', 'start_at')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='companies')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class AlertRuleListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('companies', 'rule_levels', 'search', 'thing_types')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='companies')
    rule_levels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RuleLevel)), graphql_name='ruleLevels')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='thingTypes')


class AlertRuleNameFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('alert_rule_name', 'company')
    alert_rule_name = sgqlc.types.Field(String, graphql_name='alertRuleName')
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class AppListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class AppUserListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app_codes', 'company')
    app_codes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='appCodes')
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class ApproveChangeBorrowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'opinion')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    opinion = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='opinion')


class ApproveThingBorrowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'opinion')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    opinion = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='opinion')


class ApproveThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class AppsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class AppsOmit(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_ids',)
    company_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='companyIDs')


class BIFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('aggregation', 'end', 'granularity', 'metric', 'series', 'start')
    aggregation = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='aggregation')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    granularity = sgqlc.types.Field(Granularity, graphql_name='granularity')
    metric = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='metric')
    series = sgqlc.types.Field(String, graphql_name='series')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')


class BomFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'is_released', 'product', 'project', 'search', 'task')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    is_released = sgqlc.types.Field(Boolean, graphql_name='isReleased')
    product = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='product')
    project = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='project')
    search = sgqlc.types.Field(String, graphql_name='search')
    task = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='task')


class BomMaterialFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('bom', 'company', 'is_released', 'property', 'search')
    bom = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='bom')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    is_released = sgqlc.types.Field(Boolean, graphql_name='isReleased')
    property = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MaterialProperty)), graphql_name='property')
    search = sgqlc.types.Field(String, graphql_name='search')


class BomMaterialInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('amount', 'field_data', 'material', 'proportion', 'research_unit')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    material = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='material')
    proportion = sgqlc.types.Field(Float, graphql_name='proportion')
    research_unit = sgqlc.types.Field(String, graphql_name='researchUnit')


class BusinessKnowledgeListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('business_knowledge_type_ids', 'companies', 'search')
    business_knowledge_type_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='businessKnowledgeTypeIds')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='companies')
    search = sgqlc.types.Field(String, graphql_name='search')


class BusinessKnowledgeNameFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('business_knowledge_name', 'business_knowledge_type', 'company')
    business_knowledge_name = sgqlc.types.Field(String, graphql_name='businessKnowledgeName')
    business_knowledge_type = sgqlc.types.Field('IDInput', graphql_name='businessKnowledgeType')
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class BusinessKnowledgeTypeListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('companies', 'search')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='companies')
    search = sgqlc.types.Field(String, graphql_name='search')


class BusinessKnowledgeTypeNameFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('business_knowledge_type_name', 'company')
    business_knowledge_type_name = sgqlc.types.Field(String, graphql_name='businessKnowledgeTypeName')
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class CalibrateOrganizationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class CalibrateRepeatInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('frequency', 'period')
    frequency = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='frequency')
    period = sgqlc.types.Field(sgqlc.types.non_null(CalibrateRepeatPeriod), graphql_name='period')


class CalibrateScheduleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class CalibrateScheduleRepeatInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('day_of_month',)
    day_of_month = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='dayOfMonth')


class ChangeBorrowApproveConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrowState)), graphql_name='source')


class ChangeBorrowItemListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('change_borrow',)
    change_borrow = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='changeBorrow')


class ChangeBorrowListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('applicant', 'company', 'department_of_applicant', 'department_of_manager', 'end_at', 'search', 'start_at', 'state')
    applicant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='applicant')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    department_of_applicant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='departmentOfApplicant')
    department_of_manager = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='departmentOfManager')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrowState)), graphql_name='state')


class CheckAlterDepartmentThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('children_depts', 'current_dept', 'operation', 'parent_dept', 'thing_group')
    children_depts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='childrenDepts')
    current_dept = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='currentDept')
    operation = sgqlc.types.Field(sgqlc.types.non_null(ThingGroupAlterOperation), graphql_name='operation')
    parent_dept = sgqlc.types.Field('IDInput', graphql_name='parentDept')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thingGroup')


class CockpitAggregationFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id',)
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')


class CockpitKeyFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id',)
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')


class CockpitThingListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('duration_max', 'duration_min', 'organization', 'search', 'status', 'type')
    duration_max = sgqlc.types.Field(Int, graphql_name='durationMax')
    duration_min = sgqlc.types.Field(Int, graphql_name='durationMin')
    organization = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingStatusType)), graphql_name='status')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='type')


class CombaLineDailyProductionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('date', 'end_date', 'line', 'start_date')
    date = sgqlc.types.Field(Timestamp, graphql_name='date')
    end_date = sgqlc.types.Field(Timestamp, graphql_name='endDate')
    line = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='line')
    start_date = sgqlc.types.Field(Timestamp, graphql_name='startDate')


class CombaLineFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('line',)
    line = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='line')


class CombaOrderListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='search')


class CombaOweFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_date', 'end_plan_start_date', 'search', 'start_date', 'start_plan_start_date')
    end_date = sgqlc.types.Field(Timestamp, graphql_name='endDate')
    end_plan_start_date = sgqlc.types.Field(Timestamp, graphql_name='endPlanStartDate')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_date = sgqlc.types.Field(Timestamp, graphql_name='startDate')
    start_plan_start_date = sgqlc.types.Field(Timestamp, graphql_name='startPlanStartDate')


class CompanyAdminPermissionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'permission')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')
    permission = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('IDInput')), graphql_name='permission')


class CompanyAdminUsersFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_ids', 'department_ids', 'search')
    company_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='companyIDs')
    department_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='departmentIDs')
    search = sgqlc.types.Field(String, graphql_name='search')


class CompanyAppsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id',)
    company_id = sgqlc.types.Field(ID, graphql_name='companyID')


class CompanyBIDatasourceFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class CompanyElectricityConsumptionsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'granularity', 'start_at')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(EnergyTimeGranularity), graphql_name='granularity')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class CompanyElectricityPeriodConsumptionsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'start_at')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class CompanyElectricityPriceDistributionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')


class CompanyElectricityTotalConsumptionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'start_at')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class CompanyFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_type', 'county', 'ids', 'search')
    company_type = sgqlc.types.Field('IDInput', graphql_name='companyType')
    county = sgqlc.types.Field(String, graphql_name='county')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids')
    search = sgqlc.types.Field(String, graphql_name='search')


class CompanyHistoryVaporPriceFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'start_at')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class CompanyHistoryWaterPriceFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'start_at')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class CompanyThingGroupTreeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')


class CompanyThingSpecificationLanguageFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class CompanyThingTypeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class CompanyTypeFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class CompanyVaporConsumptionsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'granularity', 'start_at')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(EnergyTimeGranularity), graphql_name='granularity')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class CompanyVaporTotalConsumptionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'start_at')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class CompanyWaterConsumptionsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'granularity', 'start_at')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(EnergyTimeGranularity), graphql_name='granularity')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class CompanyWaterTotalConsumptionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'start_at')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class ConfirmBorrowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('borrow_at', 'id', 'remark')
    borrow_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='borrowAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class ConfirmReturnInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark', 'return_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='returnAt')


class CreateAdapterKeyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('desc', 'function', 'key', 'precision', 'thing_type_id', 'type', 'unit')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    function = sgqlc.types.Field(JSON, graphql_name='function')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    thing_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingTypeId')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')


class CreateAlertRuleDetailInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('adapter_key_id', 'adapter_key_name', 'adapter_key_unit', 'duration_time', 'name', 'rule_level', 'rule_operator', 'rule_operator_params')
    adapter_key_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='adapterKeyId')
    adapter_key_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='adapterKeyName')
    adapter_key_unit = sgqlc.types.Field(String, graphql_name='adapterKeyUnit')
    duration_time = sgqlc.types.Field('DurationTimeInput', graphql_name='durationTime')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    rule_level = sgqlc.types.Field(sgqlc.types.non_null(RuleLevel), graphql_name='ruleLevel')
    rule_operator = sgqlc.types.Field(sgqlc.types.non_null(RuleOperator), graphql_name='ruleOperator')
    rule_operator_params = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ruleOperatorParams')


class CreateAlertRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('alert_rules', 'company', 'thing_type', 'things')
    alert_rules = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateAlertRuleDetailInput))), graphql_name='alertRules')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thingType')
    things = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingInput'))), graphql_name='things')


class CreateAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('avatar', 'code', 'description', 'jump_kind', 'kind', 'name', 'order', 'redirect_url', 'url', 'whether_new_client')
    avatar = sgqlc.types.Field('IDInput', graphql_name='avatar')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    description = sgqlc.types.Field(String, graphql_name='description')
    jump_kind = sgqlc.types.Field(sgqlc.types.non_null(JumpKind), graphql_name='jumpKind')
    kind = sgqlc.types.Field(sgqlc.types.non_null(AppKind), graphql_name='kind')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    order = sgqlc.types.Field(Float, graphql_name='order')
    redirect_url = sgqlc.types.Field(String, graphql_name='redirectUrl')
    url = sgqlc.types.Field(String, graphql_name='url')
    whether_new_client = sgqlc.types.Field(Boolean, graphql_name='whetherNewClient')


class CreateBusinessKnowledgeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('business_knowledge_type', 'company', 'content', 'name')
    business_knowledge_type = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='businessKnowledgeType')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateBusinessKnowledgeTypeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateCalibrateOrganizationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateCalibrateScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'department', 'is_all_department', 'is_all_thing_category', 'is_before_month_calibrate', 'is_inside_calibrate', 'is_next_month_calibrate', 'is_outside_calibrate', 'name', 'repeat', 'thing_category')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='department')
    is_all_department = sgqlc.types.Field(Boolean, graphql_name='isAllDepartment')
    is_all_thing_category = sgqlc.types.Field(Boolean, graphql_name='isAllThingCategory')
    is_before_month_calibrate = sgqlc.types.Field(Boolean, graphql_name='isBeforeMonthCalibrate')
    is_inside_calibrate = sgqlc.types.Field(Boolean, graphql_name='isInsideCalibrate')
    is_next_month_calibrate = sgqlc.types.Field(Boolean, graphql_name='isNextMonthCalibrate')
    is_outside_calibrate = sgqlc.types.Field(Boolean, graphql_name='isOutsideCalibrate')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    repeat = sgqlc.types.Field(sgqlc.types.non_null(CalibrateScheduleRepeatInput), graphql_name='repeat')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='thingCategory')


class CreateChangeBorrowApproveConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'destination', 'source', 'trigger')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='destination')
    source = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowTrigger), graphql_name='trigger')


class CreateCockpitAggregation(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end', 'frame', 'start', 'tag', 'thing_type_id')
    end = sgqlc.types.Field(String, graphql_name='end')
    frame = sgqlc.types.Field(AggregationFrame, graphql_name='frame')
    start = sgqlc.types.Field(String, graphql_name='start')
    tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tag')
    thing_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingTypeId')


class CreateCockpitKey(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('key', 'key_type', 'name', 'precision', 'thing_type_id', 'type', 'unit')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    key_type = sgqlc.types.Field(sgqlc.types.non_null(CockpitKeyType), graphql_name='keyType')
    name = sgqlc.types.Field(String, graphql_name='name')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    thing_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingTypeId')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')


class CreateCockpitTargetInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('oee', 'company', 'operation_rate', 'organization', 'performance_rate', 'timestamp', 'yield_rate')
    oee = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='OEE')
    company = sgqlc.types.Field(ID, graphql_name='company')
    operation_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='operationRate')
    organization = sgqlc.types.Field(ID, graphql_name='organization')
    performance_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='performanceRate')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    yield_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yieldRate')


class CreateCompanyAdminUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'company', 'email', 'name', 'phone')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')


class CreateCompanyBIDatasourceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'datasource')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='datasource')


class CreateCompanyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('address', 'city', 'contact', 'county', 'email', 'name', 'phone', 'province', 'type', 'uscc')
    address = sgqlc.types.Field(String, graphql_name='address')
    city = sgqlc.types.Field(String, graphql_name='city')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    county = sgqlc.types.Field(String, graphql_name='county')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    type = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='type')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')


class CreateDepartmentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'parent')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='parent')


class CreateDepositoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'factory', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    factory = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='factory')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateEamFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'length', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateEnergyGroup(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateEnergyNodeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'is_electricity', 'is_vapor', 'is_water', 'measurement_object', 'name', 'parent_id')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    is_electricity = sgqlc.types.Field(Boolean, graphql_name='isElectricity')
    is_vapor = sgqlc.types.Field(Boolean, graphql_name='isVapor')
    is_water = sgqlc.types.Field(Boolean, graphql_name='isWater')
    measurement_object = sgqlc.types.Field(sgqlc.types.non_null(MeasurementObject), graphql_name='measurementObject')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class CreateErrorTypeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateEvasionDateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'end_date', 'name', 'start_date')
    company_id = sgqlc.types.Field(Int, graphql_name='companyId')
    end_date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endDate')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    start_date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startDate')


class CreateFactoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('length', 'name')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateImageInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('length', 'name')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateInspectionMethodInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'field_data', 'name', 'thing_label')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='thingLabel')


class CreateIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachments', 'content', 'title')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='attachments')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class CreateLeapTargetInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('operation_rate', 'paused_duration', 'paused_times', 'timestamp')
    operation_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='operationRate')
    paused_duration = sgqlc.types.Field(Int, graphql_name='pausedDuration')
    paused_times = sgqlc.types.Field(Int, graphql_name='pausedTimes')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class CreateMaintenanceMethodInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'field_data', 'name', 'thing_label')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='thingLabel')


class CreateMarketAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('brief', 'cover_image', 'description', 'is_recommended', 'screenshot', 'title', 'type')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    cover_image = sgqlc.types.Field('IDInput', graphql_name='coverImage')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    screenshot = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='screenshot')
    title = sgqlc.types.Field(String, graphql_name='title')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketAppType), graphql_name='type')


class CreateMarketFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('length', 'name')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateMarketIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app', 'company_name', 'contact', 'content', 'email', 'phone', 'solution', 'type')
    app = sgqlc.types.Field('IDInput', graphql_name='app')
    company_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='companyName')
    contact = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contact')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    solution = sgqlc.types.Field('IDInput', graphql_name='solution')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketConsultationType), graphql_name='type')


class CreateMarketSolutionDetailInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('content', 'image', 'items', 'title', 'type')
    content = sgqlc.types.Field(String, graphql_name='content')
    image = sgqlc.types.Field('IDInput', graphql_name='image')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MarketCommonComponentInput')), graphql_name='items')
    title = sgqlc.types.Field(String, graphql_name='title')
    type = sgqlc.types.Field(sgqlc.types.non_null(CardType), graphql_name='type')


class CreateMarketSolutionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app', 'brief', 'cover_image', 'description', 'detail', 'is_recommended', 'title', 'type')
    app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='app')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    cover_image = sgqlc.types.Field('IDInput', graphql_name='coverImage')
    description = sgqlc.types.Field(String, graphql_name='description')
    detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CreateMarketSolutionDetailInput)), graphql_name='detail')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    title = sgqlc.types.Field(String, graphql_name='title')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketSolutionType), graphql_name='type')


class CreateMaterialCategoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name', 'property')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    property = sgqlc.types.Field(sgqlc.types.non_null(MaterialProperty), graphql_name='property')


class CreateMaterialInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('category', 'code', 'company', 'field_data', 'name', 'property', 'specification', 'unit', 'versions')
    category = sgqlc.types.Field('IntIDInput', graphql_name='category')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    property = sgqlc.types.Field(sgqlc.types.non_null(MaterialProperty), graphql_name='property')
    specification = sgqlc.types.Field(String, graphql_name='specification')
    unit = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='unit')
    versions = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='versions')


class CreateOriginalInventoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('depository', 'inventory')
    depository = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='depository')
    inventory = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='inventory')


class CreateOutsideCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('apply_for_at', 'calibrate_at', 'calibrate_organization', 'company', 'name', 'pay_at', 'pay_status')
    apply_for_at = sgqlc.types.Field(Timestamp, graphql_name='applyForAt')
    calibrate_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='calibrateAt')
    calibrate_organization = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='calibrateOrganization')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pay_at = sgqlc.types.Field(Timestamp, graphql_name='payAt')
    pay_status = sgqlc.types.Field(OutsideCalibratePayStatus, graphql_name='payStatus')


class CreatePlmFileInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'length', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateProductFlowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name', 'task_configuration')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    task_configuration = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TaskConfigurationInput'))), graphql_name='taskConfiguration')


class CreateProductProjectInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'category', 'code', 'company', 'description', 'field_data', 'name', 'plan_start_at', 'project_group')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='attachment')
    category = sgqlc.types.Field(sgqlc.types.non_null(ProductProjectCategory), graphql_name='category')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    plan_start_at = sgqlc.types.Field(Timestamp, graphql_name='planStartAt')
    project_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput'))), graphql_name='projectGroup')


class CreateProjectGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateReportInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'data', 'tag', 'thing_id', 'timestamp')
    company_id = sgqlc.types.Field(ID, graphql_name='companyID')
    data = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='data')
    tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tag')
    thing_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingID')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class CreateRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'desc', 'name', 'permissions')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('PermissionInput')), graphql_name='permissions')


class CreateScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'estimated_time', 'inspection_method', 'maintenance_method', 'name', 'operator', 'repeat', 'start_at', 'ticket_type')
    end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endAt')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    inspection_method = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='inspectionMethod')
    maintenance_method = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='maintenanceMethod')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    repeat = sgqlc.types.Field(sgqlc.types.non_null('RepeatInput'), graphql_name='repeat')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    ticket_type = sgqlc.types.Field(sgqlc.types.non_null(TicketType), graphql_name='ticketType')


class CreateSourceKeyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('desc', 'key', 'thing_type_id')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    thing_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingTypeId')


class CreateSparePartInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'code', 'company_id', 'distributor', 'field_data', 'image', 'manufacturer', 'name', 'original_inventory', 'safe_inventory_max', 'safe_inventory_min', 'specification')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='attachment')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='image')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    original_inventory = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CreateOriginalInventoryInput)), graphql_name='originalInventory')
    safe_inventory_max = sgqlc.types.Field(Int, graphql_name='safeInventoryMax')
    safe_inventory_min = sgqlc.types.Field(Int, graphql_name='safeInventoryMin')
    specification = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='specification')


class CreateSparePartOutboundInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'date', 'depository', 'item', 'kind', 'operator', 'remark', 'thing_maintenance', 'thing_repair')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    depository = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='depository')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreateSparePartOutboundItemInput'))), graphql_name='item')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SparePartOutboundKind), graphql_name='kind')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    thing_maintenance = sgqlc.types.Field('IntIDInput', graphql_name='thingMaintenance')
    thing_repair = sgqlc.types.Field('IntIDInput', graphql_name='thingRepair')


class CreateSparePartOutboundItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='sparePart')


class CreateSparePartReceiptInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'date', 'depository', 'item', 'kind', 'operator', 'remark')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    depository = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='depository')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreateSparePartReceiptItemInput'))), graphql_name='item')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SparePartReceiptKind), graphql_name='kind')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class CreateSparePartReceiptItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='sparePart')


class CreateSparePartWriteoffInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'issue', 'item', 'kind', 'reason')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    issue = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='issue')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CreateSparePartWriteoffItemInput'))), graphql_name='item')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SparePartWriteoffKind), graphql_name='kind')
    reason = sgqlc.types.Field(String, graphql_name='reason')


class CreateSparePartWriteoffItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('item', 'quantity')
    item = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='item')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')


class CreateTaskBomInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'task', 'versions')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    task = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='task')
    versions = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='versions')


class CreateTaskInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('executive', 'name', 'participant', 'plan_end_at', 'plan_start_at')
    executive = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='executive')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    participant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='participant')
    plan_end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='planEndAt')
    plan_start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='planStartAt')


class CreateThingBorrowApproveConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'destination', 'source', 'trigger')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='destination')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowTrigger), graphql_name='trigger')


class CreateThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'reason', 'thing')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    reason = sgqlc.types.Field(sgqlc.types.non_null(CalibrateReason), graphql_name='reason')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')


class CreateThingCalibrateWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'destination', 'source', 'trigger')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateState), graphql_name='destination')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateTrigger), graphql_name='trigger')


class CreateThingCategoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name', 'parent_id')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class CreateThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name', 'parent')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent = sgqlc.types.Field('IDInput', graphql_name='parent')


class CreateThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('activated_at', 'attachment', 'can_borrowed', 'category', 'code', 'company_id', 'department', 'depreciation_rate', 'desc', 'distributor', 'field_data', 'image', 'installed_at', 'label', 'machine_number', 'maintainer', 'manager', 'manufacturer', 'name', 'on_state', 'predict_residual_rate', 'purchased_at', 'serial_number', 'specification', 'thing_group', 'used_year', 'years_of_use')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='attachment')
    can_borrowed = sgqlc.types.Field(Boolean, graphql_name='canBorrowed')
    category = sgqlc.types.Field('IntIDInput', graphql_name='category')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    department = sgqlc.types.Field('IDInput', graphql_name='department')
    depreciation_rate = sgqlc.types.Field(Float, graphql_name='depreciationRate')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='image')
    installed_at = sgqlc.types.Field(Timestamp, graphql_name='installedAt')
    label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='label')
    machine_number = sgqlc.types.Field(String, graphql_name='machineNumber')
    maintainer = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='maintainer')
    manager = sgqlc.types.Field('StringIDInput', graphql_name='manager')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    on_state = sgqlc.types.Field(OnState, graphql_name='onState')
    predict_residual_rate = sgqlc.types.Field(Float, graphql_name='predictResidualRate')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    specification = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='specification')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='thingGroup')
    used_year = sgqlc.types.Field(Float, graphql_name='usedYear')
    years_of_use = sgqlc.types.Field(Float, graphql_name='yearsOfUse')


class CreateThingInputRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('product_name', 'production', 'production_beat', 'thing_id', 'timestamp', 'yield_number')
    product_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='productName')
    production = sgqlc.types.Field('ThingInputDataIntAttributeInput', graphql_name='production')
    production_beat = sgqlc.types.Field('ThingInputDataIntAttributeInput', graphql_name='productionBeat')
    thing_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingId')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    yield_number = sgqlc.types.Field('ThingInputDataIntAttributeInput', graphql_name='yieldNumber')


class CreateThingInspectionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'estimated_time', 'inspection_method', 'operator', 'thing')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    inspection_method = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput'))), graphql_name='inspectionMethod')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')


class CreateThingInspectionWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'destination', 'source', 'trigger')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='destination')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionTrigger), graphql_name='trigger')


class CreateThingLabelInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'estimated_time', 'maintenance_method', 'operator', 'thing')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput'))), graphql_name='maintenanceMethod')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')


class CreateThingMaintenanceWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'destination', 'source', 'trigger')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='destination')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceTrigger), graphql_name='trigger')


class CreateThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'estimated_time', 'found_at', 'operator', 'thing_repair_item')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    found_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='foundAt')
    operator = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='operator')
    thing_repair_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingRepairItemInput'))), graphql_name='thingRepairItem')


class CreateThingRepairWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'destination', 'source', 'trigger')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='destination')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairTrigger), graphql_name='trigger')


class CreateThingScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'schedule')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    schedule = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateScheduleInput))), graphql_name='schedule')


class CreateThingSpecificationLanguageInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('description', 'is_public', 'name')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublic')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateThingSpecificationLanguagePropertyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data_type', 'description', 'enum_data', 'false_value', 'identifier', 'name', 'precision', 'thing_specification_language', 'true_value', 'unit')
    data_type = sgqlc.types.Field(sgqlc.types.non_null(DataType), graphql_name='dataType')
    description = sgqlc.types.Field(String, graphql_name='description')
    enum_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EnumDataInput')), graphql_name='enumData')
    false_value = sgqlc.types.Field(String, graphql_name='falseValue')
    identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identifier')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null('IntIDInput'), graphql_name='thingSpecificationLanguage')
    true_value = sgqlc.types.Field(String, graphql_name='trueValue')
    unit = sgqlc.types.Field(String, graphql_name='unit')


class CreateThingStatus(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('label', 'thing_type_id', 'type', 'value')
    label = sgqlc.types.Field(String, graphql_name='label')
    thing_type_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingTypeId')
    type = sgqlc.types.Field(sgqlc.types.non_null(ThingStatusType), graphql_name='type')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')


class CreateThingTypeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'desc', 'is_public', 'name')
    code = sgqlc.types.Field(String, graphql_name='code')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    is_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublic')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CreateUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'company', 'department', 'desc', 'email', 'is_active', 'name', 'phone', 'role')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    department = sgqlc.types.Field('IDInput', graphql_name='department')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    email = sgqlc.types.Field(String, graphql_name='email')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='role')


class CreateWorkerOrdersInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('accept_user', 'alerts')
    accept_user = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='acceptUser')
    alerts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='alerts')


class CurrentChangeBorrowApproveConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrowState)), graphql_name='source')


class CurrentThingBorrowApproveConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrowState)), graphql_name='source')


class CurrentThingCalibrateWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingCalibrateState)), graphql_name='source')


class CurrentThingInspectionWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspectionStatus)), graphql_name='source')


class CurrentThingMaintenanceWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenanceStatus)), graphql_name='source')


class CurrentThingRepairWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingRepairStatus)), graphql_name='source')


class DayOfYearInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('day', 'month')
    day = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='day')
    month = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='month')


class DebugAdapterKeyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data', 'function', 'precision', 'type')
    data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='data')
    function = sgqlc.types.Field(JSON, graphql_name='function')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    type = sgqlc.types.Field(DataType, graphql_name='type')


class DeleteCompaniesInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteCompanyAdminUsersInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteCompanyAppsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app_ids', 'company_id')
    app_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='appIDs')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='companyID')


class DeleteDepartmentThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'thing_groups')
    department = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='department')
    thing_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thingGroups')


class DeleteDepartmentsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DeleteThingBorrowDraftThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'thing')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')


class DeleteThingChangeBorrowDraftThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'thing')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='thing')


class DeleteUsersInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class DepartmentListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'current_only', 'ids', 'search')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='ids')
    search = sgqlc.types.Field(String, graphql_name='search')


class DepartmentNameSameAsSiblingsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'parent')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='parent')


class DepartmentThingGroupFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'department')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='department')


class DepartmentTreeFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field('IDInput', graphql_name='company')


class DepositoryListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'factory_id', 'search')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    factory_id = sgqlc.types.Field(Int, graphql_name='factoryId')
    search = sgqlc.types.Field(String, graphql_name='search')


class DeptUserThingGroupInputFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('departments', 'search', 'user')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='departments')
    search = sgqlc.types.Field(String, graphql_name='search')
    user = sgqlc.types.Field('IDInput', graphql_name='user')


class DuplicateUCCFormStructureInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'key_pair')
    company = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='company')
    key_pair = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DuplicateUCCFormStructureKeyInput')), graphql_name='keyPair')


class DuplicateUCCFormStructureKeyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('new_key', 'old_key')
    new_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='newKey')
    old_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='oldKey')


class DurationTimeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('hours', 'minutes', 'seconds')
    hours = sgqlc.types.Field(Int, graphql_name='hours')
    minutes = sgqlc.types.Field(Int, graphql_name='minutes')
    seconds = sgqlc.types.Field(Int, graphql_name='seconds')


class ElectricityPeriodHourInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('hour', 'period')
    hour = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hour')
    period = sgqlc.types.Field(sgqlc.types.non_null(ElectricityPeriod), graphql_name='period')


class ElectricityPeriodPriceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('period', 'price')
    period = sgqlc.types.Field(sgqlc.types.non_null(ElectricityPeriod), graphql_name='period')
    price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='price')


class EndProductProject(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'bom', 'description', 'id')
    attachment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput'))), graphql_name='attachment')
    bom = sgqlc.types.Field('IntIDInput', graphql_name='bom')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class EnergyGroupFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id',)
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')


class EnergyNodeElectricityConsumptionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'energy_node', 'start_at')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    energy_node = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='energyNode')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class EnergyNodeEnergyConsumptionReportFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'energy_node', 'granularity', 'start_at')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    energy_node = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='energyNode')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(EnergyTimeGranularity), graphql_name='granularity')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class EnergyNodeListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'is_electricity', 'is_vapor', 'is_water', 'measurement_object', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    is_electricity = sgqlc.types.Field(Boolean, graphql_name='isElectricity')
    is_vapor = sgqlc.types.Field(Boolean, graphql_name='isVapor')
    is_water = sgqlc.types.Field(Boolean, graphql_name='isWater')
    measurement_object = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MeasurementObject)), graphql_name='measurementObject')
    search = sgqlc.types.Field(String, graphql_name='search')


class EnergyNodeVaporConsumptionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'energy_node', 'start_at')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    energy_node = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='energyNode')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class EnergyNodeWaterConsumptionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'energy_node', 'start_at')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    energy_node = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='energyNode')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class EnergyThingGroupListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')


class EnergyThingsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')


class EnumDataInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class EprectMoldFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class EprectProductionRecordFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end', 'mold', 'only_the_best_arguments', 'search', 'start', 'thing_id')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    mold = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='mold')
    only_the_best_arguments = sgqlc.types.Field(Boolean, graphql_name='onlyTheBestArguments')
    search = sgqlc.types.Field(String, graphql_name='search')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    thing_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='thingId')


class ErrorTypeListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('companies', 'search')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='companies')
    search = sgqlc.types.Field(String, graphql_name='search')


class ErrorTypeNameFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'error_type_name')
    company = sgqlc.types.Field('IDInput', graphql_name='company')
    error_type_name = sgqlc.types.Field(String, graphql_name='errorTypeName')


class EvasionDateFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IDInput')), graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    search = sgqlc.types.Field(String, graphql_name='search')


class ExportThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id')


class ExportUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('ids',)
    ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids')


class FactoryListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'search')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    search = sgqlc.types.Field(String, graphql_name='search')


class FinishWorkerOrderInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('business_knowledges', 'error_types', 'message', 'worker_order')
    business_knowledges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='businessKnowledges')
    error_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IDInput'))), graphql_name='errorTypes')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    worker_order = sgqlc.types.Field(sgqlc.types.non_null('IDInput'), graphql_name='workerOrder')


class ForbiddenUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class GrantRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('role_id', 'user_id')
    role_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='roleId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='userId')


class IDInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class InspectionMethodListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search', 'thing_label')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IntIDInput')), graphql_name='thingLabel')


class InspectionProcessItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'image', 'is_finished', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='image')
    is_finished = sgqlc.types.Field(Boolean, graphql_name='isFinished')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class IntIDInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class IsAdapterKeyExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('key', 'thing_type')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingType')


class IsBomExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'product', 'versions')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    product = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='product')
    versions = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='versions')


class IsCalibrateOrganizationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(String, graphql_name='name')


class IsCalibrateScheduleExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsChangeBorrowApproveConfigurationExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source', 'trigger')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowTrigger), graphql_name='trigger')


class IsDepositoryExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('factory_id', 'name')
    factory_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='factoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsEnergyNodeExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsFactoryExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsInspectionMethodExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsMaintenanceMethodExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsMaterialCategoryExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name', 'property')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    property = sgqlc.types.Field(sgqlc.types.non_null(MaterialProperty), graphql_name='property')


class IsMaterialExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'name', 'versions')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    versions = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='versions')


class IsOutsideCalibrateExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsProductFlowExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsProductProjectExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsProjectGroupNameExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsSparePartExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company_id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')


class IsThingBorrowApproveConfigurationExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source', 'trigger')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowTrigger), graphql_name='trigger')


class IsThingCalibrateWorkflowConfigurationExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source', 'trigger')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateTrigger), graphql_name='trigger')


class IsThingCategoryExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsThingExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company_id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')


class IsThingInspectionWorkflowConfigurationExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source', 'trigger')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionTrigger), graphql_name='trigger')


class IsThingLabelExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'name')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsThingMaintenanceWorkflowConfigurationExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source', 'trigger')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceTrigger), graphql_name='trigger')


class IsThingRepairWorkflowConfigurationExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source', 'trigger')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairTrigger), graphql_name='trigger')


class IsThingScheduleExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsThingSpecificationLanguageExistsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IsThingSpecificationLanguagePropertyExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name', 'thing_specification_language')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingSpecificationLanguage')


class IsThingTypeExists(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class IssueListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('category', 'search', 'status')
    category = sgqlc.types.Field(sgqlc.types.non_null(IssueCategory), graphql_name='category')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssueStatus)), graphql_name='status')


class LeapDailyReportFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end', 'start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')


class LoginInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'password')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')


class MaintenanceMethodListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search', 'thing_label')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingLabel')


class MaintenanceProcessItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'image', 'is_finished', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('StringIDInput')), graphql_name='image')
    is_finished = sgqlc.types.Field(Boolean, graphql_name='isFinished')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class MaintenanceSparePartItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePart')


class MarketAppFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_published', 'is_recommended', 'search', 'type')
    is_published = sgqlc.types.Field(Boolean, graphql_name='isPublished')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    search = sgqlc.types.Field(String, graphql_name='search')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketAppType)), graphql_name='type')


class MarketCommonComponentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('content', 'image', 'title')
    content = sgqlc.types.Field(String, graphql_name='content')
    image = sgqlc.types.Field(IDInput, graphql_name='image')
    title = sgqlc.types.Field(String, graphql_name='title')


class MarketIssueFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end', 'search', 'start', 'status', 'type')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    search = sgqlc.types.Field(String, graphql_name='search')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketIssueStatus)), graphql_name='status')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketConsultationType)), graphql_name='type')


class MarketSolutionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_published', 'is_recommended', 'search', 'type')
    is_published = sgqlc.types.Field(Boolean, graphql_name='isPublished')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    search = sgqlc.types.Field(String, graphql_name='search')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketSolutionType)), graphql_name='type')


class MaterialCategoryFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'property', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    property = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MaterialProperty)), graphql_name='property')
    search = sgqlc.types.Field(String, graphql_name='search')


class MaterialFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'property', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    property = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MaterialProperty)), graphql_name='property')
    search = sgqlc.types.Field(String, graphql_name='search')


class MeterReadingDataFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'search', 'start_at')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class MoveThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_group', 'things')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')
    things = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='things')


class MyAppListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company',)
    company = sgqlc.types.Field(IDInput, graphql_name='company')


class MyCompanyAppFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class NotificationConfigFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('kind', 'source_app')
    kind = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(NotificationKind)), graphql_name='kind')
    source_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='sourceApp')


class NotificationFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_read', 'source_app')
    is_read = sgqlc.types.Field(Boolean, graphql_name='isRead')
    source_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='sourceApp')


class OptimizeMaterialInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('product', 'versions')
    product = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='product')
    versions = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='versions')


class OutsideCalibrateListListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_organization', 'company', 'search')
    calibrate_organization = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='calibrateOrganization')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class PauseThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'lack_depository_name', 'lack_factory_name', 'lack_spare_part_names', 'pause_reason')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    lack_depository_name = sgqlc.types.Field(String, graphql_name='lackDepositoryName')
    lack_factory_name = sgqlc.types.Field(String, graphql_name='lackFactoryName')
    lack_spare_part_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lackSparePartNames')
    pause_reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pauseReason')


class PauseThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'lack_depository_name', 'lack_factory_name', 'lack_spare_part_names', 'pause_reason')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    lack_depository_name = sgqlc.types.Field(String, graphql_name='lackDepositoryName')
    lack_factory_name = sgqlc.types.Field(String, graphql_name='lackFactoryName')
    lack_spare_part_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lackSparePartNames')
    pause_reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pauseReason')


class PermissionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data_range', 'data_range_code', 'permission')
    data_range = sgqlc.types.Field(PermissionDataRange, graphql_name='dataRange')
    data_range_code = sgqlc.types.Field(String, graphql_name='dataRangeCode')
    permission = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='permission')


class PermissionListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_open', 'search', 'type')
    is_open = sgqlc.types.Field(Boolean, graphql_name='isOpen')
    search = sgqlc.types.Field(String, graphql_name='search')
    type = sgqlc.types.Field(PermissionType, graphql_name='type')


class PermissionTreeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'scope')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    scope = sgqlc.types.Field(String, graphql_name='scope')


class PlatformUserListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('is_active', 'origin', 'role', 'role_code', 'search')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    origin = sgqlc.types.Field(UserOrigin, graphql_name='origin')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')
    role_code = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='roleCode')
    search = sgqlc.types.Field(String, graphql_name='search')


class ProductFlowFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class ProductProjectDocumentFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('phase', 'project', 'search')
    phase = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductProjectDocumentPhase)), graphql_name='phase')
    project = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='project')
    search = sgqlc.types.Field(String, graphql_name='search')


class ProductProjectFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('category', 'company', 'project_group', 'search')
    category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProductProjectCategory)), graphql_name='category')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    project_group = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='projectGroup')
    search = sgqlc.types.Field(String, graphql_name='search')


class ProductTaskDocumentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('task',)
    task = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='task')


class ProductTaskFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'executive', 'project', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    executive = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='executive')
    project = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='project')
    search = sgqlc.types.Field(String, graphql_name='search')


class ProjectGroupFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class RegisterUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('account', 'password', 'role_code')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    role_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='roleCode')


class RejectChangeBorrowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'opinion')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    opinion = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='opinion')


class RejectThingBorrowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'opinion')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    opinion = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='opinion')


class RejectThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class RejectThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class RejectThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class RemarkWorkerOrderInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('message', 'worker_order')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    worker_order = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='workerOrder')


class RepairSparePartItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePart')


class RepeatInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('day_of_month', 'day_of_week', 'day_of_year', 'frequency', 'period')
    day_of_month = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dayOfMonth')
    day_of_week = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dayOfWeek')
    day_of_year = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DayOfYearInput)), graphql_name='dayOfYear')
    frequency = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='frequency')
    period = sgqlc.types.Field(sgqlc.types.non_null(RepeatPeriod), graphql_name='period')


class ResetPasswordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('user_ids',)
    user_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='userIDs')


class RestartThingInspectionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'operator', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class RestartThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'operator', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class RestartThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'operator', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class RestoreUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RoleExistsFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'name')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class RoleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'permission', 'scope', 'search')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    id = sgqlc.types.Field(ID, graphql_name='id')
    permission = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='permission')
    scope = sgqlc.types.Field(sgqlc.types.list_of(RoleScope), graphql_name='scope')
    search = sgqlc.types.Field(String, graphql_name='search')


class RoleThingCategoryFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'role')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')


class RuleLevelListInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('companies', 'search')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='companies')
    search = sgqlc.types.Field(String, graphql_name='search')


class SaveThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_at', 'calibrate_label', 'calibrate_method', 'calibrate_organization', 'calibrate_report', 'calibrate_result', 'certificate_return_at', 'certificate_state', 'explain', 'id', 'return_state', 'send_at')
    calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='calibrateAt')
    calibrate_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='calibrateLabel')
    calibrate_method = sgqlc.types.Field(CalibrateMethod, graphql_name='calibrateMethod')
    calibrate_organization = sgqlc.types.Field(IDInput, graphql_name='calibrateOrganization')
    calibrate_report = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='calibrateReport')
    calibrate_result = sgqlc.types.Field(CalibrateResult, graphql_name='calibrateResult')
    certificate_return_at = sgqlc.types.Field(Timestamp, graphql_name='certificateReturnAt')
    certificate_state = sgqlc.types.Field(CertificateState, graphql_name='certificateState')
    explain = sgqlc.types.Field(String, graphql_name='explain')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    return_state = sgqlc.types.Field(ReturnState, graphql_name='returnState')
    send_at = sgqlc.types.Field(Timestamp, graphql_name='sendAt')


class SaveThingInspectionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'related_operator', 'thing_inspection_process_item')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    related_operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='relatedOperator')
    thing_inspection_process_item = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingInspectionProcessItemInput')), graphql_name='thingInspectionProcessItem')


class SaveThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'related_operator', 'thing_maintenance_process_item')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    related_operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='relatedOperator')
    thing_maintenance_process_item = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingMaintenanceProcessItemInput')), graphql_name='thingMaintenanceProcessItem')


class SaveThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'related_operator', 'thing_repair_process_item')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    related_operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='relatedOperator')
    thing_repair_process_item = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingRepairProcessItemInput')), graphql_name='thingRepairProcessItem')


class SetCompanyElectricityPriceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'period_hour', 'period_price')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    period_hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ElectricityPeriodHourInput))), graphql_name='periodHour')
    period_price = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ElectricityPeriodPriceInput)), graphql_name='periodPrice')


class SetCompanyEnergyOffsetThreshold(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'threshold')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    threshold = sgqlc.types.Field(Float, graphql_name='threshold')


class SetCompanyThingSpecificationLanguageInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'thing_specification_language')
    company = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='company')
    thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='thingSpecificationLanguage')


class SetCompanyThingType(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'thing_type')
    company = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='company')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thingType')


class SetCompanyVaporPrice(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'price', 'timestamp')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    price = sgqlc.types.Field(Float, graphql_name='price')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class SetCompanyWaterPrice(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'price', 'timestamp')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    price = sgqlc.types.Field(Float, graphql_name='price')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class SetDepartmentThingGroup(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'thing_group')
    department = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='department')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thingGroup')


class SetDepartmentThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('departments', 'thing_group')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departments')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')


class SetOutsideCalibrateThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('outside_calibrate', 'thing_calibrate')
    outside_calibrate = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='outsideCalibrate')
    thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thingCalibrate')


class SetProjectProductInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('optimize_product', 'product', 'project')
    optimize_product = sgqlc.types.Field(OptimizeMaterialInput, graphql_name='optimizeProduct')
    product = sgqlc.types.Field(CreateMaterialInput, graphql_name='product')
    project = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='project')


class SetRoleThingCategory(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('role', 'thing_category')
    role = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='role')
    thing_category = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='thingCategory')


class SetSingleDepartmentThingGroups(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'department_tree', 'thing_groups')
    department = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='department')
    department_tree = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='departmentTree')
    thing_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thingGroups')


class SetSingleUserThingGroupsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_groups', 'user')
    thing_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thingGroups')
    user = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='user')


class SetSparePartThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'thing')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='sparePart')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thing')


class SetSubThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('sub_thing', 'thing')
    sub_thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='subThing')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class SetTableFieldsConfigInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('fields', 'key')
    fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableFieldConfigInput'))), graphql_name='fields')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')


class SetThingAccessConfigInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('access_key', 'energy_group_id', 'thing_id', 'thing_type_id')
    access_key = sgqlc.types.Field(String, graphql_name='accessKey')
    energy_group_id = sgqlc.types.Field(ID, graphql_name='energyGroupId')
    thing_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingId')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')


class SetThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('by_thing_repair', 'company')
    by_thing_repair = sgqlc.types.Field(Boolean, graphql_name='byThingRepair')
    company = sgqlc.types.Field(IDInput, graphql_name='company')


class SetThingDepartmentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'department')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    department = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='department')


class SetThingScheduleThing(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('schedule', 'thing')
    schedule = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='schedule')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thing')


class SetThingSparePartInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part', 'thing')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='sparePart')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class SetThingSpecificationLanguageThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing', 'thing_specification_language')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thing')
    thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='thingSpecificationLanguage')


class SetThingThingSpecificationLanguageInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing', 'thing_specification_language')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')
    thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='thingSpecificationLanguage')


class SetUCCFormStructureInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'key', 'zone')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    id = sgqlc.types.Field(ID, graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    zone = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of('UCCFieldInput')), graphql_name='zone')


class SetUserThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_group', 'users')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')
    users = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='users')


class SouceKeyFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_type_id',)
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')


class SouceModelKeyFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('serach', 'thing_mechanism_model_code')
    serach = sgqlc.types.Field(String, graphql_name='serach')
    thing_mechanism_model_code = sgqlc.types.Field(String, graphql_name='thingMechanismModelCode')


class SparePartFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'only_unsafe_inventory', 'search', 'thing_id')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    only_unsafe_inventory = sgqlc.types.Field(Boolean, graphql_name='onlyUnsafeInventory')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='thingId')


class SparePartOutboundFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'id', 'kind', 'search', 'spare_part', 'start_at', 'thing_maintenance', 'thing_repair')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    kind = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartOutboundKind)), graphql_name='kind')
    search = sgqlc.types.Field(String, graphql_name='search')
    spare_part = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='sparePart')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    thing_maintenance = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingMaintenance')
    thing_repair = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingRepair')


class SparePartOutboundItemFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part',)
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='sparePart')


class SparePartOutboundSummaryFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_maintenance', 'thing_repair')
    thing_maintenance = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingMaintenance')
    thing_repair = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingRepair')


class SparePartReceiptFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'kind', 'search', 'spare_part', 'start_at')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    kind = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartReceiptKind)), graphql_name='kind')
    search = sgqlc.types.Field(String, graphql_name='search')
    spare_part = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='sparePart')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class SparePartReceiptItemFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('spare_part',)
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='sparePart')


class SparePartStockFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'depository', 'spare_part')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    depository = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='depository')
    spare_part = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='sparePart')


class SparePartWriteoffFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'kind', 'search', 'start_at')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    kind = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(SparePartWriteoffKind)), graphql_name='kind')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class StringIDInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')


class SubThingListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing',)
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class SubmitThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_at', 'calibrate_label', 'calibrate_method', 'calibrate_organization', 'calibrate_report', 'calibrate_result', 'certificate_return_at', 'certificate_state', 'explain', 'id', 'is_synchronized', 'return_state', 'send_at')
    calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='calibrateAt')
    calibrate_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='calibrateLabel')
    calibrate_method = sgqlc.types.Field(CalibrateMethod, graphql_name='calibrateMethod')
    calibrate_organization = sgqlc.types.Field(IDInput, graphql_name='calibrateOrganization')
    calibrate_report = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='calibrateReport')
    calibrate_result = sgqlc.types.Field(CalibrateResult, graphql_name='calibrateResult')
    certificate_return_at = sgqlc.types.Field(Timestamp, graphql_name='certificateReturnAt')
    certificate_state = sgqlc.types.Field(CertificateState, graphql_name='certificateState')
    explain = sgqlc.types.Field(String, graphql_name='explain')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_synchronized = sgqlc.types.Field(Boolean, graphql_name='isSynchronized')
    return_state = sgqlc.types.Field(ReturnState, graphql_name='returnState')
    send_at = sgqlc.types.Field(Timestamp, graphql_name='sendAt')


class SystemLogFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('action', 'company', 'end', 'search', 'start')
    action = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='action')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    search = sgqlc.types.Field(String, graphql_name='search')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')


class TableFieldConfigFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('disable_role_config', 'disable_user_config')
    disable_role_config = sgqlc.types.Field(Boolean, graphql_name='disableRoleConfig')
    disable_user_config = sgqlc.types.Field(Boolean, graphql_name='disableUserConfig')


class TableFieldConfigInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('editable', 'group', 'key', 'label', 'visible')
    editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='editable')
    group = sgqlc.types.Field(TableFieldGroup, graphql_name='group')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    visible = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visible')


class TaskConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ThingAccessConfigFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search', 'thing_type')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thingType')


class ThingBorrowApproveConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrowState)), graphql_name='source')


class ThingBorrowItemListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('thing_borrow',)
    thing_borrow = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thingBorrow')


class ThingBorrowListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('applicant', 'company', 'department_of_applicant', 'department_of_manager', 'end_at', 'search', 'start_at', 'state')
    applicant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='applicant')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    department_of_applicant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departmentOfApplicant')
    department_of_manager = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departmentOfManager')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrowState)), graphql_name='state')


class ThingCalibrateListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_organization', 'code', 'company', 'end_at', 'id', 'method', 'operator', 'reason', 'search', 'start_at', 'state', 'thing')
    calibrate_organization = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='calibrateOrganization')
    code = sgqlc.types.Field(String, graphql_name='code')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id')
    method = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateMethod)), graphql_name='method')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    reason = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateReason)), graphql_name='reason')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingCalibrateState)), graphql_name='state')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ThingCalibrateWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingCalibrateState)), graphql_name='source')


class ThingCategoryListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'is_calibration', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    is_calibration = sgqlc.types.Field(Boolean, graphql_name='isCalibration')
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingCirculationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('applicant', 'company', 'department', 'exclude_thing', 'is_lent', 'only_apply_for_department', 'only_manager', 'search', 'state', 'thing')
    applicant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='applicant')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    exclude_thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='excludeThing')
    is_lent = sgqlc.types.Field(Boolean, graphql_name='isLent')
    only_apply_for_department = sgqlc.types.Field(Boolean, graphql_name='onlyApplyForDepartment')
    only_manager = sgqlc.types.Field(Boolean, graphql_name='onlyManager')
    search = sgqlc.types.Field(String, graphql_name='search')
    state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BorrowState)), graphql_name='state')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ThingElectricityConsumptionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'start_at', 'thing')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ThingEnergyConsumptionReportFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'granularity', 'start_at', 'thing')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(EnergyTimeGranularity), graphql_name='granularity')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ThingFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_code', 'calibrate_method', 'calibrate_result', 'calibrate_state', 'can_borrowed', 'company', 'current_only', 'department', 'end_next_calibrate_at', 'exclude_thing', 'has_department', 'id', 'ids', 'include_deleted', 'is_calibration_expired', 'is_lent', 'label', 'on_state', 'organization', 'qualified_parent', 'search', 'specification', 'start_next_calibrate_at', 'thing_category', 'thing_group')
    calibrate_code = sgqlc.types.Field(String, graphql_name='calibrateCode')
    calibrate_method = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateMethod)), graphql_name='calibrateMethod')
    calibrate_result = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateResult)), graphql_name='calibrateResult')
    calibrate_state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateState)), graphql_name='calibrateState')
    can_borrowed = sgqlc.types.Field(Boolean, graphql_name='canBorrowed')
    company = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='company')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    end_next_calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='endNextCalibrateAt')
    exclude_thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='excludeThing')
    has_department = sgqlc.types.Field(Boolean, graphql_name='hasDepartment')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='id')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids')
    include_deleted = sgqlc.types.Field(Boolean, graphql_name='includeDeleted')
    is_calibration_expired = sgqlc.types.Field(Boolean, graphql_name='isCalibrationExpired')
    is_lent = sgqlc.types.Field(Boolean, graphql_name='isLent')
    label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='label')
    on_state = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(OnState)), graphql_name='onState')
    organization = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='organization')
    qualified_parent = sgqlc.types.Field(IDInput, graphql_name='qualifiedParent')
    search = sgqlc.types.Field(String, graphql_name='search')
    specification = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='specification')
    start_next_calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='startNextCalibrateAt')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thingCategory')
    thing_group = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='thingGroup')


class ThingFunctionDepartmentFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'default_calibrate_user_search', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    default_calibrate_user_search = sgqlc.types.Field(String, graphql_name='defaultCalibrateUserSearch')
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingGroupDeptFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('current_only', 'departments', 'thing_group')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    departments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='departments')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')


class ThingGroupElectricityConsumptionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'start_at', 'thing_group')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    thing_group = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thingGroup')


class ThingGroupEnergyConsumptionReportFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'granularity', 'start_at', 'thing_group')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(EnergyTimeGranularity), graphql_name='granularity')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    thing_group = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thingGroup')


class ThingGroupFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'name')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    name = sgqlc.types.Field(String, graphql_name='name')


class ThingGroupUserFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('current_only', 'thing_group', 'users')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thingGroup')
    users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='users')


class ThingGroupVaporConsumptionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'start_at', 'thing_group')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    thing_group = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thingGroup')


class ThingGroupWaterConsumptionFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'start_at', 'thing_group')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    thing_group = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thingGroup')


class ThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ThingInputDataIntAttributeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('value',)
    value = sgqlc.types.Field(Int, graphql_name='value')


class ThingInputRecordFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('finished', 'search', 'timestamp')
    finished = sgqlc.types.Field(Boolean, graphql_name='finished')
    search = sgqlc.types.Field(String, graphql_name='search')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')


class ThingInputRecordSummaryFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end', 'finished', 'start')
    end = sgqlc.types.Field(Timestamp, graphql_name='end')
    finished = sgqlc.types.Field(Boolean, graphql_name='finished')
    start = sgqlc.types.Field(Timestamp, graphql_name='start')


class ThingInspectionListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_created_at', 'operator', 'search', 'start_created_at', 'status', 'thing')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    end_created_at = sgqlc.types.Field(Timestamp, graphql_name='endCreatedAt')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_created_at = sgqlc.types.Field(Timestamp, graphql_name='startCreatedAt')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspectionStatus)), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ThingInspectionProcessItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('inspection_process_item', 'thing')
    inspection_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InspectionProcessItemInput))), graphql_name='inspectionProcessItem')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class ThingInspectionWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspectionStatus)), graphql_name='source')


class ThingLabelListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingMaintenanceFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_at', 'end_created_at', 'operator', 'search', 'start_at', 'start_created_at', 'status', 'thing')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    end_created_at = sgqlc.types.Field(Timestamp, graphql_name='endCreatedAt')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    start_created_at = sgqlc.types.Field(Timestamp, graphql_name='startCreatedAt')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenanceStatus)), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ThingMaintenanceProcessItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('maintenance_process_item', 'maintenance_spare_part_item', 'thing')
    maintenance_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceProcessItemInput))), graphql_name='maintenanceProcessItem')
    maintenance_spare_part_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceSparePartItemInput))), graphql_name='maintenanceSparePartItem')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class ThingMaintenanceWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenanceStatus)), graphql_name='source')


class ThingMechanismModelFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search',)
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingRateFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end', 'granularity', 'start', 'type')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(Granularity), graphql_name='granularity')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    type = sgqlc.types.Field(sgqlc.types.non_null(ThingRateType), graphql_name='type')


class ThingRepairFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'end_created_at', 'operator', 'search', 'start_created_at', 'status', 'thing')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    end_created_at = sgqlc.types.Field(Timestamp, graphql_name='endCreatedAt')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_created_at = sgqlc.types.Field(Timestamp, graphql_name='startCreatedAt')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingRepairStatus)), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')


class ThingRepairItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('before_repair_image', 'repair_content', 'thing')
    before_repair_image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='beforeRepairImage')
    repair_content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repairContent')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class ThingRepairProcessItemInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('after_repair_image', 'id', 'remark', 'repair_spare_part_item', 'repair_type', 'thing')
    after_repair_image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='afterRepairImage')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    repair_spare_part_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RepairSparePartItemInput))), graphql_name='repairSparePartItem')
    repair_type = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairType), graphql_name='repairType')
    thing = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='thing')


class ThingRepairWorkflowConfigurationListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'source')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    source = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingRepairStatus)), graphql_name='source')


class ThingScheduleFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'operator', 'search', 'thing', 'ticket_type')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')
    ticket_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TicketType)), graphql_name='ticketType')


class ThingSpecificationLanguageFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'exclude_company', 'is_public', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    exclude_company = sgqlc.types.Field(IDInput, graphql_name='excludeCompany')
    is_public = sgqlc.types.Field(Boolean, graphql_name='isPublic')
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingSpecificationLanguagePropertyFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('search', 'thing_specification_language')
    search = sgqlc.types.Field(String, graphql_name='search')
    thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput))), graphql_name='thingSpecificationLanguage')


class ThingStatusFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'thing_type_id')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')


class ThingTaskFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'execution_end_at', 'execution_start_at', 'operator', 'schedule', 'thing', 'ticket_type')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    execution_end_at = sgqlc.types.Field(Timestamp, graphql_name='executionEndAt')
    execution_start_at = sgqlc.types.Field(Timestamp, graphql_name='executionStartAt')
    operator = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='operator')
    schedule = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='schedule')
    thing = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='thing')
    ticket_type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TicketType)), graphql_name='ticketType')


class ThingThingSpecificationLanguageFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'search')
    company = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='company')
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingTypeCodeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'search')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    search = sgqlc.types.Field(String, graphql_name='search')


class ThingTypeFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'exclude_company', 'is_public')
    company_id = sgqlc.types.Field(ID, graphql_name='companyId')
    exclude_company = sgqlc.types.Field(IDInput, graphql_name='excludeCompany')
    is_public = sgqlc.types.Field(Boolean, graphql_name='isPublic')


class TimeDistributionDataInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end', 'start')
    end = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='end')
    start = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='start')


class TimeDistributionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data', 'price')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TimeDistributionDataInput))), graphql_name='data')
    price = sgqlc.types.Field(Float, graphql_name='price')


class TimerangeFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end', 'start')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')


class TurnToThingCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'operator', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class TurnToThingInspectionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark', 'turn_to')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    turn_to = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='turnTo')


class TurnToThingMaintenanceInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark', 'turn_to')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    turn_to = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='turnTo')


class TurnToThingRepairInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'remark', 'turn_to')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    turn_to = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='turnTo')


class TurnWorkerOrderInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('message', 'turn_to', 'worker_order')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    turn_to = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='turnTo')
    worker_order = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='workerOrder')


class UCCFieldInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('content', 'default_bool', 'default_num', 'default_str', 'default_str_list', 'field_type', 'format', 'hint', 'id', 'label', 'max', 'max_range', 'min', 'min_range', 'multi', 'name', 'option', 'required', 'role', 'round', 'set', 'type', 'unit', 'width', 'zeroable')
    content = sgqlc.types.Field(String, graphql_name='content')
    default_bool = sgqlc.types.Field(Boolean, graphql_name='defaultBool')
    default_num = sgqlc.types.Field(Float, graphql_name='defaultNum')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    default_str_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultStrList')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    format = sgqlc.types.Field(String, graphql_name='format')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(ID, graphql_name='id')
    label = sgqlc.types.Field(String, graphql_name='label')
    max = sgqlc.types.Field(Float, graphql_name='max')
    max_range = sgqlc.types.Field('UCCMetaRangeExtremumInput', graphql_name='maxRange')
    min = sgqlc.types.Field(Float, graphql_name='min')
    min_range = sgqlc.types.Field('UCCMetaRangeExtremumInput', graphql_name='minRange')
    multi = sgqlc.types.Field(Boolean, graphql_name='multi')
    name = sgqlc.types.Field(String, graphql_name='name')
    option = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='option')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    role = sgqlc.types.Field(sgqlc.types.list_of(IDInput), graphql_name='role')
    round = sgqlc.types.Field(Int, graphql_name='round')
    set = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UCCFieldInput')), graphql_name='set')
    type = sgqlc.types.Field(UCCFiledValue, graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    width = sgqlc.types.Field(Int, graphql_name='width')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class UCCFormStructureFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'key', 'scope')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    scope = sgqlc.types.Field(UCCScope, graphql_name='scope')


class UCCMetaRangeExtremumInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('default', 'hint', 'max', 'min', 'required', 'unit', 'zeroable')
    default = sgqlc.types.Field(Float, graphql_name='default')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    max = sgqlc.types.Field(Float, graphql_name='max')
    min = sgqlc.types.Field(Float, graphql_name='min')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class UpdateAdapterKeyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('desc', 'function', 'id', 'key', 'precision', 'thing_type_id', 'type', 'unit')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    function = sgqlc.types.Field(JSON, graphql_name='function')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(String, graphql_name='key')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')


class UpdateAlertRuleDetailInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('adapter_key_id', 'adapter_key_unit', 'adapter_name', 'duration_time', 'rule_level', 'rule_operator', 'rule_operator_params')
    adapter_key_id = sgqlc.types.Field(ID, graphql_name='adapterKeyId')
    adapter_key_unit = sgqlc.types.Field(String, graphql_name='adapterKeyUnit')
    adapter_name = sgqlc.types.Field(String, graphql_name='adapterName')
    duration_time = sgqlc.types.Field(DurationTimeInput, graphql_name='durationTime')
    rule_level = sgqlc.types.Field(RuleLevel, graphql_name='ruleLevel')
    rule_operator = sgqlc.types.Field(RuleOperator, graphql_name='ruleOperator')
    rule_operator_params = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ruleOperatorParams')


class UpdateAlertRuleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('alert_rule', 'id', 'things')
    alert_rule = sgqlc.types.Field(UpdateAlertRuleDetailInput, graphql_name='alertRule')
    id = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='id')
    things = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingInput)), graphql_name='things')


class UpdateAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('allowed_permissions', 'avatar', 'code', 'description', 'id', 'jump_kind', 'kind', 'name', 'order', 'redirect_url', 'url', 'whether_new_client')
    allowed_permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='allowedPermissions')
    avatar = sgqlc.types.Field(IDInput, graphql_name='avatar')
    code = sgqlc.types.Field(String, graphql_name='code')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    jump_kind = sgqlc.types.Field(JumpKind, graphql_name='jumpKind')
    kind = sgqlc.types.Field(AppKind, graphql_name='kind')
    name = sgqlc.types.Field(String, graphql_name='name')
    order = sgqlc.types.Field(Float, graphql_name='order')
    redirect_url = sgqlc.types.Field(String, graphql_name='redirectUrl')
    url = sgqlc.types.Field(String, graphql_name='url')
    whether_new_client = sgqlc.types.Field(Boolean, graphql_name='whetherNewClient')


class UpdateBomInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'versions')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    versions = sgqlc.types.Field(String, graphql_name='versions')


class UpdateBomMaterialInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('bom', 'bom_material')
    bom = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='bom')
    bom_material = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BomMaterialInput))), graphql_name='bomMaterial')


class UpdateBusinessKnowledgeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('content', 'id', 'name')
    content = sgqlc.types.Field(String, graphql_name='content')
    id = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateBusinessKnowledgeTypeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateCalibrateOrganizationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateCalibrateScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'id', 'is_all_department', 'is_all_thing_category', 'is_before_month_calibrate', 'is_inside_calibrate', 'is_next_month_calibrate', 'is_outside_calibrate', 'name', 'repeat', 'thing_category')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_all_department = sgqlc.types.Field(Boolean, graphql_name='isAllDepartment')
    is_all_thing_category = sgqlc.types.Field(Boolean, graphql_name='isAllThingCategory')
    is_before_month_calibrate = sgqlc.types.Field(Boolean, graphql_name='isBeforeMonthCalibrate')
    is_inside_calibrate = sgqlc.types.Field(Boolean, graphql_name='isInsideCalibrate')
    is_next_month_calibrate = sgqlc.types.Field(Boolean, graphql_name='isNextMonthCalibrate')
    is_outside_calibrate = sgqlc.types.Field(Boolean, graphql_name='isOutsideCalibrate')
    name = sgqlc.types.Field(String, graphql_name='name')
    repeat = sgqlc.types.Field(CalibrateScheduleRepeatInput, graphql_name='repeat')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingCategory')


class UpdateChangeBorrowApproveConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(ChangeBorrowState, graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(ChangeBorrowState, graphql_name='source')
    trigger = sgqlc.types.Field(ChangeBorrowTrigger, graphql_name='trigger')


class UpdateCockpitAggregation(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end', 'frame', 'id', 'start', 'tag', 'thing_type_id')
    end = sgqlc.types.Field(String, graphql_name='end')
    frame = sgqlc.types.Field(AggregationFrame, graphql_name='frame')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    start = sgqlc.types.Field(String, graphql_name='start')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')


class UpdateCockpitKey(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'key', 'key_type', 'name', 'precision', 'thing_type_id', 'type', 'unit')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(String, graphql_name='key')
    key_type = sgqlc.types.Field(CockpitKeyType, graphql_name='keyType')
    name = sgqlc.types.Field(String, graphql_name='name')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')


class UpdateCockpitTargetInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('oee', 'id', 'operation_rate', 'performance_rate', 'timestamp', 'yield_rate')
    oee = sgqlc.types.Field(Float, graphql_name='OEE')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    performance_rate = sgqlc.types.Field(Float, graphql_name='performanceRate')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    yield_rate = sgqlc.types.Field(Float, graphql_name='yieldRate')


class UpdateCompanyAdminUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('email', 'id', 'name', 'phone')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')


class UpdateCompanyEnergyThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'thing_group')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thingGroup')


class UpdateCompanyEnergyThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'thing')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thing')


class UpdateCompanyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('address', 'city', 'company_type', 'contact', 'county', 'email', 'id', 'name', 'phone', 'province', 'uscc')
    address = sgqlc.types.Field(String, graphql_name='address')
    city = sgqlc.types.Field(String, graphql_name='city')
    company_type = sgqlc.types.Field(IDInput, graphql_name='companyType')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    county = sgqlc.types.Field(String, graphql_name='county')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')


class UpdateDepartmentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'parent')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent = sgqlc.types.Field(IDInput, graphql_name='parent')


class UpdateDepartmentThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'new_thing_group', 'old_thing_group')
    department = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='department')
    new_thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='newThingGroup')
    old_thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='oldThingGroup')


class UpdateDepositoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateEnergyGroup(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateEnergyNodeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_electricity', 'is_vapor', 'is_water', 'measurement_object', 'name', 'parent_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_electricity = sgqlc.types.Field(Boolean, graphql_name='isElectricity')
    is_vapor = sgqlc.types.Field(Boolean, graphql_name='isVapor')
    is_water = sgqlc.types.Field(Boolean, graphql_name='isWater')
    measurement_object = sgqlc.types.Field(MeasurementObject, graphql_name='measurementObject')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class UpdateEnergyTimeDistribution(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('normal', 'peak', 'sharp', 'valley')
    normal = sgqlc.types.Field(TimeDistributionInput, graphql_name='normal')
    peak = sgqlc.types.Field(TimeDistributionInput, graphql_name='peak')
    sharp = sgqlc.types.Field(TimeDistributionInput, graphql_name='sharp')
    valley = sgqlc.types.Field(TimeDistributionInput, graphql_name='valley')


class UpdateErrorTypeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateEvasionDateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_date', 'id', 'name', 'start_date')
    end_date = sgqlc.types.Field(Timestamp, graphql_name='endDate')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    start_date = sgqlc.types.Field(Timestamp, graphql_name='startDate')


class UpdateFactoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateInspectionMethodInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('field_data', 'id', 'name', 'thing_label')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    thing_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingLabel')


class UpdateIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('action', 'attachments', 'id', 'reason', 'receiver', 'remark')
    action = sgqlc.types.Field(sgqlc.types.non_null(IssueAction), graphql_name='action')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='attachments')
    id = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='id')
    reason = sgqlc.types.Field(IssueReason, graphql_name='reason')
    receiver = sgqlc.types.Field(IDInput, graphql_name='receiver')
    remark = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='remark')


class UpdateLeapTargetInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'operation_rate', 'paused_duration', 'paused_times', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    paused_duration = sgqlc.types.Field(Int, graphql_name='pausedDuration')
    paused_times = sgqlc.types.Field(Int, graphql_name='pausedTimes')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')


class UpdateMaintenanceMethodInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('field_data', 'id', 'name', 'thing_label')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    thing_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='thingLabel')


class UpdateMarketAppInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('brief', 'cover_image', 'description', 'id', 'is_recommended', 'screenshot', 'title', 'type')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    cover_image = sgqlc.types.Field(IDInput, graphql_name='coverImage')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    screenshot = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='screenshot')
    title = sgqlc.types.Field(String, graphql_name='title')
    type = sgqlc.types.Field(MarketAppType, graphql_name='type')


class UpdateMarketIssueInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('action', 'attachment', 'description', 'id', 'receiver')
    action = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueAction), graphql_name='action')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='attachment')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    receiver = sgqlc.types.Field(IDInput, graphql_name='receiver')


class UpdateMarketSolutionInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('app', 'brief', 'cover_image', 'description', 'detail', 'id', 'is_recommended', 'title', 'type')
    app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='app')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    cover_image = sgqlc.types.Field(IDInput, graphql_name='coverImage')
    description = sgqlc.types.Field(String, graphql_name='description')
    detail = sgqlc.types.Field(sgqlc.types.list_of(CreateMarketSolutionDetailInput), graphql_name='detail')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    title = sgqlc.types.Field(String, graphql_name='title')
    type = sgqlc.types.Field(MarketSolutionType, graphql_name='type')


class UpdateMaterialCategoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'property')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    property = sgqlc.types.Field(MaterialProperty, graphql_name='property')


class UpdateMaterialInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('category', 'code', 'field_data', 'id', 'name', 'property', 'specification', 'unit', 'versions')
    category = sgqlc.types.Field(IntIDInput, graphql_name='category')
    code = sgqlc.types.Field(String, graphql_name='code')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    property = sgqlc.types.Field(MaterialProperty, graphql_name='property')
    specification = sgqlc.types.Field(String, graphql_name='specification')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    versions = sgqlc.types.Field(String, graphql_name='versions')


class UpdateMeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('avatar', 'email', 'nickname', 'phone')
    avatar = sgqlc.types.Field(IDInput, graphql_name='avatar')
    email = sgqlc.types.Field(String, graphql_name='email')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    phone = sgqlc.types.Field(String, graphql_name='phone')


class UpdateMyCompanyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('address', 'city', 'county', 'email', 'name', 'phone', 'province', 'uscc')
    address = sgqlc.types.Field(String, graphql_name='address')
    city = sgqlc.types.Field(String, graphql_name='city')
    county = sgqlc.types.Field(String, graphql_name='county')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(String, graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')


class UpdateMyPasswordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('new_password', 'old_password')
    new_password = sgqlc.types.Field(String, graphql_name='newPassword')
    old_password = sgqlc.types.Field(String, graphql_name='oldPassword')


class UpdateNotificationConfigInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'receiver_role', 'receiver_user', 'to_email', 'to_inbox')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    receiver_role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='receiverRole')
    receiver_user = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='receiverUser')
    to_email = sgqlc.types.Field(Boolean, graphql_name='toEmail')
    to_inbox = sgqlc.types.Field(Boolean, graphql_name='toInbox')


class UpdateOutsideCalibrateInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('apply_for_at', 'calibrate_at', 'id', 'name', 'pay_at', 'pay_status')
    apply_for_at = sgqlc.types.Field(Timestamp, graphql_name='applyForAt')
    calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='calibrateAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    pay_at = sgqlc.types.Field(Timestamp, graphql_name='payAt')
    pay_status = sgqlc.types.Field(OutsideCalibratePayStatus, graphql_name='payStatus')


class UpdateProductFlowInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'task_configuration')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    task_configuration = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TaskConfigurationInput)), graphql_name='taskConfiguration')


class UpdateProductTaskInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('executive', 'id', 'name', 'participant', 'plan_end_at', 'plan_start_at')
    executive = sgqlc.types.Field(IDInput, graphql_name='executive')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    participant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='participant')
    plan_end_at = sgqlc.types.Field(Timestamp, graphql_name='planEndAt')
    plan_start_at = sgqlc.types.Field(Timestamp, graphql_name='planStartAt')


class UpdateProjectDocumentInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'phase', 'project', 'task')
    attachment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput))), graphql_name='attachment')
    phase = sgqlc.types.Field(sgqlc.types.non_null(ProductProjectDocumentPhase), graphql_name='phase')
    project = sgqlc.types.Field(sgqlc.types.non_null(IntIDInput), graphql_name='project')
    task = sgqlc.types.Field(IntIDInput, graphql_name='task')


class UpdateProjectGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateReportInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data', 'id', 'tag', 'timestamp')
    data = sgqlc.types.Field(JSONString, graphql_name='data')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')


class UpdateRoleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'desc', 'id', 'name', 'permissions')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermissionInput)), graphql_name='permissions')


class UpdateSourceKeyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('desc', 'id', 'key', 'thing_type_id')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(String, graphql_name='key')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')


class UpdateSparePartInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'distributor', 'field_data', 'id', 'image', 'manufacturer', 'name', 'safe_inventory_max', 'safe_inventory_min', 'specification')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='attachment')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='image')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    name = sgqlc.types.Field(String, graphql_name='name')
    safe_inventory_max = sgqlc.types.Field(Int, graphql_name='safeInventoryMax')
    safe_inventory_min = sgqlc.types.Field(Int, graphql_name='safeInventoryMin')
    specification = sgqlc.types.Field(String, graphql_name='specification')


class UpdateThingBorrowApproveConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(ThingBorrowState, graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(ThingBorrowState, graphql_name='source')
    trigger = sgqlc.types.Field(ThingBorrowTrigger, graphql_name='trigger')


class UpdateThingBorrowDraftThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'company', 'expected_borrow_at', 'expected_return_at', 'thing')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    expected_borrow_at = sgqlc.types.Field(Timestamp, graphql_name='expectedBorrowAt')
    expected_return_at = sgqlc.types.Field(Timestamp, graphql_name='expectedReturnAt')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thing')


class UpdateThingCalibrateWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(ThingCalibrateState, graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(ThingCalibrateState, graphql_name='source')
    trigger = sgqlc.types.Field(ThingCalibrateTrigger, graphql_name='trigger')


class UpdateThingCategoryInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'parent_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class UpdateThingChangeBorrowDraftThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('change_return_at', 'code', 'company', 'thing')
    change_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='changeReturnAt')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='thing')


class UpdateThingFunctionDepartmentsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('default_calibrate_user', 'id')
    default_calibrate_user = sgqlc.types.Field(IDInput, graphql_name='defaultCalibrateUser')
    id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id')


class UpdateThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'parent')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent = sgqlc.types.Field(IDInput, graphql_name='parent')


class UpdateThingInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('activated_at', 'attachment', 'calibrate_code', 'calibrate_method', 'calibrate_repeat', 'can_borrowed', 'category', 'department', 'depreciation_rate', 'desc', 'distributor', 'field_data', 'id', 'image', 'installed_at', 'label', 'machine_number', 'maintainer', 'manager', 'manufacturer', 'name', 'on_state', 'predict_residual_rate', 'purchased_at', 'serial_number', 'specification', 'thing_group', 'used_year', 'years_of_use')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='attachment')
    calibrate_code = sgqlc.types.Field(String, graphql_name='calibrateCode')
    calibrate_method = sgqlc.types.Field(CalibrateMethod, graphql_name='calibrateMethod')
    calibrate_repeat = sgqlc.types.Field(CalibrateRepeatInput, graphql_name='calibrateRepeat')
    can_borrowed = sgqlc.types.Field(Boolean, graphql_name='canBorrowed')
    category = sgqlc.types.Field(IntIDInput, graphql_name='category')
    department = sgqlc.types.Field(IDInput, graphql_name='department')
    depreciation_rate = sgqlc.types.Field(Float, graphql_name='depreciationRate')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='image')
    installed_at = sgqlc.types.Field(Timestamp, graphql_name='installedAt')
    label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='label')
    machine_number = sgqlc.types.Field(String, graphql_name='machineNumber')
    maintainer = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(StringIDInput)), graphql_name='maintainer')
    manager = sgqlc.types.Field(StringIDInput, graphql_name='manager')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    name = sgqlc.types.Field(String, graphql_name='name')
    on_state = sgqlc.types.Field(OnState, graphql_name='onState')
    predict_residual_rate = sgqlc.types.Field(Float, graphql_name='predictResidualRate')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    specification = sgqlc.types.Field(String, graphql_name='specification')
    thing_group = sgqlc.types.Field(IDInput, graphql_name='thingGroup')
    used_year = sgqlc.types.Field(Float, graphql_name='usedYear')
    years_of_use = sgqlc.types.Field(Float, graphql_name='yearsOfUse')


class UpdateThingInputRecordInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'production', 'production_beat', 'yield_number')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    production = sgqlc.types.Field(ThingInputDataIntAttributeInput, graphql_name='production')
    production_beat = sgqlc.types.Field(ThingInputDataIntAttributeInput, graphql_name='productionBeat')
    yield_number = sgqlc.types.Field(ThingInputDataIntAttributeInput, graphql_name='yieldNumber')


class UpdateThingInspectionWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(ThingInspectionStatus, graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(ThingInspectionStatus, graphql_name='source')
    trigger = sgqlc.types.Field(ThingInspectionTrigger, graphql_name='trigger')


class UpdateThingLabelInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateThingMaintenanceWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(ThingMaintenanceStatus, graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(ThingMaintenanceStatus, graphql_name='source')
    trigger = sgqlc.types.Field(ThingMaintenanceTrigger, graphql_name='trigger')


class UpdateThingRepairWorkflowConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(ThingRepairStatus, graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(ThingRepairStatus, graphql_name='source')
    trigger = sgqlc.types.Field(ThingRepairTrigger, graphql_name='trigger')


class UpdateThingScheduleInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'estimated_time', 'id', 'inspection_method', 'maintenance_method', 'name', 'operator', 'repeat', 'start_at')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    inspection_method = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='inspectionMethod')
    maintenance_method = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IntIDInput)), graphql_name='maintenanceMethod')
    name = sgqlc.types.Field(String, graphql_name='name')
    operator = sgqlc.types.Field(IDInput, graphql_name='operator')
    repeat = sgqlc.types.Field(RepeatInput, graphql_name='repeat')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class UpdateThingSpecificationLanguageInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('description', 'id', 'is_public', 'name')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_public = sgqlc.types.Field(Boolean, graphql_name='isPublic')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateThingSpecificationLanguagePropertyInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('data_type', 'description', 'enum_data', 'false_value', 'id', 'identifier', 'name', 'precision', 'true_value', 'unit')
    data_type = sgqlc.types.Field(DataType, graphql_name='dataType')
    description = sgqlc.types.Field(String, graphql_name='description')
    enum_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EnumDataInput)), graphql_name='enumData')
    false_value = sgqlc.types.Field(String, graphql_name='falseValue')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    identifier = sgqlc.types.Field(String, graphql_name='identifier')
    name = sgqlc.types.Field(String, graphql_name='name')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    true_value = sgqlc.types.Field(String, graphql_name='trueValue')
    unit = sgqlc.types.Field(String, graphql_name='unit')


class UpdateThingStatus(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'label', 'thing_type_id', 'type', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    label = sgqlc.types.Field(String, graphql_name='label')
    thing_type_id = sgqlc.types.Field(ID, graphql_name='thingTypeId')
    type = sgqlc.types.Field(ThingStatusType, graphql_name='type')
    value = sgqlc.types.Field(Int, graphql_name='value')


class UpdateThingTaskInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('execution_at', 'id', 'operator')
    execution_at = sgqlc.types.Field(Timestamp, graphql_name='executionAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(IDInput, graphql_name='operator')


class UpdateThingTypeInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('code', 'desc', 'id', 'is_public', 'name')
    code = sgqlc.types.Field(String, graphql_name='code')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_public = sgqlc.types.Field(Boolean, graphql_name='isPublic')
    name = sgqlc.types.Field(String, graphql_name='name')


class UpdateThingsInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_method', 'calibrate_repeat', 'id')
    calibrate_method = sgqlc.types.Field(CalibrateMethod, graphql_name='calibrateMethod')
    calibrate_repeat = sgqlc.types.Field(CalibrateRepeatInput, graphql_name='calibrateRepeat')
    id = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id')


class UpdateUserInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('department', 'desc', 'email', 'id', 'is_active', 'name', 'phone', 'role')
    department = sgqlc.types.Field(IDInput, graphql_name='department')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    name = sgqlc.types.Field(String, graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')


class UpdateUserThingGroupInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('new_thing_group', 'old_thing_group')
    new_thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='newThingGroup')
    old_thing_group = sgqlc.types.Field(sgqlc.types.non_null(IDInput), graphql_name='oldThingGroup')


class UpdateWorkflowBaseConfigurationInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('change_borrow_init_state', 'change_borrow_use_default_workflow', 'company', 'thing_borrow_init_state', 'thing_borrow_use_default_workflow', 'thing_calibrate_init_state', 'thing_calibrate_use_default_workflow', 'thing_inspection_init_state', 'thing_inspection_use_default_workflow', 'thing_maintenance_init_state', 'thing_maintenance_use_default_workflow', 'thing_repair_init_state', 'thing_repair_use_default_workflow')
    change_borrow_init_state = sgqlc.types.Field(ChangeBorrowState, graphql_name='changeBorrowInitState')
    change_borrow_use_default_workflow = sgqlc.types.Field(Boolean, graphql_name='changeBorrowUseDefaultWorkflow')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    thing_borrow_init_state = sgqlc.types.Field(ThingBorrowState, graphql_name='thingBorrowInitState')
    thing_borrow_use_default_workflow = sgqlc.types.Field(Boolean, graphql_name='thingBorrowUseDefaultWorkflow')
    thing_calibrate_init_state = sgqlc.types.Field(ThingCalibrateState, graphql_name='thingCalibrateInitState')
    thing_calibrate_use_default_workflow = sgqlc.types.Field(Boolean, graphql_name='thingCalibrateUseDefaultWorkflow')
    thing_inspection_init_state = sgqlc.types.Field(ThingInspectionStatus, graphql_name='thingInspectionInitState')
    thing_inspection_use_default_workflow = sgqlc.types.Field(Boolean, graphql_name='thingInspectionUseDefaultWorkflow')
    thing_maintenance_init_state = sgqlc.types.Field(ThingMaintenanceStatus, graphql_name='thingMaintenanceInitState')
    thing_maintenance_use_default_workflow = sgqlc.types.Field(Boolean, graphql_name='thingMaintenanceUseDefaultWorkflow')
    thing_repair_init_state = sgqlc.types.Field(ThingRepairStatus, graphql_name='thingRepairInitState')
    thing_repair_use_default_workflow = sgqlc.types.Field(Boolean, graphql_name='thingRepairUseDefaultWorkflow')


class UserListFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('company', 'current_only', 'department', 'ids', 'is_active', 'role', 'search', 'search_name', 'type')
    company = sgqlc.types.Field(IDInput, graphql_name='company')
    current_only = sgqlc.types.Field(Boolean, graphql_name='currentOnly')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='department')
    ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='ids')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    role = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='role')
    search = sgqlc.types.Field(String, graphql_name='search')
    search_name = sgqlc.types.Field(String, graphql_name='searchName')
    type = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(UserType)), graphql_name='type')


class WorkerOrderFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('companies', 'end_at', 'start_at')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='companies')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')


class WorkerOrderListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('companies', 'end_at', 'is_me', 'rule_level', 'search', 'start_at', 'status')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='companies')
    end_at = sgqlc.types.Field(Timestamp, graphql_name='endAt')
    is_me = sgqlc.types.Field(Boolean, graphql_name='isMe')
    rule_level = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RuleLevel)), graphql_name='ruleLevel')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    status = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(WorkerOrderStatus)), graphql_name='status')


class WorkerOrderOperatorListFilterInput(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('companies', 'worker_orders')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='companies')
    worker_orders = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='workerOrders')


class companyExistsFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'uscc')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')


class countryFilter(sgqlc.types.Input):
    __schema__ = platform_schema
    __field_names__ = ('full',)
    full = sgqlc.types.Field(Boolean, graphql_name='full')



########################################################################
# Output Objects and Interfaces
########################################################################
class AdapterAlertRuleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('adapter_keys',)
    adapter_keys = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AdapterKey')), graphql_name='adapterKeys')


class AdapterKey(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('desc', 'function', 'id', 'key', 'precision', 'thing_type', 'type', 'unit')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    function = sgqlc.types.Field(JSON, graphql_name='function')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')


class AdapterKeyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AdapterKey))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AdapterModelKey(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('function', 'key', 'precision', 'thing_mechanism_model', 'type')
    function = sgqlc.types.Field(JSON, graphql_name='function')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    thing_mechanism_model = sgqlc.types.Field(sgqlc.types.non_null('ThingMechanismModel'), graphql_name='thingMechanismModel')
    type = sgqlc.types.Field(DataType, graphql_name='type')


class AdapterModelKeyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AdapterModelKey))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AlertDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('adapter_key', 'alert_duration_time', 'id', 'monitoring_value', 'rule_description', 'rule_duration_time', 'rule_level', 'rule_name', 'rule_operator', 'rule_operator_params', 'start_at', 'status', 'thing', 'thing_type', 'worker_order_id', 'worker_order_status')
    adapter_key = sgqlc.types.Field(sgqlc.types.non_null(AdapterKey), graphql_name='adapterKey')
    alert_duration_time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='alertDurationTime')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    monitoring_value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='monitoringValue')
    rule_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ruleDescription')
    rule_duration_time = sgqlc.types.Field('DurationTime', graphql_name='ruleDurationTime')
    rule_level = sgqlc.types.Field(sgqlc.types.non_null(RuleLevel), graphql_name='ruleLevel')
    rule_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ruleName')
    rule_operator = sgqlc.types.Field(sgqlc.types.non_null(RuleOperator), graphql_name='ruleOperator')
    rule_operator_params = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ruleOperatorParams')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(AlertStatus), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='thing')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    worker_order_id = sgqlc.types.Field(Int, graphql_name='workerOrderId')
    worker_order_status = sgqlc.types.Field(sgqlc.types.non_null(WorkerOrderStatus), graphql_name='workerOrderStatus')


class AlertLevelSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('high_alert_count', 'low_alert_count', 'middle_alert_count', 'total_alert_count')
    high_alert_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='highAlertCount')
    low_alert_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='lowAlertCount')
    middle_alert_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='middleAlertCount')
    total_alert_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalAlertCount')


class AlertList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AlertDetail))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AlertRule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('adapter_key', 'created_at', 'id', 'name', 'rule_description', 'rule_duration_time', 'rule_level', 'rule_operator', 'rule_operator_params', 'thing_type', 'things')
    adapter_key = sgqlc.types.Field(sgqlc.types.non_null(AdapterKey), graphql_name='adapterKey')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    rule_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ruleDescription')
    rule_duration_time = sgqlc.types.Field('DurationTime', graphql_name='ruleDurationTime')
    rule_level = sgqlc.types.Field(sgqlc.types.non_null(RuleLevel), graphql_name='ruleLevel')
    rule_operator = sgqlc.types.Field(sgqlc.types.non_null(RuleOperator), graphql_name='ruleOperator')
    rule_operator_params = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='ruleOperatorParams')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    things = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Thing'))), graphql_name='things')


class AlertRuleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AlertRule)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AlertRuleSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('count', 'rule_name')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    rule_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ruleName')


class AlertTendencyCount(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('count', 'timestamp')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class AlertTendencySummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AlertTendencyCount))), graphql_name='data')


class AlertTopRuleSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(AlertRuleSummary))), graphql_name='data')


class AlertTopThingSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingTopCount'))), graphql_name='data')


class App(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('allowed_permissions', 'avatar', 'client_id', 'client_secret', 'code', 'description', 'id', 'jump_kind', 'key', 'kind', 'name', 'order', 'redirect_url', 'url')
    allowed_permissions = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Permission')), graphql_name='allowedPermissions')
    avatar = sgqlc.types.Field('Image', graphql_name='avatar')
    client_id = sgqlc.types.Field(String, graphql_name='clientId')
    client_secret = sgqlc.types.Field(String, graphql_name='clientSecret')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    jump_kind = sgqlc.types.Field(sgqlc.types.non_null(JumpKind), graphql_name='jumpKind')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    kind = sgqlc.types.Field(sgqlc.types.non_null(AppKind), graphql_name='kind')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    order = sgqlc.types.Field(Float, graphql_name='order')
    redirect_url = sgqlc.types.Field(String, graphql_name='redirectUrl')
    url = sgqlc.types.Field(String, graphql_name='url')


class AppBIDatasourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'datasource')
    app = sgqlc.types.Field(App, graphql_name='app')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BIDatasource'))), graphql_name='datasource')


class AppConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('entries', 'hide_sidebar', 'icon_url', 'id', 'logo_url', 'public_url', 'route_url', 'title')
    entries = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AppEntry'))), graphql_name='entries')
    hide_sidebar = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hideSidebar')
    icon_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='iconUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    logo_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='logoUrl')
    public_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='publicUrl')
    route_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='routeUrl')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class AppEntry(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('children', 'hidden', 'icon', 'label', 'path', 'permission_key')
    children = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('AppEntry')), graphql_name='children')
    hidden = sgqlc.types.Field(Boolean, graphql_name='hidden')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    label = sgqlc.types.Field(String, graphql_name='label')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    permission_key = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='permissionKey')


class AppList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(App)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AreaEnergyConsumptionByCompany(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'energy', 'energy_per_product', 'power_on_rate')
    company = sgqlc.types.Field('Company', graphql_name='company')
    energy = sgqlc.types.Field(Float, graphql_name='energy')
    energy_per_product = sgqlc.types.Field(Float, graphql_name='energyPerProduct')
    power_on_rate = sgqlc.types.Field(Float, graphql_name='powerOnRate')


class AreaEnergyConsumptionByCompanyData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AreaEnergyConsumptionByCompany)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AreaEnergyConsumptionOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('energy', 'energy_last', 'energy_previous', 'energy_to_last', 'energy_to_previsous', 'peak_power', 'peak_power_ever', 'peak_power_ever_timestamp', 'peak_power_last', 'peak_power_last_timestamp', 'peak_power_previous', 'peak_power_previous_timestamp', 'peak_power_to_last', 'peak_power_to_previsous', 'peak_rate', 'peak_rate_last', 'peak_rate_previous', 'peak_rate_to_last', 'peak_rate_to_previsous', 'present_power')
    energy = sgqlc.types.Field(Float, graphql_name='energy')
    energy_last = sgqlc.types.Field(Float, graphql_name='energyLast')
    energy_previous = sgqlc.types.Field(Float, graphql_name='energyPrevious')
    energy_to_last = sgqlc.types.Field(Float, graphql_name='energyToLast')
    energy_to_previsous = sgqlc.types.Field(Float, graphql_name='energyToPrevisous')
    peak_power = sgqlc.types.Field(Float, graphql_name='peakPower')
    peak_power_ever = sgqlc.types.Field(Float, graphql_name='peakPowerEver')
    peak_power_ever_timestamp = sgqlc.types.Field(Timestamp, graphql_name='peakPowerEverTimestamp')
    peak_power_last = sgqlc.types.Field(Float, graphql_name='peakPowerLast')
    peak_power_last_timestamp = sgqlc.types.Field(Timestamp, graphql_name='peakPowerLastTimestamp')
    peak_power_previous = sgqlc.types.Field(Float, graphql_name='peakPowerPrevious')
    peak_power_previous_timestamp = sgqlc.types.Field(Timestamp, graphql_name='peakPowerPreviousTimestamp')
    peak_power_to_last = sgqlc.types.Field(Float, graphql_name='peakPowerToLast')
    peak_power_to_previsous = sgqlc.types.Field(Float, graphql_name='peakPowerToPrevisous')
    peak_rate = sgqlc.types.Field(Float, graphql_name='peakRate')
    peak_rate_last = sgqlc.types.Field(Float, graphql_name='peakRateLast')
    peak_rate_previous = sgqlc.types.Field(Float, graphql_name='peakRatePrevious')
    peak_rate_to_last = sgqlc.types.Field(Float, graphql_name='peakRateToLast')
    peak_rate_to_previsous = sgqlc.types.Field(Float, graphql_name='peakRateToPrevisous')
    present_power = sgqlc.types.Field(Float, graphql_name='presentPower')


class AreaPeakRateByCompany(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'energy', 'peak_energy', 'peak_rate')
    company = sgqlc.types.Field('Company', graphql_name='company')
    energy = sgqlc.types.Field(Float, graphql_name='energy')
    peak_energy = sgqlc.types.Field(Float, graphql_name='peakEnergy')
    peak_rate = sgqlc.types.Field(Float, graphql_name='peakRate')


class AreaPeakRateByCompanyData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AreaPeakRateByCompany)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AreaProductionByCompany(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'products', 'to_last', 'to_previous')
    company = sgqlc.types.Field('Company', graphql_name='company')
    products = sgqlc.types.Field(Float, graphql_name='products')
    to_last = sgqlc.types.Field(Float, graphql_name='toLast')
    to_previous = sgqlc.types.Field(Float, graphql_name='toPrevious')


class AreaProductionByCompanyData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AreaProductionByCompany)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AreaProductionDistribution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('to_last', 'to_previous', 'total')
    to_last = sgqlc.types.Field(Float, graphql_name='toLast')
    to_previous = sgqlc.types.Field(Float, graphql_name='toPrevious')
    total = sgqlc.types.Field(Float, graphql_name='total')


class AreaThingTimeseriesUnit(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('num', 'rate', 'timestamp')
    num = sgqlc.types.Field(Int, graphql_name='num')
    rate = sgqlc.types.Field(Float, graphql_name='rate')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class AreaThingsByCompany(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'energy', 'num', 'products')
    company = sgqlc.types.Field('Company', graphql_name='company')
    energy = sgqlc.types.Field(Float, graphql_name='energy')
    num = sgqlc.types.Field(Float, graphql_name='num')
    products = sgqlc.types.Field(Float, graphql_name='products')


class AreaThingsByCompanyData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AreaThingsByCompany)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AreaThingsOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('bottleneck', 'bottleneck_last', 'bottleneck_previous', 'bottleneck_rate', 'bottleneck_to_last', 'bottleneck_to_previous', 'num', 'redundant', 'redundant_last', 'redundant_previous', 'redundant_rate', 'redundant_to_last', 'redundant_to_previous')
    bottleneck = sgqlc.types.Field(Int, graphql_name='bottleneck')
    bottleneck_last = sgqlc.types.Field(Int, graphql_name='bottleneckLast')
    bottleneck_previous = sgqlc.types.Field(Int, graphql_name='bottleneckPrevious')
    bottleneck_rate = sgqlc.types.Field(Float, graphql_name='bottleneckRate')
    bottleneck_to_last = sgqlc.types.Field(Float, graphql_name='bottleneckToLast')
    bottleneck_to_previous = sgqlc.types.Field(Float, graphql_name='bottleneckToPrevious')
    num = sgqlc.types.Field(Int, graphql_name='num')
    redundant = sgqlc.types.Field(Int, graphql_name='redundant')
    redundant_last = sgqlc.types.Field(Int, graphql_name='redundantLast')
    redundant_previous = sgqlc.types.Field(Int, graphql_name='redundantPrevious')
    redundant_rate = sgqlc.types.Field(Float, graphql_name='redundantRate')
    redundant_to_last = sgqlc.types.Field(Float, graphql_name='redundantToLast')
    redundant_to_previous = sgqlc.types.Field(Float, graphql_name='redundantToPrevious')


class AuthInfo(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('token', 'user_id')
    token = sgqlc.types.Field(String, graphql_name='token')
    user_id = sgqlc.types.Field(String, graphql_name='userId')


class BIDatasource(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'name', 'used')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    used = sgqlc.types.Field(Boolean, graphql_name='used')


class BIResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('metric', 'timestamp', 'value')
    metric = sgqlc.types.Field(String, graphql_name='metric')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')


class Bom(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_released', 'product', 'released_at', 'status', 'versions')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_released = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isReleased')
    product = sgqlc.types.Field(sgqlc.types.non_null('Material'), graphql_name='product')
    released_at = sgqlc.types.Field(Timestamp, graphql_name='releasedAt')
    status = sgqlc.types.Field(sgqlc.types.non_null(BomStatus), graphql_name='status')
    versions = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='versions')


class BomList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bom))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class BomMaterial(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('amount', 'bom', 'field_data', 'id', 'material', 'proportion', 'research_unit')
    amount = sgqlc.types.Field(Float, graphql_name='amount')
    bom = sgqlc.types.Field(sgqlc.types.non_null(Bom), graphql_name='bom')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    material = sgqlc.types.Field(sgqlc.types.non_null('Material'), graphql_name='material')
    proportion = sgqlc.types.Field(Float, graphql_name='proportion')
    research_unit = sgqlc.types.Field(String, graphql_name='researchUnit')


class BomMaterialList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BomMaterial))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class BusinessKnowledge(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('author', 'business_knowledge_type', 'content', 'created_at', 'id', 'name')
    author = sgqlc.types.Field('User', graphql_name='author')
    business_knowledge_type = sgqlc.types.Field(sgqlc.types.non_null('BusinessKnowledgeType'), graphql_name='businessKnowledgeType')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class BusinessKnowledgeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BusinessKnowledge))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class BusinessKnowledgeType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class BusinessKnowledgeTypeDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_empty', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_empty = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEmpty')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class BusinessKnowledgeTypeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BusinessKnowledgeTypeDetail))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CNCAlert(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'created_at', 'duration')
    code = sgqlc.types.Field(String, graphql_name='code')
    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')
    duration = sgqlc.types.Field(Int, graphql_name='duration')


class CNCAlertList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CNCAlert)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CNCAlertOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('duration', 'num')
    duration = sgqlc.types.Field(Int, graphql_name='duration')
    num = sgqlc.types.Field(Int, graphql_name='num')


class CNCAlertTimeseries(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('duration', 'num', 'timestamp')
    duration = sgqlc.types.Field(Int, graphql_name='duration')
    num = sgqlc.types.Field(Int, graphql_name='num')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class CNCOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('start_at', 'status')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    status = sgqlc.types.Field(Int, graphql_name='status')


class CalibrateOrganization(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CalibrateOrganizationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateOrganization))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CalibrateRepeat(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('frequency', 'period')
    frequency = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='frequency')
    period = sgqlc.types.Field(sgqlc.types.non_null(CalibrateRepeatPeriod), graphql_name='period')


class CalibrateSchedule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'department', 'id', 'is_all_department', 'is_all_thing_category', 'is_before_month_calibrate', 'is_inside_calibrate', 'is_next_month_calibrate', 'is_outside_calibrate', 'name', 'repeat', 'thing_category', 'updated_at')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    department = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('Department')), graphql_name='department')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_all_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllDepartment')
    is_all_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllThingCategory')
    is_before_month_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBeforeMonthCalibrate')
    is_inside_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isInsideCalibrate')
    is_next_month_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isNextMonthCalibrate')
    is_outside_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOutsideCalibrate')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    repeat = sgqlc.types.Field(sgqlc.types.non_null('CalibrateScheduleRepeat'), graphql_name='repeat')
    thing_category = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingCategory')), graphql_name='thingCategory')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class CalibrateScheduleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CalibrateSchedule))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CalibrateScheduleRepeat(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('day_of_month',)
    day_of_month = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='dayOfMonth')


class ChangeBorrow(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('applicant', 'code', 'created_at', 'department_of_applicant', 'department_of_manager', 'id', 'reason', 'state', 'updated_at')
    applicant = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='applicant')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    department_of_applicant = sgqlc.types.Field(sgqlc.types.non_null('Department'), graphql_name='departmentOfApplicant')
    department_of_manager = sgqlc.types.Field(sgqlc.types.non_null('Department'), graphql_name='departmentOfManager')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reason')
    state = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='state')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ChangeBorrowApproveConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowTrigger), graphql_name='trigger')


class ChangeBorrowApproveConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrowApproveConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ChangeBorrowItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('change_borrow', 'change_return_at', 'id', 'thing', 'thing_circulation')
    change_borrow = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrow), graphql_name='changeBorrow')
    change_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='changeReturnAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing = sgqlc.types.Field(sgqlc.types.non_null('Thing'), graphql_name='thing')
    thing_circulation = sgqlc.types.Field(sgqlc.types.non_null('ThingCirculation'), graphql_name='thingCirculation')


class ChangeBorrowItemList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrowItem))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ChangeBorrowList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrow))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ChangeBorrowOperatorRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'id', 'operate_type', 'operator', 'opinion')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operate_type = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowOperatorType), graphql_name='operateType')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    opinion = sgqlc.types.Field(String, graphql_name='opinion')


class ChangeBorrowStateOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('finished_count', 'not_pass_count', 'pending_count', 'total_count', 'under_review_by_apply_for_count', 'under_review_by_borrowed_count')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    not_pass_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='notPassCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    under_review_by_apply_for_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='underReviewByApplyForCount')
    under_review_by_borrowed_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='underReviewByBorrowedCount')


class City(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('counties', 'name')
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('County')), graphql_name='counties')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class City_(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'province')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    province = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='province')


class CockpitAggregation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('end', 'frame', 'id', 'start', 'tag', 'thing_type')
    end = sgqlc.types.Field(String, graphql_name='end')
    frame = sgqlc.types.Field(AggregationFrame, graphql_name='frame')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    start = sgqlc.types.Field(String, graphql_name='start')
    tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tag')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')


class CockpitKey(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'key', 'key_type', 'name', 'precision', 'statistic', 'thing_type', 'type', 'unit')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    key_type = sgqlc.types.Field(sgqlc.types.non_null(CockpitKeyType), graphql_name='keyType')
    name = sgqlc.types.Field(String, graphql_name='name')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    statistic = sgqlc.types.Field(CockpitKeyStatistic, graphql_name='statistic')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    type = sgqlc.types.Field(DataType, graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')


class CockpitKeyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitKey))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CockpitOrganizationRank(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('organization', 'value')
    organization = sgqlc.types.Field('ThingGroup', graphql_name='organization')
    value = sgqlc.types.Field(Float, graphql_name='value')


class CockpitOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('focus', 'live', 'number_by_organziation', 'number_by_thing_type', 'total')
    focus = sgqlc.types.Field('CockpitOverallFocus', graphql_name='focus')
    live = sgqlc.types.Field('CockpitOverallLive', graphql_name='live')
    number_by_organziation = sgqlc.types.Field(sgqlc.types.list_of('NumberByOrganziation'), graphql_name='numberByOrganziation')
    number_by_thing_type = sgqlc.types.Field(sgqlc.types.list_of('NumberByThingType'), graphql_name='numberByThingType')
    total = sgqlc.types.Field(Int, graphql_name='total')


class CockpitOverallFocus(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('alarm', 'standby')
    alarm = sgqlc.types.Field(Int, graphql_name='alarm')
    standby = sgqlc.types.Field(Int, graphql_name='standby')


class CockpitOverallLive(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('alarm', 'operation', 'shutdown', 'standby')
    alarm = sgqlc.types.Field(Int, graphql_name='alarm')
    operation = sgqlc.types.Field(Int, graphql_name='operation')
    shutdown = sgqlc.types.Field(Int, graphql_name='shutdown')
    standby = sgqlc.types.Field(Int, graphql_name='standby')


class CockpitRate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('oee', 'operation_rate', 'performance_rate', 'timestamp', 'yield_rate')
    oee = sgqlc.types.Field(Float, graphql_name='OEE')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    performance_rate = sgqlc.types.Field(Float, graphql_name='performanceRate')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    yield_rate = sgqlc.types.Field(Float, graphql_name='yieldRate')


class CockpitRateList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitRate))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CockpitRateOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('oee', 'operation_rate', 'performance_rate', 'yield_rate')
    oee = sgqlc.types.Field(Float, graphql_name='OEE')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    performance_rate = sgqlc.types.Field(Float, graphql_name='performanceRate')
    yield_rate = sgqlc.types.Field(Float, graphql_name='yieldRate')


class CockpitTarget(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('oee', 'id', 'operation_rate', 'performance_rate', 'timestamp', 'yield_rate')
    oee = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='OEE')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='operationRate')
    performance_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='performanceRate')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    yield_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='yieldRate')


class CockpitTargetList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitTarget))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CockpitThing(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('duration', 'status', 'thing')
    duration = sgqlc.types.Field(Int, graphql_name='duration')
    status = sgqlc.types.Field(ThingStatusType, graphql_name='status')
    thing = sgqlc.types.Field('Thing', graphql_name='thing')


class CockpitThingList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitThing))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CockpitThingTypeRank(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('type', 'value')
    type = sgqlc.types.Field('ThingType', graphql_name='type')
    value = sgqlc.types.Field(Float, graphql_name='value')


class CockpitTimeseries(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('target', 'timestamp', 'value')
    target = sgqlc.types.Field(Float, graphql_name='target')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')


class CombaAttendance(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('actual', 'date', 'department', 'estimated', 'rate')
    actual = sgqlc.types.Field(Int, graphql_name='actual')
    date = sgqlc.types.Field(Timestamp, graphql_name='date')
    department = sgqlc.types.Field(String, graphql_name='department')
    estimated = sgqlc.types.Field(Int, graphql_name='estimated')
    rate = sgqlc.types.Field(Float, graphql_name='rate')


class CombaAttendanceOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('actual', 'estimated', 'rate')
    actual = sgqlc.types.Field(Int, graphql_name='actual')
    estimated = sgqlc.types.Field(Int, graphql_name='estimated')
    rate = sgqlc.types.Field(Float, graphql_name='rate')


class CombaCostOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('fee_rate', 'salary')
    fee_rate = sgqlc.types.Field(Float, graphql_name='feeRate')
    salary = sgqlc.types.Field(Float, graphql_name='salary')


class CombaDeliverDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('count', 'follow_order_no', 'material_desc', 'material_no', 'sale_order_no', 'sec_production_type_desc')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    follow_order_no = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='followOrderNo')
    material_desc = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='materialDesc')
    material_no = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='materialNo')
    sale_order_no = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='saleOrderNo')
    sec_production_type_desc = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='secProductionTypeDesc')


class CombaDeliverList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(CombaDeliverDetail)), graphql_name='data')


class CombaDeliverSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('combaDeliverCount'))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CombaDeliveryByProductLine(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('detail', 'line', 'rate', 'total_finish', 'total_plan')
    detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CombaDeliveryByStage')), graphql_name='detail')
    line = sgqlc.types.Field('CombaProductLine', graphql_name='line')
    rate = sgqlc.types.Field(Float, graphql_name='rate')
    total_finish = sgqlc.types.Field(Int, graphql_name='totalFinish')
    total_plan = sgqlc.types.Field(Int, graphql_name='totalPlan')


class CombaDeliveryByStage(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('finish', 'plan', 'stage')
    finish = sgqlc.types.Field(Int, graphql_name='finish')
    plan = sgqlc.types.Field(Int, graphql_name='plan')
    stage = sgqlc.types.Field(sgqlc.types.non_null('CombaStage'), graphql_name='stage')


class CombaDeliveryHistoryDaily(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('date', 'value')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    value = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaDeliveryByProductLine)), graphql_name='value')


class CombaDeliveryHistoryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('daily', 'total')
    daily = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaDeliveryHistoryDaily)), graphql_name='daily')
    total = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaDeliveryByProductLine)), graphql_name='total')


class CombaDeliveryHistoryTotal(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('line', 'value')
    line = sgqlc.types.Field('CombaProductLine', graphql_name='line')
    value = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaDeliveryByStage)), graphql_name='value')


class CombaDeliveryOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('close_rate',)
    close_rate = sgqlc.types.Field(Float, graphql_name='closeRate')


class CombaLine(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('definition', 'id', 'name', 'status')
    definition = sgqlc.types.Field(String, graphql_name='definition')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    status = sgqlc.types.Field(CombaDeviceStatus, graphql_name='status')


class CombaLineDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('line', 'oee', 'operation_rate')
    line = sgqlc.types.Field(sgqlc.types.non_null(CombaLine), graphql_name='line')
    oee = sgqlc.types.Field(Float, graphql_name='oee')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')


class CombaLineOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('oee', 'operation_rate', 'standby')
    oee = sgqlc.types.Field(Float, graphql_name='oee')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    standby = sgqlc.types.Field(Int, graphql_name='standby')


class CombaOrder(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('compose', 'detect', 'is_dispatched', 'is_issued', 'is_set', 'model', 'no', 'old', 'pack', 'start_at', 'stock', 'test')
    compose = sgqlc.types.Field(Int, graphql_name='compose')
    detect = sgqlc.types.Field(Int, graphql_name='detect')
    is_dispatched = sgqlc.types.Field(Boolean, graphql_name='isDispatched')
    is_issued = sgqlc.types.Field(Boolean, graphql_name='isIssued')
    is_set = sgqlc.types.Field(Boolean, graphql_name='isSet')
    model = sgqlc.types.Field(String, graphql_name='model')
    no = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='no')
    old = sgqlc.types.Field(Int, graphql_name='old')
    pack = sgqlc.types.Field(Int, graphql_name='pack')
    start_at = sgqlc.types.Field(Timestamp, graphql_name='startAt')
    stock = sgqlc.types.Field(Int, graphql_name='stock')
    test = sgqlc.types.Field(Int, graphql_name='test')


class CombaOwe(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'date', 'description', 'model', 'num', 'order_description', 'order_no', 'order_num', 'plan_start_date', 'sap_code', 'stage')
    code = sgqlc.types.Field(String, graphql_name='code')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    description = sgqlc.types.Field(String, graphql_name='description')
    model = sgqlc.types.Field(String, graphql_name='model')
    num = sgqlc.types.Field(Int, graphql_name='num')
    order_description = sgqlc.types.Field(String, graphql_name='orderDescription')
    order_no = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='orderNo')
    order_num = sgqlc.types.Field(Int, graphql_name='orderNum')
    plan_start_date = sgqlc.types.Field(Timestamp, graphql_name='planStartDate')
    sap_code = sgqlc.types.Field(String, graphql_name='sapCode')
    stage = sgqlc.types.Field(String, graphql_name='stage')


class CombaOweOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('owed_order_num', 'set_order_num', 'set_rate')
    owed_order_num = sgqlc.types.Field(Int, graphql_name='owedOrderNum')
    set_order_num = sgqlc.types.Field(Int, graphql_name='setOrderNum')
    set_rate = sgqlc.types.Field(Float, graphql_name='setRate')


class CombaPPMDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('date', 'total', 'value')
    date = sgqlc.types.Field(Timestamp, graphql_name='date')
    total = sgqlc.types.Field(Int, graphql_name='total')
    value = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('combaPPMTotal')), graphql_name='value')


class CombaPPMList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('detail', 'line_total', 'total')
    detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaPPMDetail)), graphql_name='detail')
    line_total = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('combaPPMTotal')), graphql_name='lineTotal')
    total = sgqlc.types.Field(Int, graphql_name='total')


class CombaProductLine(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CombaProductionCategory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(String, graphql_name='name')


class CombaProductionType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CombaQualifiedRate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('production', 'rate')
    production = sgqlc.types.Field(CombaProductionType, graphql_name='production')
    rate = sgqlc.types.Field(Float, graphql_name='rate')


class CombaQualifiedRateByMonth(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('month', 'value')
    month = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='month')
    value = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaQualifiedRate)), graphql_name='value')


class CombaSMTChangeLineTimeseries(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('count', 'date', 'time')
    count = sgqlc.types.Field(Int, graphql_name='count')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    time = sgqlc.types.Field(Int, graphql_name='time')


class CombaSMTDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('change_line_day', 'change_line_night', 'change_line_time_day', 'change_line_time_night', 'complete_order', 'complete_order_day', 'complete_order_night', 'complete_point', 'complete_point_day', 'complete_point_night', 'plan_order', 'plan_order_day', 'plan_order_night', 'plan_point', 'plan_point_day', 'plan_point_night', 'point', 'rate_day_order', 'rate_day_point', 'rate_night_order', 'rate_night_point', 'standard', 'time')
    change_line_day = sgqlc.types.Field(Int, graphql_name='changeLineDay')
    change_line_night = sgqlc.types.Field(Int, graphql_name='changeLineNight')
    change_line_time_day = sgqlc.types.Field(Int, graphql_name='changeLineTimeDay')
    change_line_time_night = sgqlc.types.Field(Int, graphql_name='changeLineTimeNight')
    complete_order = sgqlc.types.Field(Int, graphql_name='completeOrder')
    complete_order_day = sgqlc.types.Field(Int, graphql_name='completeOrderDay')
    complete_order_night = sgqlc.types.Field(Int, graphql_name='completeOrderNight')
    complete_point = sgqlc.types.Field(Int, graphql_name='completePoint')
    complete_point_day = sgqlc.types.Field(Int, graphql_name='completePointDay')
    complete_point_night = sgqlc.types.Field(Int, graphql_name='completePointNight')
    plan_order = sgqlc.types.Field(Int, graphql_name='planOrder')
    plan_order_day = sgqlc.types.Field(Int, graphql_name='planOrderDay')
    plan_order_night = sgqlc.types.Field(Int, graphql_name='planOrderNight')
    plan_point = sgqlc.types.Field(Int, graphql_name='planPoint')
    plan_point_day = sgqlc.types.Field(Int, graphql_name='planPointDay')
    plan_point_night = sgqlc.types.Field(Int, graphql_name='planPointNight')
    point = sgqlc.types.Field(Int, graphql_name='point')
    rate_day_order = sgqlc.types.Field(Float, graphql_name='rateDayOrder')
    rate_day_point = sgqlc.types.Field(Float, graphql_name='rateDayPoint')
    rate_night_order = sgqlc.types.Field(Float, graphql_name='rateNightOrder')
    rate_night_point = sgqlc.types.Field(Float, graphql_name='rateNightPoint')
    standard = sgqlc.types.Field(Int, graphql_name='standard')
    time = sgqlc.types.Field(Int, graphql_name='time')


class CombaSMTDetailByLine(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('detail', 'line')
    detail = sgqlc.types.Field(CombaSMTDetail, graphql_name='detail')
    line = sgqlc.types.Field(CombaLine, graphql_name='line')


class CombaSMTList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total', 'value')
    total = sgqlc.types.Field(CombaSMTDetail, graphql_name='total')
    value = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaSMTDetailByLine)), graphql_name='value')


class CombaSMTOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('avg_change_line_time', 'change_line', 'complete_order', 'complete_point', 'dispatch_order', 'plan_order', 'plan_point', 'rate_order', 'rate_point')
    avg_change_line_time = sgqlc.types.Field(Int, graphql_name='avgChangeLineTime')
    change_line = sgqlc.types.Field(Int, graphql_name='changeLine')
    complete_order = sgqlc.types.Field(Int, graphql_name='completeOrder')
    complete_point = sgqlc.types.Field(Int, graphql_name='completePoint')
    dispatch_order = sgqlc.types.Field(Int, graphql_name='dispatchOrder')
    plan_order = sgqlc.types.Field(Int, graphql_name='planOrder')
    plan_point = sgqlc.types.Field(Int, graphql_name='planPoint')
    rate_order = sgqlc.types.Field(Float, graphql_name='rateOrder')
    rate_point = sgqlc.types.Field(Float, graphql_name='ratePoint')


class CombaSMTRealtime(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('complete_point', 'ppm')
    complete_point = sgqlc.types.Field(Int, graphql_name='completePoint')
    ppm = sgqlc.types.Field(Int, graphql_name='ppm')


class CombaStage(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name',)
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CombaStockingDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('date', 'total', 'value')
    date = sgqlc.types.Field(Timestamp, graphql_name='date')
    total = sgqlc.types.Field(Int, graphql_name='total')
    value = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('combaStockingOverall')), graphql_name='value')


class CombaStockingKVCell(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('col', 'row', 'value')
    col = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='col')
    row = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='row')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')


class CombaStockingList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('detail', 'production_total', 'total')
    detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaStockingDetail)), graphql_name='detail')
    production_total = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('combaStockingOverall')), graphql_name='productionTotal')
    total = sgqlc.types.Field(Int, graphql_name='total')


class CombaStockingMap(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('column', 'row', 'values')
    column = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='column')
    row = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='row')
    values = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaStockingKVCell)), graphql_name='values')


class CombaUnqualifiedList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_num')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CombaUnqualifiedOverall'))), graphql_name='data')
    total_num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalNum')


class CombaUnqualifiedOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('accurate_rate', 'num', 'rate', 'reason')
    accurate_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='accurateRate')
    num = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='num')
    rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='rate')
    reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reason')


class Company(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('address', 'city', 'contact', 'county', 'email', 'id', 'is_mine', 'name', 'phone', 'province', 'type', 'uscc')
    address = sgqlc.types.Field(String, graphql_name='address')
    city = sgqlc.types.Field(String, graphql_name='city')
    contact = sgqlc.types.Field(String, graphql_name='contact')
    county = sgqlc.types.Field(String, graphql_name='county')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_mine = sgqlc.types.Field(Boolean, graphql_name='isMine')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    type = sgqlc.types.Field(sgqlc.types.non_null('CompanyType'), graphql_name='type')
    uscc = sgqlc.types.Field(String, graphql_name='uscc')


class CompanyApps(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('apps', 'company')
    apps = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(App)), graphql_name='apps')
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company')


class CompanyAppsList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompanyApps)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyBIDatasource(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'created_at', 'datasource', 'id')
    app = sgqlc.types.Field(sgqlc.types.non_null(App), graphql_name='app')
    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')
    datasource = sgqlc.types.Field(sgqlc.types.non_null(BIDatasource), graphql_name='datasource')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class CompanyBIDatasourceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CompanyBIDatasource)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyElectricityConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee', 'id', 'timestamp')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class CompanyElectricityPeriodConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee', 'period')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    period = sgqlc.types.Field(sgqlc.types.non_null(ElectricityPeriod), graphql_name='period')


class CompanyElectricityPrice(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('period_hour', 'period_price')
    period_hour = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ElectricityPeriodHour'))), graphql_name='periodHour')
    period_price = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('ElectricityPeriodPrice')), graphql_name='periodPrice')


class CompanyElectricityTotalConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')


class CompanyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('energy', 'fee', 'products')
    energy = sgqlc.types.Field(Float, graphql_name='energy')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    products = sgqlc.types.Field(Float, graphql_name='products')


class CompanyRank(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CompanyRankDetail')), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyRankDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'value')
    company = sgqlc.types.Field(Company, graphql_name='company')
    value = sgqlc.types.Field(Float, graphql_name='value')


class CompanyRealTimeElectricityData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('power', 'timestamp')
    power = sgqlc.types.Field(Float, graphql_name='power')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class CompanyRealTimeVaporData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('flow', 'timestamp')
    flow = sgqlc.types.Field(Float, graphql_name='flow')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class CompanyRealTimeWaterData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('flow', 'timestamp')
    flow = sgqlc.types.Field(Float, graphql_name='flow')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class CompanyThingGroupNode(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'thing_groups')
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company')
    thing_groups = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='thingGroups')


class CompanyThingList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Thing'))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyThingOrganizationNode(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'thing_organizations')
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company')
    thing_organizations = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingOrganizationWithChildren')), graphql_name='thingOrganizations')


class CompanyThingSpecificationLanguage(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'thing_specification_language')
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null('ThingSpecificationLanguage'), graphql_name='thingSpecificationLanguage')


class CompanyThingSpecificationLanguageList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyThingSpecificationLanguage))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyThingType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'id', 'thing_type')
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')


class CompanyThingTypeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyThingType))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyTimeVaporPrice(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('price', 'timestamp')
    price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='price')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class CompanyTimeWaterPrice(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('price', 'timestamp')
    price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='price')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class CompanyType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class CompanyTypeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyType))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CompanyVaporConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee', 'id', 'timestamp')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class CompanyVaporTotalConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')


class CompanyWaterConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee', 'id', 'timestamp')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class CompanyWaterTotalConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')


class Country(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('alpha2', 'alpha3', 'chinese', 'english', 'id')
    alpha2 = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alpha2')
    alpha3 = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='alpha3')
    chinese = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='chinese')
    english = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='english')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class County(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('companies', 'name')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='companies')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class County_(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('city', 'id', 'name')
    city = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='city')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class DailyMeterReadingData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('energy_node', 'id', 'timestamp', 'vapor_consumption', 'vapor_reading', 'water_consumption', 'water_reading')
    energy_node = sgqlc.types.Field(sgqlc.types.non_null('EnergyNode'), graphql_name='energyNode')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    vapor_consumption = sgqlc.types.Field(Float, graphql_name='vaporConsumption')
    vapor_reading = sgqlc.types.Field(Float, graphql_name='vaporReading')
    water_consumption = sgqlc.types.Field(Float, graphql_name='waterConsumption')
    water_reading = sgqlc.types.Field(Float, graphql_name='waterReading')


class DayOfYear(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('day', 'month')
    day = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='day')
    month = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='month')


class Department(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_deleted', 'name', 'parent_id', 'path_name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_deleted = sgqlc.types.Field(Boolean, graphql_name='isDeleted')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentID')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')


class DepartmentList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Depository(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('factory', 'id', 'name')
    factory = sgqlc.types.Field(sgqlc.types.non_null('Factory'), graphql_name='factory')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class DepositoryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Depository))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeptThingGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('DeptThingGroups')), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeptThingGroups(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('department', 'thing_groups')
    department = sgqlc.types.Field(sgqlc.types.non_null(Department), graphql_name='department')
    thing_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingGroup')), graphql_name='thingGroups')


class DurationTime(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('hours', 'minutes', 'seconds')
    hours = sgqlc.types.Field(Int, graphql_name='hours')
    minutes = sgqlc.types.Field(Int, graphql_name='minutes')
    seconds = sgqlc.types.Field(Int, graphql_name='seconds')


class EamExcelValidationResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('abnormal_row_count', 'commented_data', 'duplicated_row_count', 'is_data_valid', 'is_header_valid', 'missing_fields', 'normal_row_count', 'redundant_fields', 'total_row_count')
    abnormal_row_count = sgqlc.types.Field(Int, graphql_name='abnormalRowCount')
    commented_data = sgqlc.types.Field('TempFile', graphql_name='commentedData')
    duplicated_row_count = sgqlc.types.Field(Int, graphql_name='duplicatedRowCount')
    is_data_valid = sgqlc.types.Field(Boolean, graphql_name='isDataValid')
    is_header_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isHeaderValid')
    missing_fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='missingFields')
    normal_row_count = sgqlc.types.Field(Int, graphql_name='normalRowCount')
    redundant_fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='redundantFields')
    total_row_count = sgqlc.types.Field(Int, graphql_name='totalRowCount')


class EamImportResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('failed_data', 'failed_row_count', 'is_all_successful', 'successful_row_count', 'total_row_count')
    failed_data = sgqlc.types.Field('TempFile', graphql_name='failedData')
    failed_row_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='failedRowCount')
    is_all_successful = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllSuccessful')
    successful_row_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successfulRowCount')
    total_row_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRowCount')


class ElectricityConsumptionData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')


class ElectricityMeterReadingData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'consumption_deviation', 'reading')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    consumption_deviation = sgqlc.types.Field(Float, graphql_name='consumptionDeviation')
    reading = sgqlc.types.Field(Float, graphql_name='reading')


class ElectricityPeriodHour(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('hour', 'period')
    hour = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hour')
    period = sgqlc.types.Field(sgqlc.types.non_null(ElectricityPeriod), graphql_name='period')


class ElectricityPeriodPrice(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('period', 'price')
    period = sgqlc.types.Field(sgqlc.types.non_null(ElectricityPeriod), graphql_name='period')
    price = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='price')


class EmsExcelValidationResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('abnormal_row_count', 'commented_data', 'duplicated_row_count', 'is_data_valid', 'is_header_valid', 'missing_fields', 'normal_row_count', 'redundant_fields', 'total_row_count')
    abnormal_row_count = sgqlc.types.Field(Int, graphql_name='abnormalRowCount')
    commented_data = sgqlc.types.Field('TempFile', graphql_name='commentedData')
    duplicated_row_count = sgqlc.types.Field(Int, graphql_name='duplicatedRowCount')
    is_data_valid = sgqlc.types.Field(Boolean, graphql_name='isDataValid')
    is_header_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isHeaderValid')
    missing_fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='missingFields')
    normal_row_count = sgqlc.types.Field(Int, graphql_name='normalRowCount')
    redundant_fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='redundantFields')
    total_row_count = sgqlc.types.Field(Int, graphql_name='totalRowCount')


class EmsImportResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('failed_data', 'failed_row_count', 'is_all_successful', 'successful_row_count', 'total_row_count')
    failed_data = sgqlc.types.Field('TempFile', graphql_name='failedData')
    failed_row_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='failedRowCount')
    is_all_successful = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAllSuccessful')
    successful_row_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='successfulRowCount')
    total_row_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRowCount')


class EnergyConsumptionComparison(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('avg', 'num', 'total', 'trends')
    avg = sgqlc.types.Field(Float, graphql_name='avg')
    num = sgqlc.types.Field(Int, graphql_name='num')
    total = sgqlc.types.Field(Float, graphql_name='total')
    trends = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('EnergyConsumptionComparisonTrend')), graphql_name='trends')


class EnergyConsumptionComparisonTrend(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'order', 'total', 'values')
    name = sgqlc.types.Field(String, graphql_name='name')
    order = sgqlc.types.Field(Int, graphql_name='order')
    total = sgqlc.types.Field(Float, graphql_name='total')
    values = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit')), graphql_name='values')


class EnergyConsumptionToT(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('delta', 'last', 'present', 'tot')
    delta = sgqlc.types.Field(Float, graphql_name='delta')
    last = sgqlc.types.Field(Float, graphql_name='last')
    present = sgqlc.types.Field(Float, graphql_name='present')
    tot = sgqlc.types.Field(Float, graphql_name='tot')


class EnergyFeeBIResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('energy_group', 'timestamp', 'value')
    energy_group = sgqlc.types.Field('EnergyGroup', graphql_name='energyGroup')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')


class EnergyGroup(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class EnergyGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EnergyGroup))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnergyNode(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_electricity', 'is_vapor', 'is_water', 'measurement_object', 'name', 'parent_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_electricity = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isElectricity')
    is_vapor = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVapor')
    is_water = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isWater')
    measurement_object = sgqlc.types.Field(sgqlc.types.non_null(MeasurementObject), graphql_name='measurementObject')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class EnergyNodeElectricityConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'energy_node', 'fee', 'id')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    energy_node = sgqlc.types.Field(sgqlc.types.non_null(EnergyNode), graphql_name='energyNode')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class EnergyNodeElectricityConsumptionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EnergyNodeElectricityConsumption))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnergyNodeEnergyConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('electricity', 'electricity_of_last_year', 'electricity_of_previous_period', 'energy_node', 'granularity', 'id', 'timestamp', 'vapor', 'vapor_of_last_year', 'vapor_of_previous_period', 'water', 'water_of_last_year', 'water_of_previous_period')
    electricity = sgqlc.types.Field(ElectricityConsumptionData, graphql_name='electricity')
    electricity_of_last_year = sgqlc.types.Field(ElectricityConsumptionData, graphql_name='electricityOfLastYear')
    electricity_of_previous_period = sgqlc.types.Field(ElectricityConsumptionData, graphql_name='electricityOfPreviousPeriod')
    energy_node = sgqlc.types.Field(sgqlc.types.non_null(EnergyNode), graphql_name='energyNode')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(EnergyTimeGranularity), graphql_name='granularity')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    vapor = sgqlc.types.Field('VaporConsumptionData', graphql_name='vapor')
    vapor_of_last_year = sgqlc.types.Field('VaporConsumptionData', graphql_name='vaporOfLastYear')
    vapor_of_previous_period = sgqlc.types.Field('VaporConsumptionData', graphql_name='vaporOfPreviousPeriod')
    water = sgqlc.types.Field('WaterConsumptionData', graphql_name='water')
    water_of_last_year = sgqlc.types.Field('WaterConsumptionData', graphql_name='waterOfLastYear')
    water_of_previous_period = sgqlc.types.Field('WaterConsumptionData', graphql_name='waterOfPreviousPeriod')


class EnergyNodeEnergyConsumptionData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('electricity', 'vapor', 'water')
    electricity = sgqlc.types.Field(sgqlc.types.non_null(ElectricityConsumptionData), graphql_name='electricity')
    vapor = sgqlc.types.Field(sgqlc.types.non_null('VaporConsumptionData'), graphql_name='vapor')
    water = sgqlc.types.Field(sgqlc.types.non_null('WaterConsumptionData'), graphql_name='water')


class EnergyNodeEnergyConsumptionReport(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count', 'total_data')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EnergyNodeEnergyConsumption))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_data = sgqlc.types.Field(sgqlc.types.non_null(EnergyNodeEnergyConsumptionData), graphql_name='totalData')


class EnergyNodeEnergyConsumptionReportData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'timestamp')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Float)), graphql_name='data')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class EnergyNodeEnergyConsumptionReportList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(EnergyNodeEnergyConsumptionReportData)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnergyNodeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EnergyNode))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnergyNodeVaporConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'energy_node', 'fee', 'id')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    energy_node = sgqlc.types.Field(sgqlc.types.non_null(EnergyNode), graphql_name='energyNode')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class EnergyNodeVaporConsumptionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EnergyNodeVaporConsumption))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnergyNodeWaterConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'energy_node', 'fee', 'id')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    energy_node = sgqlc.types.Field(sgqlc.types.non_null(EnergyNode), graphql_name='energyNode')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class EnergyNodeWaterConsumptionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EnergyNodeWaterConsumption))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnergyTimeDistribution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('normal', 'peak', 'sharp', 'valley')
    normal = sgqlc.types.Field('TimeDistribution', graphql_name='normal')
    peak = sgqlc.types.Field('TimeDistribution', graphql_name='peak')
    sharp = sgqlc.types.Field('TimeDistribution', graphql_name='sharp')
    valley = sgqlc.types.Field('TimeDistribution', graphql_name='valley')


class EnergyTimeDistributionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EnergyTimeDistribution))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnergyTrend(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('last', 'present')
    last = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit')), graphql_name='last')
    present = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit')), graphql_name='present')


class EnumData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class EprectMold(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class EprectMoldList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EprectMold))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EprectProductionDaily(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('operation_rate', 'products', 'timestamp')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    products = sgqlc.types.Field(Float, graphql_name='products')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class EprectProductionDailyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(EprectProductionDaily), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EprectProductionRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('arguments', 'end', 'id', 'mold_code', 'mold_id', 'mold_name', 'start', 'thing_id', 'thing_name', 'yield_per_unit_time')
    arguments = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='arguments')
    end = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='end')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    mold_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='moldCode')
    mold_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='moldId')
    mold_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='moldName')
    start = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='start')
    thing_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='thingId')
    thing_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='thingName')
    yield_per_unit_time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='yieldPerUnitTime')


class EprectProductionRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EprectProductionRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ErrorType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'id', 'name')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ErrorTypeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ErrorType)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EvasionDate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('end_date', 'id', 'name', 'start_date')
    end_date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endDate')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    start_date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startDate')


class EvasionDateList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(EvasionDate))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Factory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class FactoryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Factory))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class Fee(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('energy_consumption', 'timestamp', 'value')
    energy_consumption = sgqlc.types.Field(Float, graphql_name='energyConsumption')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')


class FeeReport(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('energy_group', 'energy_type', 'fees', 'total')
    energy_group = sgqlc.types.Field(sgqlc.types.non_null(EnergyGroup), graphql_name='energyGroup')
    energy_type = sgqlc.types.Field(EnergyType, graphql_name='energyType')
    fees = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Fee)), graphql_name='fees')
    total = sgqlc.types.Field(sgqlc.types.non_null('TotalFee'), graphql_name='total')


class FeeReportList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(FeeReport)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class File(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'length', 'name', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class HistoryStatusData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp',)
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class Image(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'url')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class InspectionMethod(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('field_data', 'id', 'name', 'thing_label')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_label = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingLabel'))), graphql_name='thingLabel')


class InspectionMethodList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InspectionMethod))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class InspectionOperatorRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('cost_time', 'created_at', 'id', 'operator', 'operator_record_type', 'remark', 'restart_operator', 'turn_to')
    cost_time = sgqlc.types.Field(Int, graphql_name='costTime')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    operator_record_type = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionOperatorType), graphql_name='operatorRecordType')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    restart_operator = sgqlc.types.Field('User', graphql_name='restartOperator')
    turn_to = sgqlc.types.Field('User', graphql_name='turnTo')


class InspectionProcessItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'image', 'inspection_method', 'is_finished', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='image')
    inspection_method = sgqlc.types.Field(sgqlc.types.non_null(InspectionMethod), graphql_name='inspectionMethod')
    is_finished = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFinished')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class Issue(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('attachments', 'code', 'company', 'content', 'create_time', 'id', 'issuer', 'logs', 'owner', 'status', 'title', 'type', 'update_time')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='attachments')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company = sgqlc.types.Field(Company, graphql_name='company')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createTime')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issuer = sgqlc.types.Field('User', graphql_name='issuer')
    logs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('IssueLog')), graphql_name='logs')
    owner = sgqlc.types.Field('User', graphql_name='owner')
    status = sgqlc.types.Field(sgqlc.types.non_null(IssueStatus), graphql_name='status')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    type = sgqlc.types.Field(IssueType, graphql_name='type')
    update_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updateTime')


class IssueList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('close', 'data', 'dealing', 'ready', 'total_count')
    close = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='close')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Issue)), graphql_name='data')
    dealing = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dealing')
    ready = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ready')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueLog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('action', 'attachments', 'reason', 'receiver', 'remark', 'sender', 'timestamp')
    action = sgqlc.types.Field(IssueAction, graphql_name='action')
    attachments = sgqlc.types.Field(sgqlc.types.list_of(File), graphql_name='attachments')
    reason = sgqlc.types.Field(IssueReason, graphql_name='reason')
    receiver = sgqlc.types.Field('User', graphql_name='receiver')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    sender = sgqlc.types.Field('User', graphql_name='sender')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')


class LeapDailyData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('operation_rate', 'paused_duration', 'paused_times', 'timestamp')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    paused_duration = sgqlc.types.Field(Int, graphql_name='pausedDuration')
    paused_times = sgqlc.types.Field(Int, graphql_name='pausedTimes')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class LeapDailyReportList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(LeapDailyData)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class LeapOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('online', 'operation', 'operation_rate', 'operation_rate_target', 'paused', 'paused_duration', 'paused_duration_target', 'paused_times', 'paused_times_target')
    online = sgqlc.types.Field(Int, graphql_name='online')
    operation = sgqlc.types.Field(Int, graphql_name='operation')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    operation_rate_target = sgqlc.types.Field(Float, graphql_name='operationRateTarget')
    paused = sgqlc.types.Field(Int, graphql_name='paused')
    paused_duration = sgqlc.types.Field(Int, graphql_name='pausedDuration')
    paused_duration_target = sgqlc.types.Field(Int, graphql_name='pausedDurationTarget')
    paused_times = sgqlc.types.Field(Int, graphql_name='pausedTimes')
    paused_times_target = sgqlc.types.Field(Int, graphql_name='pausedTimesTarget')


class LeapTarget(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'operation_rate', 'paused_duration', 'paused_times', 'timestamp')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='operationRate')
    paused_duration = sgqlc.types.Field(Int, graphql_name='pausedDuration')
    paused_times = sgqlc.types.Field(Int, graphql_name='pausedTimes')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class LeapTargetList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(LeapTarget))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MacroBIResult(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company', 'timestamp', 'value')
    company = sgqlc.types.Field(Company, graphql_name='company')
    timestamp = sgqlc.types.Field(Timestamp, graphql_name='timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')


class MaintenanceMethod(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('field_data', 'id', 'name', 'thing_label')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    thing_label = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingLabel'))), graphql_name='thingLabel')


class MaintenanceMethodList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceMethod))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MaintenanceProcessItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'image', 'is_finished', 'maintenance_method', 'remark')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='image')
    is_finished = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFinished')
    maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(MaintenanceMethod), graphql_name='maintenanceMethod')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class MaintenanceSparePartItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null('SparePart'), graphql_name='sparePart')


class MarketApp(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('brief', 'cover_image', 'created_by', 'description', 'id', 'is_recommended', 'published_at', 'screenshot', 'title', 'type', 'updated_at')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    cover_image = sgqlc.types.Field(File, graphql_name='coverImage')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_recommended = sgqlc.types.Field(Boolean, graphql_name='isRecommended')
    published_at = sgqlc.types.Field(Timestamp, graphql_name='publishedAt')
    screenshot = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='screenshot')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketAppType), graphql_name='type')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class MarketAppList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketApp)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MarketAppSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('draft', 'published', 'total')
    draft = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='draft')
    published = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='published')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class MarketCommonComponent(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('content', 'image', 'title')
    content = sgqlc.types.Field(String, graphql_name='content')
    image = sgqlc.types.Field(File, graphql_name='image')
    title = sgqlc.types.Field(String, graphql_name='title')


class MarketIssue(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'code', 'company_name', 'contact', 'content', 'created_at', 'email', 'id', 'issue_log', 'owner', 'phone', 'solution', 'status', 'type', 'updated_at')
    app = sgqlc.types.Field(MarketApp, graphql_name='app')
    code = sgqlc.types.Field(String, graphql_name='code')
    company_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='companyName')
    contact = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contact')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issue_log = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MarketIssueLog')), graphql_name='issueLog')
    owner = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='owner')
    phone = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='phone')
    solution = sgqlc.types.Field('MarketSolution', graphql_name='solution')
    status = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueStatus), graphql_name='status')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketConsultationType), graphql_name='type')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class MarketIssueList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketIssue)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MarketIssueLog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('action', 'attachment', 'description', 'id', 'operated_at', 'receiver', 'sender')
    action = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueAction), graphql_name='action')
    attachment = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='attachment')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='operatedAt')
    receiver = sgqlc.types.Field('User', graphql_name='receiver')
    sender = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='sender')


class MarketIssueSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('close', 'dealing', 'ready')
    close = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='close')
    dealing = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dealing')
    ready = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ready')


class MarketSolution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'brief', 'cover_image', 'created_by', 'description', 'detail', 'id', 'is_recommended', 'published_at', 'title', 'type', 'updated_at')
    app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketApp)), graphql_name='app')
    brief = sgqlc.types.Field(String, graphql_name='brief')
    cover_image = sgqlc.types.Field(File, graphql_name='coverImage')
    created_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createdBy')
    description = sgqlc.types.Field(String, graphql_name='description')
    detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('MarketSolutionDetail')), graphql_name='detail')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_recommended = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRecommended')
    published_at = sgqlc.types.Field(Timestamp, graphql_name='publishedAt')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    type = sgqlc.types.Field(sgqlc.types.non_null(MarketSolutionType), graphql_name='type')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class MarketSolutionDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('content', 'image', 'items', 'title', 'type')
    content = sgqlc.types.Field(String, graphql_name='content')
    image = sgqlc.types.Field(File, graphql_name='image')
    items = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketCommonComponent)), graphql_name='items')
    title = sgqlc.types.Field(String, graphql_name='title')
    type = sgqlc.types.Field(sgqlc.types.non_null(CardType), graphql_name='type')


class MarketSolutionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(MarketSolution)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MarketSolutionSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('draft', 'published', 'total')
    draft = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='draft')
    published = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='published')
    total = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='total')


class Material(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('category', 'code', 'field_data', 'id', 'name', 'property', 'specification', 'unit', 'versions')
    category = sgqlc.types.Field('MaterialCategory', graphql_name='category')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    property = sgqlc.types.Field(sgqlc.types.non_null(MaterialProperty), graphql_name='property')
    specification = sgqlc.types.Field(String, graphql_name='specification')
    unit = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='unit')
    versions = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='versions')


class MaterialCategory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'property')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    property = sgqlc.types.Field(sgqlc.types.non_null(MaterialProperty), graphql_name='property')


class MaterialCategoryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaterialCategory))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MaterialList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Material))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MeterReadingDataList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_data')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(DailyMeterReadingData))), graphql_name='data')
    total_data = sgqlc.types.Field(sgqlc.types.non_null('TotalDataMeterReadingData'), graphql_name='totalData')


class Mutation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('_eam', '_ems', '_plm', 'accept_thing_calibrate', 'accept_thing_inspection', 'accept_thing_maintenance', 'accept_thing_repair', 'activate_user', 'add_bom_material', 'add_company_apps', 'add_product_task', 'add_project_document', 'add_project_group_member', 'add_thing_borrow_draft', 'add_thing_change_borrow_draft', 'approve_change_borrow', 'approve_thing_borrow', 'approve_thing_calibrate', 'approve_thing_maintenance', 'approve_thing_repair', 'confirm_borrow', 'confirm_return', 'create_adapter_key', 'create_alert_rule', 'create_app', 'create_business_knowledge', 'create_business_knowledge_type', 'create_calibrate_organization', 'create_calibrate_schedule', 'create_change_borrow_approve_configuration', 'create_cockpit_aggregation', 'create_cockpit_key', 'create_cockpit_target', 'create_company', 'create_company_admin_user', 'create_company_bidatasource', 'create_department', 'create_depository', 'create_eam_file', 'create_eam_files', 'create_education_issue', 'create_energy_group', 'create_energy_node', 'create_error_type', 'create_evasion_date', 'create_factory', 'create_file', 'create_files', 'create_help_issue', 'create_image', 'create_images', 'create_inspection_method', 'create_leap_target', 'create_maintenance_method', 'create_market_app', 'create_market_file', 'create_market_files', 'create_market_issue', 'create_market_solution', 'create_material', 'create_material_category', 'create_outside_calibrate', 'create_pdm_file', 'create_pdm_files', 'create_plm_file', 'create_plm_files', 'create_product_flow', 'create_product_project', 'create_project_group', 'create_report', 'create_role', 'create_source_key', 'create_spare_part', 'create_spare_part_outbound', 'create_spare_part_receipt', 'create_spare_part_writeoff', 'create_system_issue', 'create_task_bom', 'create_thing', 'create_thing_borrow_approve_configuration', 'create_thing_borrow_by_draft', 'create_thing_calibrate', 'create_thing_calibrate_workflow_configuration', 'create_thing_category', 'create_thing_change_borrow_by_draft', 'create_thing_group', 'create_thing_input_record', 'create_thing_inspection', 'create_thing_inspection_workflow_configuration', 'create_thing_label', 'create_thing_maintenance', 'create_thing_maintenance_workflow_configuration', 'create_thing_repair', 'create_thing_repair_workflow_configuration', 'create_thing_schedule', 'create_thing_specification_language', 'create_thing_specification_language_property', 'create_thing_status', 'create_thing_type', 'create_user', 'create_worker_orders', 'debug_adapter_key', 'delete_adapter_keys', 'delete_alert_rule', 'delete_app', 'delete_bom', 'delete_business_knowledge', 'delete_business_knowledge_type', 'delete_calibrate_organization', 'delete_calibrate_schedule', 'delete_change_borrow_approve_configuration', 'delete_cockpit_aggregations', 'delete_cockpit_keys', 'delete_cockpit_target', 'delete_comba_data', 'delete_companies', 'delete_company_admin_users', 'delete_company_apps', 'delete_company_bidatasource', 'delete_company_thing_specification_language', 'delete_company_thing_type', 'delete_department', 'delete_department_thing_groups', 'delete_depository', 'delete_energy_groups', 'delete_energy_node', 'delete_error_type', 'delete_evasion_date', 'delete_factory', 'delete_inspection_method', 'delete_leap_target', 'delete_maintenance_method', 'delete_market_app', 'delete_market_solution', 'delete_material', 'delete_material_category', 'delete_outside_calibrate', 'delete_product_flow', 'delete_project_group', 'delete_role', 'delete_source_keys', 'delete_spare_part', 'delete_table_fields_config', 'delete_thing', 'delete_thing_access_config', 'delete_thing_borrow_approve_configuration', 'delete_thing_borrow_draft_thing', 'delete_thing_calibrate_workflow_configuration', 'delete_thing_category', 'delete_thing_change_borrow_draft_thing', 'delete_thing_group', 'delete_thing_input_record', 'delete_thing_inspection_workflow_configuration', 'delete_thing_label', 'delete_thing_maintenance_workflow_configuration', 'delete_thing_repair_workflow_configuration', 'delete_thing_schedule', 'delete_thing_specification_language', 'delete_thing_specification_language_property', 'delete_thing_statuses', 'delete_thing_task', 'delete_thing_thing_specification_language', 'delete_thing_types', 'delete_user_thing_groups', 'delete_users', 'duplicate_uccform_structure', 'end_product_project', 'finish_thing_inspection', 'finish_thing_maintenance', 'finish_thing_repair', 'finish_worker_order', 'forbidden_user', 'import_comba_data', 'import_inspection_method', 'import_maintenance_method', 'import_meter_reading_data', 'import_spare_part', 'import_thing', 'import_thing_category', 'import_thing_label', 'import_thing_schedule', 'import_thing_schedule_thing', 'import_thing_spare_part', 'import_user', 'login', 'logout', 'move_things', 'notify_energy_consumption', 'oauth_authorize', 'pause_thing_maintenance', 'pause_thing_repair', 'publish_market_app', 'publish_market_solution', 'read_all_notification', 'read_notification', 'register_user', 'reject_change_borrow', 'reject_thing_borrow', 'reject_thing_calibrate', 'reject_thing_maintenance', 'reject_thing_repair', 'remark_worker_order', 'remove_bom_material', 'remove_calibrate_thing_category', 'remove_project_document', 'remove_project_group_member', 'remove_thing_function_department', 'reset_password', 'restart_thing_inspection', 'restart_thing_maintenance', 'restart_thing_repair', 'restore_user', 'save_thing_calibrate', 'save_thing_inspection', 'save_thing_maintenance', 'save_thing_repair', 'set_calibrate_thing_category', 'set_company_admin_permission', 'set_company_electricity_price', 'set_company_energy_offset_threshold', 'set_company_thing_specification_language', 'set_company_thing_type', 'set_company_vapor_price', 'set_company_water_price', 'set_department_thing_group', 'set_departments_thing_group', 'set_outside_calibrate_thing_calibrate', 'set_project_product', 'set_quick_access_app', 'set_role_thing_category', 'set_single_department_thing_groups', 'set_single_user_thing_groups', 'set_spare_part_thing', 'set_sub_thing', 'set_table_fields_config', 'set_thing_access_config', 'set_thing_calibrate', 'set_thing_function_department', 'set_thing_schedule_thing', 'set_thing_spare_part', 'set_thing_specification_language_thing', 'set_thing_thing_specification_language', 'set_third_party_app_permission', 'set_uccform_structure', 'set_users_thing_group', 'set_workbench', 'start_product_project', 'submit_change_borrow', 'submit_thing_borrow', 'submit_thing_calibrate', 'turn_to_thing_calibrate', 'turn_to_thing_inspection', 'turn_to_thing_maintenance', 'turn_to_thing_repair', 'turn_worker_order', 'update_adapter_key', 'update_alert_rule', 'update_app', 'update_bom', 'update_bom_material', 'update_business_knowledge', 'update_business_knowledge_type', 'update_calibrate_organization', 'update_calibrate_schedule', 'update_change_borrow_approve_configuration', 'update_cockpit_aggregation', 'update_cockpit_key', 'update_cockpit_target', 'update_company', 'update_company_admin_user', 'update_company_energy_thing', 'update_company_energy_thing_group', 'update_department', 'update_department_thing_group', 'update_depository', 'update_education_issue', 'update_energy_group', 'update_energy_node', 'update_energy_time_distribution', 'update_error_type', 'update_evasion_date', 'update_factory', 'update_help_issue', 'update_inspection_method', 'update_leap_target', 'update_maintenance_method', 'update_market_app', 'update_market_issue', 'update_market_solution', 'update_material', 'update_material_category', 'update_me', 'update_my_company', 'update_my_password', 'update_notification_config', 'update_outside_calibrate', 'update_product_flow', 'update_product_task', 'update_project_document', 'update_project_group', 'update_report', 'update_role', 'update_source_key', 'update_spare_part', 'update_system_issue', 'update_thing', 'update_thing_borrow_approve_configuration', 'update_thing_borrow_by_draft', 'update_thing_borrow_draft_thing', 'update_thing_calibrate_workflow_configuration', 'update_thing_category', 'update_thing_change_borrow_by_draft', 'update_thing_change_borrow_draft_thing', 'update_thing_function_departments', 'update_thing_group', 'update_thing_input_record', 'update_thing_inspection_workflow_configuration', 'update_thing_label', 'update_thing_maintenance_workflow_configuration', 'update_thing_repair_workflow_configuration', 'update_thing_schedule', 'update_thing_specification_language', 'update_thing_specification_language_property', 'update_thing_status', 'update_thing_task', 'update_thing_type', 'update_things', 'update_user', 'update_user_thing_group', 'update_workflow_base_configuration', 'visit_app')
    _eam = sgqlc.types.Field(Boolean, graphql_name='_eam')
    _ems = sgqlc.types.Field(Boolean, graphql_name='_ems')
    _plm = sgqlc.types.Field(Boolean, graphql_name='_plm')
    accept_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='acceptThingCalibrate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    accept_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='acceptThingInspection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    accept_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='acceptThingMaintenance', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    accept_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='acceptThingRepair', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    activate_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='activateUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ActivateUserInput), graphql_name='input', default=None)),
))
    )
    add_bom_material = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addBomMaterial', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddBomMaterialInput), graphql_name='input', default=None)),
))
    )
    add_company_apps = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addCompanyApps', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddCompanyAppsInput), graphql_name='input', default=None)),
))
    )
    add_product_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addProductTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddProductTaskInput), graphql_name='input', default=None)),
))
    )
    add_project_document = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addProjectDocument', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddProjectDocumentInput), graphql_name='input', default=None)),
))
    )
    add_project_group_member = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addProjectGroupMember', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddProjectGroupMemberInput), graphql_name='input', default=None)),
))
    )
    add_thing_borrow_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addThingBorrowDraft', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddThingBorrowDraftInput), graphql_name='input', default=None)),
))
    )
    add_thing_change_borrow_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='addThingChangeBorrowDraft', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddThingChangeBorrowDraftInput), graphql_name='input', default=None)),
))
    )
    approve_change_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='approveChangeBorrow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApproveChangeBorrowInput), graphql_name='input', default=None)),
))
    )
    approve_thing_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='approveThingBorrow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApproveThingBorrowInput), graphql_name='input', default=None)),
))
    )
    approve_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='approveThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ApproveThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    approve_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='approveThingMaintenance', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    approve_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='approveThingRepair', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    confirm_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='confirmBorrow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConfirmBorrowInput), graphql_name='input', default=None)),
))
    )
    confirm_return = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='confirmReturn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConfirmReturnInput), graphql_name='input', default=None)),
))
    )
    create_adapter_key = sgqlc.types.Field(AdapterKey, graphql_name='createAdapterKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateAdapterKeyInput), graphql_name='input', default=None)),
))
    )
    create_alert_rule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createAlertRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateAlertRuleInput), graphql_name='input', default=None)),
))
    )
    create_app = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateAppInput), graphql_name='input', default=None)),
))
    )
    create_business_knowledge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createBusinessKnowledge', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateBusinessKnowledgeInput), graphql_name='input', default=None)),
))
    )
    create_business_knowledge_type = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createBusinessKnowledgeType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateBusinessKnowledgeTypeInput), graphql_name='input', default=None)),
))
    )
    create_calibrate_organization = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createCalibrateOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCalibrateOrganizationInput), graphql_name='input', default=None)),
))
    )
    create_calibrate_schedule = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createCalibrateSchedule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCalibrateScheduleInput), graphql_name='input', default=None)),
))
    )
    create_change_borrow_approve_configuration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createChangeBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateChangeBorrowApproveConfigurationInput, graphql_name='input', default=None)),
))
    )
    create_cockpit_aggregation = sgqlc.types.Field(CockpitAggregation, graphql_name='createCockpitAggregation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCockpitAggregation), graphql_name='input', default=None)),
))
    )
    create_cockpit_key = sgqlc.types.Field(CockpitKey, graphql_name='createCockpitKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCockpitKey), graphql_name='input', default=None)),
))
    )
    create_cockpit_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createCockpitTarget', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateCockpitTargetInput))), graphql_name='input', default=None)),
))
    )
    create_company = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createCompany', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCompanyInput), graphql_name='input', default=None)),
))
    )
    create_company_admin_user = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createCompanyAdminUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateCompanyAdminUserInput, graphql_name='input', default=None)),
))
    )
    create_company_bidatasource = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createCompanyBIDatasource', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCompanyBIDatasourceInput), graphql_name='input', default=None)),
))
    )
    create_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createDepartment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateDepartmentInput, graphql_name='input', default=None)),
))
    )
    create_depository = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createDepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateDepositoryInput), graphql_name='input', default=None)),
))
    )
    create_eam_file = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='createEamFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEamFileInput), graphql_name='input', default=None)),
))
    )
    create_eam_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createEamFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateEamFileInput))), graphql_name='input', default=None)),
))
    )
    create_education_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='createEducationIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateIssueInput, graphql_name='input', default=None)),
))
    )
    create_energy_group = sgqlc.types.Field(EnergyGroup, graphql_name='createEnergyGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEnergyGroup), graphql_name='input', default=None)),
))
    )
    create_energy_node = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createEnergyNode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEnergyNodeInput), graphql_name='input', default=None)),
))
    )
    create_error_type = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createErrorType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateErrorTypeInput), graphql_name='input', default=None)),
))
    )
    create_evasion_date = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createEvasionDate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEvasionDateInput), graphql_name='input', default=None)),
))
    )
    create_factory = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createFactory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFactoryInput), graphql_name='input', default=None)),
))
    )
    create_file = sgqlc.types.Field(File, graphql_name='createFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFileInput), graphql_name='input', default=None)),
))
    )
    create_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateFileInput)), graphql_name='input', default=None)),
))
    )
    create_help_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='createHelpIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateIssueInput, graphql_name='input', default=None)),
))
    )
    create_image = sgqlc.types.Field(Image, graphql_name='createImage', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateImageInput), graphql_name='input', default=None)),
))
    )
    create_images = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Image)), graphql_name='createImages', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateImageInput)), graphql_name='input', default=None)),
))
    )
    create_inspection_method = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createInspectionMethod', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateInspectionMethodInput), graphql_name='input', default=None)),
))
    )
    create_leap_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createLeapTarget', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateLeapTargetInput))), graphql_name='input', default=None)),
))
    )
    create_maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createMaintenanceMethod', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMaintenanceMethodInput), graphql_name='input', default=None)),
))
    )
    create_market_app = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createMarketApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketAppInput), graphql_name='input', default=None)),
))
    )
    create_market_file = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='createMarketFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketFileInput), graphql_name='input', default=None)),
))
    )
    create_market_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createMarketFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CreateMarketFileInput)), graphql_name='input', default=None)),
))
    )
    create_market_issue = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createMarketIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketIssueInput), graphql_name='input', default=None)),
))
    )
    create_market_solution = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createMarketSolution', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMarketSolutionInput), graphql_name='input', default=None)),
))
    )
    create_material = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createMaterial', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMaterialInput), graphql_name='input', default=None)),
))
    )
    create_material_category = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createMaterialCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMaterialCategoryInput), graphql_name='input', default=None)),
))
    )
    create_outside_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createOutsideCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateOutsideCalibrateInput), graphql_name='input', default=None)),
))
    )
    create_pdm_file = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='createPdmFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFileInput), graphql_name='input', default=None)),
))
    )
    create_pdm_files = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='createPdmFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreateFileInput))), graphql_name='input', default=None)),
))
    )
    create_plm_file = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='createPlmFile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreatePlmFileInput), graphql_name='input', default=None)),
))
    )
    create_plm_files = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='createPlmFiles', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CreatePlmFileInput))), graphql_name='input', default=None)),
))
    )
    create_product_flow = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createProductFlow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProductFlowInput), graphql_name='input', default=None)),
))
    )
    create_product_project = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createProductProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProductProjectInput), graphql_name='input', default=None)),
))
    )
    create_project_group = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createProjectGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectGroupInput), graphql_name='input', default=None)),
))
    )
    create_report = sgqlc.types.Field('RawData', graphql_name='createReport', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateReportInput), graphql_name='input', default=None)),
))
    )
    create_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRoleInput), graphql_name='input', default=None)),
))
    )
    create_source_key = sgqlc.types.Field('SourceKey', graphql_name='createSourceKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSourceKeyInput), graphql_name='input', default=None)),
))
    )
    create_spare_part = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createSparePart', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartInput), graphql_name='input', default=None)),
))
    )
    create_spare_part_outbound = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createSparePartOutbound', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartOutboundInput), graphql_name='input', default=None)),
))
    )
    create_spare_part_receipt = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createSparePartReceipt', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartReceiptInput), graphql_name='input', default=None)),
))
    )
    create_spare_part_writeoff = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createSparePartWriteoff', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateSparePartWriteoffInput), graphql_name='input', default=None)),
))
    )
    create_system_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='createSystemIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateIssueInput, graphql_name='input', default=None)),
))
    )
    create_task_bom = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createTaskBom', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTaskBomInput), graphql_name='input', default=None)),
))
    )
    create_thing = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingInput), graphql_name='input', default=None)),
))
    )
    create_thing_borrow_approve_configuration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateThingBorrowApproveConfigurationInput, graphql_name='input', default=None)),
))
    )
    create_thing_borrow_by_draft = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='createThingBorrowByDraft', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('reason', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='reason', default=None)),
))
    )
    create_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='createThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    create_thing_calibrate_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingCalibrateWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateThingCalibrateWorkflowConfigurationInput, graphql_name='input', default=None)),
))
    )
    create_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingCategoryInput), graphql_name='input', default=None)),
))
    )
    create_thing_change_borrow_by_draft = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='createThingChangeBorrowByDraft', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('reason', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='reason', default=None)),
))
    )
    create_thing_group = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='createThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingGroupInput), graphql_name='input', default=None)),
))
    )
    create_thing_input_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createThingInputRecord', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingInputRecordInput), graphql_name='input', default=None)),
))
    )
    create_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingInspection', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingInspectionInput), graphql_name='input', default=None)),
))
    )
    create_thing_inspection_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingInspectionWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateThingInspectionWorkflowConfigurationInput, graphql_name='input', default=None)),
))
    )
    create_thing_label = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingLabel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingLabelInput), graphql_name='input', default=None)),
))
    )
    create_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    create_thing_maintenance_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingMaintenanceWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateThingMaintenanceWorkflowConfigurationInput, graphql_name='input', default=None)),
))
    )
    create_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingRepairInput), graphql_name='input', default=None)),
))
    )
    create_thing_repair_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingRepairWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateThingRepairWorkflowConfigurationInput, graphql_name='input', default=None)),
))
    )
    create_thing_schedule = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='createThingSchedule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingScheduleInput), graphql_name='input', default=None)),
))
    )
    create_thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingSpecificationLanguage', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingSpecificationLanguageInput), graphql_name='input', default=None)),
))
    )
    create_thing_specification_language_property = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='createThingSpecificationLanguageProperty', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingSpecificationLanguagePropertyInput), graphql_name='input', default=None)),
))
    )
    create_thing_status = sgqlc.types.Field('ThingStatus', graphql_name='createThingStatus', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingStatus), graphql_name='input', default=None)),
))
    )
    create_thing_type = sgqlc.types.Field('ThingType', graphql_name='createThingType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateThingTypeInput), graphql_name='input', default=None)),
))
    )
    create_user = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='createUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserInput), graphql_name='input', default=None)),
))
    )
    create_worker_orders = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createWorkerOrders', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateWorkerOrdersInput), graphql_name='input', default=None)),
))
    )
    debug_adapter_key = sgqlc.types.Field(JSON, graphql_name='debugAdapterKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DebugAdapterKeyInput), graphql_name='input', default=None)),
))
    )
    delete_adapter_keys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteAdapterKeys', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    delete_alert_rule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteAlertRule', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    delete_app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='deleteApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_bom = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteBom', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_business_knowledge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteBusinessKnowledge', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    delete_business_knowledge_type = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteBusinessKnowledgeType', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    delete_calibrate_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCalibrateOrganization', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_calibrate_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCalibrateSchedule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_change_borrow_approve_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteChangeBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_cockpit_aggregations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteCockpitAggregations', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    delete_cockpit_keys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteCockpitKeys', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    delete_cockpit_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCockpitTarget', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_comba_data = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCombaData', args=sgqlc.types.ArgDict((
        ('data_type', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CombaDataType))), graphql_name='dataType', default=None)),
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    delete_companies = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanies', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteCompaniesInput), graphql_name='input', default=None)),
))
    )
    delete_company_admin_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyAdminUsers', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(DeleteCompanyAdminUsersInput, graphql_name='input', default=None)),
))
    )
    delete_company_apps = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyApps', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteCompanyAppsInput), graphql_name='input', default=None)),
))
    )
    delete_company_bidatasource = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyBIDatasource', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_company_thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyThingSpecificationLanguage', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_company_thing_type = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteCompanyThingType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteDepartment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    delete_department_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteDepartmentThingGroups', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteDepartmentThingGroupInput), graphql_name='input', default=None)),
))
    )
    delete_depository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteDepository', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_energy_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteEnergyGroups', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    delete_energy_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteEnergyNode', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_error_type = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteErrorType', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='ids', default=None)),
))
    )
    delete_evasion_date = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteEvasionDate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_factory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteFactory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_inspection_method = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteInspectionMethod', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_leap_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteLeapTarget', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMaintenanceMethod', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_market_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMarketApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_market_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMarketSolution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_material = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMaterial', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_material_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteMaterialCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_outside_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteOutsideCalibrate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_product_flow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteProductFlow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_project_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteProjectGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteRole', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_source_keys = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteSourceKeys', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    delete_spare_part = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteSparePart', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_table_fields_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteTableFieldsConfig', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    delete_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThing', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_thing_access_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingAccessConfig', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_borrow_approve_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_borrow_draft_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingBorrowDraftThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteThingBorrowDraftThingInput), graphql_name='input', default=None)),
))
    )
    delete_thing_calibrate_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingCalibrateWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_change_borrow_draft_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingChangeBorrowDraftThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteThingChangeBorrowDraftThingInput), graphql_name='input', default=None)),
))
    )
    delete_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingGroup', args=sgqlc.types.ArgDict((
        ('thing_group', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='thingGroup', default=None)),
))
    )
    delete_thing_input_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingInputRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_thing_inspection_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingInspectionWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_label = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingLabel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_maintenance_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingMaintenanceWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_repair_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingRepairWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingSchedule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingSpecificationLanguage', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_specification_language_property = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingSpecificationLanguageProperty', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_statuses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteThingStatuses', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    delete_thing_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingTask', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    delete_thing_thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteThingThingSpecificationLanguage', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    delete_thing_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='deleteThingTypes', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInput), graphql_name='input', default=None)),
))
    )
    delete_user_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUserThingGroups', args=sgqlc.types.ArgDict((
        ('thing_groups', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='thingGroups', default=None)),
))
    )
    delete_users = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deleteUsers', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteUsersInput), graphql_name='input', default=None)),
))
    )
    duplicate_uccform_structure = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='duplicateUCCFormStructure', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DuplicateUCCFormStructureInput), graphql_name='input', default=None)),
))
    )
    end_product_project = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='endProductProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(EndProductProject), graphql_name='input', default=None)),
))
    )
    finish_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='finishThingInspection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    finish_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='finishThingMaintenance', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    finish_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='finishThingRepair', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    finish_worker_order = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='finishWorkerOrder', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(FinishWorkerOrderInput), graphql_name='input', default=None)),
))
    )
    forbidden_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='forbiddenUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ForbiddenUserInput), graphql_name='input', default=None)),
))
    )
    import_comba_data = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='importCombaData', args=sgqlc.types.ArgDict((
        ('data_type', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CombaDataType))), graphql_name='dataType', default=None)),
        ('filename', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filename', default=None)),
))
    )
    import_inspection_method = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importInspectionMethod', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importMaintenanceMethod', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_meter_reading_data = sgqlc.types.Field(sgqlc.types.non_null(EmsImportResult), graphql_name='importMeterReadingData', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EmsImportOption), graphql_name='option', default=None)),
))
    )
    import_spare_part = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importSparePart', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThing', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing_category = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThingCategory', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing_label = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThingLabel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing_schedule = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThingSchedule', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing_schedule_thing = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThingScheduleThing', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_thing_spare_part = sgqlc.types.Field(sgqlc.types.non_null(EamImportResult), graphql_name='importThingSparePart', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
        ('option', sgqlc.types.Arg(sgqlc.types.non_null(EamImportOption), graphql_name='option', default=None)),
))
    )
    import_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='importUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateFileInput), graphql_name='input', default=None)),
))
    )
    login = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='login', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LoginInput), graphql_name='input', default=None)),
))
    )
    logout = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='logout')
    move_things = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='moveThings', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MoveThingInput), graphql_name='input', default=None)),
))
    )
    notify_energy_consumption = sgqlc.types.Field(Boolean, graphql_name='notifyEnergyConsumption', args=sgqlc.types.ArgDict((
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(IDInput))), graphql_name='ids', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    oauth_authorize = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='oauthAuthorize', args=sgqlc.types.ArgDict((
        ('client_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientId', default=None)),
        ('nonce', sgqlc.types.Arg(String, graphql_name='nonce', default=None)),
        ('state', sgqlc.types.Arg(String, graphql_name='state', default=None)),
))
    )
    pause_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='pauseThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PauseThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    pause_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='pauseThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(PauseThingRepairInput), graphql_name='input', default=None)),
))
    )
    publish_market_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='publishMarketApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    publish_market_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='publishMarketSolution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    read_all_notification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='readAllNotification', args=sgqlc.types.ArgDict((
        ('source_app', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IDInput)), graphql_name='sourceApp', default=None)),
))
    )
    read_notification = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='readNotification', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    register_user = sgqlc.types.Field(sgqlc.types.non_null(AuthInfo), graphql_name='registerUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(RegisterUserInput, graphql_name='input', default=None)),
))
    )
    reject_change_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rejectChangeBorrow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RejectChangeBorrowInput), graphql_name='input', default=None)),
))
    )
    reject_thing_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rejectThingBorrow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RejectThingBorrowInput), graphql_name='input', default=None)),
))
    )
    reject_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rejectThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RejectThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    reject_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rejectThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RejectThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    reject_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rejectThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RejectThingRepairInput), graphql_name='input', default=None)),
))
    )
    remark_worker_order = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='remarkWorkerOrder', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemarkWorkerOrderInput), graphql_name='input', default=None)),
))
    )
    remove_bom_material = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeBomMaterial', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    remove_calibrate_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeCalibrateThingCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    remove_project_document = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeProjectDocument', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    remove_project_group_member = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeProjectGroupMember', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    remove_thing_function_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='removeThingFunctionDepartment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    reset_password = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='resetPassword', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ResetPasswordInput, graphql_name='input', default=None)),
        ('scenario', sgqlc.types.Arg(ResetPasswordScenario, graphql_name='scenario', default=None)),
))
    )
    restart_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restartThingInspection', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RestartThingInspectionInput), graphql_name='input', default=None)),
))
    )
    restart_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restartThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RestartThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    restart_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restartThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RestartThingRepairInput), graphql_name='input', default=None)),
))
    )
    restore_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restoreUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RestoreUserInput), graphql_name='input', default=None)),
))
    )
    save_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='saveThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SaveThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    save_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='saveThingInspection', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SaveThingInspectionInput), graphql_name='input', default=None)),
))
    )
    save_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='saveThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SaveThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    save_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='saveThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SaveThingRepairInput), graphql_name='input', default=None)),
))
    )
    set_calibrate_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCalibrateThingCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    set_company_admin_permission = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCompanyAdminPermission', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CompanyAdminPermissionInput, graphql_name='input', default=None)),
))
    )
    set_company_electricity_price = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCompanyElectricityPrice', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetCompanyElectricityPriceInput), graphql_name='input', default=None)),
))
    )
    set_company_energy_offset_threshold = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCompanyEnergyOffsetThreshold', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetCompanyEnergyOffsetThreshold), graphql_name='input', default=None)),
))
    )
    set_company_thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCompanyThingSpecificationLanguage', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetCompanyThingSpecificationLanguageInput), graphql_name='input', default=None)),
))
    )
    set_company_thing_type = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCompanyThingType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetCompanyThingType), graphql_name='input', default=None)),
))
    )
    set_company_vapor_price = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setCompanyVaporPrice', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetCompanyVaporPrice), graphql_name='input', default=None)),
))
    )
    set_company_water_price = sgqlc.types.Field(Boolean, graphql_name='setCompanyWaterPrice', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetCompanyWaterPrice), graphql_name='input', default=None)),
))
    )
    set_department_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setDepartmentThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetDepartmentThingGroup), graphql_name='input', default=None)),
))
    )
    set_departments_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setDepartmentsThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetDepartmentThingGroupInput), graphql_name='input', default=None)),
))
    )
    set_outside_calibrate_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setOutsideCalibrateThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetOutsideCalibrateThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    set_project_product = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setProjectProduct', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetProjectProductInput), graphql_name='input', default=None)),
))
    )
    set_quick_access_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setQuickAccessApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='id', default=None)),
))
    )
    set_role_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setRoleThingCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetRoleThingCategory), graphql_name='input', default=None)),
))
    )
    set_single_department_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setSingleDepartmentThingGroups', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(SetSingleDepartmentThingGroups, graphql_name='input', default=None)),
))
    )
    set_single_user_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setSingleUserThingGroups', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetSingleUserThingGroupsInput), graphql_name='input', default=None)),
))
    )
    set_spare_part_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setSparePartThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetSparePartThingInput), graphql_name='input', default=None)),
))
    )
    set_sub_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setSubThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetSubThingInput), graphql_name='input', default=None)),
))
    )
    set_table_fields_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setTableFieldsConfig', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetTableFieldsConfigInput), graphql_name='input', default=None)),
))
    )
    set_thing_access_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingAccessConfig', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingAccessConfigInput), graphql_name='input', default=None)),
))
    )
    set_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    set_thing_function_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingFunctionDepartment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingDepartmentInput), graphql_name='input', default=None)),
))
    )
    set_thing_schedule_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingScheduleThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingScheduleThing), graphql_name='input', default=None)),
))
    )
    set_thing_spare_part = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingSparePart', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingSparePartInput), graphql_name='input', default=None)),
))
    )
    set_thing_specification_language_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingSpecificationLanguageThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingSpecificationLanguageThingInput), graphql_name='input', default=None)),
))
    )
    set_thing_thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThingThingSpecificationLanguage', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetThingThingSpecificationLanguageInput), graphql_name='input', default=None)),
))
    )
    set_third_party_app_permission = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setThirdPartyAppPermission', args=sgqlc.types.ArgDict((
        ('app_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='appID', default=None)),
        ('permission', sgqlc.types.Arg(sgqlc.types.non_null(JSONString), graphql_name='permission', default=None)),
))
    )
    set_uccform_structure = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='setUCCFormStructure', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(SetUCCFormStructureInput, graphql_name='input', default=None)),
))
    )
    set_users_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setUsersThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetUserThingGroupInput), graphql_name='input', default=None)),
))
    )
    set_workbench = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='setWorkbench', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='input', default=None)),
))
    )
    start_product_project = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='startProductProject', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    submit_change_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='submitChangeBorrow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    submit_thing_borrow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='submitThingBorrow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    submit_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='submitThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SubmitThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    turn_to_thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='turnToThingCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TurnToThingCalibrateInput), graphql_name='input', default=None)),
))
    )
    turn_to_thing_inspection = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='turnToThingInspection', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TurnToThingInspectionInput), graphql_name='input', default=None)),
))
    )
    turn_to_thing_maintenance = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='turnToThingMaintenance', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TurnToThingMaintenanceInput), graphql_name='input', default=None)),
))
    )
    turn_to_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='turnToThingRepair', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TurnToThingRepairInput), graphql_name='input', default=None)),
))
    )
    turn_worker_order = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='turnWorkerOrder', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TurnWorkerOrderInput), graphql_name='input', default=None)),
))
    )
    update_adapter_key = sgqlc.types.Field(Boolean, graphql_name='updateAdapterKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateAdapterKeyInput), graphql_name='input', default=None)),
))
    )
    update_alert_rule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateAlertRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateAlertRuleInput), graphql_name='input', default=None)),
))
    )
    update_app = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='updateApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateAppInput), graphql_name='input', default=None)),
))
    )
    update_bom = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateBom', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateBomInput), graphql_name='input', default=None)),
))
    )
    update_bom_material = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateBomMaterial', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateBomMaterialInput), graphql_name='input', default=None)),
))
    )
    update_business_knowledge = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateBusinessKnowledge', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateBusinessKnowledgeInput), graphql_name='input', default=None)),
))
    )
    update_business_knowledge_type = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateBusinessKnowledgeType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateBusinessKnowledgeTypeInput), graphql_name='input', default=None)),
))
    )
    update_calibrate_organization = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCalibrateOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCalibrateOrganizationInput), graphql_name='input', default=None)),
))
    )
    update_calibrate_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCalibrateSchedule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCalibrateScheduleInput), graphql_name='input', default=None)),
))
    )
    update_change_borrow_approve_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateChangeBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateChangeBorrowApproveConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_cockpit_aggregation = sgqlc.types.Field(Boolean, graphql_name='updateCockpitAggregation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCockpitAggregation), graphql_name='input', default=None)),
))
    )
    update_cockpit_key = sgqlc.types.Field(Boolean, graphql_name='updateCockpitKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCockpitKey), graphql_name='input', default=None)),
))
    )
    update_cockpit_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCockpitTarget', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCockpitTargetInput), graphql_name='input', default=None)),
))
    )
    update_company = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCompany', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCompanyInput), graphql_name='input', default=None)),
        ('scenario', sgqlc.types.Arg(UpdateCompanyScenario, graphql_name='scenario', default=None)),
))
    )
    update_company_admin_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCompanyAdminUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateCompanyAdminUserInput, graphql_name='input', default=None)),
))
    )
    update_company_energy_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCompanyEnergyThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCompanyEnergyThingInput), graphql_name='input', default=None)),
))
    )
    update_company_energy_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateCompanyEnergyThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCompanyEnergyThingGroupInput), graphql_name='input', default=None)),
))
    )
    update_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateDepartment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateDepartmentInput, graphql_name='input', default=None)),
))
    )
    update_department_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateDepartmentThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateDepartmentThingGroupInput), graphql_name='input', default=None)),
))
    )
    update_depository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateDepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateDepositoryInput), graphql_name='input', default=None)),
))
    )
    update_education_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='updateEducationIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateIssueInput, graphql_name='input', default=None)),
))
    )
    update_energy_group = sgqlc.types.Field(Boolean, graphql_name='updateEnergyGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnergyGroup), graphql_name='input', default=None)),
))
    )
    update_energy_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateEnergyNode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnergyNodeInput), graphql_name='input', default=None)),
))
    )
    update_energy_time_distribution = sgqlc.types.Field(EnergyTimeDistribution, graphql_name='updateEnergyTimeDistribution', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnergyTimeDistribution), graphql_name='input', default=None)),
))
    )
    update_error_type = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateErrorType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateErrorTypeInput), graphql_name='input', default=None)),
))
    )
    update_evasion_date = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateEvasionDate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEvasionDateInput), graphql_name='input', default=None)),
))
    )
    update_factory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateFactory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFactoryInput), graphql_name='input', default=None)),
))
    )
    update_help_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='updateHelpIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateIssueInput, graphql_name='input', default=None)),
))
    )
    update_inspection_method = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateInspectionMethod', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateInspectionMethodInput), graphql_name='input', default=None)),
))
    )
    update_leap_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateLeapTarget', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateLeapTargetInput), graphql_name='input', default=None)),
))
    )
    update_maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMaintenanceMethod', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMaintenanceMethodInput), graphql_name='input', default=None)),
))
    )
    update_market_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMarketApp', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMarketAppInput), graphql_name='input', default=None)),
))
    )
    update_market_issue = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMarketIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMarketIssueInput), graphql_name='input', default=None)),
))
    )
    update_market_solution = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMarketSolution', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMarketSolutionInput), graphql_name='input', default=None)),
))
    )
    update_material = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMaterial', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMaterialInput), graphql_name='input', default=None)),
))
    )
    update_material_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMaterialCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMaterialCategoryInput), graphql_name='input', default=None)),
))
    )
    update_me = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMe', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMeInput), graphql_name='input', default=None)),
))
    )
    update_my_company = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMyCompany', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateMyCompanyInput, graphql_name='input', default=None)),
))
    )
    update_my_password = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateMyPassword', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateMyPasswordInput, graphql_name='input', default=None)),
))
    )
    update_notification_config = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateNotificationConfig', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(UpdateNotificationConfigInput))), graphql_name='input', default=None)),
))
    )
    update_outside_calibrate = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateOutsideCalibrate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOutsideCalibrateInput), graphql_name='input', default=None)),
))
    )
    update_product_flow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateProductFlow', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProductFlowInput), graphql_name='input', default=None)),
))
    )
    update_product_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateProductTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProductTaskInput), graphql_name='input', default=None)),
))
    )
    update_project_document = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateProjectDocument', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectDocumentInput), graphql_name='input', default=None)),
))
    )
    update_project_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateProjectGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectGroupInput), graphql_name='input', default=None)),
))
    )
    update_report = sgqlc.types.Field('RawData', graphql_name='updateReport', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateReportInput), graphql_name='input', default=None)),
))
    )
    update_role = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRoleInput), graphql_name='input', default=None)),
))
    )
    update_source_key = sgqlc.types.Field(Boolean, graphql_name='updateSourceKey', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSourceKeyInput), graphql_name='input', default=None)),
))
    )
    update_spare_part = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateSparePart', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSparePartInput), graphql_name='input', default=None)),
))
    )
    update_system_issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='updateSystemIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateIssueInput, graphql_name='input', default=None)),
))
    )
    update_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingInput), graphql_name='input', default=None)),
))
    )
    update_thing_borrow_approve_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateThingBorrowApproveConfigurationInput, graphql_name='input', default=None)),
))
    )
    update_thing_borrow_by_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingBorrowByDraft', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(String, graphql_name='code', default=None)),
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
))
    )
    update_thing_borrow_draft_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingBorrowDraftThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingBorrowDraftThingInput), graphql_name='input', default=None)),
))
    )
    update_thing_calibrate_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingCalibrateWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(UpdateThingCalibrateWorkflowConfigurationInput, graphql_name='input', default=None)),
))
    )
    update_thing_category = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingCategoryInput), graphql_name='input', default=None)),
))
    )
    update_thing_change_borrow_by_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingChangeBorrowByDraft', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(String, graphql_name='code', default=None)),
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('reason', sgqlc.types.Arg(String, graphql_name='reason', default=None)),
))
    )
    update_thing_change_borrow_draft_thing = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingChangeBorrowDraftThing', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingChangeBorrowDraftThingInput), graphql_name='input', default=None)),
))
    )
    update_thing_function_departments = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingFunctionDepartments', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingFunctionDepartmentsInput), graphql_name='input', default=None)),
))
    )
    update_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingGroupInput), graphql_name='input', default=None)),
))
    )
    update_thing_input_record = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingInputRecord', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingInputRecordInput), graphql_name='input', default=None)),
))
    )
    update_thing_inspection_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingInspectionWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingInspectionWorkflowConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_thing_label = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingLabel', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingLabelInput), graphql_name='input', default=None)),
))
    )
    update_thing_maintenance_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingMaintenanceWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingMaintenanceWorkflowConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_thing_repair_workflow_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingRepairWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingRepairWorkflowConfigurationInput), graphql_name='input', default=None)),
))
    )
    update_thing_schedule = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingSchedule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingScheduleInput), graphql_name='input', default=None)),
))
    )
    update_thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingSpecificationLanguage', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingSpecificationLanguageInput), graphql_name='input', default=None)),
))
    )
    update_thing_specification_language_property = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingSpecificationLanguageProperty', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingSpecificationLanguagePropertyInput), graphql_name='input', default=None)),
))
    )
    update_thing_status = sgqlc.types.Field(Boolean, graphql_name='updateThingStatus', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingStatus), graphql_name='input', default=None)),
))
    )
    update_thing_task = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThingTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingTaskInput), graphql_name='input', default=None)),
))
    )
    update_thing_type = sgqlc.types.Field(Boolean, graphql_name='updateThingType', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingTypeInput), graphql_name='input', default=None)),
))
    )
    update_things = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateThings', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateThingsInput), graphql_name='input', default=None)),
))
    )
    update_user = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserInput), graphql_name='input', default=None)),
))
    )
    update_user_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateUserThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserThingGroupInput), graphql_name='input', default=None)),
))
    )
    update_workflow_base_configuration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='updateWorkflowBaseConfiguration', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateWorkflowBaseConfigurationInput), graphql_name='input', default=None)),
))
    )
    visit_app = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visitApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )


class Notification(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('content', 'created_at', 'id', 'is_read', 'kind', 'source_app', 'url')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_read = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRead')
    kind = sgqlc.types.Field(sgqlc.types.non_null(NotificationKind), graphql_name='kind')
    source_app = sgqlc.types.Field(App, graphql_name='sourceApp')
    url = sgqlc.types.Field(String, graphql_name='url')


class NotificationConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('description', 'id', 'kind', 'name', 'receiver_role', 'receiver_user', 'source_app', 'template', 'to_email', 'to_inbox')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    kind = sgqlc.types.Field(sgqlc.types.non_null(NotificationKind), graphql_name='kind')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    receiver_role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Role'))), graphql_name='receiverRole')
    receiver_user = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='receiverUser')
    source_app = sgqlc.types.Field(App, graphql_name='sourceApp')
    template = sgqlc.types.Field(sgqlc.types.non_null('NotificationTemplate'), graphql_name='template')
    to_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='toEmail')
    to_inbox = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='toInbox')


class NotificationConfigList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(NotificationConfig))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class NotificationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'read_count', 'total_count', 'unread_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Notification))), graphql_name='data')
    read_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='readCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    unread_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='unreadCount')


class NotificationTemplate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('email', 'inbox')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    inbox = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='inbox')


class NumberByOrganziation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('num', 'organization')
    num = sgqlc.types.Field(Int, graphql_name='num')
    organization = sgqlc.types.Field('ThingGroup', graphql_name='organization')


class NumberByThingType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('num', 'type')
    num = sgqlc.types.Field(Int, graphql_name='num')
    type = sgqlc.types.Field('ThingType', graphql_name='type')


class OutsideCalibrate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('apply_for_at', 'calibrate_at', 'calibrate_organization', 'id', 'name', 'pay_at', 'pay_status', 'thing_calibrate')
    apply_for_at = sgqlc.types.Field(Timestamp, graphql_name='applyForAt')
    calibrate_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='calibrateAt')
    calibrate_organization = sgqlc.types.Field(sgqlc.types.non_null(CalibrateOrganization), graphql_name='calibrateOrganization')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pay_at = sgqlc.types.Field(Timestamp, graphql_name='payAt')
    pay_status = sgqlc.types.Field(OutsideCalibratePayStatus, graphql_name='payStatus')
    thing_calibrate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='thingCalibrate')


class OutsideCalibrateList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(OutsideCalibrate))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ParetoTimeseries(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('accumulative', 'timestamp', 'value')
    accumulative = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='accumulative')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    value = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='value')


class PermDataRange(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Permission(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'data_range_code', 'data_range_code_options', 'desc', 'id', 'is_open', 'name', 'type', 'weakrefs')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    data_range_code = sgqlc.types.Field(String, graphql_name='dataRangeCode')
    data_range_code_options = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermDataRange)), graphql_name='dataRangeCodeOptions')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_open = sgqlc.types.Field(Boolean, graphql_name='isOpen')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    type = sgqlc.types.Field(sgqlc.types.non_null(PermissionType), graphql_name='type')
    weakrefs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='weakrefs')


class PermissionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Permission))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProductFlow(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name', 'task_template')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    task_template = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProductTaskTemplate'))), graphql_name='taskTemplate')


class ProductProject(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'category', 'code', 'create_by', 'created_at', 'description', 'end_attachment', 'end_description', 'field_data', 'id', 'name', 'plan_start_at', 'product', 'project_group', 'released_bom', 'status')
    attachment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='attachment')
    category = sgqlc.types.Field(sgqlc.types.non_null(ProductProjectCategory), graphql_name='category')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    create_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createBy')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    end_attachment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='endAttachment')
    end_description = sgqlc.types.Field(String, graphql_name='endDescription')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    plan_start_at = sgqlc.types.Field(Timestamp, graphql_name='planStartAt')
    product = sgqlc.types.Field(Material, graphql_name='product')
    project_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectGroup'))), graphql_name='projectGroup')
    released_bom = sgqlc.types.Field(Bom, graphql_name='releasedBom')
    status = sgqlc.types.Field(sgqlc.types.non_null(ProductProjectStatus), graphql_name='status')


class ProductProjectDocument(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('document', 'id', 'phase', 'project', 'task')
    document = sgqlc.types.Field(sgqlc.types.non_null(File), graphql_name='document')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    phase = sgqlc.types.Field(sgqlc.types.non_null(ProductProjectDocumentPhase), graphql_name='phase')
    project = sgqlc.types.Field(sgqlc.types.non_null(ProductProject), graphql_name='project')
    task = sgqlc.types.Field('ProductTask', graphql_name='task')


class ProductProjectDocumentList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductProjectDocument))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProductProjectList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductProject))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProductStockCount(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('count', 'production_code', 'production_description')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    production_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='productionCode')
    production_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='productionDescription')


class ProductTask(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('bom', 'executive', 'id', 'name', 'output_attachment', 'participant', 'plan_end_at', 'plan_start_at', 'product_project')
    bom = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Bom))), graphql_name='bom')
    executive = sgqlc.types.Field('User', graphql_name='executive')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    output_attachment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='outputAttachment')
    participant = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='participant')
    plan_end_at = sgqlc.types.Field(Timestamp, graphql_name='planEndAt')
    plan_start_at = sgqlc.types.Field(Timestamp, graphql_name='planStartAt')
    product_project = sgqlc.types.Field(sgqlc.types.non_null(ProductProject), graphql_name='productProject')


class ProductTaskDocument(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'id', 'task')
    attachment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='attachment')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    task = sgqlc.types.Field(sgqlc.types.non_null(ProductTask), graphql_name='task')


class ProductTaskList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductTask))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProductTaskTemplate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ProductWorkingTime(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('count', 'production_code')
    count = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='count')
    production_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='productionCode')


class ProductWorkingTimeSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductWorkingTime))), graphql_name='data')


class ProjectGroup(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ProjectGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProjectGroup))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectGroupMember(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'member', 'project_group')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    member = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='member')
    project_group = sgqlc.types.Field(sgqlc.types.non_null(ProjectGroup), graphql_name='projectGroup')


class Province(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class Query(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('_eam', '_ems', '_plm', 'account_exists', 'adapter_key', 'adapter_key_list', 'adapter_model_key_list', 'alert_detail', 'alert_level_summary', 'alert_list', 'alert_rule', 'alert_rule_list', 'alert_tendency_summary', 'alert_top_rule_summary', 'alert_top_thing_summary', 'app', 'app_config', 'app_list', 'app_users', 'area_bottleneck_by_company', 'area_bottlenecks', 'area_energy_consumption', 'area_energy_consumption_by_company', 'area_energy_consumption_overall', 'area_energy_consumption_rank', 'area_energy_per_product_rank', 'area_peak_power', 'area_peak_rate_by_company', 'area_power_on_rate_rank', 'area_production', 'area_production_by_company', 'area_production_distribution', 'area_redundant_by_company', 'area_redundants', 'area_things_overall', 'bi_energy_device', 'bi_energy_electric_quantity', 'bi_energy_fee', 'bi_energy_operation_time', 'bi_issue_issue', 'bi_macro_electric_quantity', 'bi_macro_peak_rate', 'bom', 'bom_list', 'bom_material_list', 'business_knowledge', 'business_knowledge_list', 'business_knowledge_type', 'business_knowledge_type_list', 'calibrate_organization', 'calibrate_organization_list', 'calibrate_schedule', 'calibrate_schedule_list', 'change_borrow', 'change_borrow_approve_configuration', 'change_borrow_approve_configuration_list', 'change_borrow_default_approve_configuration_list', 'change_borrow_item', 'change_borrow_item_list', 'change_borrow_list', 'change_borrow_operator_record_list', 'change_borrow_state_overview', 'check_alter_department_thing_group', 'check_delete_department', 'cities', 'city_companies', 'cnc_alert_list', 'cnc_alert_overall', 'cnc_alerts', 'cnc_current_alerts', 'cnc_overall', 'cockpit_aggregation', 'cockpit_aggregations', 'cockpit_key', 'cockpit_key_list', 'cockpit_oee', 'cockpit_operation_rate', 'cockpit_organization_oeerank', 'cockpit_organization_operation_rate_rank', 'cockpit_organization_performance_rate_rank', 'cockpit_organization_yield_rate_rank', 'cockpit_overall', 'cockpit_performance_rate', 'cockpit_rate_list', 'cockpit_rate_overall', 'cockpit_target_list', 'cockpit_thing', 'cockpit_thing_list', 'cockpit_thing_type_oeerank', 'cockpit_thing_type_operation_rate_rank', 'cockpit_thing_type_performance_rate_rank', 'cockpit_thing_type_yield_rate_rank', 'cockpit_yield_rate', 'comba_attendance_list', 'comba_attendance_overall', 'comba_cost_overall', 'comba_deliver_list', 'comba_deliver_summary', 'comba_delivery_history_list', 'comba_delivery_list', 'comba_delivery_overall', 'comba_line', 'comba_line_list', 'comba_line_overall', 'comba_order_list', 'comba_owe_list', 'comba_owe_overall', 'comba_ppmlist', 'comba_qualified_rate', 'comba_qualified_rate_list', 'comba_smtchange_line', 'comba_smtlist', 'comba_smtoverall', 'comba_smtrealtime', 'comba_stocking_list', 'comba_stocking_list2_darray', 'comba_stocking_list_map', 'comba_stocking_overall', 'comba_unqualified_list', 'companies', 'company', 'company_admin_users', 'company_apps', 'company_bidatasource_list', 'company_bidatasource_tree', 'company_bottleneck', 'company_electricity_consumptions', 'company_electricity_period_consumptions', 'company_electricity_price', 'company_electricity_total_consumption', 'company_energy', 'company_energy_offset_threshold', 'company_exists', 'company_history_vapor_price', 'company_history_water_price', 'company_overall', 'company_production', 'company_real_time_electricity_data', 'company_real_time_vapor_data', 'company_real_time_water_data', 'company_redundant', 'company_thing_calibrate_configuration', 'company_thing_group_tree', 'company_thing_specification_language_list', 'company_thing_type_list', 'company_type_list', 'company_vapor_consumptions', 'company_vapor_price', 'company_vapor_total_consumption', 'company_water_consumptions', 'company_water_price', 'company_water_total_consumption', 'counties', 'countries', 'current_change_borrow_approve_configuration_list', 'current_date_data', 'current_product_working_time_summary', 'current_shift_data', 'current_thing_borrow_approve_configuration_list', 'current_thing_calibrate_workflow_configuration_list', 'current_thing_inspection_workflow_configuration_list', 'current_thing_maintenance_workflow_configuration_list', 'current_thing_repair_workflow_configuration_list', 'department_list', 'department_name_same_as_siblings', 'department_thing_groups', 'department_tree', 'depository', 'depository_list', 'dept_user_thing_groups', 'energy_consumption_comparison_by_group', 'energy_consumption_comparison_by_type', 'energy_consumption_to_t', 'energy_consumption_trend', 'energy_group', 'energy_group_list', 'energy_node', 'energy_node_electricity_consumption_list', 'energy_node_electricity_consumption_report_list', 'energy_node_energy_consumption_report', 'energy_node_list', 'energy_node_tree', 'energy_node_vapor_consumption_list', 'energy_node_vapor_consumption_report_list', 'energy_node_water_consumption_list', 'energy_node_water_consumption_report_list', 'energy_power_daily_trend', 'energy_power_trend', 'energy_thing_groups', 'energy_things', 'energy_time_distribution', 'eprect_mold_list', 'eprect_production_daily', 'eprect_production_record', 'eprect_production_record_list', 'error_type', 'error_type_list', 'evasion_date', 'evasion_date_list', 'exists_alert_rule_name', 'exists_business_knowledge_name', 'exists_business_knowledge_type_name', 'exists_error_type_name', 'export_area_bottleneck_by_company', 'export_area_energy_consumption_by_company', 'export_area_peak_rate_by_company', 'export_area_production_by_company', 'export_area_redundant_by_company', 'export_cockpit_oee', 'export_cockpit_operation_rate', 'export_cockpit_performance_rate', 'export_cockpit_rate_list', 'export_cockpit_thing_list', 'export_cockpit_yield_rate', 'export_comba_attendance_list', 'export_comba_deliver_summary', 'export_comba_order_list', 'export_comba_owe_list', 'export_comba_ppmlist', 'export_comba_smtlist', 'export_comba_stocking_list', 'export_comba_stocking_summary', 'export_comba_unqualified_list', 'export_delivery_history_list', 'export_energy_node_energy_consumption_report', 'export_fee_report_list', 'export_history_report', 'export_issues', 'export_qualified_rate_list', 'export_thing_energy_consumption_report', 'export_thing_energy_detail', 'export_thing_energy_detail_daily', 'export_thing_group_energy_consumption_report', 'export_thing_report_list', 'export_thing_total_report_list', 'export_user', 'factory', 'factory_list', 'fee_report_list', 'history_data', 'history_raw', 'history_report', 'history_report_list', 'history_status_data', 'import_comba_data_template', 'inspection_method', 'inspection_method_import_template', 'inspection_method_list', 'is_adapter_key_exists', 'is_bom_exists', 'is_calibrate_organization_exists', 'is_calibrate_schedule_exists', 'is_change_borrow_approve_configuration_exists', 'is_depository_exists', 'is_energy_node_exists', 'is_factory_exists', 'is_inspection_method_exists', 'is_maintenance_method_exists', 'is_material_category_exists', 'is_material_exists', 'is_outside_calibrate_exists', 'is_product_flow_exists', 'is_product_project_exists', 'is_project_group_name_exists', 'is_spare_part_exists', 'is_thing_borrow_approve_configuration_exists', 'is_thing_calibrate_workflow_configuration_exists', 'is_thing_category_exists', 'is_thing_exists', 'is_thing_inspection_workflow_configuration_exists', 'is_thing_label_exists', 'is_thing_maintenance_workflow_configuration_exists', 'is_thing_repair_workflow_configuration_exists', 'is_thing_schedule_exists', 'is_thing_specification_language_exists', 'is_thing_specification_language_property_exists', 'is_thing_type_exists', 'issue', 'issues', 'leap_daily_report', 'leap_overall', 'leap_target_list', 'maintenance_method', 'maintenance_method_import_template', 'maintenance_method_list', 'market_app', 'market_app_list', 'market_app_summary', 'market_issue', 'market_issue_list', 'market_issue_summary', 'market_solution', 'market_solution_list', 'market_solution_summary', 'material', 'material_category', 'material_category_list', 'material_list', 'me', 'meter_reading_data_import_template', 'meter_reading_data_list', 'multi_history_raw', 'my_app_list', 'my_company', 'my_company_apps', 'my_thing_group', 'notification', 'notification_app', 'notification_config', 'notification_config_app', 'notification_config_list', 'notification_list', 'oauth_permission_list', 'outside_calibrate', 'outside_calibrate_list', 'permission_list', 'permission_tree', 'platform_admin_users', 'platform_user_list', 'product_flow', 'product_flows', 'product_project', 'product_project_document_list', 'product_project_list', 'product_task', 'product_task_list', 'project_group', 'project_group_list', 'project_group_member_list', 'provinces', 'quick_access_app', 'range_data', 'real_raw', 'real_report', 'recent_app', 'repair_rate_summary', 'role_exists', 'role_list', 'role_thing_categories', 'sale_order_summary', 'source_key', 'source_key_list', 'source_model_key_list', 'spare_part', 'spare_part_import_template', 'spare_part_list', 'spare_part_outbound', 'spare_part_outbound_item_list', 'spare_part_outbound_list', 'spare_part_outbound_summary', 'spare_part_receipt', 'spare_part_receipt_item_list', 'spare_part_receipt_list', 'spare_part_stock_list', 'spare_part_writeoff_list', 'stock_top_summary', 'sub_thing_list', 'support_users', 'system_log_action', 'system_log_list', 'table_fields_config', 'thing', 'thing_access_config_list', 'thing_borrow', 'thing_borrow_approve_configuration', 'thing_borrow_approve_configuration_list', 'thing_borrow_default_approve_configuration_list', 'thing_borrow_draft', 'thing_borrow_item', 'thing_borrow_item_list', 'thing_borrow_list', 'thing_borrow_operator_record_list', 'thing_borrow_state_overview', 'thing_by_qr_code', 'thing_calibrate', 'thing_calibrate_default_workflow_configuration_list', 'thing_calibrate_list', 'thing_calibrate_record_list', 'thing_calibrate_status_overview', 'thing_calibrate_workflow_configuration', 'thing_calibrate_workflow_configuration_list', 'thing_category', 'thing_category_import_template', 'thing_category_list', 'thing_category_tree', 'thing_change_borrow_draft', 'thing_circulation_list', 'thing_electricity_consumption_list', 'thing_electricity_consumption_report_list', 'thing_energy_consumption_report', 'thing_function_department', 'thing_function_department_list', 'thing_group', 'thing_group_depts', 'thing_group_electricity_consumption_list', 'thing_group_electricity_consumption_report_list', 'thing_group_energy_consumption_report', 'thing_group_list', 'thing_group_tree', 'thing_group_users', 'thing_group_vapor_consumption_list', 'thing_group_vapor_consumption_report_list', 'thing_group_water_consumption_list', 'thing_group_water_consumption_report_list', 'thing_import_template', 'thing_input_record_list', 'thing_input_record_summary_list', 'thing_inspection', 'thing_inspection_default_workflow_configuration_list', 'thing_inspection_list', 'thing_inspection_operator_record_list', 'thing_inspection_status_overview', 'thing_inspection_workflow_configuration', 'thing_inspection_workflow_configuration_list', 'thing_label', 'thing_label_import_template', 'thing_label_list', 'thing_list', 'thing_maintenance', 'thing_maintenance_default_workflow_configuration_list', 'thing_maintenance_list', 'thing_maintenance_operator_record_list', 'thing_maintenance_status_overview', 'thing_maintenance_workflow_configuration', 'thing_maintenance_workflow_configuration_list', 'thing_mechanism_model', 'thing_on_state_overview', 'thing_rate', 'thing_rate_overall', 'thing_repair', 'thing_repair_default_workflow_configuration_list', 'thing_repair_list', 'thing_repair_operator_record_list', 'thing_repair_status_overview', 'thing_repair_workflow_configuration', 'thing_repair_workflow_configuration_list', 'thing_report_list', 'thing_schedule', 'thing_schedule_import_template', 'thing_schedule_list', 'thing_schedule_thing_import_template', 'thing_spare_part_import_template', 'thing_specification_language', 'thing_specification_language_list', 'thing_specification_language_property', 'thing_specification_language_property_list', 'thing_status', 'thing_statuses', 'thing_task_list', 'thing_thing_specification_language_list', 'thing_total_report_list', 'thing_type', 'thing_type_code_list', 'thing_type_list', 'thing_types', 'things', 'things_energy_consumption_overall', 'things_energy_consumption_overall_sub', 'things_energy_consumption_rank', 'things_operation_rate_rank', 'things_overall', 'things_peak_rate_rank', 'things_power_on_rate_rank', 'total_report', 'type_companies', 'ucc_form_structure', 'ucc_form_structure_json_schema', 'upload_config', 'upload_configs', 'upload_pdm_config', 'upload_pdm_configs', 'user', 'user_template', 'users', 'validate_inspection_method_excel', 'validate_maintenance_method_excel', 'validate_meter_reading_data_excel', 'validate_spare_part_excel', 'validate_thing_category_excel', 'validate_thing_excel', 'validate_thing_label_excel', 'validate_thing_schedule_excel', 'validate_thing_schedule_thing_excel', 'validate_thing_spare_part_excel', 'workbench', 'workbench_card_data', 'workbench_card_option', 'worker_order_detail', 'worker_order_list', 'worker_order_operator_detail', 'worker_order_operator_list', 'worker_order_status_summary', 'worker_order_thing_type_summary', 'worker_order_top_personnel_summary', 'workflow_base_configuration', 'workflow_default_init_state')
    _eam = sgqlc.types.Field(Boolean, graphql_name='_eam')
    _ems = sgqlc.types.Field(Boolean, graphql_name='_ems')
    _plm = sgqlc.types.Field(Boolean, graphql_name='_plm')
    account_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='accountExists', args=sgqlc.types.ArgDict((
        ('account', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='account', default=None)),
))
    )
    adapter_key = sgqlc.types.Field(AdapterKey, graphql_name='adapterKey', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    adapter_key_list = sgqlc.types.Field(sgqlc.types.non_null(AdapterKeyList), graphql_name='adapterKeyList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AdapterFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
))
    )
    adapter_model_key_list = sgqlc.types.Field(sgqlc.types.non_null(AdapterModelKeyList), graphql_name='adapterModelKeyList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AdapterModelFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    alert_detail = sgqlc.types.Field(AlertDetail, graphql_name='alertDetail', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    alert_level_summary = sgqlc.types.Field(sgqlc.types.non_null(AlertLevelSummary), graphql_name='alertLevelSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AlertLevelFilterInput, graphql_name='filter', default=None)),
))
    )
    alert_list = sgqlc.types.Field(sgqlc.types.non_null(AlertList), graphql_name='alertList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AlertFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    alert_rule = sgqlc.types.Field(AlertRule, graphql_name='alertRule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    alert_rule_list = sgqlc.types.Field(sgqlc.types.non_null(AlertRuleList), graphql_name='alertRuleList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AlertRuleListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    alert_tendency_summary = sgqlc.types.Field(sgqlc.types.non_null(AlertTendencySummary), graphql_name='alertTendencySummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AlertLevelFilterInput, graphql_name='filter', default=None)),
))
    )
    alert_top_rule_summary = sgqlc.types.Field(sgqlc.types.non_null(AlertTopRuleSummary), graphql_name='alertTopRuleSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AlertLevelFilterInput, graphql_name='filter', default=None)),
))
    )
    alert_top_thing_summary = sgqlc.types.Field(sgqlc.types.non_null(AlertTopThingSummary), graphql_name='alertTopThingSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AlertLevelFilterInput, graphql_name='filter', default=None)),
))
    )
    app = sgqlc.types.Field(App, graphql_name='app', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    app_config = sgqlc.types.Field(sgqlc.types.non_null(AppConfig), graphql_name='appConfig', args=sgqlc.types.ArgDict((
        ('app_code', sgqlc.types.Arg(String, graphql_name='appCode', default='main')),
))
    )
    app_list = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='appList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AppListFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    app_users = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='appUsers', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AppUserListFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    area_bottleneck_by_company = sgqlc.types.Field(AreaThingsByCompanyData, graphql_name='areaBottleneckByCompany', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    area_bottlenecks = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AreaThingTimeseriesUnit)), graphql_name='areaBottlenecks', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    area_energy_consumption = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit')), graphql_name='areaEnergyConsumption', args=sgqlc.types.ArgDict((
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    area_energy_consumption_by_company = sgqlc.types.Field(AreaEnergyConsumptionByCompanyData, graphql_name='areaEnergyConsumptionByCompany', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    area_energy_consumption_overall = sgqlc.types.Field(AreaEnergyConsumptionOverall, graphql_name='areaEnergyConsumptionOverall', args=sgqlc.types.ArgDict((
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    area_energy_consumption_rank = sgqlc.types.Field(CompanyRank, graphql_name='areaEnergyConsumptionRank', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    area_energy_per_product_rank = sgqlc.types.Field(CompanyRank, graphql_name='areaEnergyPerProductRank', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    area_peak_power = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit')), graphql_name='areaPeakPower', args=sgqlc.types.ArgDict((
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    area_peak_rate_by_company = sgqlc.types.Field(AreaPeakRateByCompanyData, graphql_name='areaPeakRateByCompany', args=sgqlc.types.ArgDict((
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    area_power_on_rate_rank = sgqlc.types.Field(CompanyRank, graphql_name='areaPowerOnRateRank', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    area_production = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit')), graphql_name='areaProduction', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    area_production_by_company = sgqlc.types.Field(AreaProductionByCompanyData, graphql_name='areaProductionByCompany', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    area_production_distribution = sgqlc.types.Field(AreaProductionDistribution, graphql_name='areaProductionDistribution', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    area_redundant_by_company = sgqlc.types.Field(AreaThingsByCompanyData, graphql_name='areaRedundantByCompany', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    area_redundants = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(AreaThingTimeseriesUnit)), graphql_name='areaRedundants', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    area_things_overall = sgqlc.types.Field(AreaThingsOverall, graphql_name='areaThingsOverall', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    bi_energy_device = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biEnergyDevice', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_energy_electric_quantity = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biEnergyElectricQuantity', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_energy_fee = sgqlc.types.Field(sgqlc.types.list_of(EnergyFeeBIResult), graphql_name='biEnergyFee', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_energy_operation_time = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biEnergyOperationTime', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_issue_issue = sgqlc.types.Field(sgqlc.types.list_of(BIResult), graphql_name='biIssueIssue', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_macro_electric_quantity = sgqlc.types.Field(sgqlc.types.list_of(MacroBIResult), graphql_name='biMacroElectricQuantity', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    bi_macro_peak_rate = sgqlc.types.Field(sgqlc.types.list_of(MacroBIResult), graphql_name='biMacroPeakRate', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BIFilterInput, graphql_name='filter', default=None)),
))
    )
    bom = sgqlc.types.Field(Bom, graphql_name='bom', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    bom_list = sgqlc.types.Field(sgqlc.types.non_null(BomList), graphql_name='bomList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BomFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    bom_material_list = sgqlc.types.Field(sgqlc.types.non_null(BomMaterialList), graphql_name='bomMaterialList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BomMaterialFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    business_knowledge = sgqlc.types.Field(BusinessKnowledge, graphql_name='businessKnowledge', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    business_knowledge_list = sgqlc.types.Field(sgqlc.types.non_null(BusinessKnowledgeList), graphql_name='businessKnowledgeList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BusinessKnowledgeListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    business_knowledge_type = sgqlc.types.Field(BusinessKnowledgeType, graphql_name='businessKnowledgeType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    business_knowledge_type_list = sgqlc.types.Field(sgqlc.types.non_null(BusinessKnowledgeTypeList), graphql_name='businessKnowledgeTypeList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BusinessKnowledgeTypeListFilterInput, graphql_name='filter', default=None)),
))
    )
    calibrate_organization = sgqlc.types.Field(sgqlc.types.non_null(CalibrateOrganization), graphql_name='calibrateOrganization', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    calibrate_organization_list = sgqlc.types.Field(sgqlc.types.non_null(CalibrateOrganizationList), graphql_name='calibrateOrganizationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CalibrateOrganizationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    calibrate_schedule = sgqlc.types.Field(CalibrateSchedule, graphql_name='calibrateSchedule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    calibrate_schedule_list = sgqlc.types.Field(sgqlc.types.non_null(CalibrateScheduleList), graphql_name='calibrateScheduleList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CalibrateScheduleFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    change_borrow = sgqlc.types.Field(ChangeBorrow, graphql_name='changeBorrow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    change_borrow_approve_configuration = sgqlc.types.Field(ChangeBorrowApproveConfiguration, graphql_name='changeBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    change_borrow_approve_configuration_list = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowApproveConfigurationList), graphql_name='changeBorrowApproveConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ChangeBorrowApproveConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    change_borrow_default_approve_configuration_list = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowApproveConfigurationList), graphql_name='changeBorrowDefaultApproveConfigurationList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    change_borrow_item = sgqlc.types.Field(ChangeBorrowItem, graphql_name='changeBorrowItem', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    change_borrow_item_list = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowItemList), graphql_name='changeBorrowItemList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ChangeBorrowItemListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    change_borrow_list = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowList), graphql_name='changeBorrowList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ChangeBorrowListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    change_borrow_operator_record_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ChangeBorrowOperatorRecord))), graphql_name='changeBorrowOperatorRecordList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    change_borrow_state_overview = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowStateOverview), graphql_name='changeBorrowStateOverview', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    check_alter_department_thing_group = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkAlterDepartmentThingGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CheckAlterDepartmentThingGroupInput), graphql_name='input', default=None)),
))
    )
    check_delete_department = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='checkDeleteDepartment', args=sgqlc.types.ArgDict((
        ('department', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='department', default=None)),
))
    )
    cities = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(City_)), graphql_name='cities', args=sgqlc.types.ArgDict((
        ('province_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='provinceID', default=None)),
))
    )
    city_companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(City)), graphql_name='cityCompanies')
    cnc_alert_list = sgqlc.types.Field(CNCAlertList, graphql_name='cncAlertList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(TimerangeFilter), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    cnc_alert_overall = sgqlc.types.Field(CNCAlertOverall, graphql_name='cncAlertOverall', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(TimerangeFilter), graphql_name='filter', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    cnc_alerts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CNCAlertTimeseries))), graphql_name='cncAlerts', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(TimerangeFilter), graphql_name='filter', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    cnc_current_alerts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CNCAlert))), graphql_name='cncCurrentAlerts', args=sgqlc.types.ArgDict((
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    cnc_overall = sgqlc.types.Field(sgqlc.types.non_null(CNCOverall), graphql_name='cncOverall', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    cockpit_aggregation = sgqlc.types.Field(CockpitAggregation, graphql_name='cockpitAggregation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    cockpit_aggregations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitAggregation))), graphql_name='cockpitAggregations', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CockpitAggregationFilterInput, graphql_name='filter', default=None)),
))
    )
    cockpit_key = sgqlc.types.Field(CockpitKey, graphql_name='cockpitKey', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    cockpit_key_list = sgqlc.types.Field(sgqlc.types.non_null(CockpitKeyList), graphql_name='cockpitKeyList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CockpitKeyFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
))
    )
    cockpit_oee = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitTimeseries))), graphql_name='cockpitOEE', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
))
    )
    cockpit_operation_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitTimeseries))), graphql_name='cockpitOperationRate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
))
    )
    cockpit_organization_oeerank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitOrganizationRank))), graphql_name='cockpitOrganizationOEERank', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    cockpit_organization_operation_rate_rank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitOrganizationRank))), graphql_name='cockpitOrganizationOperationRateRank', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    cockpit_organization_performance_rate_rank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitOrganizationRank))), graphql_name='cockpitOrganizationPerformanceRateRank', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    cockpit_organization_yield_rate_rank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitOrganizationRank))), graphql_name='cockpitOrganizationYieldRateRank', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    cockpit_overall = sgqlc.types.Field(CockpitOverall, graphql_name='cockpitOverall', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('thing_type', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='thingType', default=None)),
))
    )
    cockpit_performance_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitTimeseries))), graphql_name='cockpitPerformanceRate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
))
    )
    cockpit_rate_list = sgqlc.types.Field(CockpitRateList, graphql_name='cockpitRateList', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    cockpit_rate_overall = sgqlc.types.Field(CockpitRateOverall, graphql_name='cockpitRateOverall', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    cockpit_target_list = sgqlc.types.Field(sgqlc.types.non_null(CockpitTargetList), graphql_name='cockpitTargetList', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
))
    )
    cockpit_thing = sgqlc.types.Field(CockpitThing, graphql_name='cockpitThing', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    cockpit_thing_list = sgqlc.types.Field(sgqlc.types.non_null(CockpitThingList), graphql_name='cockpitThingList', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('filter', sgqlc.types.Arg(CockpitThingListFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
))
    )
    cockpit_thing_type_oeerank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitThingTypeRank))), graphql_name='cockpitThingTypeOEERank', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    cockpit_thing_type_operation_rate_rank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitThingTypeRank))), graphql_name='cockpitThingTypeOperationRateRank', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    cockpit_thing_type_performance_rate_rank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitThingTypeRank))), graphql_name='cockpitThingTypePerformanceRateRank', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    cockpit_thing_type_yield_rate_rank = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitThingTypeRank))), graphql_name='cockpitThingTypeYieldRateRank', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    cockpit_yield_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CockpitTimeseries))), graphql_name='cockpitYieldRate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
))
    )
    comba_attendance_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CombaAttendance))), graphql_name='combaAttendanceList', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    comba_attendance_overall = sgqlc.types.Field(CombaAttendanceOverall, graphql_name='combaAttendanceOverall', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    comba_cost_overall = sgqlc.types.Field(CombaCostOverall, graphql_name='combaCostOverall', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    comba_deliver_list = sgqlc.types.Field(sgqlc.types.non_null(CombaDeliverList), graphql_name='combaDeliverList', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    comba_deliver_summary = sgqlc.types.Field(sgqlc.types.non_null(CombaDeliverSummary), graphql_name='combaDeliverSummary', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    comba_delivery_history_list = sgqlc.types.Field(CombaDeliveryHistoryList, graphql_name='combaDeliveryHistoryList', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    comba_delivery_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaDeliveryByProductLine)), graphql_name='combaDeliveryList', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    comba_delivery_overall = sgqlc.types.Field(CombaDeliveryOverall, graphql_name='combaDeliveryOverall', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    comba_line = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaLine)), graphql_name='combaLine')
    comba_line_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaLineDetail)), graphql_name='combaLineList', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    comba_line_overall = sgqlc.types.Field(CombaLineOverall, graphql_name='combaLineOverall', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
        ('filter', sgqlc.types.Arg(CombaLineFilter, graphql_name='filter', default=None)),
))
    )
    comba_order_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaOrder)), graphql_name='combaOrderList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(CombaOrderListFilter), graphql_name='filter', default=None)),
))
    )
    comba_owe_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaOwe)), graphql_name='combaOweList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CombaOweFilterInput, graphql_name='filter', default=None)),
))
    )
    comba_owe_overall = sgqlc.types.Field(CombaOweOverall, graphql_name='combaOweOverall', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    comba_ppmlist = sgqlc.types.Field(CombaPPMList, graphql_name='combaPPMList', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    comba_qualified_rate = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaQualifiedRate)), graphql_name='combaQualifiedRate', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    comba_qualified_rate_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CombaQualifiedRateByMonth))), graphql_name='combaQualifiedRateList', args=sgqlc.types.ArgDict((
        ('year', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='year', default=None)),
))
    )
    comba_smtchange_line = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(CombaSMTChangeLineTimeseries)), graphql_name='combaSMTChangeLine', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CombaLineDailyProductionFilterInput, graphql_name='filter', default=None)),
))
    )
    comba_smtlist = sgqlc.types.Field(CombaSMTList, graphql_name='combaSMTList', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(Timestamp, graphql_name='date', default=None)),
))
    )
    comba_smtoverall = sgqlc.types.Field(CombaSMTOverall, graphql_name='combaSMTOverall', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
        ('filter', sgqlc.types.Arg(CombaLineFilter, graphql_name='filter', default=None)),
))
    )
    comba_smtrealtime = sgqlc.types.Field(CombaSMTRealtime, graphql_name='combaSMTRealtime', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
        ('filter', sgqlc.types.Arg(CombaLineFilter, graphql_name='filter', default=None)),
))
    )
    comba_stocking_list = sgqlc.types.Field(CombaStockingList, graphql_name='combaStockingList', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    comba_stocking_list2_darray = sgqlc.types.Field(JSON, graphql_name='combaStockingList2DArray', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    comba_stocking_list_map = sgqlc.types.Field(sgqlc.types.non_null(CombaStockingMap), graphql_name='combaStockingListMap', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    comba_stocking_overall = sgqlc.types.Field(sgqlc.types.non_null('combaStockingOverallList'), graphql_name='combaStockingOverall', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
        ('granularity', sgqlc.types.Arg(CombaGranularity, graphql_name='granularity', default=None)),
))
    )
    comba_unqualified_list = sgqlc.types.Field(sgqlc.types.non_null(CombaUnqualifiedList), graphql_name='combaUnqualifiedList', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    companies = sgqlc.types.Field(sgqlc.types.non_null(CompanyList), graphql_name='companies', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='company', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    company_admin_users = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='companyAdminUsers', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyAdminUsersFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    company_apps = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='companyApps', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyAppsFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    company_bidatasource_list = sgqlc.types.Field(sgqlc.types.non_null(CompanyBIDatasourceList), graphql_name='companyBIDatasourceList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyBIDatasourceFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    company_bidatasource_tree = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(AppBIDatasourceList)), graphql_name='companyBIDatasourceTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyBIDatasourceFilter, graphql_name='filter', default=None)),
))
    )
    company_bottleneck = sgqlc.types.Field(sgqlc.types.non_null(CompanyThingList), graphql_name='companyBottleneck', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    company_electricity_consumptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyElectricityConsumption))), graphql_name='companyElectricityConsumptions', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyElectricityConsumptionsFilterInput, graphql_name='filter', default=None)),
))
    )
    company_electricity_period_consumptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyElectricityPeriodConsumption))), graphql_name='companyElectricityPeriodConsumptions', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyElectricityPeriodConsumptionsFilterInput, graphql_name='filter', default=None)),
))
    )
    company_electricity_price = sgqlc.types.Field(sgqlc.types.non_null(CompanyElectricityPrice), graphql_name='companyElectricityPrice', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    company_electricity_total_consumption = sgqlc.types.Field(CompanyElectricityTotalConsumption, graphql_name='companyElectricityTotalConsumption', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyElectricityTotalConsumptionFilterInput, graphql_name='filter', default=None)),
))
    )
    company_energy = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ParetoTimeseries)), graphql_name='companyEnergy', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    company_energy_offset_threshold = sgqlc.types.Field(Float, graphql_name='companyEnergyOffsetThreshold', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    company_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='companyExists', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(companyExistsFilter), graphql_name='filter', default=None)),
))
    )
    company_history_vapor_price = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyTimeVaporPrice))), graphql_name='companyHistoryVaporPrice', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyHistoryVaporPriceFilterInput, graphql_name='filter', default=None)),
))
    )
    company_history_water_price = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyTimeWaterPrice))), graphql_name='companyHistoryWaterPrice', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyHistoryWaterPriceFilterInput, graphql_name='filter', default=None)),
))
    )
    company_overall = sgqlc.types.Field(sgqlc.types.non_null(CompanyOverall), graphql_name='companyOverall', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    company_production = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ParetoTimeseries)), graphql_name='companyProduction', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    company_real_time_electricity_data = sgqlc.types.Field(CompanyRealTimeElectricityData, graphql_name='companyRealTimeElectricityData', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    company_real_time_vapor_data = sgqlc.types.Field(CompanyRealTimeVaporData, graphql_name='companyRealTimeVaporData', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    company_real_time_water_data = sgqlc.types.Field(CompanyRealTimeWaterData, graphql_name='companyRealTimeWaterData', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    company_redundant = sgqlc.types.Field(sgqlc.types.non_null(CompanyThingList), graphql_name='companyRedundant', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    company_thing_calibrate_configuration = sgqlc.types.Field('ThingCalibrateConfiguration', graphql_name='companyThingCalibrateConfiguration', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    company_thing_group_tree = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyThingGroupNode))), graphql_name='companyThingGroupTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyThingGroupTreeFilterInput, graphql_name='filter', default=None)),
))
    )
    company_thing_specification_language_list = sgqlc.types.Field(sgqlc.types.non_null(CompanyThingSpecificationLanguageList), graphql_name='companyThingSpecificationLanguageList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyThingSpecificationLanguageFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    company_thing_type_list = sgqlc.types.Field(sgqlc.types.non_null(CompanyThingTypeList), graphql_name='companyThingTypeList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyThingTypeFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    company_type_list = sgqlc.types.Field(sgqlc.types.non_null(CompanyTypeList), graphql_name='companyTypeList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyTypeFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    company_vapor_consumptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyVaporConsumption))), graphql_name='companyVaporConsumptions', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyVaporConsumptionsFilterInput, graphql_name='filter', default=None)),
))
    )
    company_vapor_price = sgqlc.types.Field(Float, graphql_name='companyVaporPrice', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    company_vapor_total_consumption = sgqlc.types.Field(CompanyVaporTotalConsumption, graphql_name='companyVaporTotalConsumption', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyVaporTotalConsumptionFilterInput, graphql_name='filter', default=None)),
))
    )
    company_water_consumptions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CompanyWaterConsumption))), graphql_name='companyWaterConsumptions', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyWaterConsumptionsFilterInput, graphql_name='filter', default=None)),
))
    )
    company_water_price = sgqlc.types.Field(Float, graphql_name='companyWaterPrice', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    company_water_total_consumption = sgqlc.types.Field(CompanyWaterTotalConsumption, graphql_name='companyWaterTotalConsumption', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyWaterTotalConsumptionFilterInput, graphql_name='filter', default=None)),
))
    )
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(County_)), graphql_name='counties', args=sgqlc.types.ArgDict((
        ('city_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='cityID', default=None)),
))
    )
    countries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Country)), graphql_name='countries', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(countryFilter, graphql_name='filter', default=None)),
))
    )
    current_change_borrow_approve_configuration_list = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowApproveConfigurationList), graphql_name='currentChangeBorrowApproveConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CurrentChangeBorrowApproveConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    current_date_data = sgqlc.types.Field('ThingData', graphql_name='currentDateData', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    current_product_working_time_summary = sgqlc.types.Field(sgqlc.types.non_null(ProductWorkingTimeSummary), graphql_name='currentProductWorkingTimeSummary', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    current_shift_data = sgqlc.types.Field('ThingData', graphql_name='currentShiftData', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    current_thing_borrow_approve_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowApproveConfigurationList'), graphql_name='currentThingBorrowApproveConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CurrentThingBorrowApproveConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    current_thing_calibrate_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingCalibrateWorkflowConfigurationList'), graphql_name='currentThingCalibrateWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CurrentThingCalibrateWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    current_thing_inspection_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionWorkflowConfigurationList'), graphql_name='currentThingInspectionWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CurrentThingInspectionWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    current_thing_maintenance_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceWorkflowConfigurationList'), graphql_name='currentThingMaintenanceWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CurrentThingMaintenanceWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    current_thing_repair_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairWorkflowConfigurationList'), graphql_name='currentThingRepairWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CurrentThingRepairWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    department_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Department)), graphql_name='departmentList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DepartmentListFilter), graphql_name='filter', default=None)),
))
    )
    department_name_same_as_siblings = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='departmentNameSameAsSiblings', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DepartmentNameSameAsSiblingsFilter), graphql_name='filter', default=None)),
))
    )
    department_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingGroup'))), graphql_name='departmentThingGroups', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DepartmentThingGroupFilterInput, graphql_name='filter', default=None)),
))
    )
    department_tree = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='departmentTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DepartmentTreeFilter, graphql_name='filter', default=None)),
))
    )
    depository = sgqlc.types.Field(Depository, graphql_name='depository', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    depository_list = sgqlc.types.Field(sgqlc.types.non_null(DepositoryList), graphql_name='depositoryList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(DepositoryListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    dept_user_thing_groups = sgqlc.types.Field(sgqlc.types.non_null('ThingGroupList'), graphql_name='deptUserThingGroups', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(DeptUserThingGroupInputFilter), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    energy_consumption_comparison_by_group = sgqlc.types.Field(EnergyConsumptionComparison, graphql_name='energyConsumptionComparisonByGroup', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    energy_consumption_comparison_by_type = sgqlc.types.Field(EnergyConsumptionComparison, graphql_name='energyConsumptionComparisonByType', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    energy_consumption_to_t = sgqlc.types.Field(EnergyConsumptionToT, graphql_name='energyConsumptionToT', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('timestamp', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='timestamp', default=None)),
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='type', default=None)),
))
    )
    energy_consumption_trend = sgqlc.types.Field(EnergyTrend, graphql_name='energyConsumptionTrend', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('timestamp', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='timestamp', default=None)),
))
    )
    energy_group = sgqlc.types.Field(EnergyGroup, graphql_name='energyGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    energy_group_list = sgqlc.types.Field(sgqlc.types.non_null(EnergyGroupList), graphql_name='energyGroupList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EnergyGroupFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
))
    )
    energy_node = sgqlc.types.Field(EnergyNode, graphql_name='energyNode', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    energy_node_electricity_consumption_list = sgqlc.types.Field(sgqlc.types.non_null(EnergyNodeElectricityConsumptionList), graphql_name='energyNodeElectricityConsumptionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EnergyNodeElectricityConsumptionFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    energy_node_electricity_consumption_report_list = sgqlc.types.Field(sgqlc.types.non_null(EnergyNodeEnergyConsumptionReportList), graphql_name='energyNodeElectricityConsumptionReportList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EnergyNodeEnergyConsumptionReportFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    energy_node_energy_consumption_report = sgqlc.types.Field(sgqlc.types.non_null(EnergyNodeEnergyConsumptionReport), graphql_name='energyNodeEnergyConsumptionReport', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EnergyNodeEnergyConsumptionReportFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    energy_node_list = sgqlc.types.Field(sgqlc.types.non_null(EnergyNodeList), graphql_name='energyNodeList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EnergyNodeListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    energy_node_tree = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='energyNodeTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EnergyNodeListFilterInput), graphql_name='filter', default=None)),
))
    )
    energy_node_vapor_consumption_list = sgqlc.types.Field(sgqlc.types.non_null(EnergyNodeVaporConsumptionList), graphql_name='energyNodeVaporConsumptionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EnergyNodeVaporConsumptionFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    energy_node_vapor_consumption_report_list = sgqlc.types.Field(sgqlc.types.non_null(EnergyNodeEnergyConsumptionReportList), graphql_name='energyNodeVaporConsumptionReportList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EnergyNodeEnergyConsumptionReportFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    energy_node_water_consumption_list = sgqlc.types.Field(sgqlc.types.non_null(EnergyNodeWaterConsumptionList), graphql_name='energyNodeWaterConsumptionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EnergyNodeWaterConsumptionFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    energy_node_water_consumption_report_list = sgqlc.types.Field(sgqlc.types.non_null(EnergyNodeEnergyConsumptionReportList), graphql_name='energyNodeWaterConsumptionReportList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EnergyNodeEnergyConsumptionReportFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    energy_power_daily_trend = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit'))), graphql_name='energyPowerDailyTrend', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end_at', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='endAt', default=None)),
        ('start_at', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='startAt', default=None)),
))
    )
    energy_power_trend = sgqlc.types.Field(EnergyTrend, graphql_name='energyPowerTrend', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('timestamp', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='timestamp', default=None)),
))
    )
    energy_thing_groups = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingGroup'))), graphql_name='energyThingGroups', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EnergyThingGroupListFilterInput, graphql_name='filter', default=None)),
))
    )
    energy_things = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Thing'))), graphql_name='energyThings', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EnergyThingsFilterInput, graphql_name='filter', default=None)),
))
    )
    energy_time_distribution = sgqlc.types.Field(EnergyTimeDistribution, graphql_name='energyTimeDistribution')
    eprect_mold_list = sgqlc.types.Field(sgqlc.types.non_null(EprectMoldList), graphql_name='eprectMoldList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EprectMoldFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    eprect_production_daily = sgqlc.types.Field(EprectProductionDailyList, graphql_name='eprectProductionDaily', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyId', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_id', sgqlc.types.Arg(ID, graphql_name='thingId', default=None)),
))
    )
    eprect_production_record = sgqlc.types.Field(sgqlc.types.non_null(EprectProductionRecord), graphql_name='eprectProductionRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    eprect_production_record_list = sgqlc.types.Field(sgqlc.types.non_null(EprectProductionRecordList), graphql_name='eprectProductionRecordList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(EprectProductionRecordFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    error_type = sgqlc.types.Field(ErrorType, graphql_name='errorType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    error_type_list = sgqlc.types.Field(sgqlc.types.non_null(ErrorTypeList), graphql_name='errorTypeList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ErrorTypeListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    evasion_date = sgqlc.types.Field(EvasionDate, graphql_name='evasionDate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    evasion_date_list = sgqlc.types.Field(sgqlc.types.non_null(EvasionDateList), graphql_name='evasionDateList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EvasionDateFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    exists_alert_rule_name = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='existsAlertRuleName', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(AlertRuleNameFilterInput, graphql_name='filter', default=None)),
))
    )
    exists_business_knowledge_name = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='existsBusinessKnowledgeName', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BusinessKnowledgeNameFilterInput, graphql_name='filter', default=None)),
))
    )
    exists_business_knowledge_type_name = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='existsBusinessKnowledgeTypeName', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(BusinessKnowledgeTypeNameFilterInput, graphql_name='filter', default=None)),
))
    )
    exists_error_type_name = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='existsErrorTypeName', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ErrorTypeNameFilterInput, graphql_name='filter', default=None)),
))
    )
    export_area_bottleneck_by_company = sgqlc.types.Field('RawFile', graphql_name='exportAreaBottleneckByCompany', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    export_area_energy_consumption_by_company = sgqlc.types.Field('RawFile', graphql_name='exportAreaEnergyConsumptionByCompany', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    export_area_peak_rate_by_company = sgqlc.types.Field('RawFile', graphql_name='exportAreaPeakRateByCompany', args=sgqlc.types.ArgDict((
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    export_area_production_by_company = sgqlc.types.Field('RawFile', graphql_name='exportAreaProductionByCompany', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    export_area_redundant_by_company = sgqlc.types.Field('RawFile', graphql_name='exportAreaRedundantByCompany', args=sgqlc.types.ArgDict((
        ('company_type', sgqlc.types.Arg(IDInput, graphql_name='companyType', default=None)),
        ('county', sgqlc.types.Arg(String, graphql_name='county', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    export_cockpit_oee = sgqlc.types.Field('RawFile', graphql_name='exportCockpitOEE', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
))
    )
    export_cockpit_operation_rate = sgqlc.types.Field('RawFile', graphql_name='exportCockpitOperationRate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
))
    )
    export_cockpit_performance_rate = sgqlc.types.Field('RawFile', graphql_name='exportCockpitPerformanceRate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
))
    )
    export_cockpit_rate_list = sgqlc.types.Field('RawFile', graphql_name='exportCockpitRateList', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    export_cockpit_thing_list = sgqlc.types.Field('RawFile', graphql_name='exportCockpitThingList', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('filter', sgqlc.types.Arg(CockpitThingListFilter, graphql_name='filter', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
))
    )
    export_cockpit_yield_rate = sgqlc.types.Field('RawFile', graphql_name='exportCockpitYieldRate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='company', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('organization', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='organization', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('target', sgqlc.types.Arg(ID, graphql_name='target', default=None)),
))
    )
    export_comba_attendance_list = sgqlc.types.Field('RawFile', graphql_name='exportCombaAttendanceList', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    export_comba_deliver_summary = sgqlc.types.Field('RawFile', graphql_name='exportCombaDeliverSummary', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    export_comba_order_list = sgqlc.types.Field('RawFile', graphql_name='exportCombaOrderList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CombaOrderListFilter, graphql_name='filter', default=None)),
))
    )
    export_comba_owe_list = sgqlc.types.Field('RawFile', graphql_name='exportCombaOweList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CombaOweFilterInput, graphql_name='filter', default=None)),
))
    )
    export_comba_ppmlist = sgqlc.types.Field('RawFile', graphql_name='exportCombaPPMList', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    export_comba_smtlist = sgqlc.types.Field('RawFile', graphql_name='exportCombaSMTList', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(Timestamp, graphql_name='date', default=None)),
))
    )
    export_comba_stocking_list = sgqlc.types.Field('RawFile', graphql_name='exportCombaStockingList', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    export_comba_stocking_summary = sgqlc.types.Field('RawFile', graphql_name='exportCombaStockingSummary', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    export_comba_unqualified_list = sgqlc.types.Field('RawFile', graphql_name='exportCombaUnqualifiedList', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    export_delivery_history_list = sgqlc.types.Field('RawFile', graphql_name='exportDeliveryHistoryList', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    export_energy_node_energy_consumption_report = sgqlc.types.Field('RawFile', graphql_name='exportEnergyNodeEnergyConsumptionReport', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(EnergyNodeEnergyConsumptionReportFilterInput, graphql_name='filter', default=None)),
))
    )
    export_fee_report_list = sgqlc.types.Field('RawFile', graphql_name='exportFeeReportList', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('energy_type', sgqlc.types.Arg(sgqlc.types.list_of(EnergyType), graphql_name='energyType', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    export_history_report = sgqlc.types.Field('RawFile', graphql_name='exportHistoryReport', args=sgqlc.types.ArgDict((
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fields', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('tag', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tag', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    export_issues = sgqlc.types.Field('RawFile', graphql_name='exportIssues', args=sgqlc.types.ArgDict((
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('filter', sgqlc.types.Arg(IssueListFilter, graphql_name='filter', default=None)),
        ('mine_only', sgqlc.types.Arg(Boolean, graphql_name='mineOnly', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    export_qualified_rate_list = sgqlc.types.Field('RawFile', graphql_name='exportQualifiedRateList', args=sgqlc.types.ArgDict((
        ('year', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='year', default=None)),
))
    )
    export_thing_energy_consumption_report = sgqlc.types.Field('RawFile', graphql_name='exportThingEnergyConsumptionReport', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingEnergyConsumptionReportFilterInput, graphql_name='filter', default=None)),
))
    )
    export_thing_energy_detail = sgqlc.types.Field('RawFile', graphql_name='exportThingEnergyDetail', args=sgqlc.types.ArgDict((
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    export_thing_energy_detail_daily = sgqlc.types.Field('RawFile', graphql_name='exportThingEnergyDetailDaily', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
        ('timestamp', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='timestamp', default=None)),
))
    )
    export_thing_group_energy_consumption_report = sgqlc.types.Field('RawFile', graphql_name='exportThingGroupEnergyConsumptionReport', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingGroupEnergyConsumptionReportFilterInput), graphql_name='filter', default=None)),
))
    )
    export_thing_report_list = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportThingReportList', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('energy_group', sgqlc.types.Arg(sgqlc.types.list_of(IDInput), graphql_name='energyGroup', default=None)),
        ('energy_type', sgqlc.types.Arg(sgqlc.types.list_of(EnergyType), graphql_name='energyType', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('tag', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tag', default=None)),
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(IDInput), graphql_name='types', default=None)),
))
    )
    export_thing_total_report_list = sgqlc.types.Field('RawFile', graphql_name='exportThingTotalReportList', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('energy_type', sgqlc.types.Arg(sgqlc.types.list_of(EnergyType), graphql_name='energyType', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    export_user = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='exportUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ExportUserInput, graphql_name='input', default=None)),
))
    )
    factory = sgqlc.types.Field(Factory, graphql_name='factory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    factory_list = sgqlc.types.Field(sgqlc.types.non_null(FactoryList), graphql_name='factoryList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(FactoryListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    fee_report_list = sgqlc.types.Field(FeeReportList, graphql_name='feeReportList', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('energy_type', sgqlc.types.Arg(sgqlc.types.list_of(EnergyType), graphql_name='energyType', default=None)),
        ('granularity', sgqlc.types.Arg(sgqlc.types.non_null(Granularity), graphql_name='granularity', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    history_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingData')), graphql_name='historyData', args=sgqlc.types.ArgDict((
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    history_raw = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RawData')), graphql_name='historyRaw', args=sgqlc.types.ArgDict((
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('field', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='field', default=None)),
        ('granularity', sgqlc.types.Arg(Granularity, graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    history_report = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RawData')), graphql_name='historyReport', args=sgqlc.types.ArgDict((
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fields', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    history_report_list = sgqlc.types.Field('RawDataList', graphql_name='historyReportList', args=sgqlc.types.ArgDict((
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fields', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    history_status_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(HistoryStatusData)), graphql_name='historyStatusData', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    import_comba_data_template = sgqlc.types.Field('RawFile', graphql_name='importCombaDataTemplate')
    inspection_method = sgqlc.types.Field(InspectionMethod, graphql_name='inspectionMethod', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    inspection_method_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='inspectionMethodImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    inspection_method_list = sgqlc.types.Field(sgqlc.types.non_null(InspectionMethodList), graphql_name='inspectionMethodList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(InspectionMethodListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    is_adapter_key_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdapterKeyExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsAdapterKeyExists), graphql_name='input', default=None)),
))
    )
    is_bom_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBomExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsBomExistsInput), graphql_name='input', default=None)),
))
    )
    is_calibrate_organization_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCalibrateOrganizationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsCalibrateOrganizationInput), graphql_name='input', default=None)),
))
    )
    is_calibrate_schedule_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCalibrateScheduleExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsCalibrateScheduleExistsInput), graphql_name='input', default=None)),
))
    )
    is_change_borrow_approve_configuration_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isChangeBorrowApproveConfigurationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsChangeBorrowApproveConfigurationExists), graphql_name='input', default=None)),
))
    )
    is_depository_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDepositoryExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsDepositoryExistsInput), graphql_name='input', default=None)),
))
    )
    is_energy_node_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEnergyNodeExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsEnergyNodeExistsInput), graphql_name='input', default=None)),
))
    )
    is_factory_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFactoryExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsFactoryExistsInput), graphql_name='input', default=None)),
))
    )
    is_inspection_method_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isInspectionMethodExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsInspectionMethodExistsInput), graphql_name='input', default=None)),
))
    )
    is_maintenance_method_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMaintenanceMethodExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsMaintenanceMethodExistsInput), graphql_name='input', default=None)),
))
    )
    is_material_category_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMaterialCategoryExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsMaterialCategoryExistsInput), graphql_name='input', default=None)),
))
    )
    is_material_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMaterialExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsMaterialExistsInput), graphql_name='input', default=None)),
))
    )
    is_outside_calibrate_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOutsideCalibrateExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsOutsideCalibrateExistsInput), graphql_name='input', default=None)),
))
    )
    is_product_flow_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isProductFlowExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsProductFlowExistsInput), graphql_name='input', default=None)),
))
    )
    is_product_project_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isProductProjectExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsProductProjectExistsInput), graphql_name='input', default=None)),
))
    )
    is_project_group_name_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isProjectGroupNameExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsProjectGroupNameExistsInput), graphql_name='input', default=None)),
))
    )
    is_spare_part_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSparePartExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsSparePartExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_borrow_approve_configuration_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingBorrowApproveConfigurationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingBorrowApproveConfigurationExists), graphql_name='input', default=None)),
))
    )
    is_thing_calibrate_workflow_configuration_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingCalibrateWorkflowConfigurationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingCalibrateWorkflowConfigurationExists), graphql_name='input', default=None)),
))
    )
    is_thing_category_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingCategoryExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingCategoryExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_inspection_workflow_configuration_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingInspectionWorkflowConfigurationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(IsThingInspectionWorkflowConfigurationExists, graphql_name='input', default=None)),
))
    )
    is_thing_label_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingLabelExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingLabelExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_maintenance_workflow_configuration_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingMaintenanceWorkflowConfigurationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(IsThingMaintenanceWorkflowConfigurationExists, graphql_name='input', default=None)),
))
    )
    is_thing_repair_workflow_configuration_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingRepairWorkflowConfigurationExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(IsThingRepairWorkflowConfigurationExists, graphql_name='input', default=None)),
))
    )
    is_thing_schedule_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingScheduleExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingScheduleExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_specification_language_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingSpecificationLanguageExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingSpecificationLanguageExistsInput), graphql_name='input', default=None)),
))
    )
    is_thing_specification_language_property_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingSpecificationLanguagePropertyExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingSpecificationLanguagePropertyExists), graphql_name='input', default=None)),
))
    )
    is_thing_type_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isThingTypeExists', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(IsThingTypeExists), graphql_name='input', default=None)),
))
    )
    issue = sgqlc.types.Field(Issue, graphql_name='issue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    issues = sgqlc.types.Field(IssueList, graphql_name='issues', args=sgqlc.types.ArgDict((
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('filter', sgqlc.types.Arg(IssueListFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('mine_only', sgqlc.types.Arg(Boolean, graphql_name='mineOnly', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    leap_daily_report = sgqlc.types.Field(LeapDailyReportList, graphql_name='leapDailyReport', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(LeapDailyReportFilter), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    leap_overall = sgqlc.types.Field(LeapOverall, graphql_name='leapOverall')
    leap_target_list = sgqlc.types.Field(sgqlc.types.non_null(LeapTargetList), graphql_name='leapTargetList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    maintenance_method = sgqlc.types.Field(MaintenanceMethod, graphql_name='maintenanceMethod', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    maintenance_method_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='maintenanceMethodImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    maintenance_method_list = sgqlc.types.Field(sgqlc.types.non_null(MaintenanceMethodList), graphql_name='maintenanceMethodList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MaintenanceMethodListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    market_app = sgqlc.types.Field(sgqlc.types.non_null(MarketApp), graphql_name='marketApp', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    market_app_list = sgqlc.types.Field(sgqlc.types.non_null(MarketAppList), graphql_name='marketAppList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MarketAppFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    market_app_summary = sgqlc.types.Field(sgqlc.types.non_null(MarketAppSummary), graphql_name='marketAppSummary')
    market_issue = sgqlc.types.Field(sgqlc.types.non_null(MarketIssue), graphql_name='marketIssue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    market_issue_list = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueList), graphql_name='marketIssueList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(MarketIssueFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    market_issue_summary = sgqlc.types.Field(sgqlc.types.non_null(MarketIssueSummary), graphql_name='marketIssueSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(MarketIssueFilterInput), graphql_name='filter', default=None)),
))
    )
    market_solution = sgqlc.types.Field(sgqlc.types.non_null(MarketSolution), graphql_name='marketSolution', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    market_solution_list = sgqlc.types.Field(sgqlc.types.non_null(MarketSolutionList), graphql_name='marketSolutionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MarketSolutionFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    market_solution_summary = sgqlc.types.Field(sgqlc.types.non_null(MarketSolutionSummary), graphql_name='marketSolutionSummary')
    material = sgqlc.types.Field(Material, graphql_name='material', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    material_category = sgqlc.types.Field(MaterialCategory, graphql_name='materialCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    material_category_list = sgqlc.types.Field(sgqlc.types.non_null(MaterialCategoryList), graphql_name='materialCategoryList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MaterialCategoryFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    material_list = sgqlc.types.Field(sgqlc.types.non_null(MaterialList), graphql_name='materialList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MaterialFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    me = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='me')
    meter_reading_data_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='meterReadingDataImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    meter_reading_data_list = sgqlc.types.Field(sgqlc.types.non_null(MeterReadingDataList), graphql_name='meterReadingDataList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MeterReadingDataFilterInput, graphql_name='filter', default=None)),
))
    )
    multi_history_raw = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('RawData')), graphql_name='multiHistoryRaw', args=sgqlc.types.ArgDict((
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='fields', default=None)),
        ('func_type', sgqlc.types.Arg(FuncType, graphql_name='funcType', default=None)),
        ('granularity', sgqlc.types.Arg(Granularity, graphql_name='granularity', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    my_app_list = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='myAppList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MyAppListFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    my_company = sgqlc.types.Field(sgqlc.types.non_null(Company), graphql_name='myCompany')
    my_company_apps = sgqlc.types.Field(sgqlc.types.non_null(AppList), graphql_name='myCompanyApps', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(MyCompanyAppFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    my_thing_group = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='myThingGroup', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyId', default=None)),
))
    )
    notification = sgqlc.types.Field(sgqlc.types.non_null(Notification), graphql_name='notification', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    notification_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(App)), graphql_name='notificationApp')
    notification_config = sgqlc.types.Field(sgqlc.types.non_null(NotificationConfig), graphql_name='notificationConfig', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    notification_config_app = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(App)), graphql_name='notificationConfigApp')
    notification_config_list = sgqlc.types.Field(sgqlc.types.non_null(NotificationConfigList), graphql_name='notificationConfigList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(NotificationConfigFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    notification_list = sgqlc.types.Field(sgqlc.types.non_null(NotificationList), graphql_name='notificationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(NotificationFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    oauth_permission_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Permission)), graphql_name='oauthPermissionList', args=sgqlc.types.ArgDict((
        ('client_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='clientId', default=None)),
))
    )
    outside_calibrate = sgqlc.types.Field(OutsideCalibrate, graphql_name='outsideCalibrate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    outside_calibrate_list = sgqlc.types.Field(sgqlc.types.non_null(OutsideCalibrateList), graphql_name='outsideCalibrateList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(OutsideCalibrateListListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    permission_list = sgqlc.types.Field(sgqlc.types.non_null(PermissionList), graphql_name='permissionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PermissionListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    permission_tree = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='permissionTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PermissionTreeFilterInput, graphql_name='filter', default=None)),
))
    )
    platform_admin_users = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='platformAdminUsers', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    platform_user_list = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='platformUserList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(PlatformUserListFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    product_flow = sgqlc.types.Field(ProductFlow, graphql_name='productFlow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    product_flows = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ProductFlow)), graphql_name='productFlows', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProductFlowFilterInput, graphql_name='filter', default=None)),
))
    )
    product_project = sgqlc.types.Field(ProductProject, graphql_name='productProject', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    product_project_document_list = sgqlc.types.Field(sgqlc.types.non_null(ProductProjectDocumentList), graphql_name='productProjectDocumentList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProductProjectDocumentFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    product_project_list = sgqlc.types.Field(sgqlc.types.non_null(ProductProjectList), graphql_name='productProjectList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProductProjectFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    product_task = sgqlc.types.Field(ProductTask, graphql_name='productTask', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    product_task_list = sgqlc.types.Field(sgqlc.types.non_null(ProductTaskList), graphql_name='productTaskList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProductTaskFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    project_group = sgqlc.types.Field(ProjectGroup, graphql_name='projectGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    project_group_list = sgqlc.types.Field(sgqlc.types.non_null(ProjectGroupList), graphql_name='projectGroupList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ProjectGroupFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    project_group_member_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProjectGroupMember))), graphql_name='projectGroupMemberList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='id', default=None)),
))
    )
    provinces = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Province)), graphql_name='provinces')
    quick_access_app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(App))), graphql_name='quickAccessApp')
    range_data = sgqlc.types.Field('RangeData', graphql_name='rangeData', args=sgqlc.types.ArgDict((
        ('duty_person', sgqlc.types.Arg(String, graphql_name='dutyPerson', default=None)),
        ('end_date', sgqlc.types.Arg(Timestamp, graphql_name='endDate', default=None)),
        ('end_shift', sgqlc.types.Arg(Int, graphql_name='endShift', default=None)),
        ('shift', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='shift', default=None)),
        ('start_date', sgqlc.types.Arg(Timestamp, graphql_name='startDate', default=None)),
        ('start_shift', sgqlc.types.Arg(Int, graphql_name='startShift', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    real_raw = sgqlc.types.Field(JSONString, graphql_name='realRaw', args=sgqlc.types.ArgDict((
        ('fields', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='fields', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    real_report = sgqlc.types.Field(JSONString, graphql_name='realReport', args=sgqlc.types.ArgDict((
        ('fields', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='fields', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    recent_app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(App))), graphql_name='recentApp', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limit', default=None)),
))
    )
    repair_rate_summary = sgqlc.types.Field(sgqlc.types.non_null('RepairRateSummary'), graphql_name='repairRateSummary', args=sgqlc.types.ArgDict((
        ('month', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='month', default=None)),
))
    )
    role_exists = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='roleExists', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(RoleExistsFilterInput, graphql_name='filter', default=None)),
))
    )
    role_list = sgqlc.types.Field(sgqlc.types.non_null('RoleList'), graphql_name='roleList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(RoleFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    role_thing_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingCategory'))), graphql_name='roleThingCategories', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(RoleThingCategoryFilterInput, graphql_name='filter', default=None)),
))
    )
    sale_order_summary = sgqlc.types.Field(sgqlc.types.non_null('SaleOrderSummary'), graphql_name='saleOrderSummary', args=sgqlc.types.ArgDict((
        ('date', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='date', default=None)),
))
    )
    source_key = sgqlc.types.Field('SourceKey', graphql_name='sourceKey', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    source_key_list = sgqlc.types.Field(sgqlc.types.non_null('SourceKeyList'), graphql_name='sourceKeyList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SouceKeyFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
))
    )
    source_model_key_list = sgqlc.types.Field(sgqlc.types.non_null('SourceModelKeyList'), graphql_name='sourceModelKeyList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SouceModelKeyFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    spare_part = sgqlc.types.Field('SparePart', graphql_name='sparePart', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    spare_part_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='sparePartImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    spare_part_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartList'), graphql_name='sparePartList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_outbound = sgqlc.types.Field('SparePartOutbound', graphql_name='sparePartOutbound', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    spare_part_outbound_item_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartOutboundItemList'), graphql_name='sparePartOutboundItemList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SparePartOutboundItemFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_outbound_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartOutboundList'), graphql_name='sparePartOutboundList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartOutboundFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_outbound_summary = sgqlc.types.Field(sgqlc.types.non_null('SparePartOutboundSummary'), graphql_name='sparePartOutboundSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartOutboundSummaryFilterInput, graphql_name='filter', default=None)),
))
    )
    spare_part_receipt = sgqlc.types.Field('SparePartReceipt', graphql_name='sparePartReceipt', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    spare_part_receipt_item_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartReceiptItemList'), graphql_name='sparePartReceiptItemList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SparePartReceiptItemFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_receipt_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartReceiptList'), graphql_name='sparePartReceiptList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartReceiptFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_stock_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartStockList'), graphql_name='sparePartStockList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartStockFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    spare_part_writeoff_list = sgqlc.types.Field(sgqlc.types.non_null('SparePartWriteoffList'), graphql_name='sparePartWriteoffList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SparePartWriteoffFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    stock_top_summary = sgqlc.types.Field(sgqlc.types.non_null('StockTopSummary'), graphql_name='stockTopSummary')
    sub_thing_list = sgqlc.types.Field(sgqlc.types.non_null('ThingList'), graphql_name='subThingList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(SubThingListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    support_users = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('User')), graphql_name='supportUsers')
    system_log_action = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='systemLogAction', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyId', default=None)),
))
    )
    system_log_list = sgqlc.types.Field(sgqlc.types.non_null('SystemLogList'), graphql_name='systemLogList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(SystemLogFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    table_fields_config = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableFieldConfig'))), graphql_name='tableFieldsConfig', args=sgqlc.types.ArgDict((
        ('default_fields_config', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TableFieldConfigInput))), graphql_name='defaultFieldsConfig', default=None)),
        ('filter', sgqlc.types.Arg(TableFieldConfigFilterInput, graphql_name='filter', default=None)),
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    thing = sgqlc.types.Field('Thing', graphql_name='thing', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    thing_access_config_list = sgqlc.types.Field(sgqlc.types.non_null('ThingAccessConfigList'), graphql_name='thingAccessConfigList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingAccessConfigFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
))
    )
    thing_borrow = sgqlc.types.Field('ThingBorrow', graphql_name='thingBorrow', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_borrow_approve_configuration = sgqlc.types.Field('ThingBorrowApproveConfiguration', graphql_name='thingBorrowApproveConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_borrow_approve_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowApproveConfigurationList'), graphql_name='thingBorrowApproveConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingBorrowApproveConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_borrow_default_approve_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowApproveConfigurationList'), graphql_name='thingBorrowDefaultApproveConfigurationList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_borrow_draft = sgqlc.types.Field('ThingBorrowDraft', graphql_name='thingBorrowDraft', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_borrow_item = sgqlc.types.Field('ThingBorrowItem', graphql_name='thingBorrowItem', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_borrow_item_list = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowItemList'), graphql_name='thingBorrowItemList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingBorrowItemListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_borrow_list = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowList'), graphql_name='thingBorrowList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingBorrowListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_borrow_operator_record_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingBorrowOperatorRecord'))), graphql_name='thingBorrowOperatorRecordList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_borrow_state_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingBorrowStateOverview'), graphql_name='thingBorrowStateOverview', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_by_qr_code = sgqlc.types.Field('Thing', graphql_name='thingByQrCode', args=sgqlc.types.ArgDict((
        ('qr_code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='qrCode', default=None)),
))
    )
    thing_calibrate = sgqlc.types.Field('ThingCalibrate', graphql_name='thingCalibrate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_calibrate_default_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingCalibrateWorkflowConfigurationList'), graphql_name='thingCalibrateDefaultWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_calibrate_list = sgqlc.types.Field(sgqlc.types.non_null('ThingCalibrateList'), graphql_name='thingCalibrateList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingCalibrateListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_calibrate_record_list = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingCalibrateRecord'))), graphql_name='thingCalibrateRecordList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_calibrate_status_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingCalibrateStatusOverview'), graphql_name='thingCalibrateStatusOverview', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_calibrate_workflow_configuration = sgqlc.types.Field('ThingCalibrateWorkflowConfiguration', graphql_name='thingCalibrateWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_calibrate_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingCalibrateWorkflowConfigurationList'), graphql_name='thingCalibrateWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingCalibrateWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_category = sgqlc.types.Field('ThingCategory', graphql_name='thingCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_category_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingCategoryImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_category_list = sgqlc.types.Field(sgqlc.types.non_null('ThingCategoryList'), graphql_name='thingCategoryList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingCategoryListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_category_tree = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='thingCategoryTree', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingCategoryListFilterInput), graphql_name='filter', default=None)),
))
    )
    thing_change_borrow_draft = sgqlc.types.Field('ThingChangeBorrowDraft', graphql_name='thingChangeBorrowDraft', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='code', default=None)),
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_circulation_list = sgqlc.types.Field(sgqlc.types.non_null('ThingCirculationList'), graphql_name='thingCirculationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingCirculationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_electricity_consumption_list = sgqlc.types.Field(sgqlc.types.non_null('ThingElectricityConsumptionList'), graphql_name='thingElectricityConsumptionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingElectricityConsumptionFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_electricity_consumption_report_list = sgqlc.types.Field(sgqlc.types.non_null('ThingEnergyConsumptionReportList'), graphql_name='thingElectricityConsumptionReportList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingEnergyConsumptionReportFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_energy_consumption_report = sgqlc.types.Field(sgqlc.types.non_null('ThingEnergyConsumptionReport'), graphql_name='thingEnergyConsumptionReport', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingEnergyConsumptionReportFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_function_department = sgqlc.types.Field('ThingFunctionDepartment', graphql_name='thingFunctionDepartment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_function_department_list = sgqlc.types.Field(sgqlc.types.non_null('ThingFunctionDepartmentList'), graphql_name='thingFunctionDepartmentList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingFunctionDepartmentFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_group = sgqlc.types.Field(sgqlc.types.non_null('ThingGroup'), graphql_name='thingGroup', args=sgqlc.types.ArgDict((
        ('thing_group', sgqlc.types.Arg(sgqlc.types.non_null(IDInput), graphql_name='thingGroup', default=None)),
))
    )
    thing_group_depts = sgqlc.types.Field(sgqlc.types.non_null(DeptThingGroupList), graphql_name='thingGroupDepts', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingGroupDeptFilter), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_group_electricity_consumption_list = sgqlc.types.Field(sgqlc.types.non_null('ThingGroupElectricityConsumptionList'), graphql_name='thingGroupElectricityConsumptionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingGroupElectricityConsumptionFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_group_electricity_consumption_report_list = sgqlc.types.Field(sgqlc.types.non_null('ThingGroupEnergyConsumptionReportList'), graphql_name='thingGroupElectricityConsumptionReportList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingGroupEnergyConsumptionReportFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_group_energy_consumption_report = sgqlc.types.Field(sgqlc.types.non_null('ThingGroupEnergyConsumptionReport'), graphql_name='thingGroupEnergyConsumptionReport', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingGroupEnergyConsumptionReportFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_group_list = sgqlc.types.Field(sgqlc.types.non_null('ThingGroupList'), graphql_name='thingGroupList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingGroupFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_group_tree = sgqlc.types.Field(sgqlc.types.non_null(JSONString), graphql_name='thingGroupTree', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(Int, graphql_name='companyId', default=None)),
))
    )
    thing_group_users = sgqlc.types.Field(sgqlc.types.non_null('UserThingGroupList'), graphql_name='thingGroupUsers', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingGroupUserFilter), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_group_vapor_consumption_list = sgqlc.types.Field(sgqlc.types.non_null('ThingGroupVaporConsumptionList'), graphql_name='thingGroupVaporConsumptionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingGroupVaporConsumptionFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_group_vapor_consumption_report_list = sgqlc.types.Field(sgqlc.types.non_null('ThingGroupEnergyConsumptionReportList'), graphql_name='thingGroupVaporConsumptionReportList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingGroupEnergyConsumptionReportFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_group_water_consumption_list = sgqlc.types.Field(sgqlc.types.non_null('ThingGroupWaterConsumptionList'), graphql_name='thingGroupWaterConsumptionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingGroupWaterConsumptionFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_group_water_consumption_report_list = sgqlc.types.Field(sgqlc.types.non_null('ThingGroupEnergyConsumptionReportList'), graphql_name='thingGroupWaterConsumptionReportList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingGroupEnergyConsumptionReportFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_input_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInputRecordList'), graphql_name='thingInputRecordList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInputRecordFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_input_record_summary_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInputRecordSummaryList'), graphql_name='thingInputRecordSummaryList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInputRecordSummaryFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    thing_inspection = sgqlc.types.Field('ThingInspection', graphql_name='thingInspection', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_inspection_default_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionWorkflowConfigurationList'), graphql_name='thingInspectionDefaultWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_inspection_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionList'), graphql_name='thingInspectionList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInspectionListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_inspection_operator_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionOperatorRecordList'), graphql_name='thingInspectionOperatorRecordList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_inspection_status_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionStatusOverview'), graphql_name='thingInspectionStatusOverview', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_inspection_workflow_configuration = sgqlc.types.Field('ThingInspectionWorkflowConfiguration', graphql_name='thingInspectionWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_inspection_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingInspectionWorkflowConfigurationList'), graphql_name='thingInspectionWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingInspectionWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_label = sgqlc.types.Field('ThingLabel', graphql_name='thingLabel', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_label_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingLabelImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_label_list = sgqlc.types.Field(sgqlc.types.non_null('ThingLabelList'), graphql_name='thingLabelList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingLabelListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_list = sgqlc.types.Field(sgqlc.types.non_null('ThingList'), graphql_name='thingList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_maintenance = sgqlc.types.Field('ThingMaintenance', graphql_name='thingMaintenance', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_maintenance_default_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceWorkflowConfigurationList'), graphql_name='thingMaintenanceDefaultWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_maintenance_list = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceList'), graphql_name='thingMaintenanceList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingMaintenanceFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_maintenance_operator_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceOperatorRecordList'), graphql_name='thingMaintenanceOperatorRecordList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_maintenance_status_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceStatusOverview'), graphql_name='thingMaintenanceStatusOverview', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_maintenance_workflow_configuration = sgqlc.types.Field('ThingMaintenanceWorkflowConfiguration', graphql_name='thingMaintenanceWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_maintenance_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingMaintenanceWorkflowConfigurationList'), graphql_name='thingMaintenanceWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingMaintenanceWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_mechanism_model = sgqlc.types.Field(sgqlc.types.non_null('ThingMechanismModelList'), graphql_name='thingMechanismModel', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingMechanismModelFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_on_state_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingOnStateOverview'), graphql_name='thingOnStateOverview', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(Int, graphql_name='companyId', default=None)),
))
    )
    thing_rate = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TimeseriesUnit'))), graphql_name='thingRate', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(ThingRateFilter), graphql_name='filter', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    thing_rate_overall = sgqlc.types.Field(CockpitRateOverall, graphql_name='thingRateOverall', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(TimerangeFilter), graphql_name='filter', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    thing_repair = sgqlc.types.Field('ThingRepair', graphql_name='thingRepair', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_repair_default_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairWorkflowConfigurationList'), graphql_name='thingRepairDefaultWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_repair_list = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairList'), graphql_name='thingRepairList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingRepairFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_repair_operator_record_list = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairOperatorRecordList'), graphql_name='thingRepairOperatorRecordList', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_repair_status_overview = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairStatusOverview'), graphql_name='thingRepairStatusOverview', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_repair_workflow_configuration = sgqlc.types.Field('ThingRepairWorkflowConfiguration', graphql_name='thingRepairWorkflowConfiguration', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_repair_workflow_configuration_list = sgqlc.types.Field(sgqlc.types.non_null('ThingRepairWorkflowConfigurationList'), graphql_name='thingRepairWorkflowConfigurationList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingRepairWorkflowConfigurationListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_report_list = sgqlc.types.Field('ThingReportList', graphql_name='thingReportList', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('energy_group', sgqlc.types.Arg(sgqlc.types.list_of(IDInput), graphql_name='energyGroup', default=None)),
        ('energy_type', sgqlc.types.Arg(sgqlc.types.list_of(EnergyType), graphql_name='energyType', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('tag', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tag', default=None)),
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(IDInput), graphql_name='types', default=None)),
))
    )
    thing_schedule = sgqlc.types.Field('ThingSchedule', graphql_name='thingSchedule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_schedule_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingScheduleImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_schedule_list = sgqlc.types.Field(sgqlc.types.non_null('ThingScheduleList'), graphql_name='thingScheduleList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingScheduleFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_schedule_thing_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingScheduleThingImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_spare_part_import_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='thingSparePartImportTemplate', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    thing_specification_language = sgqlc.types.Field('ThingSpecificationLanguage', graphql_name='thingSpecificationLanguage', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_specification_language_list = sgqlc.types.Field(sgqlc.types.non_null('ThingSpecificationLanguageList'), graphql_name='thingSpecificationLanguageList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingSpecificationLanguageFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_specification_language_property = sgqlc.types.Field('ThingSpecificationLanguageProperty', graphql_name='thingSpecificationLanguageProperty', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    thing_specification_language_property_list = sgqlc.types.Field(sgqlc.types.non_null('ThingSpecificationLanguagePropertyList'), graphql_name='thingSpecificationLanguagePropertyList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingSpecificationLanguagePropertyFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_status = sgqlc.types.Field('ThingStatus', graphql_name='thingStatus', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    thing_statuses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingStatus'))), graphql_name='thingStatuses', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingStatusFilterInput, graphql_name='filter', default=None)),
))
    )
    thing_task_list = sgqlc.types.Field(sgqlc.types.non_null('ThingTaskList'), graphql_name='thingTaskList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingTaskFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_thing_specification_language_list = sgqlc.types.Field(sgqlc.types.non_null('ThingThingSpecificationLanguageList'), graphql_name='thingThingSpecificationLanguageList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingThingSpecificationLanguageFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_total_report_list = sgqlc.types.Field('ThingTotalReportList', graphql_name='thingTotalReportList', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('energy_type', sgqlc.types.Arg(sgqlc.types.list_of(EnergyType), graphql_name='energyType', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
))
    )
    thing_type = sgqlc.types.Field('ThingType', graphql_name='thingType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    thing_type_code_list = sgqlc.types.Field(sgqlc.types.non_null('ThingTypeCodeList'), graphql_name='thingTypeCodeList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingTypeCodeFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    thing_type_list = sgqlc.types.Field(sgqlc.types.non_null('ThingTypeList'), graphql_name='thingTypeList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingTypeFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
))
    )
    thing_types = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingType'))), graphql_name='thingTypes', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingTypeFilterInput, graphql_name='filter', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
))
    )
    things = sgqlc.types.Field(sgqlc.types.non_null('ThingList'), graphql_name='things', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(ThingFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    things_energy_consumption_overall = sgqlc.types.Field('ThingsEnergyConsumptionOverall', graphql_name='thingsEnergyConsumptionOverall', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    things_energy_consumption_overall_sub = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingsEnergyConsumptionOverall')), graphql_name='thingsEnergyConsumptionOverallSub', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('organizations', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='organizations', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    things_energy_consumption_rank = sgqlc.types.Field('ThingsRank', graphql_name='thingsEnergyConsumptionRank', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    things_operation_rate_rank = sgqlc.types.Field('ThingsRank', graphql_name='thingsOperationRateRank', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    things_overall = sgqlc.types.Field('ThingsOverall', graphql_name='thingsOverall', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    things_peak_rate_rank = sgqlc.types.Field('ThingsRank', graphql_name='thingsPeakRateRank', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    things_power_on_rate_rank = sgqlc.types.Field('ThingsRank', graphql_name='thingsPowerOnRateRank', args=sgqlc.types.ArgDict((
        ('company_id', sgqlc.types.Arg(ID, graphql_name='companyID', default=None)),
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('thing_type', sgqlc.types.Arg(ID, graphql_name='thingType', default=None)),
))
    )
    total_report = sgqlc.types.Field(JSONString, graphql_name='totalReport', args=sgqlc.types.ArgDict((
        ('end', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='end', default=None)),
        ('fields', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='fields', default=None)),
        ('start', sgqlc.types.Arg(sgqlc.types.non_null(Timestamp), graphql_name='start', default=None)),
        ('tags', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='tags', default=None)),
        ('thing_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='thingID', default=None)),
))
    )
    type_companies = sgqlc.types.Field(sgqlc.types.non_null('TypeCompaniesList'), graphql_name='typeCompanies', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(CompanyFilter, graphql_name='filter', default=None)),
        ('scenario', sgqlc.types.Arg(TypeCompaniesScenario, graphql_name='scenario', default=None)),
))
    )
    ucc_form_structure = sgqlc.types.Field(sgqlc.types.non_null('UCCFormStructure'), graphql_name='uccFormStructure', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(UCCFormStructureFilter), graphql_name='filter', default=None)),
))
    )
    ucc_form_structure_json_schema = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='uccFormStructureJsonSchema', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(UCCFormStructureFilter), graphql_name='filter', default=None)),
))
    )
    upload_config = sgqlc.types.Field('UploadConfig', graphql_name='uploadConfig', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    upload_configs = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UploadConfig')), graphql_name='uploadConfigs', args=sgqlc.types.ArgDict((
        ('names', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='names', default=None)),
))
    )
    upload_pdm_config = sgqlc.types.Field('UploadConfig', graphql_name='uploadPdmConfig', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    upload_pdm_configs = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UploadConfig'))), graphql_name='uploadPdmConfigs', args=sgqlc.types.ArgDict((
        ('names', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='names', default=None)),
))
    )
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    user_template = sgqlc.types.Field(sgqlc.types.non_null('RawFile'), graphql_name='userTemplate')
    users = sgqlc.types.Field(sgqlc.types.non_null('UserList'), graphql_name='users', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(UserListFilter, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    validate_inspection_method_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateInspectionMethodExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_maintenance_method_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateMaintenanceMethodExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_meter_reading_data_excel = sgqlc.types.Field(sgqlc.types.non_null(EmsExcelValidationResult), graphql_name='validateMeterReadingDataExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_spare_part_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateSparePartExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_category_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingCategoryExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_label_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingLabelExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_schedule_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingScheduleExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_schedule_thing_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingScheduleThingExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    validate_thing_spare_part_excel = sgqlc.types.Field(sgqlc.types.non_null(EamExcelValidationResult), graphql_name='validateThingSparePartExcel', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
        ('file_path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='filePath', default=None)),
))
    )
    workbench = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkbenchCard'))), graphql_name='workbench')
    workbench_card_data = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='workbenchCardData', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    workbench_card_option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkbenchCard'))), graphql_name='workbenchCardOption')
    worker_order_detail = sgqlc.types.Field('WorkerOrder', graphql_name='workerOrderDetail', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    worker_order_list = sgqlc.types.Field(sgqlc.types.non_null('WorkerOrderList'), graphql_name='workerOrderList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(WorkerOrderListFilterInput, graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    worker_order_operator_detail = sgqlc.types.Field('WorkerOrderOperator', graphql_name='workerOrderOperatorDetail', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    worker_order_operator_list = sgqlc.types.Field(sgqlc.types.non_null('WorkerOrderOperatorList'), graphql_name='workerOrderOperatorList', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(sgqlc.types.non_null(WorkerOrderOperatorListFilterInput), graphql_name='filter', default=None)),
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='orderBy', default=None)),
))
    )
    worker_order_status_summary = sgqlc.types.Field(sgqlc.types.non_null('WorkerOrderStatusSummary'), graphql_name='workerOrderStatusSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(WorkerOrderFilterInput, graphql_name='filter', default=None)),
))
    )
    worker_order_thing_type_summary = sgqlc.types.Field(sgqlc.types.non_null('WorkerOrderThingTypeSummary'), graphql_name='workerOrderThingTypeSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(WorkerOrderFilterInput, graphql_name='filter', default=None)),
))
    )
    worker_order_top_personnel_summary = sgqlc.types.Field(sgqlc.types.non_null('WorkerOrderTopPersonnelSummary'), graphql_name='workerOrderTopPersonnelSummary', args=sgqlc.types.ArgDict((
        ('filter', sgqlc.types.Arg(WorkerOrderFilterInput, graphql_name='filter', default=None)),
))
    )
    workflow_base_configuration = sgqlc.types.Field('WorkflowBaseConfiguration', graphql_name='workflowBaseConfiguration', args=sgqlc.types.ArgDict((
        ('company', sgqlc.types.Arg(IDInput, graphql_name='company', default=None)),
))
    )
    workflow_default_init_state = sgqlc.types.Field(sgqlc.types.non_null('WorkflowDefaultInitState'), graphql_name='workflowDefaultInitState')


class RangeData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('detail', 'total')
    detail = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ThingData')), graphql_name='detail')
    total = sgqlc.types.Field('ThingData', graphql_name='total')


class RawData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('company_id', 'data', 'id', 'tag', 'thing_id', 'timestamp')
    company_id = sgqlc.types.Field(ID, graphql_name='companyID')
    data = sgqlc.types.Field(JSONString, graphql_name='data')
    id = sgqlc.types.Field(ID, graphql_name='id')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    thing_id = sgqlc.types.Field(ID, graphql_name='thingID')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class RawDataList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(RawData)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RawFile(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'name')
    data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='data')
    name = sgqlc.types.Field(String, graphql_name='name')


class RepairRate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('production_code', 'rate')
    production_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='productionCode')
    rate = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rate')


class RepairRateSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RepairRate))), graphql_name='data')


class RepairSparePartItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null('SparePart'), graphql_name='sparePart')


class Repeat(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('day_of_month', 'day_of_week', 'day_of_year', 'frequency', 'period')
    day_of_month = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dayOfMonth')
    day_of_week = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='dayOfWeek')
    day_of_year = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(DayOfYear)), graphql_name='dayOfYear')
    frequency = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='frequency')
    period = sgqlc.types.Field(sgqlc.types.non_null(RepeatPeriod), graphql_name='period')


class Role(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('app', 'created_at', 'desc', 'id', 'name', 'permissions', 'updated_at')
    app = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(App)), graphql_name='app')
    created_at = sgqlc.types.Field(Timestamp, graphql_name='createdAt')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Permission))), graphql_name='permissions')
    updated_at = sgqlc.types.Field(Timestamp, graphql_name='updatedAt')


class RoleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Role))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SaleOrderSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('current_month_sale_order_count', 'today_sale_order_count')
    current_month_sale_order_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='currentMonthSaleOrderCount')
    today_sale_order_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='todaySaleOrderCount')


class SourceKey(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('desc', 'id', 'key', 'thing_type')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')


class SourceKeyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SourceKey))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SourceModelKey(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('desc', 'key', 'thing_mechanism_model')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    thing_mechanism_model = sgqlc.types.Field(sgqlc.types.non_null('ThingMechanismModel'), graphql_name='thingMechanismModel')


class SourceModelKeyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SourceModelKey))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePart(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('attachment', 'code', 'distributor', 'field_data', 'id', 'image', 'inventory', 'manufacturer', 'name', 'safe_inventory_max', 'safe_inventory_min', 'specification', 'thing')
    attachment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='attachment')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='image')
    inventory = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='inventory')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    safe_inventory_max = sgqlc.types.Field(Int, graphql_name='safeInventoryMax')
    safe_inventory_min = sgqlc.types.Field(Int, graphql_name='safeInventoryMin')
    specification = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='specification')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Thing'))), graphql_name='thing')


class SparePartInventory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('depository', 'inventory')
    depository = sgqlc.types.Field(sgqlc.types.non_null(Depository), graphql_name='depository')
    inventory = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='inventory')


class SparePartItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('quantity', 'spare_part')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')


class SparePartList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePart))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartOutbound(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'date', 'depository', 'id', 'item', 'kind', 'operator', 'remark', 'thing_maintenance', 'thing_repair')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    depository = sgqlc.types.Field(sgqlc.types.non_null(Depository), graphql_name='depository')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartOutboundItem'))), graphql_name='item')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SparePartOutboundKind), graphql_name='kind')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    thing_maintenance = sgqlc.types.Field('ThingMaintenance', graphql_name='thingMaintenance')
    thing_repair = sgqlc.types.Field('ThingRepair', graphql_name='thingRepair')


class SparePartOutboundItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'quantity', 'spare_part', 'spare_part_outbound', 'writeoff_quantity')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')
    spare_part_outbound = sgqlc.types.Field(sgqlc.types.non_null(SparePartOutbound), graphql_name='sparePartOutbound')
    writeoff_quantity = sgqlc.types.Field(Int, graphql_name='writeoffQuantity')


class SparePartOutboundItemList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartOutboundItem))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartOutboundList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartOutbound))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartOutboundSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartItem))), graphql_name='data')


class SparePartReceipt(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'date', 'depository', 'id', 'item', 'kind', 'operator', 'remark')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    depository = sgqlc.types.Field(sgqlc.types.non_null(Depository), graphql_name='depository')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartReceiptItem'))), graphql_name='item')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SparePartReceiptKind), graphql_name='kind')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    remark = sgqlc.types.Field(String, graphql_name='remark')


class SparePartReceiptItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'quantity', 'spare_part', 'spare_part_receipt', 'stock', 'writeoff_quantity')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')
    spare_part_receipt = sgqlc.types.Field(sgqlc.types.non_null(SparePartReceipt), graphql_name='sparePartReceipt')
    stock = sgqlc.types.Field(sgqlc.types.non_null('SparePartStock'), graphql_name='stock')
    writeoff_quantity = sgqlc.types.Field(Int, graphql_name='writeoffQuantity')


class SparePartReceiptItemList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartReceiptItem))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartReceiptList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartReceipt))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartStock(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('depository', 'quantity', 'spare_part')
    depository = sgqlc.types.Field(sgqlc.types.non_null(Depository), graphql_name='depository')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')


class SparePartStockList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartStock))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SparePartWriteoff(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'date', 'depository', 'id', 'item', 'kind', 'reason', 'spare_part_outbound', 'spare_part_receipt')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    date = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='date')
    depository = sgqlc.types.Field(sgqlc.types.non_null(Depository), graphql_name='depository')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SparePartWriteoffItem'))), graphql_name='item')
    kind = sgqlc.types.Field(sgqlc.types.non_null(SparePartWriteoffKind), graphql_name='kind')
    reason = sgqlc.types.Field(String, graphql_name='reason')
    spare_part_outbound = sgqlc.types.Field(SparePartOutbound, graphql_name='sparePartOutbound')
    spare_part_receipt = sgqlc.types.Field(SparePartReceipt, graphql_name='sparePartReceipt')


class SparePartWriteoffItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'quantity', 'spare_part', 'spare_part_outbound_item', 'spare_part_receipt_item')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    quantity = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='quantity')
    spare_part = sgqlc.types.Field(sgqlc.types.non_null(SparePart), graphql_name='sparePart')
    spare_part_outbound_item = sgqlc.types.Field(SparePartOutboundItem, graphql_name='sparePartOutboundItem')
    spare_part_receipt_item = sgqlc.types.Field(SparePartReceiptItem, graphql_name='sparePartReceiptItem')


class SparePartWriteoffList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SparePartWriteoff))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class StatusDistribution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('operation', 'shutdown', 'standby')
    operation = sgqlc.types.Field(Int, graphql_name='operation')
    shutdown = sgqlc.types.Field(Int, graphql_name='shutdown')
    standby = sgqlc.types.Field(Int, graphql_name='standby')


class StockTopSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ProductStockCount))), graphql_name='data')


class SystemLog(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('action', 'app', 'id', 'resource', 'timestamp', 'user')
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    app = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='app')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    resource = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='resource')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    user = sgqlc.types.Field('User', graphql_name='user')


class SystemLogList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SystemLog))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TableConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('fields', 'key', 'label')
    fields = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TableFieldConfig'))), graphql_name='fields')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')


class TableFieldConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('editable', 'group', 'key', 'label', 'visible')
    editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='editable')
    group = sgqlc.types.Field(TableFieldGroup, graphql_name='group')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')
    visible = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='visible')


class TempFile(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('length', 'name', 'url')
    length = sgqlc.types.Field(Int, graphql_name='length')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class Thing(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('access_key', 'activated_at', 'attachment', 'calibrate_code', 'calibrate_method', 'calibrate_repeat', 'calibrate_result', 'calibrate_state', 'can_borrowed', 'category', 'code', 'company_id', 'department', 'depreciation_rate', 'desc', 'distributor', 'energy_group', 'field_data', 'id', 'image', 'installed_at', 'is_calibration_expired', 'is_deleted', 'is_lent', 'label', 'last_calibrate_at', 'machine_number', 'maintainer', 'manager', 'manufacturer', 'name', 'next_calibrate_at', 'on_state', 'parent_thing', 'predict_residual_rate', 'purchased_at', 'qr_code', 'serial_number', 'specification', 'status', 'thing_group', 'type', 'used_year', 'years_of_use')
    access_key = sgqlc.types.Field(String, graphql_name='accessKey')
    activated_at = sgqlc.types.Field(Timestamp, graphql_name='activatedAt')
    attachment = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='attachment')
    calibrate_code = sgqlc.types.Field(String, graphql_name='calibrateCode')
    calibrate_method = sgqlc.types.Field(sgqlc.types.non_null(CalibrateMethod), graphql_name='calibrateMethod')
    calibrate_repeat = sgqlc.types.Field(CalibrateRepeat, graphql_name='calibrateRepeat')
    calibrate_result = sgqlc.types.Field(sgqlc.types.non_null(CalibrateResult), graphql_name='calibrateResult')
    calibrate_state = sgqlc.types.Field(sgqlc.types.non_null(CalibrateState), graphql_name='calibrateState')
    can_borrowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='canBorrowed')
    category = sgqlc.types.Field('ThingCategory', graphql_name='category')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    company_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='companyID')
    department = sgqlc.types.Field(Department, graphql_name='department')
    depreciation_rate = sgqlc.types.Field(Float, graphql_name='depreciationRate')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    distributor = sgqlc.types.Field(String, graphql_name='distributor')
    energy_group = sgqlc.types.Field(EnergyGroup, graphql_name='energyGroup')
    field_data = sgqlc.types.Field(JSON, graphql_name='fieldData')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    image = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='image')
    installed_at = sgqlc.types.Field(Timestamp, graphql_name='installedAt')
    is_calibration_expired = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCalibrationExpired')
    is_deleted = sgqlc.types.Field(Boolean, graphql_name='isDeleted')
    is_lent = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLent')
    label = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingLabel'))), graphql_name='label')
    last_calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='lastCalibrateAt')
    machine_number = sgqlc.types.Field(String, graphql_name='machineNumber')
    maintainer = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='maintainer')
    manager = sgqlc.types.Field('User', graphql_name='manager')
    manufacturer = sgqlc.types.Field(String, graphql_name='manufacturer')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    next_calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='nextCalibrateAt')
    on_state = sgqlc.types.Field(sgqlc.types.non_null(OnState), graphql_name='onState')
    parent_thing = sgqlc.types.Field('Thing', graphql_name='parentThing')
    predict_residual_rate = sgqlc.types.Field(Float, graphql_name='predictResidualRate')
    purchased_at = sgqlc.types.Field(Timestamp, graphql_name='purchasedAt')
    qr_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='qrCode')
    serial_number = sgqlc.types.Field(String, graphql_name='serialNumber')
    specification = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='specification')
    status = sgqlc.types.Field(Int, graphql_name='status')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null('ThingGroup'), graphql_name='thingGroup')
    type = sgqlc.types.Field('ThingType', graphql_name='type')
    used_year = sgqlc.types.Field(Float, graphql_name='usedYear')
    years_of_use = sgqlc.types.Field(Float, graphql_name='yearsOfUse')


class ThingAccessConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('access_key', 'id', 'thing', 'thing_type')
    access_key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='accessKey')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    thing_type = sgqlc.types.Field('ThingType', graphql_name='thingType')


class ThingAccessConfigList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingAccessConfig))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingBorrow(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('applicant', 'code', 'created_at', 'department_of_applicant', 'department_of_manager', 'id', 'reason', 'state', 'updated_at')
    applicant = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='applicant')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    department_of_applicant = sgqlc.types.Field(sgqlc.types.non_null(Department), graphql_name='departmentOfApplicant')
    department_of_manager = sgqlc.types.Field(sgqlc.types.non_null(Department), graphql_name='departmentOfManager')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    reason = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reason')
    state = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='state')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ThingBorrowApproveConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowTrigger), graphql_name='trigger')


class ThingBorrowApproveConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrowApproveConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingBorrowDraft(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'data', 'id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingBorrowDraftData'))), graphql_name='data')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class ThingBorrowDraftData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('expected_borrow_at', 'expected_return_at', 'thing')
    expected_borrow_at = sgqlc.types.Field(Timestamp, graphql_name='expectedBorrowAt')
    expected_return_at = sgqlc.types.Field(Timestamp, graphql_name='expectedReturnAt')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')


class ThingBorrowItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('expected_borrow_at', 'expected_return_at', 'id', 'thing', 'thing_borrow')
    expected_borrow_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='expectedBorrowAt')
    expected_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='expectedReturnAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    thing_borrow = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrow), graphql_name='thingBorrow')


class ThingBorrowItemList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrowItem))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingBorrowList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingBorrow))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingBorrowOperatorRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'id', 'operate_type', 'operator', 'opinion')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operate_type = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowOperatorType), graphql_name='operateType')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    opinion = sgqlc.types.Field(String, graphql_name='opinion')


class ThingBorrowStateOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('finished_count', 'not_pass_count', 'pending_count', 'total_count', 'under_review_by_apply_for_count', 'under_review_by_borrowed_count')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    not_pass_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='notPassCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    under_review_by_apply_for_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='underReviewByApplyForCount')
    under_review_by_borrowed_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='underReviewByBorrowedCount')


class ThingCalibrate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('calibrate_at', 'calibrate_label', 'calibrate_method', 'calibrate_organization', 'calibrate_report', 'calibrate_result', 'certificate_return_at', 'certificate_state', 'code', 'created_at', 'deadline', 'explain', 'id', 'operator', 'reason', 'return_state', 'send_at', 'state', 'thing', 'thing_repair', 'updated_at')
    calibrate_at = sgqlc.types.Field(Timestamp, graphql_name='calibrateAt')
    calibrate_label = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='calibrateLabel')
    calibrate_method = sgqlc.types.Field(CalibrateMethod, graphql_name='calibrateMethod')
    calibrate_organization = sgqlc.types.Field(CalibrateOrganization, graphql_name='calibrateOrganization')
    calibrate_report = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(File)), graphql_name='calibrateReport')
    calibrate_result = sgqlc.types.Field(CalibrateResult, graphql_name='calibrateResult')
    certificate_return_at = sgqlc.types.Field(Timestamp, graphql_name='certificateReturnAt')
    certificate_state = sgqlc.types.Field(CertificateState, graphql_name='certificateState')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    deadline = sgqlc.types.Field(Timestamp, graphql_name='deadline')
    explain = sgqlc.types.Field(String, graphql_name='explain')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field('User', graphql_name='operator')
    reason = sgqlc.types.Field(sgqlc.types.non_null(CalibrateReason), graphql_name='reason')
    return_state = sgqlc.types.Field(ReturnState, graphql_name='returnState')
    send_at = sgqlc.types.Field(Timestamp, graphql_name='sendAt')
    state = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateState), graphql_name='state')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    thing_repair = sgqlc.types.Field('ThingRepair', graphql_name='thingRepair')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ThingCalibrateConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('by_thing_repair', 'id')
    by_thing_repair = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='byThingRepair')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class ThingCalibrateList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCalibrate))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingCalibrateRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'id', 'operator', 'operator_record_type', 'remark', 'turn_to')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    operator_record_type = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateOperatorType), graphql_name='operatorRecordType')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    turn_to = sgqlc.types.Field('User', graphql_name='turnTo')


class ThingCalibrateStatusOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('calibrating_count', 'finished_count', 'pending_count', 'total_count', 'under_review_count')
    calibrating_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='calibratingCount')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    under_review_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='underReviewCount')


class ThingCalibrateWorkflowConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateState), graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateState), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateTrigger), graphql_name='trigger')


class ThingCalibrateWorkflowConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCalibrateWorkflowConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingCategory(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_calibration', 'name', 'parent_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_calibration = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCalibration')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(Int, graphql_name='parentId')


class ThingCategoryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCategory))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingChangeBorrowDraft(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'data', 'id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingChangeBorrowDraftData'))), graphql_name='data')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class ThingChangeBorrowDraftData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('change_return_at', 'thing', 'thing_circulation')
    change_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='changeReturnAt')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    thing_circulation = sgqlc.types.Field(sgqlc.types.non_null('ThingCirculation'), graphql_name='thingCirculation')


class ThingCirculation(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('borrow_at', 'borrow_remark', 'expected_borrow_at', 'expected_return_at', 'id', 'return_at', 'return_remark', 'state', 'thing', 'thing_borrow')
    borrow_at = sgqlc.types.Field(Timestamp, graphql_name='borrowAt')
    borrow_remark = sgqlc.types.Field(String, graphql_name='borrowRemark')
    expected_borrow_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='expectedBorrowAt')
    expected_return_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='expectedReturnAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    return_at = sgqlc.types.Field(Timestamp, graphql_name='returnAt')
    return_remark = sgqlc.types.Field(String, graphql_name='returnRemark')
    state = sgqlc.types.Field(sgqlc.types.non_null(BorrowState), graphql_name='state')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    thing_borrow = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrow), graphql_name='thingBorrow')


class ThingCirculationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingCirculation))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('date', 'electric_quantity', 'operation_time', 'production', 'shift', 'shutdown_time', 'speed_utilization', 'standby_time', 'status_distribution', 'target_production', 'time_utilization')
    date = sgqlc.types.Field(Timestamp, graphql_name='date')
    electric_quantity = sgqlc.types.Field(Float, graphql_name='electricQuantity')
    operation_time = sgqlc.types.Field(Int, graphql_name='operationTime')
    production = sgqlc.types.Field(Int, graphql_name='production')
    shift = sgqlc.types.Field(Int, graphql_name='shift')
    shutdown_time = sgqlc.types.Field(Int, graphql_name='shutdownTime')
    speed_utilization = sgqlc.types.Field(Float, graphql_name='speedUtilization')
    standby_time = sgqlc.types.Field(Int, graphql_name='standbyTime')
    status_distribution = sgqlc.types.Field(StatusDistribution, graphql_name='statusDistribution')
    target_production = sgqlc.types.Field(Int, graphql_name='targetProduction')
    time_utilization = sgqlc.types.Field(Float, graphql_name='timeUtilization')


class ThingElectricityConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee', 'id', 'thing')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')


class ThingElectricityConsumptionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingElectricityConsumption))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingEnergyConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('electricity', 'electricity_of_last_year', 'electricity_of_previous_period', 'granularity', 'id', 'thing', 'timestamp')
    electricity = sgqlc.types.Field(ElectricityConsumptionData, graphql_name='electricity')
    electricity_of_last_year = sgqlc.types.Field(ElectricityConsumptionData, graphql_name='electricityOfLastYear')
    electricity_of_previous_period = sgqlc.types.Field(ElectricityConsumptionData, graphql_name='electricityOfPreviousPeriod')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(EnergyTimeGranularity), graphql_name='granularity')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class ThingEnergyConsumptionData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('electricity',)
    electricity = sgqlc.types.Field(sgqlc.types.non_null(ElectricityConsumptionData), graphql_name='electricity')


class ThingEnergyConsumptionReport(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count', 'total_data')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingEnergyConsumption))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_data = sgqlc.types.Field(sgqlc.types.non_null(ThingEnergyConsumptionData), graphql_name='totalData')


class ThingEnergyConsumptionReportData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'timestamp')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Float)), graphql_name='data')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class ThingEnergyConsumptionReportList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ThingEnergyConsumptionReportData)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingFunctionDepartment(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_calibrate_user', 'department', 'id')
    default_calibrate_user = sgqlc.types.Field('User', graphql_name='defaultCalibrateUser')
    department = sgqlc.types.Field(sgqlc.types.non_null(Department), graphql_name='department')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class ThingFunctionDepartmentList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingFunctionDepartment))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingGroup(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'is_selected', 'name', 'parent_id', 'path_name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_selected = sgqlc.types.Field(Boolean, graphql_name='isSelected')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    path_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathName')


class ThingGroupElectricityConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee', 'id', 'thing_group')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(ThingGroup), graphql_name='thingGroup')


class ThingGroupElectricityConsumptionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroupElectricityConsumption))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingGroupEnergyConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('electricity', 'electricity_of_last_year', 'electricity_of_previous_period', 'granularity', 'id', 'thing_group', 'timestamp', 'vapor', 'vapor_of_last_year', 'vapor_of_previous_period', 'water', 'water_of_last_year', 'water_of_previous_period')
    electricity = sgqlc.types.Field(ElectricityConsumptionData, graphql_name='electricity')
    electricity_of_last_year = sgqlc.types.Field(ElectricityConsumptionData, graphql_name='electricityOfLastYear')
    electricity_of_previous_period = sgqlc.types.Field(ElectricityConsumptionData, graphql_name='electricityOfPreviousPeriod')
    granularity = sgqlc.types.Field(sgqlc.types.non_null(EnergyTimeGranularity), graphql_name='granularity')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(ThingGroup), graphql_name='thingGroup')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    vapor = sgqlc.types.Field('VaporConsumptionData', graphql_name='vapor')
    vapor_of_last_year = sgqlc.types.Field('VaporConsumptionData', graphql_name='vaporOfLastYear')
    vapor_of_previous_period = sgqlc.types.Field('VaporConsumptionData', graphql_name='vaporOfPreviousPeriod')
    water = sgqlc.types.Field('WaterConsumptionData', graphql_name='water')
    water_of_last_year = sgqlc.types.Field('WaterConsumptionData', graphql_name='waterOfLastYear')
    water_of_previous_period = sgqlc.types.Field('WaterConsumptionData', graphql_name='waterOfPreviousPeriod')


class ThingGroupEnergyConsumptionData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('electricity', 'vapor', 'water')
    electricity = sgqlc.types.Field(sgqlc.types.non_null(ElectricityConsumptionData), graphql_name='electricity')
    vapor = sgqlc.types.Field(sgqlc.types.non_null('VaporConsumptionData'), graphql_name='vapor')
    water = sgqlc.types.Field(sgqlc.types.non_null('WaterConsumptionData'), graphql_name='water')


class ThingGroupEnergyConsumptionReport(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count', 'total_data')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroupEnergyConsumption))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_data = sgqlc.types.Field(sgqlc.types.non_null(ThingGroupEnergyConsumptionData), graphql_name='totalData')


class ThingGroupEnergyConsumptionReportData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'timestamp')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Float)), graphql_name='data')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')


class ThingGroupEnergyConsumptionReportList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroupEnergyConsumptionReportData))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroup)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingGroupVaporConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee', 'id', 'thing_group')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(ThingGroup), graphql_name='thingGroup')


class ThingGroupVaporConsumptionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroupVaporConsumption))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingGroupWaterConsumption(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee', 'id', 'thing_group')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(ThingGroup), graphql_name='thingGroup')


class ThingGroupWaterConsumptionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroupWaterConsumption))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInputDataIntAttribute(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('editable', 'value')
    editable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='editable')
    value = sgqlc.types.Field(Int, graphql_name='value')


class ThingInputRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('deletable', 'finished', 'id', 'product_name', 'production', 'production_beat', 'thing', 'timestamp', 'yield_number')
    deletable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='deletable')
    finished = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='finished')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    product_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='productName')
    production = sgqlc.types.Field(sgqlc.types.non_null(ThingInputDataIntAttribute), graphql_name='production')
    production_beat = sgqlc.types.Field(sgqlc.types.non_null(ThingInputDataIntAttribute), graphql_name='productionBeat')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    yield_number = sgqlc.types.Field(sgqlc.types.non_null(ThingInputDataIntAttribute), graphql_name='yieldNumber')


class ThingInputRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInputRecord))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInputRecordSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('finished', 'finished_count', 'timestamp', 'total_count')
    finished = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='finished')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInputRecordSummaryList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInputRecordSummary))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInspection(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'create_by', 'create_method', 'created_at', 'estimated_time', 'id', 'operator', 'related_operator', 'status', 'thing_inspection_process_item', 'updated_at')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    create_by = sgqlc.types.Field('User', graphql_name='createBy')
    create_method = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionCreateType), graphql_name='createMethod')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    related_operator = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='relatedOperator')
    status = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='status')
    thing_inspection_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingInspectionProcessItem'))), graphql_name='thingInspectionProcessItem')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ThingInspectionList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspection))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInspectionOperatorRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(InspectionOperatorRecord)), graphql_name='data')


class ThingInspectionProcessItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('inspection_process_item', 'thing')
    inspection_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InspectionProcessItem))), graphql_name='inspectionProcessItem')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')


class ThingInspectionStatusOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('finished_count', 'inspecting_count', 'pending_count', 'total_count')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    inspecting_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='inspectingCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingInspectionWorkflowConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionTrigger), graphql_name='trigger')


class ThingInspectionWorkflowConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingInspectionWorkflowConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingLabel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ThingLabelList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingLabel))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Thing))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingMaintenance(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'create_by', 'create_method', 'created_at', 'estimated_time', 'id', 'operator', 'related_operator', 'status', 'thing', 'thing_maintenance_process_item', 'updated_at')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    create_by = sgqlc.types.Field('User', graphql_name='createBy')
    create_method = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceCreateType), graphql_name='createMethod')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    related_operator = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='relatedOperator')
    status = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Thing))), graphql_name='thing')
    thing_maintenance_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingMaintenanceProcessItem'))), graphql_name='thingMaintenanceProcessItem')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ThingMaintenanceList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenance))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingMaintenanceOperatorRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('apply_depository_name', 'apply_factory_name', 'apply_remark', 'apply_spare_part_names', 'cost_time', 'created_at', 'id', 'lack_depository_name', 'lack_factory_name', 'lack_spare_part_names', 'operator', 'operator_record_type', 'pause_reason', 'remark', 'restart_operator', 'turn_to')
    apply_depository_name = sgqlc.types.Field(String, graphql_name='applyDepositoryName')
    apply_factory_name = sgqlc.types.Field(String, graphql_name='applyFactoryName')
    apply_remark = sgqlc.types.Field(String, graphql_name='applyRemark')
    apply_spare_part_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='applySparePartNames')
    cost_time = sgqlc.types.Field(Int, graphql_name='costTime')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    lack_depository_name = sgqlc.types.Field(String, graphql_name='lackDepositoryName')
    lack_factory_name = sgqlc.types.Field(String, graphql_name='lackFactoryName')
    lack_spare_part_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lackSparePartNames')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    operator_record_type = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceOperatorType), graphql_name='operatorRecordType')
    pause_reason = sgqlc.types.Field(String, graphql_name='pauseReason')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    restart_operator = sgqlc.types.Field('User', graphql_name='restartOperator')
    turn_to = sgqlc.types.Field('User', graphql_name='turnTo')


class ThingMaintenanceOperatorRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ThingMaintenanceOperatorRecord)), graphql_name='data')


class ThingMaintenanceProcessItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('maintenance_process_item', 'maintenance_spare_part_item', 'thing')
    maintenance_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceProcessItem))), graphql_name='maintenanceProcessItem')
    maintenance_spare_part_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceSparePartItem))), graphql_name='maintenanceSparePartItem')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')


class ThingMaintenanceStatusOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('finished_count', 'maintaining_count', 'paused_count', 'pending_count', 'total_count', 'under_review_count')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    maintaining_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maintainingCount')
    paused_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pausedCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    under_review_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='underReviewCount')


class ThingMaintenanceWorkflowConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceTrigger), graphql_name='trigger')


class ThingMaintenanceWorkflowConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingMaintenanceWorkflowConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingMechanismModel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id', 'name')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ThingMechanismModelList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingMechanismModel))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingOnStateOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('abandoned_count', 'available_count', 'debugging_count', 'in_use_count', 'other_count', 'total_count')
    abandoned_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='AbandonedCount')
    available_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='AvailableCount')
    debugging_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='DebuggingCount')
    in_use_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='InUseCount')
    other_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='OtherCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingOrganizationWithChildren(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('children', 'id', 'name')
    children = sgqlc.types.Field(JSON, graphql_name='children')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='name')


class ThingRankDetail(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing', 'value')
    thing = sgqlc.types.Field(Thing, graphql_name='thing')
    value = sgqlc.types.Field(Float, graphql_name='value')


class ThingRepair(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'create_by', 'created_at', 'estimated_time', 'found_at', 'id', 'operator', 'related_operator', 'status', 'thing', 'thing_repair_process_item', 'updated_at')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    create_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='createBy')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    found_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='foundAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    related_operator = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='relatedOperator')
    status = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='status')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Thing))), graphql_name='thing')
    thing_repair_process_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThingRepairProcessItem'))), graphql_name='thingRepairProcessItem')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class ThingRepairList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingRepair))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingRepairOperatorRecord(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('apply_depository_name', 'apply_factory_name', 'apply_remark', 'apply_spare_part_names', 'cost_time', 'created_at', 'id', 'lack_depository_name', 'lack_factory_name', 'lack_spare_part_names', 'operator', 'operator_record_type', 'pause_reason', 'remark', 'restart_operator', 'turn_to')
    apply_depository_name = sgqlc.types.Field(String, graphql_name='applyDepositoryName')
    apply_factory_name = sgqlc.types.Field(String, graphql_name='applyFactoryName')
    apply_remark = sgqlc.types.Field(String, graphql_name='applyRemark')
    apply_spare_part_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='applySparePartNames')
    cost_time = sgqlc.types.Field(Int, graphql_name='costTime')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    lack_depository_name = sgqlc.types.Field(String, graphql_name='lackDepositoryName')
    lack_factory_name = sgqlc.types.Field(String, graphql_name='lackFactoryName')
    lack_spare_part_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='lackSparePartNames')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    operator_record_type = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairOperatorType), graphql_name='operatorRecordType')
    pause_reason = sgqlc.types.Field(String, graphql_name='pauseReason')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    restart_operator = sgqlc.types.Field('User', graphql_name='restartOperator')
    turn_to = sgqlc.types.Field('User', graphql_name='turnTo')


class ThingRepairOperatorRecordList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ThingRepairOperatorRecord)), graphql_name='data')


class ThingRepairProcessItem(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('after_repair_image', 'before_repair_image', 'id', 'remark', 'repair_content', 'repair_spare_part_item', 'repair_type', 'thing')
    after_repair_image = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='afterRepairImage')
    before_repair_image = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(File))), graphql_name='beforeRepairImage')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    remark = sgqlc.types.Field(String, graphql_name='remark')
    repair_content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repairContent')
    repair_spare_part_item = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(RepairSparePartItem))), graphql_name='repairSparePartItem')
    repair_type = sgqlc.types.Field(ThingRepairType, graphql_name='repairType')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')


class ThingRepairStatusOverview(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('finished_count', 'paused_count', 'pending_count', 'repairing_count', 'total_count', 'under_review_count')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    paused_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pausedCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')
    repairing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='repairingCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    under_review_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='underReviewCount')


class ThingRepairWorkflowConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('destination', 'id', 'source', 'trigger')
    destination = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='destination')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    source = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='source')
    trigger = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairTrigger), graphql_name='trigger')


class ThingRepairWorkflowConfigurationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingRepairWorkflowConfiguration))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingReport(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('energy_consumption', 'energy_group', 'operation_time', 'thing')
    energy_consumption = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='energyConsumption')
    energy_group = sgqlc.types.Field(sgqlc.types.non_null(EnergyGroup), graphql_name='energyGroup')
    operation_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='operationTime')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')


class ThingReportList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingReport)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingSchedule(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('end_at', 'estimated_time', 'id', 'inspection_method', 'maintenance_method', 'name', 'operator', 'repeat', 'start_at', 'thing', 'ticket_type')
    end_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='endAt')
    estimated_time = sgqlc.types.Field(String, graphql_name='estimatedTime')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    inspection_method = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InspectionMethod))), graphql_name='inspectionMethod')
    maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceMethod))), graphql_name='maintenanceMethod')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    repeat = sgqlc.types.Field(sgqlc.types.non_null(Repeat), graphql_name='repeat')
    start_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='startAt')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Thing))), graphql_name='thing')
    ticket_type = sgqlc.types.Field(sgqlc.types.non_null(TicketType), graphql_name='ticketType')


class ThingScheduleList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingSchedule))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingSpecificationLanguage(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('created_at', 'description', 'id', 'is_public', 'name')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    is_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublic')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ThingSpecificationLanguageList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingSpecificationLanguage))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingSpecificationLanguageProperty(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data_type', 'description', 'enum_data', 'false_value', 'id', 'identifier', 'name', 'precision', 'true_value', 'unit')
    data_type = sgqlc.types.Field(sgqlc.types.non_null(DataType), graphql_name='dataType')
    description = sgqlc.types.Field(String, graphql_name='description')
    enum_data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(EnumData)), graphql_name='enumData')
    false_value = sgqlc.types.Field(String, graphql_name='falseValue')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identifier')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    precision = sgqlc.types.Field(Int, graphql_name='precision')
    true_value = sgqlc.types.Field(String, graphql_name='trueValue')
    unit = sgqlc.types.Field(String, graphql_name='unit')


class ThingSpecificationLanguagePropertyList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingSpecificationLanguageProperty))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingStatus(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'label', 'thing_type', 'value')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    label = sgqlc.types.Field(String, graphql_name='label')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null('ThingType'), graphql_name='thingType')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')


class ThingStatusData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('key', 'name', 'time_key', 'time_key_name')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    time_key = sgqlc.types.Field(String, graphql_name='timeKey')
    time_key_name = sgqlc.types.Field(String, graphql_name='timeKeyName')


class ThingTask(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('execution_at', 'id', 'inspection_method', 'maintenance_method', 'operator', 'schedule', 'thing', 'thing_inspection', 'thing_maintenance')
    execution_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='executionAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    inspection_method = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(InspectionMethod))), graphql_name='inspectionMethod')
    maintenance_method = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(MaintenanceMethod))), graphql_name='maintenanceMethod')
    operator = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='operator')
    schedule = sgqlc.types.Field(sgqlc.types.non_null(ThingSchedule), graphql_name='schedule')
    thing = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Thing))), graphql_name='thing')
    thing_inspection = sgqlc.types.Field(ThingInspection, graphql_name='thingInspection')
    thing_maintenance = sgqlc.types.Field(ThingMaintenance, graphql_name='thingMaintenance')


class ThingTaskList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingTask))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingThingSpecificationLanguage(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'thing', 'thing_specification_language')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')
    thing_specification_language = sgqlc.types.Field(sgqlc.types.non_null(ThingSpecificationLanguage), graphql_name='thingSpecificationLanguage')


class ThingThingSpecificationLanguageList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingThingSpecificationLanguage))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingTopCount(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('count', 'thing')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    thing = sgqlc.types.Field(sgqlc.types.non_null(Thing), graphql_name='thing')


class ThingTotalReport(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('delta', 'energy_consumption', 'energy_type', 'thing_total', 'timestamp', 'working_thing_total')
    delta = sgqlc.types.Field(Float, graphql_name='delta')
    energy_consumption = sgqlc.types.Field(Float, graphql_name='energyConsumption')
    energy_type = sgqlc.types.Field(EnergyType, graphql_name='energyType')
    thing_total = sgqlc.types.Field(Int, graphql_name='thingTotal')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    working_thing_total = sgqlc.types.Field(Int, graphql_name='workingThingTotal')


class ThingTotalReportList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingTotalReport)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingType(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'created_at', 'desc', 'id', 'is_public', 'mechanism_model_name', 'name')
    code = sgqlc.types.Field(String, graphql_name='code')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublic')
    mechanism_model_name = sgqlc.types.Field(String, graphql_name='mechanismModelName')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class ThingTypeCode(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('code', 'id')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ThingTypeCodeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingTypeCode))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingTypeCount(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('count', 'thing_type')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    thing_type = sgqlc.types.Field(sgqlc.types.non_null(ThingType), graphql_name='thingType')


class ThingTypeList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingType))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ThingsEnergyConsumptionOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('alert', 'bottleneck', 'energy_total', 'name', 'num', 'operation_rate', 'operation_total', 'peak_rate', 'power_on_rate', 'power_on_total', 'redundant')
    alert = sgqlc.types.Field(Int, graphql_name='alert')
    bottleneck = sgqlc.types.Field(Int, graphql_name='bottleneck')
    energy_total = sgqlc.types.Field(Float, graphql_name='energyTotal')
    name = sgqlc.types.Field(String, graphql_name='name')
    num = sgqlc.types.Field(Int, graphql_name='num')
    operation_rate = sgqlc.types.Field(Float, graphql_name='operationRate')
    operation_total = sgqlc.types.Field(Float, graphql_name='operationTotal')
    peak_rate = sgqlc.types.Field(Float, graphql_name='peakRate')
    power_on_rate = sgqlc.types.Field(Float, graphql_name='powerOnRate')
    power_on_total = sgqlc.types.Field(Float, graphql_name='powerOnTotal')
    redundant = sgqlc.types.Field(Int, graphql_name='redundant')


class ThingsOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('status', 'total')
    status = sgqlc.types.Field(JSONString, graphql_name='status')
    total = sgqlc.types.Field(Int, graphql_name='total')


class ThingsRank(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingRankDetail)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TimeDistribution(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'price')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TimeDistributionData'))), graphql_name='data')
    price = sgqlc.types.Field(Float, graphql_name='price')


class TimeDistributionData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('end', 'start')
    end = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='end')
    start = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='start')


class TimeseriesUnit(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('timestamp', 'value')
    timestamp = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='timestamp')
    value = sgqlc.types.Field(Float, graphql_name='value')


class TotalDataMeterReadingData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('vapor_consumption', 'water_consumption')
    vapor_consumption = sgqlc.types.Field(Float, graphql_name='vaporConsumption')
    water_consumption = sgqlc.types.Field(Float, graphql_name='waterConsumption')


class TotalFee(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('energy_consumption', 'value')
    energy_consumption = sgqlc.types.Field(Float, graphql_name='energyConsumption')
    value = sgqlc.types.Field(Float, graphql_name='value')


class TypeCompanies(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('companies', 'type')
    companies = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Company)), graphql_name='companies')
    type = sgqlc.types.Field(sgqlc.types.non_null(CompanyType), graphql_name='type')


class TypeCompaniesList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TypeCompanies)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UCCField(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('meta', 'name', 'required', 'role', 'width')
    meta = sgqlc.types.Field('UCCMeta', graphql_name='meta')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    role = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='role')
    width = sgqlc.types.Field(Int, graphql_name='width')


class UCCFormStructure(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'key', 'zone')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    zone = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(UCCField)), graphql_name='zone')


class UCCMetaDate(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_bool', 'field_type', 'format', 'hint', 'id')
    default_bool = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='defaultBool')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    format = sgqlc.types.Field(String, graphql_name='format')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class UCCMetaLabel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('content', 'field_type', 'id')
    content = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='content')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class UCCMetaMultiRadio(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_str_list', 'field_type', 'id', 'option')
    default_str_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultStrList')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='option')


class UCCMetaRadio(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_str', 'field_type', 'id', 'option')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='option')


class UCCMetaRange(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('field_type', 'id', 'max_range', 'min_range', 'round')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    max_range = sgqlc.types.Field(sgqlc.types.non_null('UCCMetaRangeExtremum'), graphql_name='maxRange')
    min_range = sgqlc.types.Field(sgqlc.types.non_null('UCCMetaRangeExtremum'), graphql_name='minRange')
    round = sgqlc.types.Field(Int, graphql_name='round')


class UCCMetaRangeExtremum(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default', 'field_type', 'hint', 'id', 'max', 'min', 'required', 'unit', 'zeroable')
    default = sgqlc.types.Field(Float, graphql_name='default')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    max = sgqlc.types.Field(Float, graphql_name='max')
    min = sgqlc.types.Field(Float, graphql_name='min')
    required = sgqlc.types.Field(Boolean, graphql_name='required')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class UCCMetaSelectBox(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_str', 'default_str_list', 'field_type', 'hint', 'id', 'multi', 'option')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    default_str_list = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='defaultStrList')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    multi = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='multi')
    option = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='option')


class UCCMetaSet(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('field_type', 'meta')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    meta = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UCCMeta')), graphql_name='meta')


class UCCMetaText(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('default_num', 'default_str', 'field_type', 'hint', 'id', 'label', 'max', 'min', 'round', 'type', 'unit', 'zeroable')
    default_num = sgqlc.types.Field(Float, graphql_name='defaultNum')
    default_str = sgqlc.types.Field(String, graphql_name='defaultStr')
    field_type = sgqlc.types.Field(sgqlc.types.non_null(UCCFieldType), graphql_name='fieldType')
    hint = sgqlc.types.Field(String, graphql_name='hint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    label = sgqlc.types.Field(String, graphql_name='label')
    max = sgqlc.types.Field(Float, graphql_name='max')
    min = sgqlc.types.Field(Float, graphql_name='min')
    round = sgqlc.types.Field(Int, graphql_name='round')
    type = sgqlc.types.Field(sgqlc.types.non_null(UCCFiledValue), graphql_name='type')
    unit = sgqlc.types.Field(String, graphql_name='unit')
    zeroable = sgqlc.types.Field(Boolean, graphql_name='zeroable')


class UploadConfig(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('name', 'url')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')


class User(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('account', 'avatar', 'company', 'counties', 'create_time', 'department', 'desc', 'email', 'id', 'is_active', 'is_mine', 'name', 'nickname', 'origin', 'password', 'phone', 'role', 'thing_group', 'type', 'update_time')
    account = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='account')
    avatar = sgqlc.types.Field(Image, graphql_name='avatar')
    company = sgqlc.types.Field(Company, graphql_name='company')
    counties = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='counties')
    create_time = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createTime')
    department = sgqlc.types.Field(Department, graphql_name='department')
    desc = sgqlc.types.Field(String, graphql_name='desc')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    is_mine = sgqlc.types.Field(Boolean, graphql_name='isMine')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    origin = sgqlc.types.Field(UserOrigin, graphql_name='origin')
    password = sgqlc.types.Field(String, graphql_name='password')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    role = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Role))), graphql_name='role')
    thing_group = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroup))), graphql_name='thingGroup')
    type = sgqlc.types.Field(sgqlc.types.non_null(UserType), graphql_name='type')
    update_time = sgqlc.types.Field(Timestamp, graphql_name='updateTime')


class UserList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(User)), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserThingGroupList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('UserThingGroups')), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserThingGroups(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('thing_groups', 'user')
    thing_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroup)), graphql_name='thingGroups')
    user = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='user')


class VaporConsumptionData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')


class VaporMeterReadingData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'consumption_deviation', 'reading')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    consumption_deviation = sgqlc.types.Field(Float, graphql_name='consumptionDeviation')
    reading = sgqlc.types.Field(Float, graphql_name='reading')


class WaterConsumptionData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'fee')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    fee = sgqlc.types.Field(Float, graphql_name='fee')


class WaterMeterReadingData(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('consumption', 'consumption_deviation', 'reading')
    consumption = sgqlc.types.Field(Float, graphql_name='consumption')
    consumption_deviation = sgqlc.types.Field(Float, graphql_name='consumptionDeviation')
    reading = sgqlc.types.Field(Float, graphql_name='reading')


class WorkbenchCard(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class WorkerOrder(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('accept_user', 'alert', 'business_knowledges', 'code', 'created_at', 'id', 'status', 'updated_at')
    accept_user = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='acceptUser')
    alert = sgqlc.types.Field(sgqlc.types.non_null(AlertDetail), graphql_name='alert')
    business_knowledges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(BusinessKnowledge))), graphql_name='businessKnowledges')
    code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='code')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    status = sgqlc.types.Field(sgqlc.types.non_null(WorkerOrderStatus), graphql_name='status')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='updatedAt')


class WorkerOrderList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WorkerOrder))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkerOrderOperator(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('business_knowledges', 'created_at', 'error_types', 'id', 'message', 'operation_user', 'turn_to_user', 'worker_order_operation_type')
    business_knowledges = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(BusinessKnowledge)), graphql_name='businessKnowledges')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(Timestamp), graphql_name='createdAt')
    error_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ErrorType)), graphql_name='errorTypes')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    message = sgqlc.types.Field(String, graphql_name='message')
    operation_user = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='operationUser')
    turn_to_user = sgqlc.types.Field(User, graphql_name='turnToUser')
    worker_order_operation_type = sgqlc.types.Field(sgqlc.types.non_null(WorkerOrderOperatorType), graphql_name='workerOrderOperationType')


class WorkerOrderOperatorList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('total_count', 'worker_order_operators')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    worker_order_operators = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WorkerOrderOperator))), graphql_name='workerOrderOperators')


class WorkerOrderStatusSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('accepting_count', 'finished_count', 'total_count')
    accepting_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='acceptingCount')
    finished_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='finishedCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkerOrderThingTypeSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingTypeCount))), graphql_name='data')


class WorkerOrderTopPersonnel(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('count', 'personnel')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    personnel = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='personnel')


class WorkerOrderTopPersonnelSummary(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data',)
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(WorkerOrderTopPersonnel))), graphql_name='data')


class WorkflowBaseConfiguration(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('change_borrow_init_state', 'change_borrow_use_default_workflow', 'thing_borrow_init_state', 'thing_borrow_use_default_workflow', 'thing_calibrate_init_state', 'thing_calibrate_use_default_workflow', 'thing_inspection_init_state', 'thing_inspection_use_default_workflow', 'thing_maintenance_init_state', 'thing_maintenance_use_default_workflow', 'thing_repair_init_state', 'thing_repair_use_default_workflow')
    change_borrow_init_state = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='changeBorrowInitState')
    change_borrow_use_default_workflow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='changeBorrowUseDefaultWorkflow')
    thing_borrow_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='thingBorrowInitState')
    thing_borrow_use_default_workflow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='thingBorrowUseDefaultWorkflow')
    thing_calibrate_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateState), graphql_name='thingCalibrateInitState')
    thing_calibrate_use_default_workflow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='thingCalibrateUseDefaultWorkflow')
    thing_inspection_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='thingInspectionInitState')
    thing_inspection_use_default_workflow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='thingInspectionUseDefaultWorkflow')
    thing_maintenance_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='thingMaintenanceInitState')
    thing_maintenance_use_default_workflow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='thingMaintenanceUseDefaultWorkflow')
    thing_repair_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='thingRepairInitState')
    thing_repair_use_default_workflow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='thingRepairUseDefaultWorkflow')


class WorkflowDefaultInitState(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('change_borrow_default_init_state', 'thing_borrow_default_init_state', 'thing_calibrate_init_default_state', 'thing_inspection_default_init_state', 'thing_maintenance_default_init_state', 'thing_repair_init_default_state')
    change_borrow_default_init_state = sgqlc.types.Field(sgqlc.types.non_null(ChangeBorrowState), graphql_name='changeBorrowDefaultInitState')
    thing_borrow_default_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingBorrowState), graphql_name='thingBorrowDefaultInitState')
    thing_calibrate_init_default_state = sgqlc.types.Field(sgqlc.types.non_null(ThingCalibrateState), graphql_name='thingCalibrateInitDefaultState')
    thing_inspection_default_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingInspectionStatus), graphql_name='thingInspectionDefaultInitState')
    thing_maintenance_default_init_state = sgqlc.types.Field(sgqlc.types.non_null(ThingMaintenanceStatus), graphql_name='thingMaintenanceDefaultInitState')
    thing_repair_init_default_state = sgqlc.types.Field(sgqlc.types.non_null(ThingRepairStatus), graphql_name='thingRepairInitDefaultState')


class combaDeliverCount(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('count', 'production_code')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    production_code = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='productionCode')


class combaPPMTotal(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('line', 'num')
    line = sgqlc.types.Field(sgqlc.types.non_null(CombaLine), graphql_name='line')
    num = sgqlc.types.Field(Int, graphql_name='num')


class combaStockingOverall(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('num', 'production')
    num = sgqlc.types.Field(Int, graphql_name='num')
    production = sgqlc.types.Field(CombaProductionCategory, graphql_name='production')


class combaStockingOverallList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('production_total', 'total')
    production_total = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(combaStockingOverall)), graphql_name='productionTotal')
    total = sgqlc.types.Field(Int, graphql_name='total')


class thingOrganizationList(sgqlc.types.Type):
    __schema__ = platform_schema
    __field_names__ = ('data', 'total_count')
    data = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ThingGroup))), graphql_name='data')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')



########################################################################
# Unions
########################################################################
class UCCMeta(sgqlc.types.Union):
    __schema__ = platform_schema
    __types__ = (UCCMetaDate, UCCMetaLabel, UCCMetaMultiRadio, UCCMetaRadio, UCCMetaRange, UCCMetaSelectBox, UCCMetaSet, UCCMetaText)



########################################################################
# Schema Entry Points
########################################################################
platform_schema.query_type = Query
platform_schema.mutation_type = Mutation
platform_schema.subscription_type = None

