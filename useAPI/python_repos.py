# encoding: utf-8
# 对github社区中的数据利用pygal绘制直方图的例子
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("status code:", r.status_code)

response_dict = r.json()
print(response_dict.keys())
print("total respositorees:", response_dict['total_count'])
# 键items里存放的是每一个项目的信息，ropo_dicts将每一个项目（字典形式）存到列表中，即列表中嵌套字典的格式
repo_dicts = response_dict['items']
print('repositories returned：', len(repo_dicts))
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        # 该行代码之前没进行str转化时遇到一个错误，提示'NoneType' object has no attribute 'decode'
        # 因为有些项目的description为空。或者做一个判断，如果为空时将相应的值设置为 ''
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)
print(len(names))

# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.show_legend = False
my_config.x_label_rotation = 45
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
# chart.title = 'Most-Starred Python Projects on Github'
chart.title = 'Github上python类别星数最多的项目'
# 将names值作为x轴的值
chart.x_labels = names
# 使用pygal的add方法，将纵轴数据输入到图标中
chart.add('', plot_dicts)
chart.render_to_file('python_repos3.svg')

'''
# repo_dict为第一个仓库
repo_dict = repo_dicts[0]
# 输出第一个仓库中的有关信息
print('\nSelected information about first repository:')

print('\nKeys:', len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
'''


