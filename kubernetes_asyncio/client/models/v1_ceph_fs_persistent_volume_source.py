# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.15.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1CephFSPersistentVolumeSource(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'monitors': 'list[str]',
        'path': 'str',
        'read_only': 'bool',
        'secret_file': 'str',
        'secret_ref': 'V1SecretReference',
        'user': 'str'
    }

    attribute_map = {
        'monitors': 'monitors',
        'path': 'path',
        'read_only': 'readOnly',
        'secret_file': 'secretFile',
        'secret_ref': 'secretRef',
        'user': 'user'
    }

    def __init__(self, monitors=None, path=None, read_only=None, secret_file=None, secret_ref=None, user=None, local_vars_configuration=None):  # noqa: E501
        """V1CephFSPersistentVolumeSource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._monitors = None
        self._path = None
        self._read_only = None
        self._secret_file = None
        self._secret_ref = None
        self._user = None
        self.discriminator = None

        self.monitors = monitors
        if path is not None:
            self.path = path
        if read_only is not None:
            self.read_only = read_only
        if secret_file is not None:
            self.secret_file = secret_file
        if secret_ref is not None:
            self.secret_ref = secret_ref
        if user is not None:
            self.user = user

    @property
    def monitors(self):
        """Gets the monitors of this V1CephFSPersistentVolumeSource.  # noqa: E501

        Required: Monitors is a collection of Ceph monitors More info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :return: The monitors of this V1CephFSPersistentVolumeSource.  # noqa: E501
        :rtype: list[str]
        """
        return self._monitors

    @monitors.setter
    def monitors(self, monitors):
        """Sets the monitors of this V1CephFSPersistentVolumeSource.

        Required: Monitors is a collection of Ceph monitors More info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :param monitors: The monitors of this V1CephFSPersistentVolumeSource.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and monitors is None:  # noqa: E501
            raise ValueError("Invalid value for `monitors`, must not be `None`")  # noqa: E501

        self._monitors = monitors

    @property
    def path(self):
        """Gets the path of this V1CephFSPersistentVolumeSource.  # noqa: E501

        Optional: Used as the mounted root, rather than the full Ceph tree, default is /  # noqa: E501

        :return: The path of this V1CephFSPersistentVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this V1CephFSPersistentVolumeSource.

        Optional: Used as the mounted root, rather than the full Ceph tree, default is /  # noqa: E501

        :param path: The path of this V1CephFSPersistentVolumeSource.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def read_only(self):
        """Gets the read_only of this V1CephFSPersistentVolumeSource.  # noqa: E501

        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :return: The read_only of this V1CephFSPersistentVolumeSource.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this V1CephFSPersistentVolumeSource.

        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :param read_only: The read_only of this V1CephFSPersistentVolumeSource.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def secret_file(self):
        """Gets the secret_file of this V1CephFSPersistentVolumeSource.  # noqa: E501

        Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :return: The secret_file of this V1CephFSPersistentVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._secret_file

    @secret_file.setter
    def secret_file(self, secret_file):
        """Sets the secret_file of this V1CephFSPersistentVolumeSource.

        Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :param secret_file: The secret_file of this V1CephFSPersistentVolumeSource.  # noqa: E501
        :type: str
        """

        self._secret_file = secret_file

    @property
    def secret_ref(self):
        """Gets the secret_ref of this V1CephFSPersistentVolumeSource.  # noqa: E501


        :return: The secret_ref of this V1CephFSPersistentVolumeSource.  # noqa: E501
        :rtype: V1SecretReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this V1CephFSPersistentVolumeSource.


        :param secret_ref: The secret_ref of this V1CephFSPersistentVolumeSource.  # noqa: E501
        :type: V1SecretReference
        """

        self._secret_ref = secret_ref

    @property
    def user(self):
        """Gets the user of this V1CephFSPersistentVolumeSource.  # noqa: E501

        Optional: User is the rados user name, default is admin More info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :return: The user of this V1CephFSPersistentVolumeSource.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V1CephFSPersistentVolumeSource.

        Optional: User is the rados user name, default is admin More info: https://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it  # noqa: E501

        :param user: The user of this V1CephFSPersistentVolumeSource.  # noqa: E501
        :type: str
        """

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1CephFSPersistentVolumeSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CephFSPersistentVolumeSource):
            return True

        return self.to_dict() != other.to_dict()
