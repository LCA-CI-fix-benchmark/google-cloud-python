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
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers
from google.api_core import operations_v1
from google.api_core import gapic_v1
import google.auth                         # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.edgecontainer_v1.types import resources
from google.cloud.edgecontainer_v1.types import service
from google.cloud.location import locations_pb2 # type: ignore
from google.longrunning import operations_pb2 # type: ignore
from .base import EdgeContainerTransport, DEFAULT_CLIENT_INFO


class EdgeContainerGrpcTransport(EdgeContainerTransport):
    """gRPC backend transport for EdgeContainer.

    EdgeContainer API provides management of Kubernetes Clusters
    on Google Edge Cloud deployments.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    _stubs: Dict[str, Callable]

    def __init__(self, *,
            host: str = 'edgecontainer.googleapis.com',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            channel: Optional[grpc.Channel] = None,
            api_mtls_endpoint: Optional[str] = None,
            client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
            ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
            client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            api_audience: Optional[str] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(cls,
                       host: str = 'edgecontainer.googleapis.com',
                       credentials: Optional[ga_credentials.Credentials] = None,
                       credentials_file: Optional[str] = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def list_clusters(self) -> Callable[
            [service.ListClustersRequest],
            service.ListClustersResponse]:
        r"""Return a callable for the list clusters method over gRPC.

        Lists Clusters in a given project and location.

        Returns:
            Callable[[~.ListClustersRequest],
                    ~.ListClustersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_clusters' not in self._stubs:
            self._stubs['list_clusters'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/ListClusters',
                request_serializer=service.ListClustersRequest.serialize,
                response_deserializer=service.ListClustersResponse.deserialize,
            )
        return self._stubs['list_clusters']

    @property
    def get_cluster(self) -> Callable[
            [service.GetClusterRequest],
            resources.Cluster]:
        r"""Return a callable for the get cluster method over gRPC.

        Gets details of a single Cluster.

        Returns:
            Callable[[~.GetClusterRequest],
                    ~.Cluster]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_cluster' not in self._stubs:
            self._stubs['get_cluster'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/GetCluster',
                request_serializer=service.GetClusterRequest.serialize,
                response_deserializer=resources.Cluster.deserialize,
            )
        return self._stubs['get_cluster']

    @property
    def create_cluster(self) -> Callable[
            [service.CreateClusterRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the create cluster method over gRPC.

        Creates a new Cluster in a given project and
        location.

        Returns:
            Callable[[~.CreateClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_cluster' not in self._stubs:
            self._stubs['create_cluster'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/CreateCluster',
                request_serializer=service.CreateClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['create_cluster']

    @property
    def update_cluster(self) -> Callable[
            [service.UpdateClusterRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the update cluster method over gRPC.

        Updates the parameters of a single Cluster.

        Returns:
            Callable[[~.UpdateClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_cluster' not in self._stubs:
            self._stubs['update_cluster'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/UpdateCluster',
                request_serializer=service.UpdateClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['update_cluster']

    @property
    def delete_cluster(self) -> Callable[
            [service.DeleteClusterRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the delete cluster method over gRPC.

        Deletes a single Cluster.

        Returns:
            Callable[[~.DeleteClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_cluster' not in self._stubs:
            self._stubs['delete_cluster'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/DeleteCluster',
                request_serializer=service.DeleteClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['delete_cluster']

    @property
    def generate_access_token(self) -> Callable[
            [service.GenerateAccessTokenRequest],
            service.GenerateAccessTokenResponse]:
        r"""Return a callable for the generate access token method over gRPC.

        Generates an access token for a Cluster.

        Returns:
            Callable[[~.GenerateAccessTokenRequest],
                    ~.GenerateAccessTokenResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'generate_access_token' not in self._stubs:
            self._stubs['generate_access_token'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/GenerateAccessToken',
                request_serializer=service.GenerateAccessTokenRequest.serialize,
                response_deserializer=service.GenerateAccessTokenResponse.deserialize,
            )
        return self._stubs['generate_access_token']

    @property
    def list_node_pools(self) -> Callable[
            [service.ListNodePoolsRequest],
            service.ListNodePoolsResponse]:
        r"""Return a callable for the list node pools method over gRPC.

        Lists NodePools in a given project and location.

        Returns:
            Callable[[~.ListNodePoolsRequest],
                    ~.ListNodePoolsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_node_pools' not in self._stubs:
            self._stubs['list_node_pools'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/ListNodePools',
                request_serializer=service.ListNodePoolsRequest.serialize,
                response_deserializer=service.ListNodePoolsResponse.deserialize,
            )
        return self._stubs['list_node_pools']

    @property
    def get_node_pool(self) -> Callable[
            [service.GetNodePoolRequest],
            resources.NodePool]:
        r"""Return a callable for the get node pool method over gRPC.

        Gets details of a single NodePool.

        Returns:
            Callable[[~.GetNodePoolRequest],
                    ~.NodePool]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_node_pool' not in self._stubs:
            self._stubs['get_node_pool'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/GetNodePool',
                request_serializer=service.GetNodePoolRequest.serialize,
                response_deserializer=resources.NodePool.deserialize,
            )
        return self._stubs['get_node_pool']

    @property
    def create_node_pool(self) -> Callable[
            [service.CreateNodePoolRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the create node pool method over gRPC.

        Creates a new NodePool in a given project and
        location.

        Returns:
            Callable[[~.CreateNodePoolRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_node_pool' not in self._stubs:
            self._stubs['create_node_pool'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/CreateNodePool',
                request_serializer=service.CreateNodePoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['create_node_pool']

    @property
    def update_node_pool(self) -> Callable[
            [service.UpdateNodePoolRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the update node pool method over gRPC.

        Updates the parameters of a single NodePool.

        Returns:
            Callable[[~.UpdateNodePoolRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'update_node_pool' not in self._stubs:
            self._stubs['update_node_pool'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/UpdateNodePool',
                request_serializer=service.UpdateNodePoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['update_node_pool']

    @property
    def delete_node_pool(self) -> Callable[
            [service.DeleteNodePoolRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the delete node pool method over gRPC.

        Deletes a single NodePool.

        Returns:
            Callable[[~.DeleteNodePoolRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_node_pool' not in self._stubs:
            self._stubs['delete_node_pool'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/DeleteNodePool',
                request_serializer=service.DeleteNodePoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['delete_node_pool']

    @property
    def list_machines(self) -> Callable[
            [service.ListMachinesRequest],
            service.ListMachinesResponse]:
        r"""Return a callable for the list machines method over gRPC.

        Lists Machines in a given project and location.

        Returns:
            Callable[[~.ListMachinesRequest],
                    ~.ListMachinesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_machines' not in self._stubs:
            self._stubs['list_machines'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/ListMachines',
                request_serializer=service.ListMachinesRequest.serialize,
                response_deserializer=service.ListMachinesResponse.deserialize,
            )
        return self._stubs['list_machines']

    @property
    def get_machine(self) -> Callable[
            [service.GetMachineRequest],
            resources.Machine]:
        r"""Return a callable for the get machine method over gRPC.

        Gets details of a single Machine.

        Returns:
            Callable[[~.GetMachineRequest],
                    ~.Machine]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_machine' not in self._stubs:
            self._stubs['get_machine'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/GetMachine',
                request_serializer=service.GetMachineRequest.serialize,
                response_deserializer=resources.Machine.deserialize,
            )
        return self._stubs['get_machine']

    @property
    def list_vpn_connections(self) -> Callable[
            [service.ListVpnConnectionsRequest],
            service.ListVpnConnectionsResponse]:
        r"""Return a callable for the list vpn connections method over gRPC.

        Lists VPN connections in a given project and
        location.

        Returns:
            Callable[[~.ListVpnConnectionsRequest],
                    ~.ListVpnConnectionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_vpn_connections' not in self._stubs:
            self._stubs['list_vpn_connections'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/ListVpnConnections',
                request_serializer=service.ListVpnConnectionsRequest.serialize,
                response_deserializer=service.ListVpnConnectionsResponse.deserialize,
            )
        return self._stubs['list_vpn_connections']

    @property
    def get_vpn_connection(self) -> Callable[
            [service.GetVpnConnectionRequest],
            resources.VpnConnection]:
        r"""Return a callable for the get vpn connection method over gRPC.

        Gets details of a single VPN connection.

        Returns:
            Callable[[~.GetVpnConnectionRequest],
                    ~.VpnConnection]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_vpn_connection' not in self._stubs:
            self._stubs['get_vpn_connection'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/GetVpnConnection',
                request_serializer=service.GetVpnConnectionRequest.serialize,
                response_deserializer=resources.VpnConnection.deserialize,
            )
        return self._stubs['get_vpn_connection']

    @property
    def create_vpn_connection(self) -> Callable[
            [service.CreateVpnConnectionRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the create vpn connection method over gRPC.

        Creates a new VPN connection in a given project and
        location.

        Returns:
            Callable[[~.CreateVpnConnectionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_vpn_connection' not in self._stubs:
            self._stubs['create_vpn_connection'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/CreateVpnConnection',
                request_serializer=service.CreateVpnConnectionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['create_vpn_connection']

    @property
    def delete_vpn_connection(self) -> Callable[
            [service.DeleteVpnConnectionRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the delete vpn connection method over gRPC.

        Deletes a single VPN connection.

        Returns:
            Callable[[~.DeleteVpnConnectionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_vpn_connection' not in self._stubs:
            self._stubs['delete_vpn_connection'] = self.grpc_channel.unary_unary(
                '/google.cloud.edgecontainer.v1.EdgeContainer/DeleteVpnConnection',
                request_serializer=service.DeleteVpnConnectionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['delete_vpn_connection']

    def close(self):
        self.grpc_channel.close()

    @property
    def delete_operation(
        self,
    ) -> Callable[[operations_pb2.DeleteOperationRequest], None]:
        r"""Return a callable for the delete_operation method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_operation" not in self._stubs:
            self._stubs["delete_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/DeleteOperation",
                request_serializer=operations_pb2.DeleteOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["delete_operation"]

    @property
    def cancel_operation(
        self,
    ) -> Callable[[operations_pb2.CancelOperationRequest], None]:
        r"""Return a callable for the cancel_operation method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_operation" not in self._stubs:
            self._stubs["cancel_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/CancelOperation",
                request_serializer=operations_pb2.CancelOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["cancel_operation"]

    @property
    def get_operation(
        self,
    ) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]:
        r"""Return a callable for the get_operation method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_operation" not in self._stubs:
            self._stubs["get_operation"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/GetOperation",
                request_serializer=operations_pb2.GetOperationRequest.SerializeToString,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_operation"]

    @property
    def list_operations(
        self,
    ) -> Callable[[operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse]:
        r"""Return a callable for the list_operations method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_operations" not in self._stubs:
            self._stubs["list_operations"] = self.grpc_channel.unary_unary(
                "/google.longrunning.Operations/ListOperations",
                request_serializer=operations_pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=operations_pb2.ListOperationsResponse.FromString,
            )
        return self._stubs["list_operations"]

    @property
    def list_locations(
        self,
    ) -> Callable[[locations_pb2.ListLocationsRequest], locations_pb2.ListLocationsResponse]:
        r"""Return a callable for the list locations method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_locations" not in self._stubs:
            self._stubs["list_locations"] = self.grpc_channel.unary_unary(
                "/google.cloud.location.Locations/ListLocations",
                request_serializer=locations_pb2.ListLocationsRequest.SerializeToString,
                response_deserializer=locations_pb2.ListLocationsResponse.FromString,
            )
        return self._stubs["list_locations"]

    @property
    def get_location(
        self,
    ) -> Callable[[locations_pb2.GetLocationRequest], locations_pb2.Location]:
        r"""Return a callable for the list locations method over gRPC.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_location" not in self._stubs:
            self._stubs["get_location"] = self.grpc_channel.unary_unary(
                "/google.cloud.location.Locations/GetLocation",
                request_serializer=locations_pb2.GetLocationRequest.SerializeToString,
                response_deserializer=locations_pb2.Location.FromString,
            )
        return self._stubs["get_location"]

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = (
    'EdgeContainerGrpcTransport',
)
