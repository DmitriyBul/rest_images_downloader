from rest_framework import serializers


def file_validator(file):
    """
    file validator
    check max file size allowed for file
    :param file:
    :return:
    """
    max_file_size = 200000
    if file.size > max_file_size:
        raise serializers.ValidationError(('Max file size is {} and your file size is {}'.format(max_file_size, file.size)))


class FileSerializer(serializers.Serializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False, validators=[file_validator])
