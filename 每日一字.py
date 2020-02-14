import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery
import csv
import json
import time
import os
#创建csv文件
csvf = open('知乎每天一练.csv','a+')
writer = csv.writer(csvf)
writer.writerow(('title','url'))
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
urlall = 'https://zhuanlan.zhihu.com/api/columns/c_1040280910897201152/articles?include=data%5B%2A%5D.admin_closed_comment%2Ccomment_count%2Csuggest_edit%2Cis_title_image_full_screen%2Ccan_comment%2Cupvoted_followees%2Ccan_open_tipjar%2Ccan_tip%2Cvoteup_count%2Cvoting%2Ctopics%2Creview_info%2Cauthor.is_following%2Cis_labeled%2Clabel_info&limit=10&offset={0}'



def file_video(title):
    '''csv文件判断'''
    with open('知乎每天一练.csv','r') as file: 
        f = file.read()
        if title in f:
            print('文件已存在')
            return  'Ture'
        else :
            print('文件不存在')
            return  'Flase'
def file_name(title):
    '''视频文件判断'''
    name = os.listdir()
    #print(name)
    #文件是否存在
    exists = os.path.exists(title+'.mp4')
    print(exists)
    title = title + '.mp4'
    if title in name:
        #文件大小
        size = os.path.getsize(title)
        f = (int(size)/1024**2)
        print('文件已存在：'+'%.2f'%f + 'M')
        return  'Ture'
    else:
        print('文件不存在')
        return  'Flase'


#file_video()  
def video_download(url,title):
    response = requests.get(url,headers=headers).text
    doc = PyQuery(response)
    #<div class="RichText ztext Post-RichText __reader_view_article_wrap_786807993615199__"><p>知乎里我添加了一个新专栏，是关于硬笔行书的。</p><p><br>行书是介于楷书与草书之间的一种书体，它不像草书那样潦草，也不像楷书那样规矩板正。它就好比正在行走的人，既有动感，速度也不会很快。草书虽然潇洒，楷书虽然俊美，但都不利于日常书写与交流。行走的汉字才是最适合在日常生活中书写的。</p><p><br>这个系列每期会写一个单字，有单字静图、动图还有书写视频。</p><p><br>对本人硬笔行书感兴趣的书友可以关注。有问题的也欢迎在评论区与我交流。我也会加倍勤奋争取把这个系列做到日更，争取让更多硬笔爱好者每天都能学到新字。</p><hr><p><b>这是本系列第 192 次更新。</b></p><div><div class="RichText-video" data-za-detail-view-path-module="VideoItem" data-za-extra-module="{&quot;card&quot;:{&quot;content&quot;:{&quot;type&quot;:&quot;Video&quot;,&quot;sub_type&quot;:&quot;SelfHosted&quot;,&quot;video_id&quot;:&quot;1161414208179904512&quot;,&quot;is_playable&quot;:true}}}"><div class="VideoCard VideoCard--interactive"><div class="VideoCard-layout"><div class="VideoCard-video"><div class="VideoCard-video-content"><div class="VideoCard-player"><iframe frameborder="0" allowfullscreen="" src="https://www.zhihu.com/video/1161414208179904512?autoplay=false&amp;useMSE="></iframe></div></div></div><div class="VideoCard-content"><div class="VideoCard-title">硬笔行书每日一字 · 可</div></div></div><div class="VideoCard-mask"></div></div></div></div><figure data-size="normal"><noscript><img src="https://pic3.zhimg.com/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_b.jpg" data-caption="" data-size="normal" data-rawwidth="2110" data-rawheight="2110" class="origin_image zh-lightbox-thumb" width="2110" data-original="https://pic3.zhimg.com/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_r.jpg"/></noscript><img src="https://pic3.zhimg.com/80/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_hd.jpg" data-caption="" data-size="normal" data-rawwidth="2110" data-rawheight="2110" class="origin_image zh-lightbox-thumb lazy" width="2110" data-original="https://pic3.zhimg.com/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_r.jpg" data-actualsrc="https://pic3.zhimg.com/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_b.jpg" data-lazy-status="ok"></figure><figure data-size="normal"><noscript><img src="https://pic2.zhimg.com/v2-4c94b4f2c6ddadaecead094ee1042b09_b.gif" data-caption="" data-size="normal" data-rawwidth="400" data-rawheight="400" data-thumbnail="https://pic2.zhimg.com/v2-4c94b4f2c6ddadaecead094ee1042b09_b.jpg" class="content_image" width="400"/></noscript><div class="RichText-gifPlaceholder"><div class="GifPlayer" data-size="normal" data-za-detail-view-path-module="GifItem"><img class="ztext-gif" role="presentation" src="https://pic2.zhimg.com/v2-4c94b4f2c6ddadaecead094ee1042b09_b.jpg" data-thumbnail="https://pic2.zhimg.com/v2-4c94b4f2c6ddadaecead094ee1042b09_b.jpg" data-size="normal"><svg width="60" height="60" viewBox="0 0 60 60" class="GifPlayer-icon"><g fill="none" fill-rule="evenodd"><ellipse fill="#000" opacity="0.45" cx="30" cy="30" rx="30" ry="30"></ellipse><ellipse stroke="#FFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="4,1,4" cx="30" cy="30" rx="26" ry="26"></ellipse><svg x="16" y="18.5" class="GifPlayer-icon"><path d="M12.842 12.981V11.4H7.64v1.653h3.27v.272c-.018 1.881-1.442 3.147-3.516 3.147-2.382 0-3.876-1.846-3.876-4.834 0-2.936 1.485-4.79 3.832-4.79 1.732 0 2.936.835 3.428 2.364h1.977c-.43-2.566-2.522-4.201-5.405-4.201-3.55 0-5.845 2.601-5.845 6.644 0 4.096 2.268 6.654 5.863 6.654 3.322 0 5.475-2.083 5.475-5.327zM17.518 18V5.317H15.55V18h1.97zm5.142 0v-5.256h5.449v-1.74h-5.45V7.11h5.95V5.317h-7.918V18h1.969z" fill="#fff"></path></svg></g></svg></div></div></figure><p></p></div>V<div class="RichText ztext Post-RichText __reader_view_article_wrap_786807993615199__"><p>知乎里我添加了一个新专栏，是关于硬笔行书的。</p><p><br>行书是介于楷书与草书之间的一种书体，它不像草书那样潦草，也不像楷书那样规矩板正。它就好比正在行走的人，既有动感，速度也不会很快。草书虽然潇洒，楷书虽然俊美，但都不利于日常书写与交流。行走的汉字才是最适合在日常生活中书写的。</p><p><br>这个系列每期会写一个单字，有单字静图、动图还有书写视频。</p><p><br>对本人硬笔行书感兴趣的书友可以关注。有问题的也欢迎在评论区与我交流。我也会加倍勤奋争取把这个系列做到日更，争取让更多硬笔爱好者每天都能学到新字。</p><hr><p><b>这是本系列第 192 次更新。</b></p><div><div class="RichText-video" data-za-detail-view-path-module="VideoItem" data-za-extra-module="{&quot;card&quot;:{&quot;content&quot;:{&quot;type&quot;:&quot;Video&quot;,&quot;sub_type&quot;:&quot;SelfHosted&quot;,&quot;video_id&quot;:&quot;1161414208179904512&quot;,&quot;is_playable&quot;:true}}}"><div class="VideoCard VideoCard--interactive"><div class="VideoCard-layout"><div class="VideoCard-video"><div class="VideoCard-video-content"><div class="VideoCard-player"><iframe frameborder="0" allowfullscreen="" src="https://www.zhihu.com/video/1161414208179904512?autoplay=false&amp;useMSE="></iframe></div></div></div><div class="VideoCard-content"><div class="VideoCard-title">硬笔行书每日一字 · 可</div></div></div><div class="VideoCard-mask"></div></div></div></div><figure data-size="normal"><noscript><img src="https://pic3.zhimg.com/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_b.jpg" data-caption="" data-size="normal" data-rawwidth="2110" data-rawheight="2110" class="origin_image zh-lightbox-thumb" width="2110" data-original="https://pic3.zhimg.com/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_r.jpg"/></noscript><img src="https://pic3.zhimg.com/80/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_hd.jpg" data-caption="" data-size="normal" data-rawwidth="2110" data-rawheight="2110" class="origin_image zh-lightbox-thumb lazy" width="2110" data-original="https://pic3.zhimg.com/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_r.jpg" data-actualsrc="https://pic3.zhimg.com/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_b.jpg" data-lazy-status="ok"></figure><figure data-size="normal"><noscript><img src="https://pic2.zhimg.com/v2-4c94b4f2c6ddadaecead094ee1042b09_b.gif" data-caption="" data-size="normal" data-rawwidth="400" data-rawheight="400" data-thumbnail="https://pic2.zhimg.com/v2-4c94b4f2c6ddadaecead094ee1042b09_b.jpg" class="content_image" width="400"/></noscript><div class="RichText-gifPlaceholder"><div class="GifPlayer" data-size="normal" data-za-detail-view-path-module="GifItem"><img class="ztext-gif" role="presentation" src="https://pic2.zhimg.com/v2-4c94b4f2c6ddadaecead094ee1042b09_b.jpg" data-thumbnail="https://pic2.zhimg.com/v2-4c94b4f2c6ddadaecead094ee1042b09_b.jpg" data-size="normal"><svg width="60" height="60" viewBox="0 0 60 60" class="GifPlayer-icon"><g fill="none" fill-rule="evenodd"><ellipse fill="#000" opacity="0.45" cx="30" cy="30" rx="30" ry="30"></ellipse><ellipse stroke="#FFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="4,1,4" cx="30" cy="30" rx="26" ry="26"></ellipse><svg x="16" y="18.5" class="GifPlayer-icon"><path d="M12.842 12.981V11.4H7.64v1.653h3.27v.272c-.018 1.881-1.442 3.147-3.516 3.147-2.382 0-3.876-1.846-3.876-4.834 0-2.936 1.485-4.79 3.832-4.79 1.732 0 2.936.835 3.428 2.364h1.977c-.43-2.566-2.522-4.201-5.405-4.201-3.55 0-5.845 2.601-5.845 6.644 0 4.096 2.268 6.654 5.863 6.654 3.322 0 5.475-2.083 5.475-5.327zM17.518 18V5.317H15.55V18h1.97zm5.142 0v-5.256h5.449v-1.74h-5.45V7.11h5.95V5.317h-7.918V18h1.969z" fill="#fff"></path></svg></g></svg></div></div></figure><p></p></div>
    #<div class="Post-RichTextContainer"><div class="RichText ztext Post-RichText __reader_view_article_wrap_786807993615199__"><p>知乎里我添加了一个新专栏，是关于硬笔行书的。</p><p><br>行书是介于楷书与草书之间的一种书体，它不像草书那样潦草，也不像楷书那样规矩板正。它就好比正在行走的人，既有动感，速度也不会很快。草书虽然潇洒，楷书虽然俊美，但都不利于日常书写与交流。行走的汉字才是最适合在日常生活中书写的。</p><p><br>这个系列每期会写一个单字，有单字静图、动图还有书写视频。</p><p><br>对本人硬笔行书感兴趣的书友可以关注。有问题的也欢迎在评论区与我交流。我也会加倍勤奋争取把这个系列做到日更，争取让更多硬笔爱好者每天都能学到新字。</p><hr><p><b>这是本系列第 192 次更新。</b></p><div><div class="RichText-video" data-za-detail-view-path-module="VideoItem" data-za-extra-module="{&quot;card&quot;:{&quot;content&quot;:{&quot;type&quot;:&quot;Video&quot;,&quot;sub_type&quot;:&quot;SelfHosted&quot;,&quot;video_id&quot;:&quot;1161414208179904512&quot;,&quot;is_playable&quot;:true}}}"><div class="VideoCard VideoCard--interactive"><div class="VideoCard-layout"><div class="VideoCard-video"><div class="VideoCard-video-content"><div class="VideoCard-player"><iframe frameborder="0" allowfullscreen="" src="https://www.zhihu.com/video/1161414208179904512?autoplay=false&amp;useMSE="></iframe></div></div></div><div class="VideoCard-content"><div class="VideoCard-title">硬笔行书每日一字 · 可</div></div></div><div class="VideoCard-mask"></div></div></div></div><figure data-size="normal"><noscript><img src="https://pic3.zhimg.com/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_b.jpg" data-caption="" data-size="normal" data-rawwidth="2110" data-rawheight="2110" class="origin_image zh-lightbox-thumb" width="2110" data-original="https://pic3.zhimg.com/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_r.jpg"/></noscript><img src="https://pic3.zhimg.com/80/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_hd.jpg" data-caption="" data-size="normal" data-rawwidth="2110" data-rawheight="2110" class="origin_image zh-lightbox-thumb lazy" width="2110" data-original="https://pic3.zhimg.com/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_r.jpg" data-actualsrc="https://pic3.zhimg.com/v2-0b5f6fb5b9905f4e89a3081b9c5c4ade_b.jpg" data-lazy-status="ok"></figure><figure data-size="normal"><noscript><img src="https://pic2.zhimg.com/v2-4c94b4f2c6ddadaecead094ee1042b09_b.gif" data-caption="" data-size="normal" data-rawwidth="400" data-rawheight="400" data-thumbnail="https://pic2.zhimg.com/v2-4c94b4f2c6ddadaecead094ee1042b09_b.jpg" class="content_image" width="400"/></noscript><div class="RichText-gifPlaceholder"><div class="GifPlayer" data-size="normal" data-za-detail-view-path-module="GifItem"><img class="ztext-gif" role="presentation" src="https://pic2.zhimg.com/v2-4c94b4f2c6ddadaecead094ee1042b09_b.jpg" data-thumbnail="https://pic2.zhimg.com/v2-4c94b4f2c6ddadaecead094ee1042b09_b.jpg" data-size="normal"><svg width="60" height="60" viewBox="0 0 60 60" class="GifPlayer-icon"><g fill="none" fill-rule="evenodd"><ellipse fill="#000" opacity="0.45" cx="30" cy="30" rx="30" ry="30"></ellipse><ellipse stroke="#FFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="4,1,4" cx="30" cy="30" rx="26" ry="26"></ellipse><svg x="16" y="18.5" class="GifPlayer-icon"><path d="M12.842 12.981V11.4H7.64v1.653h3.27v.272c-.018 1.881-1.442 3.147-3.516 3.147-2.382 0-3.876-1.846-3.876-4.834 0-2.936 1.485-4.79 3.832-4.79 1.732 0 2.936.835 3.428 2.364h1.977c-.43-2.566-2.522-4.201-5.405-4.201-3.55 0-5.845 2.601-5.845 6.644 0 4.096 2.268 6.654 5.863 6.654 3.322 0 5.475-2.083 5.475-5.327zM17.518 18V5.317H15.55V18h1.97zm5.142 0v-5.256h5.449v-1.74h-5.45V7.11h5.95V5.317h-7.918V18h1.969z" fill="#fff"></path></svg></g></svg></div></div></figure><p></p></div></div>
    for item in doc.items('#root .Post-RichTextContainer div'):
        #<span class="z-ico-video"/>https://www.zhihu.com/video/1161414208179904512</span></span>
        #for url in item.items('.z-ico-video '):
        #<span class="z-ico-video"/>**************27****28******和等于55
        videourl = str(item.find('a span .z-ico-video'))[55:]
        #print(videourl)
        #获取视频链接的存储json文件链接
        videos = 'https://lens.zhihu.com/api/v4/videos/'+videourl
        resp = requests.get(videos,headers=headers).text
        urls = json.loads(resp)
        #获取视频链接
        videourl = urls['playlist']['LD']['play_url']
        print(videourl)
        videourl = videourl.replace('&','&').replace(' ','')
        #下载视频
        videofile = requests.get(videourl,headers=headers)
        with open(title+'.mp4','wb') as file:
            file.write(videofile.content)
        print('完成下载：'+title+'.mp4')
    time.sleep(1)





def url_all(urlall):
    
    '''获取所有视频目录主页面'''
    for page in range(0,200,10):
        #for循环所有链接
        url = urlall.format(page)
        #print(url)
        #获取链接网址内所有视频主页面
        data = requests.get(url, headers=headers).text
        #print(data)
        dicts = json.loads(data)
        data = dicts['data']
        for i in data:
            #获取视频主页面标题链接
            title = i['title']
            url = i['url']
            print(title)
            writer.writerow((title, url))
            print(url)
            #解析视频主页链接
            if '硬笔行书每日一字' in title:
                if file_name(title) == 'Ture':
                    print("*"*50)
                else:
                    try:
                        video_download(url,title)
                    except:
                        continue
               
                
url_all(urlall)
csvf.close()




'''
https://vdn1.vzuu.com/LD/7e3dbc0c-c287-11e9-9a80-0a580a40a95a.mp4?disable_local_cache=1&bu=com&expiration=1573124439&auth_key=1573124439-0-0-fbb0ba1d802e5f8506d1f048b33ee36c&f=mp4&v=hw
https://vdn1.vzuu.com/LD/7e3dbc0c-c287-11e9-9a80-0a580a40a95a.mp4?disable_local_cache=1&bu=com&expiration=1573124344&auth_key=1573124344-0-0-1cb5ce07702eefc776ce8b7891f53f0d&f=mp4&v=hw

'''
#https://lens.zhihu.com/api/v4/videos/1146906806734413824
#https://lens.zhihu.com/api/v4/videos/1175526514589884416
#https://lens.zhihu.com/api/v4/videos/1109336814997041152
