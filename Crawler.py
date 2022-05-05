import requests
from bs4 import BeautifulSoup
# -*- coding: UTF-8 -*-


def download_content(url):
    """
    第一个函数，用来下载网页，返回网页内容
    参数 url 代表所要下载的网页网址。
    整体代码和之前类似
    """
    response = requests.get(url).text
    return response


# 第二个函数，将字符串内容保存到文件中
# 第一个参数为所要保存的文件名，第二个参数为要保存的字符串内容的变量
def save_to_file(filename, content):
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(content)


def create_doc_from_filename(filename):
    # 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象
    with open(filename, "r", encoding='utf-8') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, "lxml")
    return soup


def parse(soup):
    post_list = soup.find_all("div")
    for post in post_list:
        # link = post.find("a")
        # print(link.text.strip())
        # print(link["href"])
        print(post)


def main():
    # 下载报考指南的网页
    url = "https://www.baidu.com/"
    filename = "tips2.html"
    result = download_content(url)
    save_to_file(filename, result)
    soup = create_doc_from_filename(filename)
    parse(soup)


if __name__ == '__main__':
    main()
