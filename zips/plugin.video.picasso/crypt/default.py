#V 0.0.1
import xbmc,xbmcaddon,xbmcgui,xbmcplugin,requests,urllib,urllib2,json,os,re,sys,datetime,urlresolver,random,liveresolver,base64
from resources.lib.common_addon import Addon
from HTMLParser import HTMLParser
from metahandler import metahandlers
import requests
import downloader as Get_Files
import extract
import time

addon_id        = 'plugin.video.manstuff'
addon           = Addon(addon_id, sys.argv)
selfAddon       = xbmcaddon.Addon(id=addon_id)
addonInfo       = xbmcaddon.Addon().getAddonInfo
fanart          = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'fanart.png'))
fanarts         = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'fanart.png'))
icon            = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
nextpage        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id+'/resources/art', 'next.png'))
adultbase       = base64.b64decode('aHR0cHM6Ly94aGFtc3Rlci5jb20v')
User_Agent      = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
s               = requests.session()
userdata        = xbmc.translatePath('special://home/userdata/addon_data/' + addon_id)
AddonTitle      ='MAN STUFF'
dialog          = xbmcgui.Dialog()
REPO            = xbmc.translatePath(os.path.join('special://home/addons','repository.Goliath'))


####################    Install Repo if not found   #####################################
if not os.path.exists(REPO):
 	choice = xbmcgui.Dialog().yesno(AddonTitle,'This Add-on requires [COLOR cyan]Goliaths Repo[/COLOR] to be installed to work correctly would you like to install it now?','',yeslabel='[B][COLOR white]YES[/COLOR][/B]',nolabel='[B][COLOR grey]NO[/COLOR][/B]')
 	if choice == 1:
 		path = xbmc.translatePath(os.path.join('special://home/addons','packages'))
 		if not os.path.exists(path):
 			os.makedirs(path)
 		url = base64.b64decode(b'aHR0cDovL21hdHNidWlsZHMudWsvcmVwby9yZXBvc2l0b3J5LkdvbGlhdGgtMi4wLjEuemlw')
 		dp = xbmcgui.DialogProgress()
 		dp.create(AddonTitle,"","","Downloading [COLOR cyan]Goliaths Repo[/COLOR]")
 		lib=os.path.join(path, 'repo.zip')
		
 		try:
 			os.remove(lib)
 		except:
 			pass

 		Get_Files.download(url, lib, dp)
 		addonfolder = xbmc.translatePath(os.path.join('special://home','addons'))
 		time.sleep(2)
 		dp.update(0,"","Installing [COLOR red]Golitaths Repo[/COLOR] Please Wait","")
 		extract.all(lib,addonfolder,dp)
 		xbmc.executebuiltin("UpdateAddonRepos")
 		xbmc.executebuiltin("UpdateLocalAddons")

################################################################################################################################
	
def MAINMENU():
    addDir('[B][COLOR gold]Categories[/COLOR][/B]',adultbase+'categories',39,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
    addDir('[B][COLOR gold]Categories A-Z[/COLOR][/B]',adultbase+'categories',38,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
    addDir('[B][COLOR gold]Porn Stars A-Z[/COLOR][/B]',adultbase + 'pornstars',43,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
    addDir('[B][COLOR gold]Channels A-Z[/COLOR][/B]',adultbase + 'channels',44,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
    addDir('[B][COLOR gold]Best[/COLOR][/B]',adultbase + 'best/weekly',37,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
    addDir('[B][COLOR gold]Top Rated[/COLOR][/B]',adultbase + 'best/weekly',37,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
    addDir('[B][COLOR gold]Top Viewed[/COLOR][/B]',adultbase + 'most-viewed',37,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
    addDir('[B][COLOR gold]HD[/COLOR][/B]',adultbase + 'hd',37,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
    addDir('[B][COLOR gold]Most Commented[/COLOR][/B]',adultbase + 'most-commented/weekly',37,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
    addDir('[B][COLOR gold]Most Viewed Of 2017[/COLOR][/B]',adultbase +'most-viewed/year-2017',37,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
    addDir('[B][COLOR gold]Search[/COLOR][/B]','url',40,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def GET_CONTENT(url):

    if 'xhamster.com' in url:
        url = url.replace('https://xhamster.com','')
    else:
        url = url
        
    OPEN = Open_Url(adultbase + url)


    Regex = '<a class="video-thumb__image-container thumb-image-container" href="https:\/\/xhamster\.com(.*?)" data-sprite="(.*?)" data-previewvideo="(.*?)">'

    Videos = re.findall(Regex, OPEN, re.DOTALL)

    for Video in Videos:
        name = Video[0].replace('-',' ').replace('/videos/','')
        url = Video[0]
        icon = Video[1].replace('s_','2_')
        addDir2('[B][COLOR gold]'+name+'[/COLOR][/B]',url,41,icon,fanart,'')

    np = re.compile('<link rel="next" href="(.+?)"',re.DOTALL).findall(OPEN)

    for url in np:
        addDir2('[B][COLOR white]Next Page>>>[/COLOR][/B]',url,37,'http://i.imgur.com/Uqrznbf.png',fanart,'')
    xbmc.executebuiltin('Container.SetViewMode(50)') 
	
def GET_STARS(url):

	OPEN = Open_Url(url)
	
	categories = re.findall('<div class="item">\s+<a href="https://xhamster.com/pornstars/(.*?)" >(.*?)</a>\s+</div>', OPEN, re.DOTALL)

	for category in categories:

		Name = category[1]
		Url = '/pornstars/'+category[0]
		addDir2('[B][COLOR gold]'+Name+'[/COLOR][/B]',Url,37,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
		
	xbmc.executebuiltin('Container.SetViewMode(50)')
	
def GET_CHANNELS(url):

	OPEN = Open_Url(url)
	
	categories = re.findall('<div class="item">\s+<a href="https://xhamster.com/channels/(.*?)" >(.*?)</a>\s+</div>', OPEN, re.DOTALL)

	for category in categories:

		Name = category[1]
		Url = '/channels/'+category[0]
		addDir2('[B][COLOR gold]'+Name+'[/COLOR][/B]',Url,37,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
		
	xbmc.executebuiltin('Container.SetViewMode(50)')

def GET_GENRES(url):

	OPEN = Open_Url(url)
	
	categories = re.findall('<div class="item">\s+<a href="https://xhamster.com/tags/(.*?)" >(.*?)</a>\s+</div>', OPEN, re.DOTALL)

	for category in categories:

		Name = category[1]
		Url = '/tags/'+category[0]
		addDir2('[B][COLOR gold]'+Name+'[/COLOR][/B]',Url,37,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
		
	xbmc.executebuiltin('Container.SetViewMode(50)')

def ALL_CATS(url):

	OPEN = Open_Url(url)
	
	categories = re.findall('<a href="https://xhamster.com/categories-(.*?)" class="view-all">', OPEN, re.DOTALL)

	for category in categories:

		Name = category[0]
		Url = adultbase+'/categories-'+category[0]
		addDir2('[B][COLOR gold]'+Name+'[/COLOR][/B]',Url,39,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
		
	xbmc.executebuiltin('Container.SetViewMode(50)')

def ALL_CATS_CONTENT(url):
    OPEN = Open_Url(url)
    Regex = re.compile('<div class="letter-categories">(.+?)</ul>',re.DOTALL).findall(OPEN)
    Regex2 = re.compile('href="(.+?)"><span >(.+?)<',re.DOTALL).findall(str(Regex))
    for url,name in Regex2:
        addDir2('[B][COLOR gold]%s[/COLOR][/B]' %name,url,37,'https://i.imgur.com/kHN7aDk.jpg',fanart,'')
    xbmc.executebuiltin('Container.SetViewMode(50)')

def ADULT_SEARCH():
        keyb = xbmc.Keyboard('', 'Search For Your Porn!')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText().replace(' ','+')
                url = adultbase + 'search.php?from=&q=' + search + '&qcat=video'
                GET_CONTENT(url)
    
def Open_Url(url):
    headers = {}
    headers['User-Agent'] = User_Agent
    link = s.get(url, headers=headers).text
    link = link.encode('ascii', 'ignore')
    return link
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def RESOLVE(url):
    dialog = xbmcgui.Dialog()
    if not 'https' in url:
        url = 'https://xhamster.com' + url
    res_quality = []
    stream_url = []
	
    quality = ''
	
    OPEN = Open_Url(url)
	
    Soeuces = re.findall('"(\d+)p":"(.*?)"', OPEN, re.DOTALL)
	
    for Source in Soeuces:
	    
        link =  Source[1].replace('\\','')
		
        if '.flv' in Source[1]:
            quality = '[B][COLOR gold]FLV : ' + Source[0] + '[/COLOR][/B]'
        elif '.mp4' in Source[1]:
            quality = '[B][COLOR gold]MP4 : ' + Source[0] + '[/COLOR][/B]'
        
        res_quality.append(quality)
        stream_url.append(link)
	
    if len(res_quality) >1:
        dialog = xbmcgui.Dialog()
        ret = dialog.select('Please Select Quality',res_quality)
		
        if ret == -1:
            return
        elif ret > -1:
            url = stream_url[ret]

    liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
    liz.setInfo(type='Video', infoLabels={"Title": name})
    liz.setProperty("IsPlayable","true")
    liz.setPath(url)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

def addDir2(name,url,mode,iconimage,fanart,description):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description})
    liz.setProperty('fanart_image', fanart)
    if mode==41:
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    else:
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

 
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]                    
        return param

	
def addDir(name,url,mode,iconimage,fanart,description=''):
        selfAddon.setSetting('favtype','folder')
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)+"&fanart="+urllib.quote_plus(fanart)+"&iconimage="+urllib.quote_plus(iconimage)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart) 
        if 'youtube.com/channel/' in url:
		u = 'plugin://plugin.video.youtube/channel/'+description+'/'
	if 'youtube.com/user/' in url:
		u = 'plugin://plugin.video.youtube/user/'+description+'/'
        if 'youtube.com/playlist?' in url:
                u = 'plugin://plugin.video.youtube/playlist/'+description+'/'
        if 'plugin://' in url:
                u=url
        cmenu=[]
        favlist=selfAddon.getSetting('favlist')
        if favlist == 'yes':cmenu.append(('[COLOR cyan]Remove From Keep Safe?[/COLOR]','XBMC.RunPlugin(%s?mode=21&name=%s&url=%s&iconimage=%s)'% (sys.argv[0],name,url,iconimage)))
        else:cmenu.append(('[COLOR cyan]Add To Keep Safe?[/COLOR]','XBMC.RunPlugin(%s?mode=20&name=%s&url=%s&iconimage=%s)'% (sys.argv[0],name,url,iconimage)))
        liz.addContextMenuItems(cmenu, replaceItems=False) 
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None; description=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: fanart=urllib.unquote_plus(params["fanart"])
except: pass
try: description=str(params["description"])
except: pass

if mode==None or url==None or len(url)<1: MAINMENU()
elif mode==37:GET_CONTENT(url)
elif mode==38:ALL_CATS(url)
elif mode==39:GET_GENRES(url)
elif mode==40:ADULT_SEARCH()
elif mode==41:RESOLVE(url)
elif mode==42:ALL_CATS_CONTENT(url)
elif mode==43:GET_STARS(url)
elif mode==44:GET_CHANNELS(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
