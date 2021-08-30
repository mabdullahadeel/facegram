class SerializerVersionMixin:
    version_map = None

    def _get_serializer_class(self, version):
        if version not in self.version_map:
            raise Exception(f'version_map is not provided for {version}')
        return self.version_map[version]


    def get_serializer_class(self):
        if not self.version_map:
            raise Exception(f'version_map is not provided for {self.__class__.__name__}')
        
        version = self.request.version
        print(version)

        return self._get_serializer_class(version)