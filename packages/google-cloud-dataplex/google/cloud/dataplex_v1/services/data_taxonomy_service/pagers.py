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

from google.cloud.dataplex_v1.types import data_taxonomy


class ListDataTaxonomiesPager:
    """A pager for iterating through ``list_data_taxonomies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListDataTaxonomiesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_taxonomies`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataTaxonomies`` requests and continue to iterate
    through the ``data_taxonomies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListDataTaxonomiesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_taxonomy.ListDataTaxonomiesResponse],
        request: data_taxonomy.ListDataTaxonomiesRequest,
        response: data_taxonomy.ListDataTaxonomiesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListDataTaxonomiesRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListDataTaxonomiesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = data_taxonomy.ListDataTaxonomiesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_taxonomy.ListDataTaxonomiesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[data_taxonomy.DataTaxonomy]:
        for page in self.pages:
            yield from page.data_taxonomies

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataTaxonomiesAsyncPager:
    """A pager for iterating through ``list_data_taxonomies`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListDataTaxonomiesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_taxonomies`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataTaxonomies`` requests and continue to iterate
    through the ``data_taxonomies`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListDataTaxonomiesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[data_taxonomy.ListDataTaxonomiesResponse]],
        request: data_taxonomy.ListDataTaxonomiesRequest,
        response: data_taxonomy.ListDataTaxonomiesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListDataTaxonomiesRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListDataTaxonomiesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = data_taxonomy.ListDataTaxonomiesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[data_taxonomy.ListDataTaxonomiesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[data_taxonomy.DataTaxonomy]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_taxonomies:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataAttributeBindingsPager:
    """A pager for iterating through ``list_data_attribute_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListDataAttributeBindingsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_attribute_bindings`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataAttributeBindings`` requests and continue to iterate
    through the ``data_attribute_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListDataAttributeBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_taxonomy.ListDataAttributeBindingsResponse],
        request: data_taxonomy.ListDataAttributeBindingsRequest,
        response: data_taxonomy.ListDataAttributeBindingsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListDataAttributeBindingsRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListDataAttributeBindingsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = data_taxonomy.ListDataAttributeBindingsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_taxonomy.ListDataAttributeBindingsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[data_taxonomy.DataAttributeBinding]:
        for page in self.pages:
            yield from page.data_attribute_bindings

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataAttributeBindingsAsyncPager:
    """A pager for iterating through ``list_data_attribute_bindings`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListDataAttributeBindingsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_attribute_bindings`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataAttributeBindings`` requests and continue to iterate
    through the ``data_attribute_bindings`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListDataAttributeBindingsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[data_taxonomy.ListDataAttributeBindingsResponse]
        ],
        request: data_taxonomy.ListDataAttributeBindingsRequest,
        response: data_taxonomy.ListDataAttributeBindingsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListDataAttributeBindingsRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListDataAttributeBindingsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = data_taxonomy.ListDataAttributeBindingsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[data_taxonomy.ListDataAttributeBindingsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[data_taxonomy.DataAttributeBinding]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_attribute_bindings:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataAttributesPager:
    """A pager for iterating through ``list_data_attributes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListDataAttributesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``data_attributes`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDataAttributes`` requests and continue to iterate
    through the ``data_attributes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListDataAttributesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., data_taxonomy.ListDataAttributesResponse],
        request: data_taxonomy.ListDataAttributesRequest,
        response: data_taxonomy.ListDataAttributesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListDataAttributesRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListDataAttributesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = data_taxonomy.ListDataAttributesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[data_taxonomy.ListDataAttributesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[data_taxonomy.DataAttribute]:
        for page in self.pages:
            yield from page.data_attributes

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListDataAttributesAsyncPager:
    """A pager for iterating through ``list_data_attributes`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.dataplex_v1.types.ListDataAttributesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``data_attributes`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDataAttributes`` requests and continue to iterate
    through the ``data_attributes`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.dataplex_v1.types.ListDataAttributesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[data_taxonomy.ListDataAttributesResponse]],
        request: data_taxonomy.ListDataAttributesRequest,
        response: data_taxonomy.ListDataAttributesResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.dataplex_v1.types.ListDataAttributesRequest):
                The initial request object.
            response (google.cloud.dataplex_v1.types.ListDataAttributesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = data_taxonomy.ListDataAttributesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[data_taxonomy.ListDataAttributesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[data_taxonomy.DataAttribute]:
        async def async_generator():
            async for page in self.pages:
                for response in page.data_attributes:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
