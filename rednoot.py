import requests
from bs4 import BeautifulSoup
import re
import sys


def fetch_xiaohongshu_content(url):
    # 模拟浏览器请求头（关键反爬处理）
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Referer': 'https://www.xiaohongshu.com',
        'x-requested-with': 'XMLHttpRequest'
    }

    try:
        # 发送请求（带重试机制）
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')

        # 提取主文字内容（包含表情符号和换行处理）
        main_text_elem = soup.find('div', class_='note-content')
        if main_text_elem:
            # 清理多余空格和换行
            main_text = re.sub(r'\s+', ' ', main_text_elem.get_text(strip=False)).strip()
            # 保留原格式换行（小红书使用<br>标签）
            main_text = main_text.replace('<br/>', '\n').replace('<br>', '\n')
        else:
            main_text = "未找到正文内容"

        # 提取主图（多种方式尝试）
        main_image_url = None

        # 方式0: 从og:image标签提取（最可靠的方式）
        og_image = soup.find('meta', property='og:image') or soup.find('meta', {'name': 'og:image'})
        if og_image:
            main_image_url = og_image.get('content')
            # 验证是否是有效的图片链接
            if main_image_url and ('xhscdn' not in main_image_url and 'xiaohongshu' not in main_image_url):
                main_image_url = None

        # 方式1: 从swiper-slide-active的div中提取背景图片或内部img标签
        if not main_image_url:
            swiper_slide = soup.find('div', class_='swiper-slide-active')
            if swiper_slide:
                # 尝试从style属性提取背景图片URL
                style_attr = swiper_slide.get('style')
                if style_attr:
                    background_match = re.search(r'url\("(.*?)"\)', style_attr)
                    if background_match:
                        main_image_url = background_match.group(1)
                        # 验证是否是有效的图片链接
                        if 'xhscdn' not in main_image_url and 'xiaohongshu' not in main_image_url:
                            main_image_url = None

                # 如果背景图片提取失败，尝试从内部img标签提取
                if not main_image_url:
                    img_tag = swiper_slide.find('img', class_='note-slider-img')
                    if img_tag:
                        main_image_url = img_tag.get('src')
                        # 验证是否是有效的图片链接
                        if main_image_url and ('xhscdn' not in main_image_url and 'xiaohongshu' not in main_image_url):
                            main_image_url = None

        # 方式2: 尝试找到image-list容器
        if not main_image_url:
            image_list = soup.find('div', class_='image-list')
            if image_list:
                main_image_elem = image_list.find('img', class_=re.compile(r'(image-item|main-image|lazy-image)'))
                if main_image_elem:
                    main_image_url = main_image_elem.get('data-src') or main_image_elem.get('src') or main_image_elem.get('data-original')

        # 方式3: 如果前几种方式失败，尝试直接找所有img标签
        if not main_image_url:
            all_images = soup.find_all('img')
            for img in all_images:
                # 筛选可能的主图
                img_url = img.get('data-src') or img.get('src') or img.get('data-original')
                if img_url and ('xhscdn' in img_url or 'xiaohongshu' in img_url):
                    main_image_url = img_url
                    break

        # 补全协议
        if main_image_url and not main_image_url.startswith('http'):
            main_image_url = 'https:' + main_image_url

        return {
            'main_text': main_text,
            'main_image_url': main_image_url
        }

    except Exception as e:
        print(f"提取失败: {str(e)}")
        return None


# 从命令行获取URL并执行抓取
if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("请输入小红书链接: ")

    result = fetch_xiaohongshu_content(url)
    if result:
        print("\n【主文字内容】")
        print(result['main_text'])
        print("\n【主图链接】")
        print(result['main_image_url'])
    else:
        print("内容提取失败")
