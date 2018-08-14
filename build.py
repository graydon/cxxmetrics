from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(test_folder="test")
    builder.add_common_builds()
    builder.run()
