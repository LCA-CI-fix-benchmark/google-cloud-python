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
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
)

from google.cloud.deploy_v1.types import cloud_deploy


class ListDeliveryPipelinesPager:
    """A pager for iterating through ``list_delivery_pipelines`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``delivery_pipelines`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDeliveryPipelines`` requests and continue to iterate
    through the ``delivery_pipelines`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListDeliveryPipelinesResponse],
        request: cloud_deploy.ListDeliveryPipelinesRequest,
        response: cloud_deploy.ListDeliveryPipelinesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListDeliveryPipelinesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListDeliveryPipelinesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListDeliveryPipelinesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[cloud_deploy.DeliveryPipeline]:
        for page in self.pages:
            yield from page.delivery_pipelines

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDeliveryPipelinesAsyncPager:
    """A pager for iterating through ``list_delivery_pipelines`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``delivery_pipelines`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDeliveryPipelines`` requests and continue to iterate
    through the ``delivery_pipelines`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListDeliveryPipelinesResponse]],
        request: cloud_deploy.ListDeliveryPipelinesRequest,
        response: cloud_deploy.ListDeliveryPipelinesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListDeliveryPipelinesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListDeliveryPipelinesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListDeliveryPipelinesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[cloud_deploy.DeliveryPipeline]:
        async def async_generator():
            async for page in self.pages:
                for response in page.delivery_pipelines:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTargetsPager:
    """A pager for iterating through ``list_targets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListTargetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``targets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListTargets`` requests and continue to iterate
    through the ``targets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListTargetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListTargetsResponse],
        request: cloud_deploy.ListTargetsRequest,
        response: cloud_deploy.ListTargetsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListTargetsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListTargetsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListTargetsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListTargetsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[cloud_deploy.Target]:
        for page in self.pages:
            yield from page.targets

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListTargetsAsyncPager:
    """A pager for iterating through ``list_targets`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListTargetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``targets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListTargets`` requests and continue to iterate
    through the ``targets`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListTargetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListTargetsResponse]],
        request: cloud_deploy.ListTargetsRequest,
        response: cloud_deploy.ListTargetsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListTargetsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListTargetsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListTargetsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListTargetsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[cloud_deploy.Target]:
        async def async_generator():
            async for page in self.pages:
                for response in page.targets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCustomTargetTypesPager:
    """A pager for iterating through ``list_custom_target_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListCustomTargetTypesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``custom_target_types`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCustomTargetTypes`` requests and continue to iterate
    through the ``custom_target_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListCustomTargetTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListCustomTargetTypesResponse],
        request: cloud_deploy.ListCustomTargetTypesRequest,
        response: cloud_deploy.ListCustomTargetTypesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListCustomTargetTypesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListCustomTargetTypesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListCustomTargetTypesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListCustomTargetTypesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[cloud_deploy.CustomTargetType]:
        for page in self.pages:
            yield from page.custom_target_types

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCustomTargetTypesAsyncPager:
    """A pager for iterating through ``list_custom_target_types`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListCustomTargetTypesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``custom_target_types`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCustomTargetTypes`` requests and continue to iterate
    through the ``custom_target_types`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListCustomTargetTypesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListCustomTargetTypesResponse]],
        request: cloud_deploy.ListCustomTargetTypesRequest,
        response: cloud_deploy.ListCustomTargetTypesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListCustomTargetTypesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListCustomTargetTypesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListCustomTargetTypesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListCustomTargetTypesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[cloud_deploy.CustomTargetType]:
        async def async_generator():
            async for page in self.pages:
                for response in page.custom_target_types:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReleasesPager:
    """A pager for iterating through ``list_releases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListReleasesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``releases`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListReleases`` requests and continue to iterate
    through the ``releases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListReleasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListReleasesResponse],
        request: cloud_deploy.ListReleasesRequest,
        response: cloud_deploy.ListReleasesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListReleasesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListReleasesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListReleasesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListReleasesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[cloud_deploy.Release]:
        for page in self.pages:
            yield from page.releases

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListReleasesAsyncPager:
    """A pager for iterating through ``list_releases`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListReleasesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``releases`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListReleases`` requests and continue to iterate
    through the ``releases`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListReleasesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListReleasesResponse]],
        request: cloud_deploy.ListReleasesRequest,
        response: cloud_deploy.ListReleasesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListReleasesRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListReleasesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListReleasesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListReleasesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[cloud_deploy.Release]:
        async def async_generator():
            async for page in self.pages:
                for response in page.releases:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRolloutsPager:
    """A pager for iterating through ``list_rollouts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListRolloutsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``rollouts`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListRollouts`` requests and continue to iterate
    through the ``rollouts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListRolloutsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListRolloutsResponse],
        request: cloud_deploy.ListRolloutsRequest,
        response: cloud_deploy.ListRolloutsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListRolloutsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListRolloutsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListRolloutsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListRolloutsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[cloud_deploy.Rollout]:
        for page in self.pages:
            yield from page.rollouts

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListRolloutsAsyncPager:
    """A pager for iterating through ``list_rollouts`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListRolloutsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``rollouts`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListRollouts`` requests and continue to iterate
    through the ``rollouts`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListRolloutsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListRolloutsResponse]],
        request: cloud_deploy.ListRolloutsRequest,
        response: cloud_deploy.ListRolloutsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListRolloutsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListRolloutsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListRolloutsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListRolloutsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[cloud_deploy.Rollout]:
        async def async_generator():
            async for page in self.pages:
                for response in page.rollouts:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListJobRunsPager:
    """A pager for iterating through ``list_job_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListJobRunsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``job_runs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListJobRuns`` requests and continue to iterate
    through the ``job_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListJobRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListJobRunsResponse],
        request: cloud_deploy.ListJobRunsRequest,
        response: cloud_deploy.ListJobRunsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListJobRunsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListJobRunsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListJobRunsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListJobRunsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[cloud_deploy.JobRun]:
        for page in self.pages:
            yield from page.job_runs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListJobRunsAsyncPager:
    """A pager for iterating through ``list_job_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListJobRunsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``job_runs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListJobRuns`` requests and continue to iterate
    through the ``job_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListJobRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListJobRunsResponse]],
        request: cloud_deploy.ListJobRunsRequest,
        response: cloud_deploy.ListJobRunsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListJobRunsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListJobRunsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListJobRunsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListJobRunsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[cloud_deploy.JobRun]:
        async def async_generator():
            async for page in self.pages:
                for response in page.job_runs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutomationsPager:
    """A pager for iterating through ``list_automations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListAutomationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``automations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAutomations`` requests and continue to iterate
    through the ``automations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListAutomationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListAutomationsResponse],
        request: cloud_deploy.ListAutomationsRequest,
        response: cloud_deploy.ListAutomationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListAutomationsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListAutomationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListAutomationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListAutomationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[cloud_deploy.Automation]:
        for page in self.pages:
            yield from page.automations

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutomationsAsyncPager:
    """A pager for iterating through ``list_automations`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListAutomationsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``automations`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAutomations`` requests and continue to iterate
    through the ``automations`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListAutomationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListAutomationsResponse]],
        request: cloud_deploy.ListAutomationsRequest,
        response: cloud_deploy.ListAutomationsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListAutomationsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListAutomationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListAutomationsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListAutomationsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[cloud_deploy.Automation]:
        async def async_generator():
            async for page in self.pages:
                for response in page.automations:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutomationRunsPager:
    """A pager for iterating through ``list_automation_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListAutomationRunsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``automation_runs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListAutomationRuns`` requests and continue to iterate
    through the ``automation_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListAutomationRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., cloud_deploy.ListAutomationRunsResponse],
        request: cloud_deploy.ListAutomationRunsRequest,
        response: cloud_deploy.ListAutomationRunsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListAutomationRunsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListAutomationRunsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListAutomationRunsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[cloud_deploy.ListAutomationRunsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[cloud_deploy.AutomationRun]:
        for page in self.pages:
            yield from page.automation_runs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListAutomationRunsAsyncPager:
    """A pager for iterating through ``list_automation_runs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.deploy_v1.types.ListAutomationRunsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``automation_runs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListAutomationRuns`` requests and continue to iterate
    through the ``automation_runs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.deploy_v1.types.ListAutomationRunsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[cloud_deploy.ListAutomationRunsResponse]],
        request: cloud_deploy.ListAutomationRunsRequest,
        response: cloud_deploy.ListAutomationRunsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.deploy_v1.types.ListAutomationRunsRequest):
                The initial request object.
            response (google.cloud.deploy_v1.types.ListAutomationRunsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = cloud_deploy.ListAutomationRunsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[cloud_deploy.ListAutomationRunsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[cloud_deploy.AutomationRun]:
        async def async_generator():
            async for page in self.pages:
                for response in page.automation_runs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
