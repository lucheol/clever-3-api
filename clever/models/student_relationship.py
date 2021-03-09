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

class StudentRelationship(object):
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
        'relationship': 'str',
        'student': 'str',
        'type': 'str'
    }

    attribute_map = {
        'relationship': 'relationship',
        'student': 'student',
        'type': 'type'
    }

    def __init__(self, relationship=None, student=None, type=None):  # noqa: E501
        """StudentRelationship - a model defined in Swagger"""  # noqa: E501
        self._relationship = None
        self._student = None
        self._type = None
        self.discriminator = None
        if relationship is not None:
            self.relationship = relationship
        if student is not None:
            self.student = student
        if type is not None:
            self.type = type

    @property
    def relationship(self):
        """Gets the relationship of this StudentRelationship.  # noqa: E501


        :return: The relationship of this StudentRelationship.  # noqa: E501
        :rtype: str
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """Sets the relationship of this StudentRelationship.


        :param relationship: The relationship of this StudentRelationship.  # noqa: E501
        :type: str
        """
        allowed_values = ["Parent", "Grandparent", "Self", "Aunt/Uncle", "Sibling", "Other", ""]  # noqa: E501
        if relationship not in allowed_values:
            raise ValueError(
                "Invalid value for `relationship` ({0}), must be one of {1}"  # noqa: E501
                .format(relationship, allowed_values)
            )

        self._relationship = relationship

    @property
    def student(self):
        """Gets the student of this StudentRelationship.  # noqa: E501


        :return: The student of this StudentRelationship.  # noqa: E501
        :rtype: str
        """
        return self._student

    @student.setter
    def student(self, student):
        """Sets the student of this StudentRelationship.


        :param student: The student of this StudentRelationship.  # noqa: E501
        :type: str
        """

        self._student = student

    @property
    def type(self):
        """Gets the type of this StudentRelationship.  # noqa: E501


        :return: The type of this StudentRelationship.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StudentRelationship.


        :param type: The type of this StudentRelationship.  # noqa: E501
        :type: str
        """
        allowed_values = ["Parent/Guardian", "Emergency", "Primary", "Secondary", "Family", "Other", ""]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(StudentRelationship, dict):
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
        if not isinstance(other, StudentRelationship):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
