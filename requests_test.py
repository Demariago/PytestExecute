import requests

zhihu_url = "https://www.zhihu.com/api/v3/feed/topstory/recommend?action=down&ad_interval=-10&after_id=23&desktop=true&end_offset=26&page_number=5&session_token=38d48cd154b9bc6913228aaea22abbb2"

HEADERS = {
    "Host": "www.zhihu.com",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "x-api-version": "3.0.53",
    "x-zse-96": "2.0_CoOuc=5Sr=Ks4B34HDUh8dgNWySgK4oWgmKXttZiGIGxTP7k6ToIhS8RcJGJ83bW",
    "sec-ch-ua-mobile": "?0",
    "x-requested-with": "fetch",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZY0Y0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIoLVqr4gxrRPOI0cY7HL8qun9g93mFukyigcmebS_FwOYPRP0E4rZUrN9DDom3hnynAUMnAVPF_PhaueTF4NGYvHYzuwOKiHqk0SmhUOxkuCOqgXB3gVYprS83qYyd9gOHugLqUXx_JSTVMpyJ4OYu9XsJ6L8GGpKTrr8rMwscDo1ZgoVBbXBpgY8y9cGYLOL_vrMrvHOQ8X9-cO_pweLXhSfc0tM7BLy0qwKJ0V_NwVCqBcVLh39JwgmjJN_yvO0Vg_zoqVGwgL_iBCMyJXK9U38sqxmv9OGaBL8k4cfHDe9YQXGLcwqgwHK6q3qjuoGxUO9bwLmAgp9TBOqEDg_x9V8bwYZsJxYrvp1r4gsYBH0drHKQAxB2w2s",
    "x-zse-93": "101_3_3.0",
    "Accept": "*/*",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.zhihu.com/",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": "_zap=ef212d1a-1e15-4846-b0e1-6d14aef5564c; d_c0=zPTTlDLWtBqPTqLPmuv4hvlgJfiNuYganE4=|1751592344; __snaker__id=nzeZ6fOCTMJZ4EtJ; q_c1=54af2e9903f445f0a256a033c8e8419a|1751592367000|1751592367000; edu_user_uuid=edu-v1|1f66e83d-1b2c-4144-92ab-9dce647949a3; _xsrf=3ynMTociijrfnR44nNbr10vbiB1HBYgP; _qimei_uuid42=1971112131f100b4c5815192430adab9f63d34a799; _qimei_i_3=54d973d3c30b06d8c8c6fa3358d726b5f3eda1a4465d07d3b2d9795872c22868353232973989e2a4a1f4; _qimei_h38=; _qimei_fingerprint=08cd366a4bc3684d38d31938072a0d34; _qimei_i_1=6ce47efbea03; z_c0=2|1:0|10:1754622227|4:z_c0|80:MS4xUXBZckFBQUFBQUFtQUFBQVlBSlZUYUpXZldsVTQzQ1gtU1BoMUxrMjNHWHVNRjdnRndPODlBPT0=|fd5b41d219c853a61e94af52b34b591acfed9a044964bc8df511c62da53fc604; HMACCOUNT=92AE88D6E09BB7E9; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1754546053,1754961961; __zse_ck=004_G3p1jj1NoMdF5cXT4vAWG7H9usmhq=n8AU8v/wXI5ITFkYxR2R4H=SJ=CrzwsnwyDoUadmyhrJQS2A1pFMkMp72JKizB3VLTWQA=6bhLhAcJ8YD4oU0=zGvZbsdomtaA-rw3pvAA5+O1FIacXCSTG1mxvYprFmRbVlq7B6oDb3tnZzDUM4HctxHwCvWXEe3Rv1muLdVr2aipDryVK1EsKWUEl28VXPxjC2l5gTVrEG1Jjmw14foskflH2XvCLSxd2; SESSIONID=o669uZrVIE6swPRetwJy9zLqMqYXYvfYrogZJDMXwxc; JOID=UVgWB0LJQGpWQf9iWabque55Lt9DpXVbYj6mEwiKBl8iO6UzPwy8zzlI_2ZTaf6RkjWfWVw7ERYyY96bBgEP-sI=; osd=W1odBkzDQmFXT_VgUqfks-xyL9FJp35abDSkGAmEDF0pOqs5PQe9wTNK9GddY_yakzuVW1c6HxwwaN-VDAME-8w=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1756362957; tst=r; BEC=b7b0f394f3fd074c6bdd2ebbdd598b4e",
    "Connection": "close"
}

try:
    response = requests.get(zhihu_url, headers=HEADERS)
    response.raise_for_status()  # 检查HTTP错误

    # 直接解析并打印JSON
    json_data = response.json()
    print(json_data)

except requests.exceptions.RequestException as e:
    print(f"请求错误: {e}")
except ValueError as e:
    print(f"JSON解析错误: {e}")
