from bs4 import BeautifulSoup


# 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象
def create_doc_from_filename(filename):
    with open(filename, "r", encoding='utf-8') as f:
        html_content = f.read()
        soup = BeautifulSoup(html_content, "lxml")
    return soup


def parse(soup):
    post_list = soup.find_all("li", class_="menu-item")
    print(post_list)
    for post in post_list:
        link = post.find("a")
        print(link.text.strip())
        print(link["href"])


def main():
    filename = "tips1.html"
    soup = create_doc_from_filename(filename)
    parse(soup)


if __name__ == '__main__':
    main()
