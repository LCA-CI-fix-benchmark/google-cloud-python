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
from google.cloud.asset_v1p2beta1 import gapic_version as package_version

__version__ = package_version.__version__


from .services.asset_service import AssetServiceAsyncClient, AssetServiceClient
from .types.asset_service import (
    BatchGetAssetsHistoryResponse,
    ContentType,
    CreateFeedRequest,
    DeleteFeedRequest,
    ExportAssetsResponse,
    Feed,
    FeedOutputConfig,
    GcsDestination,
    GetFeedRequest,
    ListFeedsRequest,
    ListFeedsResponse,
    OutputConfig,
    PubsubDestination,
    UpdateFeedRequest,
)
from .types.assets import Asset, Resource, TemporalAsset, TimeWindow

__all__ = (
    "AssetServiceAsyncClient",
    "Asset",
    "AssetServiceClient",
    "BatchGetAssetsHistoryResponse",
    "ContentType",
    "CreateFeedRequest",
    "DeleteFeedRequest",
    "ExportAssetsResponse",
    "Feed",
    "FeedOutputConfig",
    "GcsDestination",
    "GetFeedRequest",
    "ListFeedsRequest",
    "ListFeedsResponse",
    "OutputConfig",
    "PubsubDestination",
    "Resource",
    "TemporalAsset",
    "TimeWindow",
    "UpdateFeedRequest",
)
