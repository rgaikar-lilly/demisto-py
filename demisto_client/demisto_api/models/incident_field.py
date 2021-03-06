# coding: utf-8

"""
    Demisto API

    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from demisto_client.demisto_api.models.field_group import FieldGroup  # noqa: F401,E501
from demisto_client.demisto_api.models.grid_column import GridColumn  # noqa: F401,E501


class IncidentField(object):
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
        'associated_to_all': 'bool',
        'associated_types': 'list[str]',
        'breach_script': 'str',
        'case_insensitive': 'bool',
        'cli_name': 'str',
        'close_form': 'bool',
        'columns': 'list[GridColumn]',
        'commit_message': 'str',
        'content': 'bool',
        'default_rows': 'list[dict(str, object)]',
        'description': 'str',
        'edit_form': 'bool',
        'field_calc_script': 'str',
        'group': 'FieldGroup',
        'hidden': 'bool',
        'id': 'str',
        'is_read_only': 'bool',
        'locked': 'bool',
        'modified': 'datetime',
        'name': 'str',
        'never_set_as_required': 'bool',
        'owner_only': 'bool',
        'placeholder': 'str',
        'prev_name': 'str',
        'required': 'bool',
        'script': 'str',
        'select_values': 'list[str]',
        'should_commit': 'bool',
        'sla': 'int',
        'sort_values': 'list[str]',
        'system': 'bool',
        'system_associated_types': 'list[str]',
        'threshold': 'float',
        'type': 'str',
        'unmapped': 'bool',
        'unsearchable': 'bool',
        'use_as_kpi': 'bool',
        'validated_error': 'str',
        'validation_regex': 'str',
        'vc_should_ignore': 'bool',
        'version': 'int'
    }

    attribute_map = {
        'associated_to_all': 'associatedToAll',
        'associated_types': 'associatedTypes',
        'breach_script': 'breachScript',
        'case_insensitive': 'caseInsensitive',
        'cli_name': 'cliName',
        'close_form': 'closeForm',
        'columns': 'columns',
        'commit_message': 'commitMessage',
        'content': 'content',
        'default_rows': 'defaultRows',
        'description': 'description',
        'edit_form': 'editForm',
        'field_calc_script': 'fieldCalcScript',
        'group': 'group',
        'hidden': 'hidden',
        'id': 'id',
        'is_read_only': 'isReadOnly',
        'locked': 'locked',
        'modified': 'modified',
        'name': 'name',
        'never_set_as_required': 'neverSetAsRequired',
        'owner_only': 'ownerOnly',
        'placeholder': 'placeholder',
        'prev_name': 'prevName',
        'required': 'required',
        'script': 'script',
        'select_values': 'selectValues',
        'should_commit': 'shouldCommit',
        'sla': 'sla',
        'sort_values': 'sortValues',
        'system': 'system',
        'system_associated_types': 'systemAssociatedTypes',
        'threshold': 'threshold',
        'type': 'type',
        'unmapped': 'unmapped',
        'unsearchable': 'unsearchable',
        'use_as_kpi': 'useAsKpi',
        'validated_error': 'validatedError',
        'validation_regex': 'validationRegex',
        'vc_should_ignore': 'vcShouldIgnore',
        'version': 'version'
    }

    def __init__(self, associated_to_all=None, associated_types=None, breach_script=None, case_insensitive=None, cli_name=None, close_form=None, columns=None, commit_message=None, content=None, default_rows=None, description=None, edit_form=None, field_calc_script=None, group=None, hidden=None, id=None, is_read_only=None, locked=None, modified=None, name=None, never_set_as_required=None, owner_only=None, placeholder=None, prev_name=None, required=None, script=None, select_values=None, should_commit=None, sla=None, sort_values=None, system=None, system_associated_types=None, threshold=None, type=None, unmapped=None, unsearchable=None, use_as_kpi=None, validated_error=None, validation_regex=None, vc_should_ignore=None, version=None):  # noqa: E501
        """IncidentField - a model defined in Swagger"""  # noqa: E501

        self._associated_to_all = None
        self._associated_types = None
        self._breach_script = None
        self._case_insensitive = None
        self._cli_name = None
        self._close_form = None
        self._columns = None
        self._commit_message = None
        self._content = None
        self._default_rows = None
        self._description = None
        self._edit_form = None
        self._field_calc_script = None
        self._group = None
        self._hidden = None
        self._id = None
        self._is_read_only = None
        self._locked = None
        self._modified = None
        self._name = None
        self._never_set_as_required = None
        self._owner_only = None
        self._placeholder = None
        self._prev_name = None
        self._required = None
        self._script = None
        self._select_values = None
        self._should_commit = None
        self._sla = None
        self._sort_values = None
        self._system = None
        self._system_associated_types = None
        self._threshold = None
        self._type = None
        self._unmapped = None
        self._unsearchable = None
        self._use_as_kpi = None
        self._validated_error = None
        self._validation_regex = None
        self._vc_should_ignore = None
        self._version = None
        self.discriminator = None

        if associated_to_all is not None:
            self.associated_to_all = associated_to_all
        if associated_types is not None:
            self.associated_types = associated_types
        if breach_script is not None:
            self.breach_script = breach_script
        if case_insensitive is not None:
            self.case_insensitive = case_insensitive
        if cli_name is not None:
            self.cli_name = cli_name
        if close_form is not None:
            self.close_form = close_form
        if columns is not None:
            self.columns = columns
        if commit_message is not None:
            self.commit_message = commit_message
        if content is not None:
            self.content = content
        if default_rows is not None:
            self.default_rows = default_rows
        if description is not None:
            self.description = description
        if edit_form is not None:
            self.edit_form = edit_form
        if field_calc_script is not None:
            self.field_calc_script = field_calc_script
        if group is not None:
            self.group = group
        if hidden is not None:
            self.hidden = hidden
        if id is not None:
            self.id = id
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if locked is not None:
            self.locked = locked
        if modified is not None:
            self.modified = modified
        if name is not None:
            self.name = name
        if never_set_as_required is not None:
            self.never_set_as_required = never_set_as_required
        if owner_only is not None:
            self.owner_only = owner_only
        if placeholder is not None:
            self.placeholder = placeholder
        if prev_name is not None:
            self.prev_name = prev_name
        if required is not None:
            self.required = required
        if script is not None:
            self.script = script
        if select_values is not None:
            self.select_values = select_values
        if should_commit is not None:
            self.should_commit = should_commit
        if sla is not None:
            self.sla = sla
        if sort_values is not None:
            self.sort_values = sort_values
        if system is not None:
            self.system = system
        if system_associated_types is not None:
            self.system_associated_types = system_associated_types
        if threshold is not None:
            self.threshold = threshold
        if type is not None:
            self.type = type
        if unmapped is not None:
            self.unmapped = unmapped
        if unsearchable is not None:
            self.unsearchable = unsearchable
        if use_as_kpi is not None:
            self.use_as_kpi = use_as_kpi
        if validated_error is not None:
            self.validated_error = validated_error
        if validation_regex is not None:
            self.validation_regex = validation_regex
        if vc_should_ignore is not None:
            self.vc_should_ignore = vc_should_ignore
        if version is not None:
            self.version = version

    @property
    def associated_to_all(self):
        """Gets the associated_to_all of this IncidentField.  # noqa: E501


        :return: The associated_to_all of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._associated_to_all

    @associated_to_all.setter
    def associated_to_all(self, associated_to_all):
        """Sets the associated_to_all of this IncidentField.


        :param associated_to_all: The associated_to_all of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._associated_to_all = associated_to_all

    @property
    def associated_types(self):
        """Gets the associated_types of this IncidentField.  # noqa: E501

        AssociatedTypes - list of incident (case) types IDs related to specific incident field  # noqa: E501

        :return: The associated_types of this IncidentField.  # noqa: E501
        :rtype: list[str]
        """
        return self._associated_types

    @associated_types.setter
    def associated_types(self, associated_types):
        """Sets the associated_types of this IncidentField.

        AssociatedTypes - list of incident (case) types IDs related to specific incident field  # noqa: E501

        :param associated_types: The associated_types of this IncidentField.  # noqa: E501
        :type: list[str]
        """

        self._associated_types = associated_types

    @property
    def breach_script(self):
        """Gets the breach_script of this IncidentField.  # noqa: E501


        :return: The breach_script of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._breach_script

    @breach_script.setter
    def breach_script(self, breach_script):
        """Sets the breach_script of this IncidentField.


        :param breach_script: The breach_script of this IncidentField.  # noqa: E501
        :type: str
        """

        self._breach_script = breach_script

    @property
    def case_insensitive(self):
        """Gets the case_insensitive of this IncidentField.  # noqa: E501


        :return: The case_insensitive of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._case_insensitive

    @case_insensitive.setter
    def case_insensitive(self, case_insensitive):
        """Sets the case_insensitive of this IncidentField.


        :param case_insensitive: The case_insensitive of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._case_insensitive = case_insensitive

    @property
    def cli_name(self):
        """Gets the cli_name of this IncidentField.  # noqa: E501


        :return: The cli_name of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._cli_name

    @cli_name.setter
    def cli_name(self, cli_name):
        """Sets the cli_name of this IncidentField.


        :param cli_name: The cli_name of this IncidentField.  # noqa: E501
        :type: str
        """

        self._cli_name = cli_name

    @property
    def close_form(self):
        """Gets the close_form of this IncidentField.  # noqa: E501


        :return: The close_form of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._close_form

    @close_form.setter
    def close_form(self, close_form):
        """Sets the close_form of this IncidentField.


        :param close_form: The close_form of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._close_form = close_form

    @property
    def columns(self):
        """Gets the columns of this IncidentField.  # noqa: E501


        :return: The columns of this IncidentField.  # noqa: E501
        :rtype: list[GridColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this IncidentField.


        :param columns: The columns of this IncidentField.  # noqa: E501
        :type: list[GridColumn]
        """

        self._columns = columns

    @property
    def commit_message(self):
        """Gets the commit_message of this IncidentField.  # noqa: E501


        :return: The commit_message of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """Sets the commit_message of this IncidentField.


        :param commit_message: The commit_message of this IncidentField.  # noqa: E501
        :type: str
        """

        self._commit_message = commit_message

    @property
    def content(self):
        """Gets the content of this IncidentField.  # noqa: E501


        :return: The content of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this IncidentField.


        :param content: The content of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._content = content

    @property
    def default_rows(self):
        """Gets the default_rows of this IncidentField.  # noqa: E501


        :return: The default_rows of this IncidentField.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._default_rows

    @default_rows.setter
    def default_rows(self, default_rows):
        """Sets the default_rows of this IncidentField.


        :param default_rows: The default_rows of this IncidentField.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._default_rows = default_rows

    @property
    def description(self):
        """Gets the description of this IncidentField.  # noqa: E501


        :return: The description of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IncidentField.


        :param description: The description of this IncidentField.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def edit_form(self):
        """Gets the edit_form of this IncidentField.  # noqa: E501


        :return: The edit_form of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._edit_form

    @edit_form.setter
    def edit_form(self, edit_form):
        """Sets the edit_form of this IncidentField.


        :param edit_form: The edit_form of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._edit_form = edit_form

    @property
    def field_calc_script(self):
        """Gets the field_calc_script of this IncidentField.  # noqa: E501


        :return: The field_calc_script of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._field_calc_script

    @field_calc_script.setter
    def field_calc_script(self, field_calc_script):
        """Sets the field_calc_script of this IncidentField.


        :param field_calc_script: The field_calc_script of this IncidentField.  # noqa: E501
        :type: str
        """

        self._field_calc_script = field_calc_script

    @property
    def group(self):
        """Gets the group of this IncidentField.  # noqa: E501


        :return: The group of this IncidentField.  # noqa: E501
        :rtype: FieldGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this IncidentField.


        :param group: The group of this IncidentField.  # noqa: E501
        :type: FieldGroup
        """

        self._group = group

    @property
    def hidden(self):
        """Gets the hidden of this IncidentField.  # noqa: E501


        :return: The hidden of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this IncidentField.


        :param hidden: The hidden of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def id(self):
        """Gets the id of this IncidentField.  # noqa: E501


        :return: The id of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IncidentField.


        :param id: The id of this IncidentField.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_read_only(self):
        """Gets the is_read_only of this IncidentField.  # noqa: E501


        :return: The is_read_only of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """Sets the is_read_only of this IncidentField.


        :param is_read_only: The is_read_only of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._is_read_only = is_read_only

    @property
    def locked(self):
        """Gets the locked of this IncidentField.  # noqa: E501


        :return: The locked of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this IncidentField.


        :param locked: The locked of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def modified(self):
        """Gets the modified of this IncidentField.  # noqa: E501


        :return: The modified of this IncidentField.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this IncidentField.


        :param modified: The modified of this IncidentField.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this IncidentField.  # noqa: E501


        :return: The name of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IncidentField.


        :param name: The name of this IncidentField.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def never_set_as_required(self):
        """Gets the never_set_as_required of this IncidentField.  # noqa: E501


        :return: The never_set_as_required of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._never_set_as_required

    @never_set_as_required.setter
    def never_set_as_required(self, never_set_as_required):
        """Sets the never_set_as_required of this IncidentField.


        :param never_set_as_required: The never_set_as_required of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._never_set_as_required = never_set_as_required

    @property
    def owner_only(self):
        """Gets the owner_only of this IncidentField.  # noqa: E501


        :return: The owner_only of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._owner_only

    @owner_only.setter
    def owner_only(self, owner_only):
        """Sets the owner_only of this IncidentField.


        :param owner_only: The owner_only of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._owner_only = owner_only

    @property
    def placeholder(self):
        """Gets the placeholder of this IncidentField.  # noqa: E501


        :return: The placeholder of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._placeholder

    @placeholder.setter
    def placeholder(self, placeholder):
        """Sets the placeholder of this IncidentField.


        :param placeholder: The placeholder of this IncidentField.  # noqa: E501
        :type: str
        """

        self._placeholder = placeholder

    @property
    def prev_name(self):
        """Gets the prev_name of this IncidentField.  # noqa: E501


        :return: The prev_name of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._prev_name

    @prev_name.setter
    def prev_name(self, prev_name):
        """Sets the prev_name of this IncidentField.


        :param prev_name: The prev_name of this IncidentField.  # noqa: E501
        :type: str
        """

        self._prev_name = prev_name

    @property
    def required(self):
        """Gets the required of this IncidentField.  # noqa: E501


        :return: The required of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this IncidentField.


        :param required: The required of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def script(self):
        """Gets the script of this IncidentField.  # noqa: E501


        :return: The script of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this IncidentField.


        :param script: The script of this IncidentField.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def select_values(self):
        """Gets the select_values of this IncidentField.  # noqa: E501


        :return: The select_values of this IncidentField.  # noqa: E501
        :rtype: list[str]
        """
        return self._select_values

    @select_values.setter
    def select_values(self, select_values):
        """Sets the select_values of this IncidentField.


        :param select_values: The select_values of this IncidentField.  # noqa: E501
        :type: list[str]
        """

        self._select_values = select_values

    @property
    def should_commit(self):
        """Gets the should_commit of this IncidentField.  # noqa: E501


        :return: The should_commit of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._should_commit

    @should_commit.setter
    def should_commit(self, should_commit):
        """Sets the should_commit of this IncidentField.


        :param should_commit: The should_commit of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._should_commit = should_commit

    @property
    def sla(self):
        """Gets the sla of this IncidentField.  # noqa: E501


        :return: The sla of this IncidentField.  # noqa: E501
        :rtype: int
        """
        return self._sla

    @sla.setter
    def sla(self, sla):
        """Sets the sla of this IncidentField.


        :param sla: The sla of this IncidentField.  # noqa: E501
        :type: int
        """

        self._sla = sla

    @property
    def sort_values(self):
        """Gets the sort_values of this IncidentField.  # noqa: E501


        :return: The sort_values of this IncidentField.  # noqa: E501
        :rtype: list[str]
        """
        return self._sort_values

    @sort_values.setter
    def sort_values(self, sort_values):
        """Sets the sort_values of this IncidentField.


        :param sort_values: The sort_values of this IncidentField.  # noqa: E501
        :type: list[str]
        """

        self._sort_values = sort_values

    @property
    def system(self):
        """Gets the system of this IncidentField.  # noqa: E501


        :return: The system of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this IncidentField.


        :param system: The system of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def system_associated_types(self):
        """Gets the system_associated_types of this IncidentField.  # noqa: E501


        :return: The system_associated_types of this IncidentField.  # noqa: E501
        :rtype: list[str]
        """
        return self._system_associated_types

    @system_associated_types.setter
    def system_associated_types(self, system_associated_types):
        """Sets the system_associated_types of this IncidentField.


        :param system_associated_types: The system_associated_types of this IncidentField.  # noqa: E501
        :type: list[str]
        """

        self._system_associated_types = system_associated_types

    @property
    def threshold(self):
        """Gets the threshold of this IncidentField.  # noqa: E501


        :return: The threshold of this IncidentField.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this IncidentField.


        :param threshold: The threshold of this IncidentField.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

    @property
    def type(self):
        """Gets the type of this IncidentField.  # noqa: E501


        :return: The type of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IncidentField.


        :param type: The type of this IncidentField.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def unmapped(self):
        """Gets the unmapped of this IncidentField.  # noqa: E501


        :return: The unmapped of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._unmapped

    @unmapped.setter
    def unmapped(self, unmapped):
        """Sets the unmapped of this IncidentField.


        :param unmapped: The unmapped of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._unmapped = unmapped

    @property
    def unsearchable(self):
        """Gets the unsearchable of this IncidentField.  # noqa: E501


        :return: The unsearchable of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._unsearchable

    @unsearchable.setter
    def unsearchable(self, unsearchable):
        """Sets the unsearchable of this IncidentField.


        :param unsearchable: The unsearchable of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._unsearchable = unsearchable

    @property
    def use_as_kpi(self):
        """Gets the use_as_kpi of this IncidentField.  # noqa: E501


        :return: The use_as_kpi of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._use_as_kpi

    @use_as_kpi.setter
    def use_as_kpi(self, use_as_kpi):
        """Sets the use_as_kpi of this IncidentField.


        :param use_as_kpi: The use_as_kpi of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._use_as_kpi = use_as_kpi

    @property
    def validated_error(self):
        """Gets the validated_error of this IncidentField.  # noqa: E501


        :return: The validated_error of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._validated_error

    @validated_error.setter
    def validated_error(self, validated_error):
        """Sets the validated_error of this IncidentField.


        :param validated_error: The validated_error of this IncidentField.  # noqa: E501
        :type: str
        """

        self._validated_error = validated_error

    @property
    def validation_regex(self):
        """Gets the validation_regex of this IncidentField.  # noqa: E501


        :return: The validation_regex of this IncidentField.  # noqa: E501
        :rtype: str
        """
        return self._validation_regex

    @validation_regex.setter
    def validation_regex(self, validation_regex):
        """Sets the validation_regex of this IncidentField.


        :param validation_regex: The validation_regex of this IncidentField.  # noqa: E501
        :type: str
        """

        self._validation_regex = validation_regex

    @property
    def vc_should_ignore(self):
        """Gets the vc_should_ignore of this IncidentField.  # noqa: E501


        :return: The vc_should_ignore of this IncidentField.  # noqa: E501
        :rtype: bool
        """
        return self._vc_should_ignore

    @vc_should_ignore.setter
    def vc_should_ignore(self, vc_should_ignore):
        """Sets the vc_should_ignore of this IncidentField.


        :param vc_should_ignore: The vc_should_ignore of this IncidentField.  # noqa: E501
        :type: bool
        """

        self._vc_should_ignore = vc_should_ignore

    @property
    def version(self):
        """Gets the version of this IncidentField.  # noqa: E501


        :return: The version of this IncidentField.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IncidentField.


        :param version: The version of this IncidentField.  # noqa: E501
        :type: int
        """

        self._version = version

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
        if issubclass(IncidentField, dict):
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
        if not isinstance(other, IncidentField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
