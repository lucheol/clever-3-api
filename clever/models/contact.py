# coding: utf-8

"""
    Data API

    Serves the Clever Data API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Contact(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'legacy_id': 'str',
        'phone': 'str',
        'phone_type': 'str',
        'sis_id': 'str',
        'student_relationships': 'list[StudentRelationship]'
    }

    attribute_map = {
        'legacy_id': 'legacy_id',
        'phone': 'phone',
        'phone_type': 'phone_type',
        'sis_id': 'sis_id',
        'student_relationships': 'student_relationships'
    }

    def __init__(self, legacy_id=None, phone=None, phone_type=None, sis_id=None, student_relationships=None):  # noqa: E501
        """Contact - a model defined in Swagger"""  # noqa: E501
        self._legacy_id = None
        self._phone = None
        self._phone_type = None
        self._sis_id = None
        self._student_relationships = None
        self.discriminator = None
        if legacy_id is not None:
            self.legacy_id = legacy_id
        if phone is not None:
            self.phone = phone
        if phone_type is not None:
            self.phone_type = phone_type
        if sis_id is not None:
            self.sis_id = sis_id
        if student_relationships is not None:
            self.student_relationships = student_relationships

    @property
    def legacy_id(self):
        """Gets the legacy_id of this Contact.  # noqa: E501


        :return: The legacy_id of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._legacy_id

    @legacy_id.setter
    def legacy_id(self, legacy_id):
        """Sets the legacy_id of this Contact.


        :param legacy_id: The legacy_id of this Contact.  # noqa: E501
        :type: str
        """

        self._legacy_id = legacy_id

    @property
    def phone(self):
        """Gets the phone of this Contact.  # noqa: E501


        :return: The phone of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Contact.


        :param phone: The phone of this Contact.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def phone_type(self):
        """Gets the phone_type of this Contact.  # noqa: E501


        :return: The phone_type of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._phone_type

    @phone_type.setter
    def phone_type(self, phone_type):
        """Sets the phone_type of this Contact.


        :param phone_type: The phone_type of this Contact.  # noqa: E501
        :type: str
        """
        allowed_values = ["Cell", "Home", "Work", "Other", ""]  # noqa: E501
        if phone_type not in allowed_values:
            raise ValueError(
                "Invalid value for `phone_type` ({0}), must be one of {1}"  # noqa: E501
                .format(phone_type, allowed_values)
            )

        self._phone_type = phone_type

    @property
    def sis_id(self):
        """Gets the sis_id of this Contact.  # noqa: E501


        :return: The sis_id of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._sis_id

    @sis_id.setter
    def sis_id(self, sis_id):
        """Sets the sis_id of this Contact.


        :param sis_id: The sis_id of this Contact.  # noqa: E501
        :type: str
        """

        self._sis_id = sis_id

    @property
    def student_relationships(self):
        """Gets the student_relationships of this Contact.  # noqa: E501


        :return: The student_relationships of this Contact.  # noqa: E501
        :rtype: list[StudentRelationship]
        """
        return self._student_relationships

    @student_relationships.setter
    def student_relationships(self, student_relationships):
        """Sets the student_relationships of this Contact.


        :param student_relationships: The student_relationships of this Contact.  # noqa: E501
        :type: list[StudentRelationship]
        """

        self._student_relationships = student_relationships

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Contact, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Contact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
