import aiohttp
import asyncio
import json
import re
import sys
import os
import signal
import time
from urllib.parse import urlparse, parse_qs

# 禁用证书验证的全局设置
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

async def get_bilibili_video_info(bvid: str, page: int = 1):
    """获取B站视频信息"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': f'https://www.bilibili.com/video/{bvid}/?p={page}',
        }
        
        print(f"\n[1/3] 获取视频基本信息 (BV号: {bvid}, 分P: {page})...")
        async with aiohttp.ClientSession(headers=headers, connector=aiohttp.TCPConnector(ssl=False)) as session:
            video_info_url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}&p={page}"
            async with session.get(video_info_url) as response:
                if response.status != 200:
                    print(f"❌ 获取视频信息失败，状态码: {response.status}")
                    return None
                
                data = await response.json()
                if data.get('code') != 0:
                    print(f"❌ API错误: {data.get('message', '未知错误')}")
                    return None
                
                video_data = data.get('data', {})
                title = video_data.get('title', '未知视频')
                author = video_data.get('owner', {}).get('name', '未知UP主')
                duration = video_data.get('duration', 0)
                
                # 处理分P信息
                pages = video_data.get('pages', [])
                current_page_title = title
                page_cid = video_data.get('cid', 0)
                
                if pages and len(pages) > 1:
                    print(f"📋 视频共有 {len(pages)} 个分P")
                    # 查找指定分P
                    found = False
                    for p in pages:
                        if p.get('page') == page:
                            current_page_title = p.get('part', title)
                            page_cid = p.get('cid', page_cid)
                            found = True
                            break
                    
                    if not found:
                        print(f"⚠️ 未找到第 {page} 个分P，默认使用第1个分P")
                        page = 1
                        page_cid = pages[0].get('cid', page_cid) if pages else page_cid
                
                print(f"✅ 成功获取视频信息")
                print(f"   标题: {title}")
                if current_page_title != title:
                    print(f"   分P标题: {current_page_title}")
                print(f"   UP主: {author}")
                print(f"   时长: {duration}秒")
                print(f"   使用的CID: {page_cid}")
                
                return {
                    'title': title,
                    'current_page_title': current_page_title,
                    'author': author,
                    'duration': duration,
                    'cid': page_cid,
                    'bvid': bvid,
                    'page': page
                }
    except Exception as e:
        print(f"❌ 获取视频信息时发生错误: {e}")
        import traceback
        traceback.print_exc()
        return None

async def get_playable_urls(bvid: str, cid: int):
    """获取视频播放链接"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Referer': f'https://www.bilibili.com/video/{bvid}/',
        }
        
        print(f"\n[2/3] 获取播放链接 (BV号: {bvid}, CID: {cid})...")
        async with aiohttp.ClientSession(headers=headers, connector=aiohttp.TCPConnector(ssl=False)) as session:
            api_url = f"https://api.bilibili.com/x/player/playurl?bvid={bvid}&cid={cid}&qn=80&fnval=16&fourk=1"
            async with session.get(api_url) as response:
                if response.status != 200:
                    print(f"❌ 获取播放链接失败，状态码: {response.status}")
                    return None, None
                
                data = await response.json()
                if data.get('code') != 0:
                    print(f"❌ API错误: {data.get('message', '未知错误')}")
                    return None, None
                
                # 尝试从dash格式获取视频流
                dash = data.get('data', {}).get('dash', {})
                video_streams = dash.get('video', [])
                audio_streams = dash.get('audio', [])
                
                video_url = None
                audio_url = None
                
                if video_streams:
                    video_url = video_streams[0].get('baseUrl')
                    print(f"✅ 成功获取视频流链接")
                else:
                    # 尝试durl格式
                    durl = data.get('data', {}).get('durl', [])
                    if durl:
                        video_url = durl[0].get('url')
                        print(f"✅ 成功获取视频流链接 (durl格式)")
                    else:
                        print("❌ 未找到视频流")
                
                if audio_streams:
                    audio_url = audio_streams[0].get('baseUrl')
                    print(f"✅ 成功获取音频流链接")
                
                return video_url, audio_url
    except Exception as e:
        print(f"❌ 获取播放链接时发生错误: {e}")
        import traceback
        traceback.print_exc()
        return None, None

async def download_file(url, filename, headers=None):
    """下载文件并显示进度"""
    try:
        print(f"\n[3/3] 开始下载视频: {filename}")
        
        # 添加防缓存的时间戳参数
        timestamp = int(time.time())
        if '?' in url:
            url += f"&t={timestamp}"
        else:
            url += f"?t={timestamp}"
        
        # 确保headers不为None
        if headers is None:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
                'Referer': 'https://www.bilibili.com/',
            }
        
        async with aiohttp.ClientSession(headers=headers, connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.get(url, allow_redirects=True) as response:
                if response.status != 200:
                    print(f"❌ 下载失败，状态码: {response.status}")
                    return False
                
                total_size = int(response.headers.get('content-length', 0))
                downloaded_size = 0
                
                # 获取文件扩展名
                content_type = response.headers.get('content-type', '')
                ext = 'mp4'
                if 'video' in content_type:
                    ext = content_type.split('/')[-1] if '/' in content_type else 'mp4'
                
                # 确保文件名安全
                safe_filename = re.sub(r'[\\/:*?"<>|]', '_', filename)
                if not safe_filename.endswith(f'.{ext}'):
                    safe_filename += f'.{ext}'
                
                # 创建downloads目录
                os.makedirs('downloads', exist_ok=True)
                filepath = os.path.join('downloads', safe_filename)
                
                print(f"📥 保存路径: {filepath}")
                print(f"📊 文件大小: {format_size(total_size)}")
                
                start_time = time.time()
                with open(filepath, 'wb') as f:
                    async for chunk in response.content.iter_chunked(8192):
                        if not chunk:  # 确保chunk不为空
                            continue
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        
                        # 显示下载进度
                        if total_size > 0:
                            progress = (downloaded_size / total_size) * 100
                            # 计算下载速度
                            elapsed_time = time.time() - start_time
                            if elapsed_time > 0:
                                speed = downloaded_size / elapsed_time
                                # 计算剩余时间
                                remaining_time = (total_size - downloaded_size) / speed if speed > 0 else 0
                                
                                # 修复语法错误，使用正确的字符串格式化
                                progress_bar = "=" * int(progress/5) + " " * (20 - int(progress/5))
                                progress_str = f"\r[{progress_bar}] {progress:.1f}% {format_size(speed)}/s 剩余{int(remaining_time)}秒"
                                sys.stdout.write(progress_str)
                                sys.stdout.flush()
                
                sys.stdout.write('\n')
                print(f"✅ 下载完成: {filepath}")
                print(f"⚡ 总下载时间: {time.time() - start_time:.2f}秒")
                return True
    except Exception as e:
        print(f"❌ 下载时发生错误: {e}")
        import traceback
        traceback.print_exc()
        return False

def format_size(size_bytes):
    """格式化文件大小"""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"

def parse_bilibili_url(url: str) -> tuple:
    """解析B站URL，提取BV号和分P信息"""
    print(f"\n🔍 解析B站URL: {url}")
    
    # 匹配BV号的正则表达式
    bv_pattern = r'(BV\w+)'
    
    # 尝试直接从URL中提取BV号
    match = re.search(bv_pattern, url)
    if match:
        bvid = match.group(1)
        
        # 解析URL参数，获取分P信息
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        
        # 健壮地处理p参数
        page = 1
        if 'p' in query_params:
            try:
                page = int(query_params['p'][0])
                if page < 1:
                    page = 1
            except ValueError:
                page = 1
        
        print(f"✅ 解析成功 - BV号: {bvid}, 分P: {page}")
        return bvid, page
    
    print("❌ 未找到BV号")
    return None, 1

def find_and_kill_process_on_port(port):
    """查找并杀死占用指定端口的进程（仅限macOS）"""
    try:
        import subprocess
        result = subprocess.run(['lsof', '-i', f':{port}'], capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            print(f"⚠️ 发现占用端口 {port} 的进程:")
            # 提取进程ID
            lines = result.stdout.split('\n')[1:]  # 跳过标题行
            pids = []
            for line in lines:
                if line.strip():
                    parts = line.split()
                    if len(parts) >= 2:
                        pid = parts[1]
                        pids.append(pid)
                        
                        try:
                            print(f"🛑 尝试终止进程 {pid}...")
                            os.kill(int(pid), signal.SIGTERM)
                            print(f"✅ 进程 {pid} 已发送终止信号")
                        except Exception as e:
                            print(f"❌ 终止进程 {pid} 失败: {e}")
            
            return pids
        else:
            print(f"✅ 端口 {port} 未被占用")
            return []
    except Exception as e:
        print(f"❌ 查找占用端口的进程时出错: {e}")
        return []

async def main():
    # 清理可能残留的代理服务器进程
    print("🧹 清理可能残留的进程...")
    for port in [8888, 8000, 9000]:
        find_and_kill_process_on_port(port)
    await asyncio.sleep(1)  # 等待进程终止
    
    # 尝试从命令行参数获取URL
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        # 让用户输入B站URL
        print("\n🚀 欢迎使用B站视频下载工具！")
        print("📋 请粘贴B站视频的完整URL（例如：https://www.bilibili.com/video/BV1zWagzbEZ9?vd_source=xxx&p=8）")
        url = input("🔗 B站URL: ")
    
    # 解析URL获取BV号和分P信息
    bvid, page = parse_bilibili_url(url)
    
    if not bvid:
        print("❌ 无法从URL中提取BV号，请检查URL格式是否正确")
        print("📝 正确格式示例: https://www.bilibili.com/video/BV1zWagzbEZ9")
        return
    
    # 获取视频信息
    video_info = await get_bilibili_video_info(bvid, page)
    if not video_info:
        print("❌ 获取视频信息失败，无法继续")
        return
    
    # 获取播放链接
    video_url, audio_url = await get_playable_urls(bvid, video_info['cid'])
    
    if not video_url:
        print("❌ 未能获取到视频播放链接")
        print("💡 提示：B站可能更新了API或增加了访问限制")
        return
    
    # 准备下载文件名
    title = video_info['title']
    if video_info['current_page_title'] != title and video_info['page'] > 1:
        filename = f"{title} - 第{video_info['page']}集 - {video_info['current_page_title']}"
    else:
        filename = title
    
    # 添加时间戳避免文件名冲突
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"{filename}_{timestamp}"
    
    # 下载视频
    success = await download_file(video_url, filename)
    
    if success:
        print("\n🎉 视频下载成功！")
        print("📁 文件保存在: downloads/ 目录下")
        print("💡 提示：如果需要下载其他分P或视频，请重新运行脚本")
    else:
        print("❌ 视频下载失败")

if __name__ == "__main__":
    # 处理Ctrl+C信号
    def signal_handler(sig, frame):
        print('\n🛑 收到停止信号，正在清理资源...')
        sys.exit(0)
    
    # 注册信号处理函数
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\n🛑 程序已被用户中断')
    except Exception as e:
        print(f'\n❌ 程序运行出错: {e}')
        import traceback
        traceback.print_exc()