# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class AdUploadBody(object):
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
        'advertiser_id': 'str',
        'auto_bind_enabled': 'bool',
        'auto_fix_enabled': 'bool',
        'file_id': 'str',
        'file_name': 'str',
        'flaw_detect': 'bool',
        'is_third_party': 'bool',
        'upload_type': 'str',
        'video_file': 'str',
        'video_id': 'str',
        'video_signature': 'str',
        'video_url': 'str'
    }

    attribute_map = {
        'advertiser_id': 'advertiser_id',
        'auto_bind_enabled': 'auto_bind_enabled',
        'auto_fix_enabled': 'auto_fix_enabled',
        'file_id': 'file_id',
        'file_name': 'file_name',
        'flaw_detect': 'flaw_detect',
        'is_third_party': 'is_third_party',
        'upload_type': 'upload_type',
        'video_file': 'video_file',
        'video_id': 'video_id',
        'video_signature': 'video_signature',
        'video_url': 'video_url'
    }

    def __init__(self, advertiser_id=None, auto_bind_enabled=None, auto_fix_enabled=None, file_id=None, file_name=None, flaw_detect=None, is_third_party=None, upload_type=None, video_file=None, video_id=None, video_signature=None, video_url=None):  # noqa: E501
        """AdUploadBody - a model defined in Swagger"""  # noqa: E501
        self._advertiser_id = None
        self._auto_bind_enabled = None
        self._auto_fix_enabled = None
        self._file_id = None
        self._file_name = None
        self._flaw_detect = None
        self._is_third_party = None
        self._upload_type = None
        self._video_file = None
        self._video_id = None
        self._video_signature = None
        self._video_url = None
        self.discriminator = None
        if advertiser_id is not None:
            self.advertiser_id = advertiser_id
        if auto_bind_enabled is not None:
            self.auto_bind_enabled = auto_bind_enabled
        if auto_fix_enabled is not None:
            self.auto_fix_enabled = auto_fix_enabled
        if file_id is not None:
            self.file_id = file_id
        if file_name is not None:
            self.file_name = file_name
        if flaw_detect is not None:
            self.flaw_detect = flaw_detect
        if is_third_party is not None:
            self.is_third_party = is_third_party
        if upload_type is not None:
            self.upload_type = upload_type
        if video_file is not None:
            self.video_file = video_file
        if video_id is not None:
            self.video_id = video_id
        if video_signature is not None:
            self.video_signature = video_signature
        if video_url is not None:
            self.video_url = video_url

    @property
    def advertiser_id(self):
        """Gets the advertiser_id of this AdUploadBody.  # noqa: E501

        Advertiser ID  # noqa: E501

        :return: The advertiser_id of this AdUploadBody.  # noqa: E501
        :rtype: str
        """
        return self._advertiser_id

    @advertiser_id.setter
    def advertiser_id(self, advertiser_id):
        """Sets the advertiser_id of this AdUploadBody.

        Advertiser ID  # noqa: E501

        :param advertiser_id: The advertiser_id of this AdUploadBody.  # noqa: E501
        :type: str
        """

        self._advertiser_id = advertiser_id

    @property
    def auto_bind_enabled(self):
        """Gets the auto_bind_enabled of this AdUploadBody.  # noqa: E501

        Whether to automatically upload the fixed video to your creative library. Default value : False. Valid only when flaw_detect = True and auto_fix_enabled = True.  # noqa: E501

        :return: The auto_bind_enabled of this AdUploadBody.  # noqa: E501
        :rtype: bool
        """
        return self._auto_bind_enabled

    @auto_bind_enabled.setter
    def auto_bind_enabled(self, auto_bind_enabled):
        """Sets the auto_bind_enabled of this AdUploadBody.

        Whether to automatically upload the fixed video to your creative library. Default value : False. Valid only when flaw_detect = True and auto_fix_enabled = True.  # noqa: E501

        :param auto_bind_enabled: The auto_bind_enabled of this AdUploadBody.  # noqa: E501
        :type: bool
        """

        self._auto_bind_enabled = auto_bind_enabled

    @property
    def auto_fix_enabled(self):
        """Gets the auto_fix_enabled of this AdUploadBody.  # noqa: E501

        Whether to automatically fix the detected issue. Default value : False. \\n If an issue is detected in your video and: \\n auto_fix_enabled = False, then well return an error message with flaw types indicated. \\n auto_fix_enabled =True, then well automatically fix all the issues and return fix_task_id and flaw_types.  # noqa: E501

        :return: The auto_fix_enabled of this AdUploadBody.  # noqa: E501
        :rtype: bool
        """
        return self._auto_fix_enabled

    @auto_fix_enabled.setter
    def auto_fix_enabled(self, auto_fix_enabled):
        """Sets the auto_fix_enabled of this AdUploadBody.

        Whether to automatically fix the detected issue. Default value : False. \\n If an issue is detected in your video and: \\n auto_fix_enabled = False, then well return an error message with flaw types indicated. \\n auto_fix_enabled =True, then well automatically fix all the issues and return fix_task_id and flaw_types.  # noqa: E501

        :param auto_fix_enabled: The auto_fix_enabled of this AdUploadBody.  # noqa: E501
        :type: bool
        """

        self._auto_fix_enabled = auto_fix_enabled

    @property
    def file_id(self):
        """Gets the file_id of this AdUploadBody.  # noqa: E501

        The file_id of the file that you want to upload. This field is for files that are uploaded to the file repository. You can get file_id via the Upload Files endpoints. This field is required when upload_type is UPLOAD_BY_FILE_ID.  # noqa: E501

        :return: The file_id of this AdUploadBody.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this AdUploadBody.

        The file_id of the file that you want to upload. This field is for files that are uploaded to the file repository. You can get file_id via the Upload Files endpoints. This field is required when upload_type is UPLOAD_BY_FILE_ID.  # noqa: E501

        :param file_id: The file_id of this AdUploadBody.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def file_name(self):
        """Gets the file_name of this AdUploadBody.  # noqa: E501

        Video name. Length limit: 1 - 100 characters. The default value is the file name or the last path of the URL. If the file name contains more than 100 characters, only the first 100 characters will be used. Note: Videos under the same advertiser_id cannot have duplicated file names. If you get an error about duplicated file names, please rename the files or append timestamps to the original file names (for example, in the format of _, and upload the videos again.  # noqa: E501

        :return: The file_name of this AdUploadBody.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this AdUploadBody.

        Video name. Length limit: 1 - 100 characters. The default value is the file name or the last path of the URL. If the file name contains more than 100 characters, only the first 100 characters will be used. Note: Videos under the same advertiser_id cannot have duplicated file names. If you get an error about duplicated file names, please rename the files or append timestamps to the original file names (for example, in the format of _, and upload the videos again.  # noqa: E501

        :param file_name: The file_name of this AdUploadBody.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def flaw_detect(self):
        """Gets the flaw_detect of this AdUploadBody.  # noqa: E501

        Whether to automatically detect an issue in your video. Default value is False.  # noqa: E501

        :return: The flaw_detect of this AdUploadBody.  # noqa: E501
        :rtype: bool
        """
        return self._flaw_detect

    @flaw_detect.setter
    def flaw_detect(self, flaw_detect):
        """Sets the flaw_detect of this AdUploadBody.

        Whether to automatically detect an issue in your video. Default value is False.  # noqa: E501

        :param flaw_detect: The flaw_detect of this AdUploadBody.  # noqa: E501
        :type: bool
        """

        self._flaw_detect = flaw_detect

    @property
    def is_third_party(self):
        """Gets the is_third_party of this AdUploadBody.  # noqa: E501

        The video is third party or not.  # noqa: E501

        :return: The is_third_party of this AdUploadBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_third_party

    @is_third_party.setter
    def is_third_party(self, is_third_party):
        """Sets the is_third_party of this AdUploadBody.

        The video is third party or not.  # noqa: E501

        :param is_third_party: The is_third_party of this AdUploadBody.  # noqa: E501
        :type: bool
        """

        self._is_third_party = is_third_party

    @property
    def upload_type(self):
        """Gets the upload_type of this AdUploadBody.  # noqa: E501

        Image upload method. Default value: UPLOAD_BY_FILE Enum values: UPLOAD_BY_FILE, UPLOAD_BY_URL, UPLOAD_BY_FILE_ID, UPLOAD_BY_VIDEO_ID.  # noqa: E501

        :return: The upload_type of this AdUploadBody.  # noqa: E501
        :rtype: str
        """
        return self._upload_type

    @upload_type.setter
    def upload_type(self, upload_type):
        """Sets the upload_type of this AdUploadBody.

        Image upload method. Default value: UPLOAD_BY_FILE Enum values: UPLOAD_BY_FILE, UPLOAD_BY_URL, UPLOAD_BY_FILE_ID, UPLOAD_BY_VIDEO_ID.  # noqa: E501

        :param upload_type: The upload_type of this AdUploadBody.  # noqa: E501
        :type: str
        """

        self._upload_type = upload_type

    @property
    def video_file(self):
        """Gets the video_file of this AdUploadBody.  # noqa: E501

        Video file. Required when upload_type is UPLOAD_BY_FILE.  # noqa: E501

        :return: The video_file of this AdUploadBody.  # noqa: E501
        :rtype: str
        """
        return self._video_file

    @video_file.setter
    def video_file(self, video_file):
        """Sets the video_file of this AdUploadBody.

        Video file. Required when upload_type is UPLOAD_BY_FILE.  # noqa: E501

        :param video_file: The video_file of this AdUploadBody.  # noqa: E501
        :type: str
        """

        self._video_file = video_file

    @property
    def video_id(self):
        """Gets the video_id of this AdUploadBody.  # noqa: E501

        Video ID. Required when upload_type is UPLOAD_BY_VIDEO_ID.  # noqa: E501

        :return: The video_id of this AdUploadBody.  # noqa: E501
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """Sets the video_id of this AdUploadBody.

        Video ID. Required when upload_type is UPLOAD_BY_VIDEO_ID.  # noqa: E501

        :param video_id: The video_id of this AdUploadBody.  # noqa: E501
        :type: str
        """

        self._video_id = video_id

    @property
    def video_signature(self):
        """Gets the video_signature of this AdUploadBody.  # noqa: E501

        Video MD5 (used for server verification). Required when upload_type is UPLOAD_BY_FILE.  # noqa: E501

        :return: The video_signature of this AdUploadBody.  # noqa: E501
        :rtype: str
        """
        return self._video_signature

    @video_signature.setter
    def video_signature(self, video_signature):
        """Sets the video_signature of this AdUploadBody.

        Video MD5 (used for server verification). Required when upload_type is UPLOAD_BY_FILE.  # noqa: E501

        :param video_signature: The video_signature of this AdUploadBody.  # noqa: E501
        :type: str
        """

        self._video_signature = video_signature

    @property
    def video_url(self):
        """Gets the video_url of this AdUploadBody.  # noqa: E501

        Video url address, like http://xxx.xxx. Required when upload_type is UPLOAD_BY_URL. \\n (1) File size: better within 10MB. \\n (2)Verification: we will verify the data if you set a Content-MD5 in the response header. \\n (3) Others: ratio, format, resolution and bitrate limitation is the same as video_file.  # noqa: E501

        :return: The video_url of this AdUploadBody.  # noqa: E501
        :rtype: str
        """
        return self._video_url

    @video_url.setter
    def video_url(self, video_url):
        """Sets the video_url of this AdUploadBody.

        Video url address, like http://xxx.xxx. Required when upload_type is UPLOAD_BY_URL. \\n (1) File size: better within 10MB. \\n (2)Verification: we will verify the data if you set a Content-MD5 in the response header. \\n (3) Others: ratio, format, resolution and bitrate limitation is the same as video_file.  # noqa: E501

        :param video_url: The video_url of this AdUploadBody.  # noqa: E501
        :type: str
        """

        self._video_url = video_url

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
        if issubclass(AdUploadBody, dict):
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
        if not isinstance(other, AdUploadBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other