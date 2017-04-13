# coding: utf-8

"""
    ESP Documentation

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
from ..extensions.base_object import BaseObject
import re


class Alert(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, relationships=None, errors=None, id=None, created_at=None, ended_at=None, resource=None, started_at=None, status=None, risk_level=None, updated_at=None, custom_signature=None, custom_signature_id=None, external_account=None, external_account_id=None, region=None, region_id=None, signature=None, signature_id=None, supression=None, supression_id=None, metadata=None, metadata_id=None, cloud_trail_events=None, cloud_trail_event_ids=None, tags=None, tag_ids=None):
        """
        Alert - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'relationships': 'object',
            'errors': 'list[str]',
            'id': 'int',
            'created_at': 'datetime',
            'ended_at': 'datetime',
            'resource': 'str',
            'started_at': 'datetime',
            'status': 'str',
            'risk_level': 'str',
            'updated_at': 'datetime',
            'custom_signature': 'CustomSignature',
            'custom_signature_id': 'int',
            'external_account': 'ExternalAccount',
            'external_account_id': 'int',
            'region': 'Region',
            'region_id': 'int',
            'signature': 'Signature',
            'signature_id': 'int',
            'supression': 'Suppression',
            'supression_id': 'int',
            'metadata': 'Metadata',
            'metadata_id': 'int',
            'cloud_trail_events': 'list[CloudTrailEvent]',
            'cloud_trail_event_ids': 'list[int]',
            'tags': 'list[Tag]',
            'tag_ids': 'list[int]'
        }

        self.attribute_map = {
            'relationships': 'relationships',
            'errors': 'errors',
            'id': 'id',
            'created_at': 'created_at',
            'ended_at': 'ended_at',
            'resource': 'resource',
            'started_at': 'started_at',
            'status': 'status',
            'risk_level': 'risk_level',
            'updated_at': 'updated_at',
            'custom_signature': 'custom_signature',
            'custom_signature_id': 'custom_signature_id',
            'external_account': 'external_account',
            'external_account_id': 'external_account_id',
            'region': 'region',
            'region_id': 'region_id',
            'signature': 'signature',
            'signature_id': 'signature_id',
            'supression': 'supression',
            'supression_id': 'supression_id',
            'metadata': 'metadata',
            'metadata_id': 'metadata_id',
            'cloud_trail_events': 'cloud_trail_events',
            'cloud_trail_event_ids': 'cloud_trail_event_ids',
            'tags': 'tags',
            'tag_ids': 'tag_ids'
        }

        self._relationships = relationships
        self._errors = errors
        self._id = id
        self._created_at = created_at
        self._ended_at = ended_at
        self._resource = resource
        self._started_at = started_at
        self._status = status
        self._risk_level = risk_level
        self._updated_at = updated_at
        self._custom_signature = custom_signature
        self._custom_signature_id = custom_signature_id
        self._external_account = external_account
        self._external_account_id = external_account_id
        self._region = region
        self._region_id = region_id
        self._signature = signature
        self._signature_id = signature_id
        self._supression = supression
        self._supression_id = supression_id
        self._metadata = metadata
        self._metadata_id = metadata_id
        self._cloud_trail_events = cloud_trail_events
        self._cloud_trail_event_ids = cloud_trail_event_ids
        self._tags = tags
        self._tag_ids = tag_ids

    @property
    def relationships(self):
        """
        Gets the relationships of this Alert.
        Links to Associated Objects

        :return: The relationships of this Alert.
        :rtype: object
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """
        Sets the relationships of this Alert.
        Links to Associated Objects

        :param relationships: The relationships of this Alert.
        :type: object
        """

        self._relationships = relationships

    @property
    def errors(self):
        """
        Gets the errors of this Alert.
        Array of error messages if the request failed

        :return: The errors of this Alert.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this Alert.
        Array of error messages if the request failed

        :param errors: The errors of this Alert.
        :type: list[str]
        """

        self._errors = errors

    @property
    def id(self):
        """
        Gets the id of this Alert.
        Unique Id

        :return: The id of this Alert.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Alert.
        Unique Id

        :param id: The id of this Alert.
        :type: int
        """

        self._id = id

    @property
    def created_at(self):
        """
        Gets the created_at of this Alert.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this Alert.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this Alert.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this Alert.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def ended_at(self):
        """
        Gets the ended_at of this Alert.
        ISO 8601 timestamp when the alert stopped being active

        :return: The ended_at of this Alert.
        :rtype: datetime
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        """
        Sets the ended_at of this Alert.
        ISO 8601 timestamp when the alert stopped being active

        :param ended_at: The ended_at of this Alert.
        :type: datetime
        """

        self._ended_at = ended_at

    @property
    def resource(self):
        """
        Gets the resource of this Alert.
        Resource identifier in Amazon

        :return: The resource of this Alert.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this Alert.
        Resource identifier in Amazon

        :param resource: The resource of this Alert.
        :type: str
        """

        self._resource = resource

    @property
    def started_at(self):
        """
        Gets the started_at of this Alert.
        ISO 8601 timestamp when the alert started being active

        :return: The started_at of this Alert.
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """
        Sets the started_at of this Alert.
        ISO 8601 timestamp when the alert started being active

        :param started_at: The started_at of this Alert.
        :type: datetime
        """

        self._started_at = started_at

    @property
    def status(self):
        """
        Gets the status of this Alert.
        Status of the alert

        :return: The status of this Alert.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Alert.
        Status of the alert

        :param status: The status of this Alert.
        :type: str
        """

        self._status = status

    @property
    def risk_level(self):
        """
        Gets the risk_level of this Alert.
        Risk Level of the alert

        :return: The risk_level of this Alert.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """
        Sets the risk_level of this Alert.
        Risk Level of the alert

        :param risk_level: The risk_level of this Alert.
        :type: str
        """

        self._risk_level = risk_level

    @property
    def updated_at(self):
        """
        Gets the updated_at of this Alert.
        ISO 8601 timestamp when the resource was last updated

        :return: The updated_at of this Alert.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this Alert.
        ISO 8601 timestamp when the resource was last updated

        :param updated_at: The updated_at of this Alert.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def custom_signature(self):
        """
        Gets the custom_signature of this Alert.
        Either a signature or custom signature but not both will be present

        :return: The custom_signature of this Alert.
        :rtype: CustomSignature
        """
        return self._custom_signature

    @custom_signature.setter
    def custom_signature(self, custom_signature):
        """
        Sets the custom_signature of this Alert.
        Either a signature or custom signature but not both will be present

        :param custom_signature: The custom_signature of this Alert.
        :type: CustomSignature
        """

        self._custom_signature = custom_signature

    @property
    def custom_signature_id(self):
        """
        Gets the custom_signature_id of this Alert.
        Either a signature or custom signature but not both will be present

        :return: The custom_signature_id of this Alert.
        :rtype: int
        """
        return self._custom_signature_id

    @custom_signature_id.setter
    def custom_signature_id(self, custom_signature_id):
        """
        Sets the custom_signature_id of this Alert.
        Either a signature or custom signature but not both will be present

        :param custom_signature_id: The custom_signature_id of this Alert.
        :type: int
        """

        self._custom_signature_id = custom_signature_id

    @property
    def external_account(self):
        """
        Gets the external_account of this Alert.
        Associated External Account

        :return: The external_account of this Alert.
        :rtype: ExternalAccount
        """
        return self._external_account

    @external_account.setter
    def external_account(self, external_account):
        """
        Sets the external_account of this Alert.
        Associated External Account

        :param external_account: The external_account of this Alert.
        :type: ExternalAccount
        """

        self._external_account = external_account

    @property
    def external_account_id(self):
        """
        Gets the external_account_id of this Alert.
        Associated External Account Id

        :return: The external_account_id of this Alert.
        :rtype: int
        """
        return self._external_account_id

    @external_account_id.setter
    def external_account_id(self, external_account_id):
        """
        Sets the external_account_id of this Alert.
        Associated External Account Id

        :param external_account_id: The external_account_id of this Alert.
        :type: int
        """

        self._external_account_id = external_account_id

    @property
    def region(self):
        """
        Gets the region of this Alert.
        Associated Region

        :return: The region of this Alert.
        :rtype: Region
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this Alert.
        Associated Region

        :param region: The region of this Alert.
        :type: Region
        """

        self._region = region

    @property
    def region_id(self):
        """
        Gets the region_id of this Alert.
        Associated Region Id

        :return: The region_id of this Alert.
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this Alert.
        Associated Region Id

        :param region_id: The region_id of this Alert.
        :type: int
        """

        self._region_id = region_id

    @property
    def signature(self):
        """
        Gets the signature of this Alert.
        Either a signature or custom signature but not both will be present

        :return: The signature of this Alert.
        :rtype: Signature
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """
        Sets the signature of this Alert.
        Either a signature or custom signature but not both will be present

        :param signature: The signature of this Alert.
        :type: Signature
        """

        self._signature = signature

    @property
    def signature_id(self):
        """
        Gets the signature_id of this Alert.
        Either a signature or custom signature but not both will be present

        :return: The signature_id of this Alert.
        :rtype: int
        """
        return self._signature_id

    @signature_id.setter
    def signature_id(self, signature_id):
        """
        Sets the signature_id of this Alert.
        Either a signature or custom signature but not both will be present

        :param signature_id: The signature_id of this Alert.
        :type: int
        """

        self._signature_id = signature_id

    @property
    def supression(self):
        """
        Gets the supression of this Alert.
        If present the alert was suppressed

        :return: The supression of this Alert.
        :rtype: Suppression
        """
        return self._supression

    @supression.setter
    def supression(self, supression):
        """
        Sets the supression of this Alert.
        If present the alert was suppressed

        :param supression: The supression of this Alert.
        :type: Suppression
        """

        self._supression = supression

    @property
    def supression_id(self):
        """
        Gets the supression_id of this Alert.
        If present the alert was suppressed

        :return: The supression_id of this Alert.
        :rtype: int
        """
        return self._supression_id

    @supression_id.setter
    def supression_id(self, supression_id):
        """
        Sets the supression_id of this Alert.
        If present the alert was suppressed

        :param supression_id: The supression_id of this Alert.
        :type: int
        """

        self._supression_id = supression_id

    @property
    def metadata(self):
        """
        Gets the metadata of this Alert.
        Associated Metadata

        :return: The metadata of this Alert.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Alert.
        Associated Metadata

        :param metadata: The metadata of this Alert.
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def metadata_id(self):
        """
        Gets the metadata_id of this Alert.
        Associated Metadata Id

        :return: The metadata_id of this Alert.
        :rtype: int
        """
        return self._metadata_id

    @metadata_id.setter
    def metadata_id(self, metadata_id):
        """
        Sets the metadata_id of this Alert.
        Associated Metadata Id

        :param metadata_id: The metadata_id of this Alert.
        :type: int
        """

        self._metadata_id = metadata_id

    @property
    def cloud_trail_events(self):
        """
        Gets the cloud_trail_events of this Alert.
        Associated Cloud Trail Events

        :return: The cloud_trail_events of this Alert.
        :rtype: list[CloudTrailEvent]
        """
        return self._cloud_trail_events

    @cloud_trail_events.setter
    def cloud_trail_events(self, cloud_trail_events):
        """
        Sets the cloud_trail_events of this Alert.
        Associated Cloud Trail Events

        :param cloud_trail_events: The cloud_trail_events of this Alert.
        :type: list[CloudTrailEvent]
        """

        self._cloud_trail_events = cloud_trail_events

    @property
    def cloud_trail_event_ids(self):
        """
        Gets the cloud_trail_event_ids of this Alert.
        Associated Cloud Trail Event Ids

        :return: The cloud_trail_event_ids of this Alert.
        :rtype: list[int]
        """
        return self._cloud_trail_event_ids

    @cloud_trail_event_ids.setter
    def cloud_trail_event_ids(self, cloud_trail_event_ids):
        """
        Sets the cloud_trail_event_ids of this Alert.
        Associated Cloud Trail Event Ids

        :param cloud_trail_event_ids: The cloud_trail_event_ids of this Alert.
        :type: list[int]
        """

        self._cloud_trail_event_ids = cloud_trail_event_ids

    @property
    def tags(self):
        """
        Gets the tags of this Alert.
        Associated Tags

        :return: The tags of this Alert.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Alert.
        Associated Tags

        :param tags: The tags of this Alert.
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def tag_ids(self):
        """
        Gets the tag_ids of this Alert.
        Associated Tag Ids

        :return: The tag_ids of this Alert.
        :rtype: list[int]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """
        Sets the tag_ids of this Alert.
        Associated Tag Ids

        :param tag_ids: The tag_ids of this Alert.
        :type: list[int]
        """

        self._tag_ids = tag_ids

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
