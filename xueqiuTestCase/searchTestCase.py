import pytest, allure, yaml
from Page.APP import APP


@allure.epic("雪球App")
@allure.feature("搜索模块")
class Testsearch:
    @pytest.mark.parametrize("key,expValue", yaml.safe_load(open("../datapool/searchPool.yaml")),ids=["阿里巴巴股价搜索", '京东股价搜索'])
    @allure.story("搜索框搜索词汇")
    def test_search001(self, key ,expValue):
        # shiji = APP().start().Main().go_to_searchpage().search("alibaba").get_price()
        shiji = APP().start().Main().go_to_searchpage().search(key).get_price()
        assert float(expValue) > shiji
        # assert 200 > shiji
# if __name__=='__main__':
#     pytest.main()
#     Testsearch().test_search001()
