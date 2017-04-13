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


class CustomSignatureDefinition(BaseObject):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, code=None, created_at=None, error_messages=None, language=None, status=None, updated_at=None, definition=None, definition_id=None, region=None, region_id=None, external_account=None, external_account_id=None, alerts=None, alert_ids=None):
        """
        CustomSignatureDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'code': 'str',
            'created_at': 'datetime',
            'error_messages': 'list[str]',
            'language': 'str',
            'status': 'str',
            'updated_at': 'datetime',
            'definition': 'CustomSignatureDefinition',
            'definition_id': 'int',
            'region': 'Region',
            'region_id': 'int',
            'external_account': 'ExternalAccount',
            'external_account_id': 'int',
            'alerts': 'list[Alert]',
            'alert_ids': 'list[int]'
        }

        self.attribute_map = {
            'id': 'id',
            'code': 'code',
            'created_at': 'created_at',
            'error_messages': 'error_messages',
            'language': 'language',
            'status': 'status',
            'updated_at': 'updated_at',
            'definition': 'definition',
            'definition_id': 'definition_id',
            'region': 'region',
            'region_id': 'region_id',
            'external_account': 'external_account',
            'external_account_id': 'external_account_id',
            'alerts': 'alerts',
            'alert_ids': 'alert_ids'
        }

        self._id = id
        self._code = code
        self._created_at = created_at
        self._error_messages = error_messages
        self._language = language
        self._status = status
        self._updated_at = updated_at
        self._definition = definition
        self._definition_id = definition_id
        self._region = region
        self._region_id = region_id
        self._external_account = external_account
        self._external_account_id = external_account_id
        self._alerts = alerts
        self._alert_ids = alert_ids

    @property
    def id(self):
        """
        Gets the id of this CustomSignatureDefinition.
        Unique ID

        :return: The id of this CustomSignatureDefinition.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CustomSignatureDefinition.
        Unique ID

        :param id: The id of this CustomSignatureDefinition.
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """
        Gets the code of this CustomSignatureDefinition.
        The code used for this result

        :return: The code of this CustomSignatureDefinition.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this CustomSignatureDefinition.
        The code used for this result

        :param code: The code of this CustomSignatureDefinition.
        :type: str
        """

        self._code = code

    @property
    def created_at(self):
        """
        Gets the created_at of this CustomSignatureDefinition.
        ISO 8601 timestamp when the resource was created

        :return: The created_at of this CustomSignatureDefinition.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CustomSignatureDefinition.
        ISO 8601 timestamp when the resource was created

        :param created_at: The created_at of this CustomSignatureDefinition.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def error_messages(self):
        """
        Gets the error_messages of this CustomSignatureDefinition.
        Error messages that occurred while running the code

        :return: The error_messages of this CustomSignatureDefinition.
        :rtype: list[str]
        """
        return self._error_messages

    @error_messages.setter
    def error_messages(self, error_messages):
        """
        Sets the error_messages of this CustomSignatureDefinition.
        Error messages that occurred while running the code

        :param error_messages: The error_messages of this CustomSignatureDefinition.
        :type: list[str]
        """

        self._error_messages = error_messages

    @property
    def language(self):
        """
        Gets the language of this CustomSignatureDefinition.
        The language of the code

        :return: The language of this CustomSignatureDefinition.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this CustomSignatureDefinition.
        The language of the code

        :param language: The language of this CustomSignatureDefinition.
        :type: str
        """

        self._language = language

    @property
    def status(self):
        """
        Gets the status of this CustomSignatureDefinition.
        Status of the result

        :return: The status of this CustomSignatureDefinition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CustomSignatureDefinition.
        Status of the result

        :param status: The status of this CustomSignatureDefinition.
        :type: str
        """

        self._status = status

    @property
    def updated_at(self):
        """
        Gets the updated_at of this CustomSignatureDefinition.
        ISO 8601 timestamp when the resource was last updated

        :return: The updated_at of this CustomSignatureDefinition.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this CustomSignatureDefinition.
        ISO 8601 timestamp when the resource was last updated

        :param updated_at: The updated_at of this CustomSignatureDefinition.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def definition(self):
        """
        Gets the definition of this CustomSignatureDefinition.
        Associated Custom Signature Definition

        :return: The definition of this CustomSignatureDefinition.
        :rtype: CustomSignatureDefinition
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """
        Sets the definition of this CustomSignatureDefinition.
        Associated Custom Signature Definition

        :param definition: The definition of this CustomSignatureDefinition.
        :type: CustomSignatureDefinition
        """

        self._definition = definition

    @property
    def definition_id(self):
        """
        Gets the definition_id of this CustomSignatureDefinition.
        Associated Custom Signature Definition Id

        :return: The definition_id of this CustomSignatureDefinition.
        :rtype: int
        """
        return self._definition_id

    @definition_id.setter
    def definition_id(self, definition_id):
        """
        Sets the definition_id of this CustomSignatureDefinition.
        Associated Custom Signature Definition Id

        :param definition_id: The definition_id of this CustomSignatureDefinition.
        :type: int
        """

        self._definition_id = definition_id

    @property
    def region(self):
        """
        Gets the region of this CustomSignatureDefinition.
        Associated Region

        :return: The region of this CustomSignatureDefinition.
        :rtype: Region
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CustomSignatureDefinition.
        Associated Region

        :param region: The region of this CustomSignatureDefinition.
        :type: Region
        """

        self._region = region

    @property
    def region_id(self):
        """
        Gets the region_id of this CustomSignatureDefinition.
        Associated Region Id

        :return: The region_id of this CustomSignatureDefinition.
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this CustomSignatureDefinition.
        Associated Region Id

        :param region_id: The region_id of this CustomSignatureDefinition.
        :type: int
        """

        self._region_id = region_id

    @property
    def external_account(self):
        """
        Gets the external_account of this CustomSignatureDefinition.
        Associated External Account

        :return: The external_account of this CustomSignatureDefinition.
        :rtype: ExternalAccount
        """
        return self._external_account

    @external_account.setter
    def external_account(self, external_account):
        """
        Sets the external_account of this CustomSignatureDefinition.
        Associated External Account

        :param external_account: The external_account of this CustomSignatureDefinition.
        :type: ExternalAccount
        """

        self._external_account = external_account

    @property
    def external_account_id(self):
        """
        Gets the external_account_id of this CustomSignatureDefinition.
        Associated External Account Id

        :return: The external_account_id of this CustomSignatureDefinition.
        :rtype: int
        """
        return self._external_account_id

    @external_account_id.setter
    def external_account_id(self, external_account_id):
        """
        Sets the external_account_id of this CustomSignatureDefinition.
        Associated External Account Id

        :param external_account_id: The external_account_id of this CustomSignatureDefinition.
        :type: int
        """

        self._external_account_id = external_account_id

    @property
    def alerts(self):
        """
        Gets the alerts of this CustomSignatureDefinition.
        Associated Alerts

        :return: The alerts of this CustomSignatureDefinition.
        :rtype: list[Alert]
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """
        Sets the alerts of this CustomSignatureDefinition.
        Associated Alerts

        :param alerts: The alerts of this CustomSignatureDefinition.
        :type: list[Alert]
        """

        self._alerts = alerts

    @property
    def alert_ids(self):
        """
        Gets the alert_ids of this CustomSignatureDefinition.
        Associated Alert Ids

        :return: The alert_ids of this CustomSignatureDefinition.
        :rtype: list[int]
        """
        return self._alert_ids

    @alert_ids.setter
    def alert_ids(self, alert_ids):
        """
        Sets the alert_ids of this CustomSignatureDefinition.
        Associated Alert Ids

        :param alert_ids: The alert_ids of this CustomSignatureDefinition.
        :type: list[int]
        """

        self._alert_ids = alert_ids

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
        if not isinstance(other, CustomSignatureDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
