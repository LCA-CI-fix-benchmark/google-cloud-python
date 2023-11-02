# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.deploy_v1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.cloud_deploy import CloudDeployAsyncClient, CloudDeployClient
from .types.automation_payload import AutomationEvent
from .types.automationrun_payload import AutomationRunEvent
from .types.cloud_deploy import (
    AbandonReleaseRequest,
    AbandonReleaseResponse,
    AdvanceChildRolloutJob,
    AdvanceChildRolloutJobRun,
    AdvanceRolloutOperation,
    AdvanceRolloutRequest,
    AdvanceRolloutResponse,
    AdvanceRolloutRule,
    AnthosCluster,
    ApproveRolloutRequest,
    ApproveRolloutResponse,
    Automation,
    AutomationResourceSelector,
    AutomationRolloutMetadata,
    AutomationRule,
    AutomationRuleCondition,
    AutomationRun,
    BackoffMode,
    BuildArtifact,
    Canary,
    CanaryDeployment,
    CancelAutomationRunRequest,
    CancelAutomationRunResponse,
    CancelRolloutRequest,
    CancelRolloutResponse,
    ChildRolloutJobs,
    CloudRunConfig,
    CloudRunLocation,
    CloudRunMetadata,
    CloudRunRenderMetadata,
    Config,
    CreateAutomationRequest,
    CreateChildRolloutJob,
    CreateChildRolloutJobRun,
    CreateDeliveryPipelineRequest,
    CreateReleaseRequest,
    CreateRolloutRequest,
    CreateTargetRequest,
    CustomCanaryDeployment,
    DefaultPool,
    DeleteAutomationRequest,
    DeleteDeliveryPipelineRequest,
    DeleteTargetRequest,
    DeliveryPipeline,
    DeployArtifact,
    DeployJob,
    DeployJobRun,
    DeployJobRunMetadata,
    DeploymentJobs,
    DeployParameters,
    ExecutionConfig,
    GetAutomationRequest,
    GetAutomationRunRequest,
    GetConfigRequest,
    GetDeliveryPipelineRequest,
    GetJobRunRequest,
    GetReleaseRequest,
    GetRolloutRequest,
    GetTargetRequest,
    GkeCluster,
    IgnoreJobRequest,
    IgnoreJobResponse,
    Job,
    JobRun,
    KubernetesConfig,
    ListAutomationRunsRequest,
    ListAutomationRunsResponse,
    ListAutomationsRequest,
    ListAutomationsResponse,
    ListDeliveryPipelinesRequest,
    ListDeliveryPipelinesResponse,
    ListJobRunsRequest,
    ListJobRunsResponse,
    ListReleasesRequest,
    ListReleasesResponse,
    ListRolloutsRequest,
    ListRolloutsResponse,
    ListTargetsRequest,
    ListTargetsResponse,
    Metadata,
    MultiTarget,
    OperationMetadata,
    Phase,
    PipelineCondition,
    PipelineReadyCondition,
    Postdeploy,
    PostdeployJob,
    PostdeployJobRun,
    Predeploy,
    PredeployJob,
    PredeployJobRun,
    PrivatePool,
    PromoteReleaseOperation,
    PromoteReleaseRule,
    Release,
    RenderMetadata,
    RepairMode,
    RepairPhase,
    RepairRolloutOperation,
    RepairRolloutRule,
    RepairState,
    Retry,
    RetryAttempt,
    RetryJobRequest,
    RetryJobResponse,
    RetryPhase,
    Rollback,
    RollbackAttempt,
    RollbackTargetConfig,
    RollbackTargetRequest,
    RollbackTargetResponse,
    Rollout,
    RuntimeConfig,
    SerialPipeline,
    SkaffoldSupportState,
    SkaffoldVersion,
    Stage,
    Standard,
    Strategy,
    Target,
    TargetArtifact,
    TargetAttribute,
    TargetsPresentCondition,
    TargetsTypeCondition,
    TerminateJobRunRequest,
    TerminateJobRunResponse,
    UpdateAutomationRequest,
    UpdateDeliveryPipelineRequest,
    UpdateTargetRequest,
    VerifyJob,
    VerifyJobRun,
)
from .types.deliverypipeline_notification_payload import (
    DeliveryPipelineNotificationEvent,
)
from .types.jobrun_notification_payload import JobRunNotificationEvent
from .types.log_enums import Type
from .types.release_notification_payload import ReleaseNotificationEvent
from .types.release_render_payload import ReleaseRenderEvent
from .types.rollout_notification_payload import RolloutNotificationEvent
from .types.rollout_update_payload import RolloutUpdateEvent
from .types.target_notification_payload import TargetNotificationEvent

__all__ = (
    "CloudDeployAsyncClient",
    "AbandonReleaseRequest",
    "AbandonReleaseResponse",
    "AdvanceChildRolloutJob",
    "AdvanceChildRolloutJobRun",
    "AdvanceRolloutOperation",
    "AdvanceRolloutRequest",
    "AdvanceRolloutResponse",
    "AdvanceRolloutRule",
    "AnthosCluster",
    "ApproveRolloutRequest",
    "ApproveRolloutResponse",
    "Automation",
    "AutomationEvent",
    "AutomationResourceSelector",
    "AutomationRolloutMetadata",
    "AutomationRule",
    "AutomationRuleCondition",
    "AutomationRun",
    "AutomationRunEvent",
    "BackoffMode",
    "BuildArtifact",
    "Canary",
    "CanaryDeployment",
    "CancelAutomationRunRequest",
    "CancelAutomationRunResponse",
    "CancelRolloutRequest",
    "CancelRolloutResponse",
    "ChildRolloutJobs",
    "CloudDeployClient",
    "CloudRunConfig",
    "CloudRunLocation",
    "CloudRunMetadata",
    "CloudRunRenderMetadata",
    "Config",
    "CreateAutomationRequest",
    "CreateChildRolloutJob",
    "CreateChildRolloutJobRun",
    "CreateDeliveryPipelineRequest",
    "CreateReleaseRequest",
    "CreateRolloutRequest",
    "CreateTargetRequest",
    "CustomCanaryDeployment",
    "DefaultPool",
    "DeleteAutomationRequest",
    "DeleteDeliveryPipelineRequest",
    "DeleteTargetRequest",
    "DeliveryPipeline",
    "DeliveryPipelineNotificationEvent",
    "DeployArtifact",
    "DeployJob",
    "DeployJobRun",
    "DeployJobRunMetadata",
    "DeployParameters",
    "DeploymentJobs",
    "ExecutionConfig",
    "GetAutomationRequest",
    "GetAutomationRunRequest",
    "GetConfigRequest",
    "GetDeliveryPipelineRequest",
    "GetJobRunRequest",
    "GetReleaseRequest",
    "GetRolloutRequest",
    "GetTargetRequest",
    "GkeCluster",
    "IgnoreJobRequest",
    "IgnoreJobResponse",
    "Job",
    "JobRun",
    "JobRunNotificationEvent",
    "KubernetesConfig",
    "ListAutomationRunsRequest",
    "ListAutomationRunsResponse",
    "ListAutomationsRequest",
    "ListAutomationsResponse",
    "ListDeliveryPipelinesRequest",
    "ListDeliveryPipelinesResponse",
    "ListJobRunsRequest",
    "ListJobRunsResponse",
    "ListReleasesRequest",
    "ListReleasesResponse",
    "ListRolloutsRequest",
    "ListRolloutsResponse",
    "ListTargetsRequest",
    "ListTargetsResponse",
    "Metadata",
    "MultiTarget",
    "OperationMetadata",
    "Phase",
    "PipelineCondition",
    "PipelineReadyCondition",
    "Postdeploy",
    "PostdeployJob",
    "PostdeployJobRun",
    "Predeploy",
    "PredeployJob",
    "PredeployJobRun",
    "PrivatePool",
    "PromoteReleaseOperation",
    "PromoteReleaseRule",
    "Release",
    "ReleaseNotificationEvent",
    "ReleaseRenderEvent",
    "RenderMetadata",
    "RepairMode",
    "RepairPhase",
    "RepairRolloutOperation",
    "RepairRolloutRule",
    "RepairState",
    "Retry",
    "RetryAttempt",
    "RetryJobRequest",
    "RetryJobResponse",
    "RetryPhase",
    "Rollback",
    "RollbackAttempt",
    "RollbackTargetConfig",
    "RollbackTargetRequest",
    "RollbackTargetResponse",
    "Rollout",
    "RolloutNotificationEvent",
    "RolloutUpdateEvent",
    "RuntimeConfig",
    "SerialPipeline",
    "SkaffoldSupportState",
    "SkaffoldVersion",
    "Stage",
    "Standard",
    "Strategy",
    "Target",
    "TargetArtifact",
    "TargetAttribute",
    "TargetNotificationEvent",
    "TargetsPresentCondition",
    "TargetsTypeCondition",
    "TerminateJobRunRequest",
    "TerminateJobRunResponse",
    "Type",
    "UpdateAutomationRequest",
    "UpdateDeliveryPipelineRequest",
    "UpdateTargetRequest",
    "VerifyJob",
    "VerifyJobRun",
)
