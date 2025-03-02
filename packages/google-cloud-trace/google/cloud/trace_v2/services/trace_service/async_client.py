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
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.trace_v2 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object]  # type: ignore

from google.protobuf import timestamp_pb2  # type: ignore
from google.protobuf import wrappers_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore

from google.cloud.trace_v2.types import trace, tracing

from .client import TraceServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, TraceServiceTransport
from .transports.grpc_asyncio import TraceServiceGrpcAsyncIOTransport


class TraceServiceAsyncClient:
    """Service for collecting and viewing traces and spans within a
    trace.
    A trace is a collection of spans corresponding to a single
    operation or a set of operations in an application.

    A span is an individual timed event which forms a node of the
    trace tree. A single trace can contain spans from multiple
    services.
    """

    _client: TraceServiceClient

    DEFAULT_ENDPOINT = TraceServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = TraceServiceClient.DEFAULT_MTLS_ENDPOINT

    span_path = staticmethod(TraceServiceClient.span_path)
    parse_span_path = staticmethod(TraceServiceClient.parse_span_path)
    common_billing_account_path = staticmethod(
        TraceServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        TraceServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(TraceServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(TraceServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(TraceServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        TraceServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(TraceServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        TraceServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(TraceServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        TraceServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TraceServiceAsyncClient: The constructed client.
        """
        return TraceServiceClient.from_service_account_info.__func__(TraceServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TraceServiceAsyncClient: The constructed client.
        """
        return TraceServiceClient.from_service_account_file.__func__(TraceServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return TraceServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> TraceServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            TraceServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(TraceServiceClient).get_transport_class, type(TraceServiceClient)
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, TraceServiceTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the trace service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.TraceServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = TraceServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def batch_write_spans(
        self,
        request: Optional[Union[tracing.BatchWriteSpansRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        spans: Optional[MutableSequence[trace.Span]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Batch writes new spans to new or existing traces. You
        cannot update existing spans.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import trace_v2

            async def sample_batch_write_spans():
                # Create a client
                client = trace_v2.TraceServiceAsyncClient()

                # Initialize request argument(s)
                spans = trace_v2.Span()
                spans.name = "name_value"
                spans.span_id = "span_id_value"

                request = trace_v2.BatchWriteSpansRequest(
                    name="name_value",
                    spans=spans,
                )

                # Make the request
                await client.batch_write_spans(request=request)

        Args:
            request (Optional[Union[google.cloud.trace_v2.types.BatchWriteSpansRequest, dict]]):
                The request object. The request message for the ``BatchWriteSpans`` method.
            name (:class:`str`):
                Required. The name of the project where the spans
                belong. The format is ``projects/[PROJECT_ID]``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            spans (:class:`MutableSequence[google.cloud.trace_v2.types.Span]`):
                Required. A list of new spans. The
                span names must not match existing
                spans, otherwise the results are
                undefined.

                This corresponds to the ``spans`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, spans])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = tracing.BatchWriteSpansRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if spans:
            request.spans.extend(spans)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_write_spans,
            default_retry=retries.AsyncRetry(
                initial=0.1,
                maximum=30.0,
                multiplier=2,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=120.0,
            ),
            default_timeout=120.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def create_span(
        self,
        request: Optional[Union[trace.Span, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> trace.Span:
        r"""Creates a new span.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import trace_v2

            async def sample_create_span():
                # Create a client
                client = trace_v2.TraceServiceAsyncClient()

                # Initialize request argument(s)
                request = trace_v2.Span(
                    name="name_value",
                    span_id="span_id_value",
                )

                # Make the request
                response = await client.create_span(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.trace_v2.types.Span, dict]]):
                The request object. A span represents a single operation
                within a trace. Spans can be nested to
                form a trace tree. Often, a trace
                contains a root span that describes the
                end-to-end latency, and one or more
                subspans for its sub-operations.

                A trace can also contain multiple root
                spans, or none at all. Spans do not need
                to be contiguous. There might be gaps or
                overlaps between spans in a trace.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.trace_v2.types.Span:
                A span represents a single operation
                within a trace. Spans can be nested to
                form a trace tree. Often, a trace
                contains a root span that describes the
                end-to-end latency, and one or more
                subspans for its sub-operations.

                A trace can also contain multiple root
                spans, or none at all. Spans do not need
                to be contiguous. There might be gaps or
                overlaps between spans in a trace.

        """
        # Create or coerce a protobuf request object.
        request = trace.Span(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_span,
            default_retry=retries.AsyncRetry(
                initial=0.1,
                maximum=1.0,
                multiplier=1.2,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=120.0,
            ),
            default_timeout=120.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "TraceServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("TraceServiceAsyncClient",)
