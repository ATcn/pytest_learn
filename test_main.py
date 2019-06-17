import pytest

if __name__ == '__main__':
    pytest.main() # 当前目录索引符合条件的文件
    # pytest.main("-q test_class.py")  # 指定测试文件，不在控制台打印
    # pytest.main("-s test_class.py")  # 指定测试文件，在控制台打印
    #pytest.main("D:/project_pro/pytest_learn")  # 指定测试目录