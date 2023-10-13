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
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator

from google.cloud.edgecontainer_v1.types import resources
from google.cloud.edgecontainer_v1.types import service


class ListClustersPager:
    """A pager for iterating through ``list_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgecontainer_v1.types.ListClustersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``clusters`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListClusters`` requests and continue to iterate
    through the ``clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgecontainer_v1.types.ListClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., service.ListClustersResponse],
            request: service.ListClustersRequest,
            response: service.ListClustersResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgecontainer_v1.types.ListClustersRequest):
                The initial request object.
            response (google.cloud.edgecontainer_v1.types.ListClustersResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListClustersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListClustersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[resources.Cluster]:
        for page in self.pages:
            yield from page.clusters

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListClustersAsyncPager:
    """A pager for iterating through ``list_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgecontainer_v1.types.ListClustersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``clusters`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListClusters`` requests and continue to iterate
    through the ``clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgecontainer_v1.types.ListClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[service.ListClustersResponse]],
            request: service.ListClustersRequest,
            response: service.ListClustersResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgecontainer_v1.types.ListClustersRequest):
                The initial request object.
            response (google.cloud.edgecontainer_v1.types.ListClustersResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListClustersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListClustersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[resources.Cluster]:
        async def async_generator():
            async for page in self.pages:
                for response in page.clusters:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListNodePoolsPager:
    """A pager for iterating through ``list_node_pools`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgecontainer_v1.types.ListNodePoolsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``node_pools`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListNodePools`` requests and continue to iterate
    through the ``node_pools`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgecontainer_v1.types.ListNodePoolsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., service.ListNodePoolsResponse],
            request: service.ListNodePoolsRequest,
            response: service.ListNodePoolsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgecontainer_v1.types.ListNodePoolsRequest):
                The initial request object.
            response (google.cloud.edgecontainer_v1.types.ListNodePoolsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListNodePoolsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListNodePoolsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[resources.NodePool]:
        for page in self.pages:
            yield from page.node_pools

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListNodePoolsAsyncPager:
    """A pager for iterating through ``list_node_pools`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgecontainer_v1.types.ListNodePoolsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``node_pools`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListNodePools`` requests and continue to iterate
    through the ``node_pools`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgecontainer_v1.types.ListNodePoolsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[service.ListNodePoolsResponse]],
            request: service.ListNodePoolsRequest,
            response: service.ListNodePoolsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgecontainer_v1.types.ListNodePoolsRequest):
                The initial request object.
            response (google.cloud.edgecontainer_v1.types.ListNodePoolsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListNodePoolsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListNodePoolsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[resources.NodePool]:
        async def async_generator():
            async for page in self.pages:
                for response in page.node_pools:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListMachinesPager:
    """A pager for iterating through ``list_machines`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgecontainer_v1.types.ListMachinesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``machines`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListMachines`` requests and continue to iterate
    through the ``machines`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgecontainer_v1.types.ListMachinesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., service.ListMachinesResponse],
            request: service.ListMachinesRequest,
            response: service.ListMachinesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgecontainer_v1.types.ListMachinesRequest):
                The initial request object.
            response (google.cloud.edgecontainer_v1.types.ListMachinesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListMachinesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListMachinesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[resources.Machine]:
        for page in self.pages:
            yield from page.machines

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListMachinesAsyncPager:
    """A pager for iterating through ``list_machines`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgecontainer_v1.types.ListMachinesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``machines`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListMachines`` requests and continue to iterate
    through the ``machines`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgecontainer_v1.types.ListMachinesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[service.ListMachinesResponse]],
            request: service.ListMachinesRequest,
            response: service.ListMachinesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgecontainer_v1.types.ListMachinesRequest):
                The initial request object.
            response (google.cloud.edgecontainer_v1.types.ListMachinesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListMachinesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListMachinesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[resources.Machine]:
        async def async_generator():
            async for page in self.pages:
                for response in page.machines:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListVpnConnectionsPager:
    """A pager for iterating through ``list_vpn_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgecontainer_v1.types.ListVpnConnectionsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``vpn_connections`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVpnConnections`` requests and continue to iterate
    through the ``vpn_connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgecontainer_v1.types.ListVpnConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., service.ListVpnConnectionsResponse],
            request: service.ListVpnConnectionsRequest,
            response: service.ListVpnConnectionsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgecontainer_v1.types.ListVpnConnectionsRequest):
                The initial request object.
            response (google.cloud.edgecontainer_v1.types.ListVpnConnectionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListVpnConnectionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[service.ListVpnConnectionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[resources.VpnConnection]:
        for page in self.pages:
            yield from page.vpn_connections

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListVpnConnectionsAsyncPager:
    """A pager for iterating through ``list_vpn_connections`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.edgecontainer_v1.types.ListVpnConnectionsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``vpn_connections`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVpnConnections`` requests and continue to iterate
    through the ``vpn_connections`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.edgecontainer_v1.types.ListVpnConnectionsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[service.ListVpnConnectionsResponse]],
            request: service.ListVpnConnectionsRequest,
            response: service.ListVpnConnectionsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.edgecontainer_v1.types.ListVpnConnectionsRequest):
                The initial request object.
            response (google.cloud.edgecontainer_v1.types.ListVpnConnectionsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = service.ListVpnConnectionsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[service.ListVpnConnectionsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[resources.VpnConnection]:
        async def async_generator():
            async for page in self.pages:
                for response in page.vpn_connections:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
