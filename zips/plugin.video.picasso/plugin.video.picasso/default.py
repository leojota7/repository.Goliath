#V 2.1.3
import xbmc , xbmcaddon , xbmcgui , xbmcplugin , requests , urllib , urllib2 , json , os , re , sys , datetime , urlresolver , random , liveresolver , base64 , pyxbmct
from resources . lib . common_addon import Addon
from HTMLParser import HTMLParser
from metahandler import metahandlers
import universalscrapers
import requests
import downloader as Get_Files
import extract
import time
if 64 - 64: i11iIiiIii
VVeve = 'plugin.video.picasso'
VeevVee = Addon ( VVeve , sys . argv )
VevVevVVevVevVev = xbmcaddon . Addon ( id = VVeve )
iiiii = xbmcaddon . Addon ( ) . getAddonInfo
eeeevVV = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + VVeve , 'fanart.png' ) )
II1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + VVeve , 'fanart.png' ) )
Veveveeeeeevev = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + VVeve , 'icon.png' ) )
I1IiiI = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + VVeve + '/resources/art' , 'next.png' ) )
IIi1IiiiI1Ii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + VVeve + '/resources' , 'rd.txt' ) )
I11i11Ii = 'http://matsbuilds.uk/pin'
eVeveveVe = xbmcaddon . Addon ( ) . getSetting ( 'password' )
VVVeev = xbmcaddon . Addon ( ) . getSetting ( 'enable_meta' )
Veeeeveveve = base64 . b64decode ( 'aHR0cHM6Ly94aGFtc3Rlci5jb20v' )
IiIi11iIIi1Ii = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
VeevV = requests . session ( )
IiI = base64 . b64decode ( 'aHR0cDovL21hdHNidWlsZHMudWsvTWVudXMvYW5ld0V2b2x2ZW1lbnUvaW5mby50eHQ=' )
eeVe = xbmc . translatePath ( 'special://home/userdata/addon_data/' + VVeve )
Ve = xbmc . translatePath ( os . path . join ( 'special://home/userdata/Database' , 'picasso.db' ) )
eevV = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'repository.Goliath' ) )
IiiIII111iI = '[COLOR cyan]Picasso[/COLOR]'
IiII = open ( Ve , 'a' )
IiII . close ( )
if 28 - 28: Ii11111i * iiI1i1
if 46 - 46: VeeevVVeveVV * Ii * Veeve
if not os . path . exists ( eevV ) :
 VVVeveeve = xbmcgui . Dialog ( ) . yesno ( IiiIII111iI , 'This Add-on requires [COLOR cyan]Goliaths Repo[/COLOR] to be installed to work correctly would you like to install it now?' , '' , yeslabel = '[B][COLOR white]YES[/COLOR][/B]' , nolabel = '[B][COLOR grey]NO[/COLOR][/B]' )
 if VVVeveeve == 1 :
  Ii1iI = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  if not os . path . exists ( Ii1iI ) :
   os . makedirs ( Ii1iI )
  VeI1Ii11I1Ii1i = base64 . b64decode ( b'aHR0cDovL21hdHNidWlsZHMudWsvcmVwby9yZXBvc2l0b3J5LkdvbGlhdGgtMi4wLjEuemlw' )
  Vee = xbmcgui . DialogProgress ( )
  Vee . create ( IiiIII111iI , "" , "" , "Downloading [COLOR cyan]Goliaths Repo[/COLOR]" )
  eeveVeVeveve = os . path . join ( Ii1iI , 'repo.zip' )
  if 43 - 43: VevVVe . II1Iiii1111i
  try :
   os . remove ( eeveVeVeveve )
  except :
   pass
   if 25 - 25: VVeevevev
  Get_Files . download ( VeI1Ii11I1Ii1i , eeveVeVeveve , Vee )
  Vev = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
  time . sleep ( 2 )
  Vee . update ( 0 , "" , "Installing [COLOR red]Golitaths Repo[/COLOR] Please Wait" , "" )
  extract . all ( eeveVeVeveve , Vev , Vee )
  xbmc . executebuiltin ( "UpdateAddonRepos" )
  xbmc . executebuiltin ( "UpdateLocalAddons" )
  if 34 - 34: Veveevev % eeveee / VVVevV / I1ii * eVVVeeveevV + VVeVeeevevee
  if 41 - 41: i11IiIiiIIIII / IiiIII111ii / i1iIIi1
  if 50 - 50: IiIi1Iii1I1 - VevevVevVevVev
  if 75 - 75: Ii / i11IiIiiIIIII - eeveee
def ee ( ) :
 if not os . path . exists ( eeVe ) :
  os . mkdir ( eeVe )
 iii11iII ( IiI , 'GlobalCompare' )
 i1I111I ( '[B][COLOR yellow]Settings[/COLOR][/B]' , 'url' , 53 , 'http://i.imgur.com/cR0cP8f.png' , II1 )
 i1I111I ( '[B][COLOR yellow]Keep Safe[/COLOR][/B]' , 'url' , 22 , 'http://i.imgur.com/cR0cP8f.png' , II1 )
 i1I111I ( '[B][COLOR yellow]Find It...[/COLOR][/B]' , 'url' , 5 , 'http://i.imgur.com/ZQYQyHG.png' , II1 )
 i1I111I ( '[B][COLOR cyan]Movie Madness[/COLOR][/B]' , base64 . b64decode ( 'aHR0cDovL21hdHNidWlsZHMudWsvTWVudXMvTW92aWVzL01haW5tZW51LnhtbA==' ) , 26 , 'http://i.imgur.com/Y2rejnc.png' , II1 )
 i1I111I ( '[B][COLOR cyan]Telly Box[/COLOR][/B]' , base64 . b64decode ( 'aHR0cDovL21hdHNidWlsZHMudWsvTWVudXMvVHZTaG93cy9NYWlubWVudS54bWw=' ) , 27 , 'http://i.imgur.com/63LrHYW.png' , II1 )
 i11I1IIiiIi = IiIiIi ( II )
 iI = re . compile ( '<item>(.+?)</item>' ) . findall ( i11I1IIiiIi )
 for iI11iiiI1II in iI :
  VeveeeeevVeevev = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iI11iiiI1II )
  for Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV in VeveeeeevVeevev :
   i1I111I ( Ii11iii11I , VeI1Ii11I1Ii1i , 1 , eVeevevVeevevV , eeeevVV )
 xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
 if 43 - 43: VevVVe - IiiIII111ii * iiI1i1
def VevVeveveevVVVev ( name , url , iconimage , fanart ) :
 i1I111I ( '[B][COLOR yellow]MOVIE SEARCH[/COLOR][/B]' , base64 . b64decode ( 'aHR0cDovL21hdHNidWlsZHMudWsvTWVudXMvTW92aWVzL1NlYXJjaC9TZWFyY2gudHh0' ) , 5 , 'http://i.imgur.com/QArRVYb.png' , II1 )
 i1I111I ( '[B][COLOR yellow]UK CINEMA RELEASE DATES[/COLOR][/B]' , 'http://www.empireonline.com/movies/features/upcoming-movies/' , 34 , 'http://i.imgur.com/aKQgDR7.png' , II1 )
 i11I1IIiiIi = IiIiIi ( url )
 iI = re . compile ( '<item>(.+?)</item>' ) . findall ( i11I1IIiiIi )
 Ii1iIIIi1ii = re . compile ( '<item>(.+?)</item>' ) . findall ( i11I1IIiiIi )
 for iI11iiiI1II in iI :
  VeveeeeevVeevev = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iI11iiiI1II )
 for iI11iiiI1II in Ii1iIIIi1ii :
  eeveeeveevVevevVV = re . compile ( '<title>(.+?)</title>.+?lbscraper>(.+?)</lbscraper>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iI11iiiI1II )
  for name , url , iconimage , fanart in VeveeeeevVeevev :
   eeveV ( name , url , iconimage , fanart , iI11iiiI1II )
   if 48 - 48: VVeVeeevevee + VVeVeeevevee / Veeve / iiI1i1
def i1iiI11I ( name , url , iconimage , fanarts ) :
 i1I111I ( '[B][COLOR yellow]TV SEARCH[/COLOR][/B]' , base64 . b64decode ( 'aHR0cDovL21hdHNidWlsZHMudWsvYW5ld0V2b2x2ZW1lbnUvc2VhcmNoLnhtbA==' ) , 33 , 'http://i.imgur.com/he5RFkL.png' , fanarts )
 i1I111I ( '[B][COLOR yellow]TV SCHEDULE[/COLOR][/B]' , 'http://www.tvwise.co.uk/uk-premiere-dates/' , 32 , 'http://i.imgur.com/XKAapZH.png' , fanarts )
 i1I111I ( '[B][COLOR yellow]Latest Episodes[/COLOR][/B]' , base64 . b64decode ( 'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzNC5jb20=' ) , 28 , 'http://i.imgur.com/n8itltl.png' , fanarts )
 i1I111I ( '[B][COLOR yellow]Popular Shows[/COLOR][/B]' , base64 . b64decode ( 'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzNC5jb20vaG9tZS9wb3B1bGFyLXNlcmllcw==' ) , 29 , 'http://i.imgur.com/ury75ui.png' , fanarts )
 i1I111I ( '[B][COLOR yellow]New Shows[/COLOR][/B]' , base64 . b64decode ( 'aHR0cDovL3d3dy53YXRjaGVwaXNvZGVzNC5jb20vaG9tZS9uZXctc2VyaWVz' ) , 30 , 'http://i.imgur.com/UPWjTLw.png' , fanarts )
 if 29 - 29: VeeevVVeveVV
 iII1i1I1II = i1 ( name )
 VevVevVVevVevVev . setSetting ( 'tv' , iII1i1I1II )
 i11I1IIiiIi = IiIiIi ( url )
 iI = re . compile ( '<item>(.+?)</item>' ) . findall ( i11I1IIiiIi )
 for iI11iiiI1II in iI :
  VeveeeeevVeevev = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iI11iiiI1II )
  for name , url , iconimage , eeeevVV in VeveeeeevVeevev :
   eeveV ( name , url , iconimage , eeeevVV , iI11iiiI1II )
   if 48 - 48: Ii11111i + Ii11111i - VVVevV . VevevVevVevVev / iiI1i1
def VeVVVeveveVVev ( name , url , iconimage , fanart ) :
 iII1i1I1II = i1 ( name )
 VevVevVVevVevVev . setSetting ( 'tv' , iII1i1I1II )
 i11I1IIiiIi = IiIiIi ( url )
 eVee ( i11I1IIiiIi )
 if '<message>' in i11I1IIiiIi :
  IiI = re . compile ( '<message>(.+?)</message>' ) . findall ( i11I1IIiiIi ) [ 0 ]
  iii11iII ( IiI , iII1i1I1II )
 if '<intro>' in i11I1IIiiIi :
  iIii11I = re . compile ( '<intro>(.+?)</intro>' ) . findall ( i11I1IIiiIi ) [ 0 ]
  VVVevVVVevevee ( iIii11I )
 if 'XXX>yes</XXX' in i11I1IIiiIi : Iii111II ( i11I1IIiiIi )
 iI = re . compile ( '<item>(.+?)</item>' ) . findall ( i11I1IIiiIi )
 for iI11iiiI1II in iI :
  eeveV ( name , url , iconimage , fanart , iI11iiiI1II )
  if 9 - 9: VVeevevev
def eeveV ( name , url , iconimage , fanart , item ) :
 try :
  if '<sportsdevil>' in item : i11 ( name , url , iconimage , fanart , item )
  elif '<iplayer>' in item : VeveeevVVeveVVVe ( name , url , iconimage , fanart , item )
  elif '<folder>' in item : i1i1i11IIi ( name , url , iconimage , fanart , item )
  elif '<iptv>' in item : II1III ( name , url , iconimage , fanart , item )
  elif '<image>' in item : iI1iI1I1i1I ( name , url , iconimage , fanart , item )
  elif '<text>' in item : iIi11Ii1 ( name , url , iconimage , fanart , item )
  elif '<scraper>' in item : Ii11iII1 ( name , url , iconimage , fanart , item )
  elif '<lbscraper>' in item : VeevVevVeveeVevV ( name , url , iconimage , fanart , item )
  elif '<redirect>' in item : IIIIii ( name , url , iconimage , fanart , item )
  elif '<oktitle>' in item : Veveev ( name , url , iconimage , fanart , item )
  elif '<nan>' in item : VVevevVe ( name , url , iconimage , fanart , item )
  elif '<adult>' in item : VevVVVevVVeVevV ( name , url , iconimage , fanart , item )
  else : VevevVeeveveveeVev ( name , url , iconimage , fanart , item )
 except : pass
 if 100 - 100: Ii11111i + i1iIIi1 - eVVVeeveevV + i11iIiiIii * i11IiIiiIIIII
def VeveeevVVeveVVVe ( name , url , iconimage , fanart , item ) :
 url = re . compile ( '<iplayer>(.+?)</iplayer>' ) . findall ( item ) [ 0 ]
 name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( item ) [ 0 ]
 url = 'plugin://plugin.video.iplayerwww/?url=%s&mode=202&name=%s&iconimage=%s&description=&subtitles_url=&logged_in=False' % ( url , name , iconimage )
 iII ( name , url , 16 , iconimage , fanart )
 if 80 - 80: i1iIIi1 . I1ii
def VVevevVe ( name , url , iconimage , fanart , item ) :
 name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 IIi = re . compile ( '<meta>(.+?)</meta>' ) . findall ( item ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( item ) [ 0 ]
 i11iIIIIIi1 = re . compile ( '<nan>(.+?)</nan>' ) . findall ( item ) [ 0 ]
 iiII1i1 = re . compile ( '<imdb>(.+?)</imdb>' ) . findall ( item ) [ 0 ]
 if i11iIIIIIi1 == 'movie' :
  iiII1i1 = iiII1i1 + '<>movie'
 elif i11iIIIIIi1 == 'tvshow' :
  eeveveVVeve = re . compile ( '<showname>(.+?)</showname>' ) . findall ( item ) [ 0 ]
  VVVevevV = re . compile ( '<season>(.+?)</season>' ) . findall ( item ) [ 0 ]
  VVeVVeveeeveeV = re . compile ( '<episode>(.+?)</episode>' ) . findall ( item ) [ 0 ]
  VeveevVevevVeeveev = re . compile ( '<showyear>(.+?)</showyear>' ) . findall ( item ) [ 0 ]
  VevevVeveVVevevVevev = re . compile ( '<episodeyear>(.+?)</episodeyear>' ) . findall ( item ) [ 0 ]
  iiII1i1 = iiII1i1 + '<>' + eeveveVVeve + '<>' + VVVevevV + '<>' + VVeVVeveeeveeV + '<>' + VeveevVevevVeeveev + '<>' + VevevVeveVVevevVevev
  i11iIIIIIi1 = "tvep"
 i1Veevev ( name , iiII1i1 , 19 , iconimage , 1 , i11iIIIIIi1 , isFolder = True )
 if 31 - 31: IiIi1Iii1I1 . Veveevev / Ii11111i
def eevevevVeve ( name , imdb , iconimage , fanart ) :
 IIi1IiiiI1Ii = ''
 iI1iII1 = name
 iII1i1I1II = i1 ( name )
 VevVevVVevVevVev . setSetting ( 'tv' , iII1i1I1II )
 if 'movie' in imdb :
  imdb = imdb . split ( '<>' ) [ 0 ]
  eVevVVeeevVV = [ ]
  Vevii1ii1ii = [ ]
  eeeeeVeeeveee = name . partition ( '(' )
  I1I1IiI1 = eeeeeVeeeveee [ 0 ]
  I1I1IiI1 = i1 ( I1I1IiI1 )
  III1iII1I1ii = eeeeeVeeeveee [ 2 ] . partition ( ')' ) [ 0 ]
  eVVeev = universalscrapers . scrape_movie ( I1I1IiI1 , III1iII1I1ii , imdb , timeout = 800 )
 else :
  eeveveVVeve = imdb . split ( '<>' ) [ 1 ]
  eeevevVeveveV = imdb . split ( '<>' ) [ 0 ]
  VVVevevV = imdb . split ( '<>' ) [ 2 ]
  VVeVVeveeeveeV = imdb . split ( '<>' ) [ 3 ]
  VeveevVevevVeeveev = imdb . split ( '<>' ) [ 4 ]
  VevevVeveVVevevVevev = imdb . split ( '<>' ) [ 5 ]
  eVVeev = universalscrapers . scrape_episode ( eeveveVVeve , VeveevVevevVeeveev , VevevVeveVVevevVevev , VVVevevV , VVeVVeveeeveeV , eeevevVeveveV , None )
 iIiIIIi = 1
 for eeeevevVVVeeV in eVVeev ( ) :
  if type ( eeeevevVVVeeV ) != list :
   continue
  for VevevVVVeVeeevV in eeeevevVVVeeV :
   try :
    if not VevevVVVeVeeevV [ "url" ] :
     continue
    if urlresolver . HostedMediaFile ( VevevVVVeVeeevV [ 'url' ] ) . valid_url ( ) :
     IIi1IiiiI1Ii = VevevevVVeevevee ( VevevVVVeVeeevV [ 'url' ] )
     name = "Link " + str ( iIiIIIi ) + ' | ' + VevevVVVeVeeevV [ 'source' ] + IIi1IiiiI1Ii
     iIiIIIi = iIiIIIi + 1
     eeevVVe ( name , VevevVVVeVeeevV [ 'url' ] , 2 , iconimage , fanart , description = VevVevVVevVevVev . getSetting ( 'tv' ) )
   except Exception as eeVVVevevVee :
    xbmc . log ( "error: " + repr ( eeVVVevevVee ) )
    xbmc . log ( "erro result: " + repr ( VevevVVVeVeeevV ) )
    if 16 - 16: Veeve % Veveevev - Veeve + i11IiIiiIIIII
    if 12 - 12: eVVVeeveevV / eVVVeeveevV + i11iIiiIii
def VevVVVevVVeVevV ( name , url , iconimage , fanart , item ) :
 name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 url = re . compile ( '<adult>(.+?)</adult>' ) . findall ( item ) [ 0 ]
 fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( item ) [ 0 ]
 i1I111I ( name , url , 36 , iconimage , fanart )
 if 40 - 40: VevVVe . iiI1i1 / VevVVe / i11iIiiIii
def eevVeveve ( ) :
 i1I111I ( '[B][COLOR gold]Categories[/COLOR][/B]' , Veeeeveveve + 'categories' , 39 , 'http://i.imgur.com/z6WJ6RB.png' , eeeevVV , '' )
 i1I111I ( '[B][COLOR gold]Categories A-Z[/COLOR][/B]' , Veeeeveveve + 'categories' , 38 , 'http://i.imgur.com/z6WJ6RB.png' , eeeevVV , '' )
 i1I111I ( '[B][COLOR gold]Best[/COLOR][/B]' , Veeeeveveve + 'best/weekly' , 37 , 'http://i.imgur.com/z6WJ6RB.png' , eeeevVV , '' )
 i1I111I ( '[B][COLOR gold]Top Rated[/COLOR][/B]' , Veeeeveveve + 'best/weekly' , 37 , 'http://i.imgur.com/z6WJ6RB.png' , eeeevVV , '' )
 i1I111I ( '[B][COLOR gold]Top Viewed[/COLOR][/B]' , Veeeeveveve + 'most-viewed' , 37 , 'http://i.imgur.com/z6WJ6RB.png' , eeeevVV , '' )
 i1I111I ( '[B][COLOR gold]HD[/COLOR][/B]' , Veeeeveveve + 'categories/hd-videos' , 37 , 'http://i.imgur.com/z6WJ6RB.png' , eeeevVV , '' )
 i1I111I ( '[B][COLOR gold]Most Commented[/COLOR][/B]' , Veeeeveveve + 'most-commented/weekly' , 37 , 'http://i.imgur.com/z6WJ6RB.png' , eeeevVV , '' )
 i1I111I ( '[B][COLOR gold]Best of 2016[/COLOR][/B]' , Veeeeveveve + 'videos/top/year/2016' , 37 , 'http://i.imgur.com/z6WJ6RB.png' , eeeevVV , '' )
 i1I111I ( '[B][COLOR gold]Search[/COLOR][/B]' , 'url' , 40 , 'http://i.imgur.com/z6WJ6RB.png' , eeeevVV , '' )
 xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 87 - 87: i11iIiiIii
def VVevVeeeev ( url ) :
 if 62 - 62: Ii11111i * Ii * eeveee - VevVVe + VevVVe
 if 'xhamster.com' in url :
  url = url . replace ( 'https://xhamster.com' , '' )
 else :
  url = url
  if 34 - 34: iiI1i1 - eeveee
 eeveveeeVevVe = eevVevVVVevVee ( Veeeeveveve + url )
 if 45 - 45: Ii11111i / eeveee
 if 32 - 32: IiiIII111ii . i1iIIi1 . i1iIIi1
 VVevevVevV = '<a class="video-thumb__image-container thumb-image-container" href="https:\/\/xhamster\.com(.*?)" data-sprite="(.*?)" data-previewvideo="(.*?)">'
 if 33 - 33: Ii11111i . i1iIIi1 . VevVVe
 VeVV = re . findall ( VVevevVevV , eeveveeeVevVe , re . DOTALL )
 if 53 - 53: II1Iiii1111i
 for iI1Iii in VeVV :
  Ii11iii11I = iI1Iii [ 0 ] . replace ( '-' , ' ' ) . replace ( '/videos/' , '' )
  url = iI1Iii [ 0 ]
  Veveveeeeeevev = iI1Iii [ 1 ] . replace ( 's_' , '2_' )
  eVevevVVeVevev ( '[B][COLOR gold]' + Ii11iii11I + '[/COLOR][/B]' , url , 41 , Veveveeeeeevev , eeeevVV , '' )
  if 40 - 40: VevVVe * i11IiIiiIIIII + eVVVeeveevV % IiiIII111ii
 VVVVVeeev = re . compile ( '<link rel="next" href="(.+?)"' , re . DOTALL ) . findall ( eeveveeeVevVe )
 if 49 - 49: Ii11111i . IiiIII111ii
 for url in VVVVVeeev :
  eVevevVVeVevev ( '[B][COLOR white]Next Page>>>[/COLOR][/B]' , url , 37 , 'http://i.imgur.com/Uqrznbf.png' , eeeevVV , '' )
 xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 11 - 11: i1iIIi1 * VevVVe . iiI1i1 % VeeevVVeveVV + IiiIII111ii
def VVV ( url ) :
 if 68 - 68: Veeve + VVeVeeevevee
 eeveveeeVevVe = eevVevVVVevVee ( url )
 if 45 - 45: IiiIII111ii / IiiIII111ii + IiIi1Iii1I1 + VevevVevVevVev
 iI111i = re . findall ( '<div class="item">\s+<a href="https://xhamster.com/tags/(.*?)" >(.*?)</a>\s+</div>' , eeveveeeVevVe , re . DOTALL )
 if 26 - 26: VVVevV * IiiIII111ii . Veeve * i11IiIiiIIIII
 for II1iiiIi1 in iI111i :
  if 38 - 38: IiIi1Iii1I1
  VeeeveveevVeee = II1iiiIi1 [ 1 ]
  VVeeeeVevVe = '/tags/' + II1iiiIi1 [ 0 ]
  eVevevVVeVevev ( '[B][COLOR gold]' + VeeeveveevVeee + '[/COLOR][/B]' , VVeeeeVevVe , 37 , 'http://i.imgur.com/z6WJ6RB.png' , eeeevVV , '' )
  if 91 - 91: eeveee . iiI1i1 / I1ii + Ii
 xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 42 - 42: VevevVevVevVev . eeveee . VevevVevVevVev - VVVevV
def i1ii1I1I1 ( url ) :
 if 74 - 74: eeveee . IiiIII111ii
 eeveveeeVevVe = eevVevVVVevVee ( url )
 if 18 - 18: eVVVeeveevV + IiiIII111ii - i11IiIiiIIIII . Veeve + i11iIiiIii
 iI111i = re . findall ( '<a href="https://xhamster.com/categories-(.*?)" class="view-all">' , eeveveeeVevVe , re . DOTALL )
 if 20 - 20: IiIi1Iii1I1
 for II1iiiIi1 in iI111i :
  if 52 - 52: Veeve - VeeevVVeveVV % i11IiIiiIIIII + VevVVe * II1Iiii1111i . i1iIIi1
  VeeeveveevVeee = II1iiiIi1 [ 0 ]
  VVeeeeVevVe = Veeeeveveve + '/categories-' + II1iiiIi1 [ 0 ]
  eVevevVVeVevev ( '[B][COLOR gold]' + VeeeveveevVeee + '[/COLOR][/B]' , VVeeeeVevVe , 39 , 'http://i.imgur.com/z6WJ6RB.png' , eeeevVV , '' )
  if 75 - 75: VevevVevVevVev + Veveevev + eeveee * VVeVeeevevee % I1ii . IiiIII111ii
 xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 55 - 55: eVVVeeveevV . VevVVe
def eVeevVeveeveve ( url ) :
 eeveveeeVevVe = eevVevVVVevVee ( url )
 VVevevVevV = re . compile ( '<div class="letter-categories">(.+?)</ul>' , re . DOTALL ) . findall ( eeveveeeVevVe )
 eeveveVeveeevVV = re . compile ( 'href="(.+?)"><span >(.+?)<' , re . DOTALL ) . findall ( str ( VVevevVevV ) )
 for url , Ii11iii11I in eeveveVeveeevVV :
  eVevevVVeVevev ( '[B][COLOR gold]%s[/COLOR][/B]' % Ii11iii11I , url , 37 , 'http://i.imgur.com/z6WJ6RB.png' , eeeevVV , '' )
 xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 if 57 - 57: IiIi1Iii1I1 % i11IiIiiIIIII + eeveee - II1Iiii1111i
def eevVIiI1i ( ) :
 eevVeevev = xbmc . Keyboard ( '' , 'Search For Your Porn!' )
 eevVeevev . doModal ( )
 if ( eevVeevev . isConfirmed ( ) ) :
  iIVevVevVeeeeve = eevVeevev . getText ( ) . replace ( ' ' , '+' )
  VeI1Ii11I1Ii1i = Veeeeveveve + 'search.php?from=&q=' + iIVevVevVeeeeve + '&qcat=video'
  VVevVeeeev ( VeI1Ii11I1Ii1i )
  if 56 - 56: VVVevV % Ii11111i - VevVVe
def eevVevVVVevVee ( url ) :
 VeveveevVVev = { }
 VeveveevVVev [ 'User-Agent' ] = IiIi11iIIi1Ii
 i11I1IIiiIi = VeevV . get ( url , headers = VeveveevVVev ) . text
 i11I1IIiiIi = i11I1IIiiIi . encode ( 'ascii' , 'ignore' )
 return i11I1IIiiIi
 xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
 if 35 - 35: I1ii % VevevVevVevVev / IiIi1Iii1I1 + iiI1i1 . VeeevVVeveVV . VevVVe
def eeveveVVeeVVeeve ( url ) :
 VevVeveeVVV = xbmcgui . Dialog ( )
 if not 'https' in url :
  url = 'https://xhamster.com' + url
 eVVeevVeveve = [ ]
 iIiIi11 = [ ]
 if 87 - 87: II1Iiii1111i . VevVVe - Veeve + Ii11111i / II1Iiii1111i / I1ii
 IiIIIIii1I = ''
 if 97 - 97: Ii11111i + Veveevev
 eeveveeeVevVe = eevVevVVVevVee ( url )
 if 89 - 89: eeveee + VVeevevev * VVeVeeevevee * i11IiIiiIIIII
 iiIiI1i1 = re . findall ( '"(\d+)p":"(.*?)"' , eeveveeeVevVe , re . DOTALL )
 if 69 - 69: VevevVevVevVev
 for I11iII in iiIiI1i1 :
  if 5 - 5: VevVVe
  i11I1IIiiIi = I11iII [ 1 ] . replace ( '\\' , '' )
  if 48 - 48: eeveee - I1ii / VeeevVVeveVV
  if '.flv' in I11iII [ 1 ] :
   IiIIIIii1I = '[B][COLOR gold]FLV : ' + I11iII [ 0 ] + '[/COLOR][/B]'
  elif '.mp4' in I11iII [ 1 ] :
   IiIIIIii1I = '[B][COLOR gold]MP4 : ' + I11iII [ 0 ] + '[/COLOR][/B]'
   if 100 - 100: VevVVe / eeveee % Veeve % II1Iiii1111i % eVVVeeveevV
  eVVeevVeveve . append ( IiIIIIii1I )
  iIiIi11 . append ( i11I1IIiiIi )
  if 98 - 98: VVeVeeevevee % i11iIiiIii % VevevVevVevVev + i11IiIiiIIIII
 if len ( eVVeevVeveve ) > 1 :
  VevVeveeVVV = xbmcgui . Dialog ( )
  VVeVVeveeveev = VevVeveeVVV . select ( 'Please Select Quality' , eVVeevVeveve )
  if 11 - 11: VevVVe
  if VVeVVeveeveev == - 1 :
   return
  elif VVeVVeveeveev > - 1 :
   url = iIiIi11 [ VVeVVeveeveev ]
   if 16 - 16: i11IiIiiIIIII + i1iIIi1 * Ii11111i % Ii . VevVVe
 VeevVV = xbmcgui . ListItem ( Ii11iii11I , iconImage = 'DefaultVideo.png' , thumbnailImage = eVeevevVeevevV )
 VeevVV . setInfo ( type = 'Video' , infoLabels = { "Title" : Ii11iii11I } )
 VeevVV . setProperty ( "IsPlayable" , "true" )
 VeevVV . setPath ( url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , VeevVV )
 if 78 - 78: eVVVeeveevV - VeeevVVeveVV - VVVevV / VevevVevVevVev / Veeve
def eVevevVVeVevev ( name , url , mode , iconimage , fanart , description ) :
 iiI11ii1I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&iconimage=" + urllib . quote_plus ( iconimage ) + "&description=" + urllib . quote_plus ( description )
 VeeevVVeVeVev = True
 VeevVV = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 VeevVV . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 VeevVV . setProperty ( 'fanart_image' , fanart )
 if mode == 41 :
  VeevVV . setProperty ( "IsPlayable" , "true" )
  VeeevVVeVeVev = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiI11ii1I1 , listitem = VeevVV , isFolder = False )
 else :
  VeeevVVeVeVev = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiI11ii1I1 , listitem = VeevVV , isFolder = True )
 return VeeevVVeVeVev
 if 70 - 70: I1ii
 if 59 - 59: eeveee % I1ii
 if 6 - 6: iiI1i1 % i11iIiiIii % VVVevV
def Ii11iII1 ( name , url , iconimage , fanart , item ) :
 name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 url = re . compile ( '<scraper>(.+?)</scraper>' ) . findall ( item ) [ 0 ]
 fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( item ) [ 0 ]
 i1I111I ( name , url , 18 , iconimage , fanart )
 if 93 - 93: i1iIIi1 * VeeevVVeveVV + VevevVevVevVev
def IiII111i1i11 ( name , url , iconimage , fanart ) :
 i111iIi1i1II1 = url
 if i111iIi1i1II1 == 'latestmovies' :
  eeeV = 15
  i1I1i111Ii = MOVIESINDEXER ( )
  eee = re . compile ( '<item>(.+?)</item>' ) . findall ( i1I1i111Ii )
  for iI11iiiI1II in eee :
   VeveeeeevVeevev = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( iI11iiiI1II )
   i1i1iI1iiiI = len ( eee )
   for name , url , iconimage , fanart in VeveeeeevVeevev :
    if '<meta>' in iI11iiiI1II :
     VeeeveVeeeev = re . compile ( '<meta>(.+?)</meta>' ) . findall ( iI11iiiI1II ) [ 0 ]
     i1Veevev ( name , url , eeeV , iconimage , i1i1iI1iiiI , VeeeveVeeeev , isFolder = False )
    else : eeevVVe ( name , url , 15 , iconimage , fanart )
    if 61 - 61: Veveevev - eVVVeeveevV - Ii
    if 25 - 25: Ii11111i * VVeVeeevevee + VVVevV . eeveee . eeveee
def eVeeV ( name , url , iconimage , fanarts ) :
 i11I1IIiiIi = IIIIiI11I11 ( 'http://www.watchepisodes4.com' )
 eeeveveev = re . compile ( '<a title=".+?" .+? style="background-image: url(.+?)"></a>.+?<div class="hb-right">.+?<a title=".+?" href="(.+?)" class="episode">(.+?)</a>' , re . DOTALL ) . findall ( i11I1IIiiIi )
 for iconimage , url , name in eeeveveev :
  iconimage = iconimage . replace ( "('" , "" ) . replace ( "')" , "" )
  name = name . replace ( "&#39;" , "'" ) . replace ( '&amp;' , ' & ' )
  name = name . split ( '  ' ) [ 0 ]
  i1I111I ( name , url , 24 , iconimage , iconimage )
  if 4 - 4: i11IiIiiIIIII % I1ii * VVeevevev
def eevVevVVVVeVVev ( name , url , iconimage , fanart ) :
 i11I1IIiiIi = IIIIiI11I11 ( url )
 eeeveveev = re . compile ( '<div class="cb-first">.+?<a href="(.+?)" class="c-image"><img alt=".+?" title="(.+?)" src="(.+?)"></a>' , re . DOTALL ) . findall ( i11I1IIiiIi )
 for url , name , iconimage in eeeveveev :
  name = name . replace ( "&#39;" , "'" ) . replace ( '&amp;' , ' & ' )
  i1I111I ( name , url , 31 , iconimage , iconimage )
  if 23 - 23: i11iIiiIii
def II1iIi11 ( name , url , iconimage , fanart ) :
 i11I1IIiiIi = IIIIiI11I11 ( url )
 eeeveveev = re . compile ( '<div class="cb-first">.+?<a href="(.+?)" class="c-image"><img alt=".+?" title="(.+?)" src="(.+?)"></a>' , re . DOTALL ) . findall ( i11I1IIiiIi )
 for url , name , iconimage in eeeveveev :
  name = name . replace ( "&#39;" , "'" ) . replace ( '&amp;' , ' & ' )
  i1I111I ( name , url , 31 , iconimage , iconimage )
  if 12 - 12: i11IiIiiIIIII + i11iIiiIii * iiI1i1 / VVVevV . VVeVeeevevee
def Iii1iI ( name , url , iconimage , fanart ) :
 i11I1IIiiIi = IiI1iiiIii ( url )
 I1III1111iIi = re . compile ( '<div class="std-cts">.+?<div class="sdt-content tnContent">.+?<h2>(.+?)</h2>' , re . DOTALL ) . findall ( i11I1IIiiIi ) [ 0 ] . replace ( ' Episodes' , '' ) . replace ( "&#39;" , "'" ) . replace ( '&amp;' , ' & ' )
 iI = re . compile ( '<a title=".+?" href="(.+?)">.+?<div class="season">(.+?) </div>.+?<div class="episode">(.+?)</div>.+?<div class="e-name">(.+?)</div>' , re . DOTALL ) . findall ( i11I1IIiiIi )
 for url , VVVevevV , VVeVVeveeeveeV , I1i111I in iI :
  I1i111I = I1i111I . replace ( "&#39;" , "'" ) . replace ( '&amp;' , ' & ' )
  if '</div>' in name : name = 'TBA'
  i1I111I ( '%s ' % I1III1111iIi + '(%s ' % VVVevevV + '%s)' % VVeVVeveeeveeV , url , 24 , iconimage , iconimage )
  if 97 - 97: Ii . I1ii / IiiIII111ii * Ii11111i
def eevVeve ( name , url , iconimage , fanart ) :
 iI1iII1 = name
 i11I1IIiiIi = IiI1iiiIii ( url )
 VVeveeveevev = re . compile ( '<a target="_blank" href=".+?" data-episodeid=".+?" data-linkid=".+?" data-hostname=".+?" class="watch-button" data-actuallink="(.+?)">Watch Now!</a>' ) . findall ( i11I1IIiiIi )
 iIiIIIi = 1
 eVevVVeeevVV = [ ]
 Vevii1ii1ii = [ ]
 for IiIi1I1 in VVeveeveevev :
  IIi1IiiiI1Ii = VevevevVVeevevee ( IiIi1I1 )
  if 'http' in IiIi1I1 : IiIIi1 = IiIi1I1 . split ( '/' ) [ 2 ] . split ( '.' ) [ 0 ]
  else : IiIIi1 = IiIi1I1
  name = "Link " + str ( iIiIIIi ) + ' | ' + IiIIi1 + IIi1IiiiI1Ii
  if IiIIi1 != 'www' :
   eeevVVe ( IiIIi1 , IiIi1I1 , 2 , iconimage , fanart , description = '' )
   if 47 - 47: II1Iiii1111i * VVVevV + iiI1i1 / IiIi1Iii1I1 / VVeevevev - VeeevVVeveVV
def iII1i11IIi1i ( name , url , iconimage , fanart ) :
 i11I1IIiiIi = IiI1iiiIii ( url )
 eeeveveev = re . compile ( '<td height="20">(.+?)</td>.+?<td>(.+?)</td>.+?<td><a href=".+?">(.+?)</a></td>.+?<td><a href=".+?">(.+?)</a></td>.+?</tr>' , re . DOTALL ) . findall ( i11I1IIiiIi )
 for eVVeeevevevevVeveev , name , II1IIIII , time in eeeveveev :
  name = name . replace ( "&#8217;" , "'" ) . replace ( '&amp;' , ' & ' )
  i1I111I ( '[COLOR yellow]%s[/COLOR] - ' % II1IIIII + '[COLOR yellow]%s[/COLOR] ' % name + '- [COLOR white]%s[/COLOR]' % eVVeeevevevevVeveev , url , 28 , iconimage , fanart )
  if 28 - 28: IiiIII111ii . IiiIII111ii % iiI1i1 * iiI1i1 . eeveee / IiiIII111ii
def iII1i1 ( url ) :
 VeveVVeeeVVevV = ''
 eeeevevVee = xbmc . Keyboard ( VeveVVeeeVVevV , '[B][COLOR cyan]What Would You Like Me To Find?[/COLOR][/B]' )
 eeeevevVee . doModal ( )
 if eeeevevVee . isConfirmed ( ) :
  VeveVVeeeVVevV = eeeevevVee . getText ( ) . replace ( ' ' , '+' ) . replace ( '+and+' , '+%26+' )
 if len ( VeveVVeeeVVevV ) > 1 :
  url = 'http://www.watchepisodes4.com/search/ajax_search?q=' + VeveVVeeeVVevV
  i11I1IIiiIi = IiI1iiiIii ( url )
  VeveeeeevVeevev = json . loads ( i11I1IIiiIi )
  VeveeeeevVeevev = VeveeeeevVeevev [ 'series' ]
  for iI11iiiI1II in VeveeeeevVeevev :
   Ii11iii11I = iI11iiiI1II [ 'value' ]
   VeeveevVevev = iI11iiiI1II [ 'seo' ]
   url = 'http://www.watchepisodes4.com/' + VeeveevVevev
   eVeevevVeevevV = 'http://www.watchepisodes4.com/movie_images/' + VeeveevVevev + '.jpg'
   i1I111I ( Ii11iii11I , url , 31 , eVeevevVeevevV , eeeevVV )
  VeveVVeeeVVevV = VeveVVeeeVVevV [ : - 1 ]
  i11I1IIiiIi = IiIiIi ( 'http://matsbuilds.uk/anewEvolvemenu/search.xml' )
  ii1 = re . compile ( '<link>(.+?)</link>' ) . findall ( i11I1IIiiIi )
  for url in ii1 :
   try :
    i11I1IIiiIi = IiIiIi ( url )
    I1i11 = re . compile ( '<item>(.+?)</item>' ) . findall ( i11I1IIiiIi )
    for iI11iiiI1II in I1i11 :
     iI = re . compile ( '<title>(.+?)</title>' ) . findall ( iI11iiiI1II )
     for iI1iII1 in iI :
      iI1iII1 = i1 ( iI1iII1 . upper ( ) )
      VeveVVeeeVVevV = VeveVVeeeVVevV . upper ( )
      if VeveVVeeeVVevV in iI1iII1 :
       eeveV ( Ii11iii11I , url , eVeevevVeevevV , eeeevVV , iI11iiiI1II )
   except : pass
   if 51 - 51: VVeevevev . VevVVe * VevevVevVevVev % i11IiIiiIIIII + Veeve . VevevVevVevVev
def iI1IiI11ii1I1 ( name , url , iconimage , fanart ) :
 i11I1IIiiIi = IiI1iiiIii ( url )
 iI = re . compile ( '</div>.+?<a href="(.+?)" class="list cf">.+?<div class="serie-poster">.+?<img src="(.+?)" alt="(.+?)"/>.+?<span class="date">.+?</span>' , re . DOTALL ) . findall ( i11I1IIiiIi )
 for url , iconimage , name in iI :
  url = 'http://www.cinemixtv.ga/' + url
  eeevVVe ( '[B][COLOR yellow]%s[/COLOR][/B]' % name , url , 52 , iconimage , fanart )
 try :
  VVVVVeeev = re . compile ( '<li class="active"><a href=".+?">.+?</a></li><li class="noactive"><a href="(.+?)">(.+?)</a></li>' , re . DOTALL ) . findall ( i11I1IIiiIi )
  for url , ii in VVVVVeeev :
   i1I111I ( '[COLOR cyan]Next Page >> %s[/COLOR]' % ii , url , iiI , '' , '' )
 except : pass
 if 56 - 56: II1Iiii1111i . VVVevV . VevVVe
 if 39 - 39: Ii11111i + IiIi1Iii1I1
def VeVeeVeV ( name , url , iconimage ) :
 i11I1IIiiIi = IiI1iiiIii ( url )
 iI = re . compile ( '<iframe width=".+?" height=".+?" src="(.+?)" allowfullscreen></iframe>' ) . findall ( i11I1IIiiIi )
 for url in iI :
  i11I1IIiiIi = IiI1iiiIii ( url )
  iIiIi11 = 'http:' + re . compile ( '<iframe width="100%" height="100%" src="(.+?)" allowfullscreen></iframe>' ) . findall ( i11I1IIiiIi ) [ 0 ]
  iIiIi11 = urlresolver . HostedMediaFile ( iIiIi11 ) . resolve ( )
  VeevVV = xbmcgui . ListItem ( name , iconImage = 'DefaultVideo.png' , thumbnailImage = iconimage )
  VeevVV . setPath ( iIiIi11 )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , VeevVV )
  if 43 - 43: Veeve . I1ii / VVVevV
  if 20 - 20: VevVVe
def eeveVevevevee ( name , url , iconimage , fanart ) :
 i11I1IIiiIi = IiI1iiiIii ( url )
 eeeveveev = re . compile ( '<h2 id=".+?">(.+?)</h2>.+?<p><span class="article__image article__image--undefined"><img src="(.+?)" alt=".+?"></span> </p>.+?<p><strong>(.+?)</strong>(.+?)<' , re . DOTALL ) . findall ( i11I1IIiiIi )
 for iI1iII1 , iconimage , eeveveev , II1IIIII in eeeveveev :
  name = name . replace ( "&#8217;" , "'" ) . replace ( '&amp;' , ' & ' )
  i1I111I ( '[COLOR yellow]%s [/COLOR] ' % iI1iII1 + '[COLOR yellow]%s[/COLOR]' % eeveveev + '[COLOR white]%s[/COLOR]' % II1IIIII , url , 35 , iconimage , fanart )
def II1I ( name , url , iconimage , fanart ) :
 i11I1IIiiIi = IiIiIi ( 'http://matsbuilds.uk/Menus/Movies/EvolveLatest/mainmenu.xml' )
 eeeveveev = re . compile ( '<item>(.+?)</item>' ) . findall ( i11I1IIiiIi )
 for iI11iiiI1II in eeeveveev :
  eeveV ( name , url , iconimage , fanart , iI11iiiI1II )
  if 12 - 12: eeveee - VVVevV % Veveevev * VVeVeeevevee
  if 44 - 44: IiiIII111ii % i11IiIiiIIIII
  if 41 - 41: Ii - VVeVeeevevee - i11IiIiiIIIII
  if 8 - 8: VVeevevev + IiIi1Iii1I1 - eeveee % II1Iiii1111i % eeveee * I1ii
  if 9 - 9: II1Iiii1111i - i11iIiiIii - eVVVeeveevV * i11IiIiiIIIII + VevevVevVevVev
def iIIII ( name , url , iconimage , fanarts ) :
 i11I1IIiiIi = IIIIiI11I11 ( url )
 eeeveveev = re . compile ( '<div class="thumb" id="post-.+?">.+?<a href="(.+?)" title="Watch (.+?) Online"><img width=".+?" height=".+?" src="(.+?)" class="attachment-post-thumbnail size-post-thumbnail wp-post-image" alt=".+?" />' , re . DOTALL ) . findall ( i11I1IIiiIi )
 for url , name , iconimage in eeeveveev :
  i1I111I ( name , url , 46 , iconimage , iconimage )
  if 45 - 45: VVVevV % VevVVe - i11iIiiIii
def ii1iiIiIII1ii ( name , url , iconimage , fanarts ) :
 i11I1IIiiIi = IIIIiI11I11 ( url )
 eeeveveev = re . compile ( '<div class="thumb" id="post-.+?">.+?<a href="(.+?)" title="Watch (.+?) Online"><img width=".+?" height=".+?" src="(.+?)" class="attachment-post-thumbnail size-post-thumbnail wp-post-image" alt=".+?" />' , re . DOTALL ) . findall ( i11I1IIiiIi )
 for url , name , iconimage in eeeveveev :
  i1I111I ( name , url , 46 , iconimage , iconimage )
  if 82 - 82: IiiIII111ii
def Veve ( name , url , iconimage , fanarts ) :
 i11I1IIiiIi = IIIIiI11I11 ( url )
 eeeveveev = re . compile ( '<div class="thumb">.+?<a href="(.+?)" title="Watch (.+?) Online"><img width=".+?" height=".+?" src="(.+?)" class="attachment-post-thumbnail size-post-thumbnail wp-post-image"' , re . DOTALL ) . findall ( i11I1IIiiIi )
 for url , name , iconimage in eeeveveev :
  i1I111I ( name , url , 46 , iconimage , iconimage )
  if 18 - 18: VVVevV
def eeVVeV ( name , url , iconimage , fanarts ) :
 eVevVVeeevVV = [ ]
 Vevii1ii1ii = [ ]
 I1i11i = [ ]
 i11I1IIiiIi = IiI1iiiIii ( url )
 VVeveeveevev = re . compile ( '<a href="(.+?)" title=".+?" rel="nofollow" target="blank">.+?</a><br/>' ) . findall ( i11I1IIiiIi )
 iIiIIIi = 1
 eVevVVeeevVV = [ ]
 Vevii1ii1ii = [ ]
 for IiIi1I1 in VVeveeveevev :
  IIi1IiiiI1Ii = VevevevVVeevevee ( IiIi1I1 )
  if '//' in IiIi1I1 : IiIIi1 = IiIi1I1 . split ( '/' ) [ 2 ] . split ( '.' ) [ 0 ]
  else : IiIIi1 = IiIi1I1
  name = "Link " + str ( iIiIIIi ) + ' | ' + IiIIi1 + IIi1IiiiI1Ii
  if IiIIi1 != 'www' :
   eeevVVe ( IiIIi1 , IiIi1I1 , 2 , iconimage , eeeevVV , description = '' )
   if 11 - 11: VevVVe / Veeve + eeveee * VVVevV - VVVevV - VevVVe
   if 85 - 85: VVeVeeevevee % I1ii / iiI1i1 . iiI1i1
def VeevVevVeveeVevV ( name , url , iconimage , fanart , item ) :
 name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 url = re . compile ( '<lbscraper>(.+?)</lbscraper>' ) . findall ( item ) [ 0 ]
 fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( item ) [ 0 ]
 i1I111I ( name , url , 10 , iconimage , fanart )
 if 31 - 31: eeveee % VVeevevev
def iI1I ( name , url , iconimage , fanart ) :
 eVVeev = VeeVeVe ( name , url , iconimage )
 iI = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( eVVeev )
 for iI11iiiI1II in iI :
  eeveV ( name , url , iconimage , fanart , iI11iiiI1II )
  if 14 - 14: eeveee * eVVVeeveevV + IiiIII111ii + Ii11111i + i11iIiiIii
def VeeVeVe ( name , url , iconimage ) :
 i111iIi1i1II1 = url
 eVeVev = ''
 if url == 'mamahd' :
  i11I1IIiiIi = IIIIiI11I11 ( "http://mamahd.com" ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
  Veev = re . compile ( '<a href="(.+?)">.+?<img src="(.+?)"></div>.+?<div class="home cell">.+?<span>(.+?)</span>.+?<span>(.+?)</span>.+?</a>' ) . findall ( i11I1IIiiIi )
  for url , iconimage , eeevVeveeveveevV , I11i1II in Veev :
   eVeVev = eVeVev + '<item>\n<title>%s vs %s</title>\n<sportsdevil>%s</sportsdevil>\n<thumbnail>%s</thumbnail>\n<fanart>fanart</fanart>\n</item>\n\n' % ( eeevVeveeveveevV , I11i1II , url , iconimage )
  return eVeVev
  if 72 - 72: iiI1i1 . Ii / II1Iiii1111i . Veeve
 elif url == 'cricfree' :
  i11I1IIiiIi = IIIIiI11I11 ( "http://cricfree.sc/football-live-stream" )
  eeeeveveveevevev = re . compile ( '<td><span class="sport-icon(.+?)</tr>' , re . DOTALL ) . findall ( i11I1IIiiIi )
  for VeveVevVVeVVVeveV in eeeeveveveevevev :
   I1ii11 = re . compile ( '<td>(.+?)<br(.+?)</td>' ) . findall ( VeveVevVVeVVVeveV )
   for eVeVeVeeev , II1IIIII in I1ii11 :
    eVeVeVeeev = '[COLOR yellow]' + eVeVeVeeev + '[/COLOR]'
    II1IIIII = II1IIIII . replace ( '>' , '' )
   time = re . compile ( '<td class="matchtime" style="color:#545454;font-weight:bold;font-size: 9px">(.+?)</td>' ) . findall ( VeveVevVVeVVVeveV ) [ 0 ]
   time = '[COLOR white](' + time + ')[/COLOR]'
   III1ii1I = re . compile ( '<a style="text-decoration:none !important;color:#545454;" href="(.+?)" target="_blank">(.+?)</a></td>' ) . findall ( VeveVevVVeVVVeveV )
   for url , Ii1i1iI in III1ii1I :
    url = url
    Ii1i1iI = Ii1i1iI
   eVeVev = eVeVev + '\n<item>\n<title>%s</title>\n<sportsdevil>%s</sportsdevil>\n' % ( eVeVeVeeev + ' ' + time + ' - ' + Ii1i1iI , url )
   eVeVev = eVeVev + '<thumbnail>iconimage</thumbnail>\n<fanart>fanart</fanart>\n</item>\n'
  return eVeVev
  if 16 - 16: eVVVeeveevV / II1Iiii1111i / VeeevVVeveVV * VevVVe + Ii % eVVVeeveevV
 elif url == 'bigsports' :
  i11I1IIiiIi = IIIIiI11I11 ( "http://www.bigsports.me/cat/4/football-live-stream.html" )
  Veev = re . compile ( '<td>.+?<td>(.+?)\-(.+?)\-(.+?)</td>.+?<td>(.+?)\:(.+?)</td>.+?<td>Football</td>.+?<td><strong>(.+?)</strong></td>.+?<a target=.+? href=(.+?) class=.+?' , re . DOTALL ) . findall ( i11I1IIiiIi )
  for eVeVeVeeev , eeeeveevev , eeV , eeveevev , IIieVeVeveveeevV , name , url in Veev :
   if not '</td>' in eVeVeVeeev :
    url = url . replace ( '"' , '' )
    II1IIIII = eVeVeVeeev + ' ' + eeeeveevev + ' ' + eeV
    time = eeveevev + ':' + IIieVeVeveveeevV
    II1IIIII = '[COLOR yellow]' + II1IIIII + '[/COLOR]'
    time = '[COLOR cyan](' + time + ')[/COLOR]'
    eVeVev = eVeVev + '\n<item>\n<title>%s</title>\n<sportsdevil>%s</sportsdevil>\n' % ( II1IIIII + ' ' + time + ' ' + name , url )
    eVeVev = eVeVev + '<thumbnail>iconimage</thumbnail>\n<fanart>fanart</fanart>\n</item>\n'
  return eVeVev
  if 39 - 39: iiI1i1 / Ii11111i / I1ii - i11IiIiiIIIII - IiiIII111ii % eVVVeeveevV
  if 31 - 31: VVeVeeevevee - Ii11111i / VevevVevVevVev * Veveevev
def Veveev ( name , url , iconimage , fanart , item ) :
 name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 iI111i1II = re . compile ( '<oktitle>(.+?)</oktitle>' ) . findall ( item ) [ 0 ]
 VeveeeeeevVVVVev = re . compile ( '<line1>(.+?)</line1>' ) . findall ( item ) [ 0 ]
 IiiIi1III = re . compile ( '<line2>(.+?)</line2>' ) . findall ( item ) [ 0 ]
 VevVe = re . compile ( '<line3>(.+?)</line3>' ) . findall ( item ) [ 0 ]
 ii11i11i1 = '##' + iI111i1II + '#' + VeveeeeeevVVVVev + '#' + IiiIi1III + '#' + VevVe + '##'
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( item ) [ 0 ]
 iII ( name , ii11i11i1 , 17 , iconimage , fanart )
 if 53 - 53: VeeevVVeveVV % i11IiIiiIIIII . i1iIIi1 / i11iIiiIii % IiiIII111ii
def iIiIIIIIii ( name , url ) :
 VVeev = re . compile ( '##(.+?)##' ) . findall ( url ) [ 0 ] . split ( '#' )
 VevVeveeVVV = xbmcgui . Dialog ( )
 VevVeveeVVV . ok ( VVeev [ 0 ] , VVeev [ 1 ] , VVeev [ 2 ] , VVeev [ 3 ] )
 if 25 - 25: VeeevVVeveVV + i1iIIi1 * VVVevV
def IIIIii ( name , url , iconimage , fanart , item ) :
 url = re . compile ( '<redirect>(.+?)</redirect>' ) . findall ( item ) [ 0 ]
 VeVVVeveveVVev ( 'name' , url , 'iconimage' , 'fanart' )
 if 92 - 92: VevVVe + VVeVeeevevee + Ii11111i / eeveee + IiIi1Iii1I1
def iIi11Ii1 ( name , url , iconimage , fanart , item ) :
 name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 ii11i11i1 = re . compile ( '<text>(.+?)</text>' ) . findall ( item ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( item ) [ 0 ]
 iII ( name , ii11i11i1 , 9 , iconimage , fanart )
 if 18 - 18: VevevVevVevVev * Veveevev . IiiIII111ii / VVVevV / i11iIiiIii
def IIIII ( name , url ) :
 eeveeVeVeveveveV = IiI1iiiIii ( url )
 VVe ( name , eeveeVeVeveveveV )
 if 50 - 50: VevevVevVevVev
def iI1iI1I1i1I ( name , url , iconimage , fanart , item ) :
 eevVevVeveeeeveVV = re . compile ( '<image>(.+?)</image>' ) . findall ( item )
 if len ( eevVevVeveeeeveVV ) == 1 :
  name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
  iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
  eeevevev = re . compile ( '<image>(.+?)</image>' ) . findall ( item ) [ 0 ]
  fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( item ) [ 0 ]
  iII ( name , eeevevev , 7 , iconimage , fanart )
 elif len ( eevVevVeveeeeveVV ) > 1 :
  name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
  iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
  fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( item ) [ 0 ]
  iiVeV = ''
  for eeevevev in eevVevVeveeeeveVV : iiVeV = iiVeV + '<image>' + eeevevev + '</image>'
  Ii1iI = eeVe
  name = i1 ( name )
  Iiiiii111i1ii = os . path . join ( os . path . join ( Ii1iI , '' ) , name + '.txt' )
  if not os . path . exists ( Iiiiii111i1ii ) : file ( Iiiiii111i1ii , 'w' ) . close ( )
  i1i1iII1 = open ( Iiiiii111i1ii , "w" )
  i1i1iII1 . write ( iiVeV )
  i1i1iII1 . close ( )
  iII ( name , 'image' , 8 , iconimage , fanart )
  if 25 - 25: iiI1i1 % IiiIII111ii . VevevVevVevVev
def II1III ( name , url , iconimage , fanart , item ) :
 name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
 url = re . compile ( '<iptv>(.+?)</iptv>' ) . findall ( item ) [ 0 ]
 fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( item ) [ 0 ]
 i1I111I ( name , url , 6 , iconimage , fanart )
 if 14 - 14: I1ii + VVVevV - IiiIII111ii / Ii11111i . IiIi1Iii1I1
def i1iiIiI1Ii1i ( url , iconimage ) :
 i11I1IIiiIi = IiI1iiiIii ( url )
 i1iIi = re . compile ( '^#.+?:-?[0-9]*(.*?),(.*?)\n(.*?)$' , re . I + re . M + re . U + re . S ) . findall ( i11I1IIiiIi )
 iiiii1II = [ ]
 for VevVVVevVVeeeevev , Ii11iii11I , url in i1iIi :
  I111iIi1 = { "params" : VevVVVevVVeeeevev , "name" : Ii11iii11I , "url" : url }
  iiiii1II . append ( I111iIi1 )
 list = [ ]
 for eVVeeevevevevVeveev in iiiii1II :
  I111iIi1 = { "name" : eVVeeevevevevVeveev [ "name" ] , "url" : eVVeeevevevevVeveev [ "url" ] }
  i1iIi = re . compile ( ' (.+?)="(.+?)"' , re . I + re . M + re . U + re . S ) . findall ( eVVeeevevevevVeveev [ "params" ] )
  for eeevevVeveveVeveveve , VVeevevVeV in i1iIi :
   I111iIi1 [ eeevevVeveveVeveveve . strip ( ) . lower ( ) . replace ( '-' , '_' ) ] = VVeevevVeV . strip ( )
  list . append ( I111iIi1 )
 for eVVeeevevevevVeveev in list :
  if '.ts' in eVVeeevevevevVeveev [ "url" ] : iII ( eVVeeevevevevVeveev [ "name" ] , eVVeeevevevevVeveev [ "url" ] , 2 , iconimage , eeeevVV )
  else : eeevVVe ( eVVeeevevevevVeveev [ "name" ] , eVVeeevevevevVeveev [ "url" ] , 2 , iconimage , eeeevVV )
  if 10 - 10: eeveee / i11iIiiIii
def VevevVeeveveveeVev ( name , url , iconimage , fanart , item ) :
 IIi1IiiiI1Ii = ''
 eevev = re . compile ( '<link>(.+?)</link>' ) . findall ( item )
 VeveeeeevVeevev = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( item )
 for name , eV , iconimage , fanart in VeveeeeevVeevev :
  if 'youtube.com/playlist?' in eV :
   VeveVVeeeVVevV = eV . split ( 'list=' ) [ 1 ]
   i1I111I ( name , eV , iiI , iconimage , fanart , description = VeveVVeeeVVevV )
 if len ( eevev ) == 1 :
  VeveeeeevVeevev = re . compile ( '<title>(.+?)</title>.+?link>(.+?)</link>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( item )
  for name , url , iconimage , fanart in VeveeeeevVeevev :
   try :
    IIi1IiiiI1Ii = VevevevVVeevevee ( url )
    VevevVevVeeeeevev = url . split ( '/' ) [ 2 ] . replace ( 'www.' , '' )
    if 'SportsDevil' in url : VevevVevVeeeeevev = ''
   except : pass
   if '.ts' in url : eeevVVe ( name , url , 16 , iconimage , fanart , description = '' )
   if '<meta>' in item :
    VeeeveVeeeev = re . compile ( '<meta>(.+?)</meta>' ) . findall ( item ) [ 0 ]
    i1Veevev ( name + IIi1IiiiI1Ii , url , 2 , iconimage , 10 , VeeeveVeeeev , isFolder = False )
   else :
    eeevVVe ( name + IIi1IiiiI1Ii , url , 2 , iconimage , fanart )
 elif len ( eevev ) > 1 :
  name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
  iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
  fanart = re . compile ( '<fanart>(.+?)</fanart>' ) . findall ( item ) [ 0 ]
  if '.ts' in url : eeevVVe ( name , url , 16 , iconimage , fanart , description = '' )
  if '<meta>' in item :
   VeeeveVeeeev = re . compile ( '<meta>(.+?)</meta>' ) . findall ( item ) [ 0 ]
   i1Veevev ( name , url , 3 , iconimage , len ( eevev ) , VeeeveVeeeev , isFolder = True )
  else :
   i1I111I ( name , url , 3 , iconimage , fanart )
   if 97 - 97: VevevVevVevVev / IiIi1Iii1I1 % Ii % VVVevV
   if 18 - 18: iiI1i1 % VVeVeeevevee
def i11 ( name , url , iconimage , fanart , item ) :
 eevev = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( item )
 VeveveVev = re . compile ( '<link>(.+?)</link>' ) . findall ( item )
 if len ( eevev ) + len ( VeveveVev ) == 1 :
  name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
  iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
  url = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( item ) [ 0 ]
  url = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + url
  iII ( name , url , 16 , iconimage , fanart )
 elif len ( eevev ) + len ( VeveveVev ) > 1 :
  name = re . compile ( '<title>(.+?)</title>' ) . findall ( item ) [ 0 ]
  iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( item ) [ 0 ]
  i1I111I ( name , url , 3 , iconimage , fanart )
  if 97 - 97: IiIi1Iii1I1 - iiI1i1
def Iii111II ( link ) :
 if eVeveveVe == '' :
  VevVeveeVVV = xbmcgui . Dialog ( )
  VVeVVeveeveev = VevVeveeVVV . yesno ( 'Adult Content' , 'You have found the goodies ;)' , '' , 'Please set a password to prevent accidental access' , 'Cancel' , 'OK' )
  if VVeVVeveeveev == 1 :
   eevVeevev = xbmc . Keyboard ( '' , 'Set Password' )
   eevVeevev . doModal ( )
   if ( eevVeevev . isConfirmed ( ) ) :
    eeeveevVevVeeeee = eevVeevev . getText ( )
    VevVevVVevVevVev . setSetting ( 'password' , eeeveevVevVeeeee )
  else : quit ( )
 elif eVeveveVe <> '' :
  VevVeveeVVV = xbmcgui . Dialog ( )
  VVeVVeveeveev = VevVeveeVVV . yesno ( 'Adult Content' , 'Please enter the password you set!' , 'to continue' , 'dirty git' , 'Cancel' , 'OK' )
  if VVeVVeveeveev == 1 :
   eevVeevev = xbmc . Keyboard ( '' , 'Enter Password' )
   eevVeevev . doModal ( )
   if ( eevVeevev . isConfirmed ( ) ) :
    eeeveevVevVeeeee = eevVeevev . getText ( )
   if eeeveevVevVeeeee <> eVeveveVe :
    quit ( )
  else : quit ( )
  if 1 - 1: VevevVevVevVev % Veveevev * II1Iiii1111i
def eevVeveeev ( name , url , iconimage ) :
 iiiI1I1iIIIi1 = ''
 iII1i1I1II = i1 ( name )
 VevVevVVevVevVev . setSetting ( 'tv' , iII1i1I1II )
 i11I1IIiiIi = IiIiIi ( url )
 Iii = re . compile ( '<title>.*?' + re . escape ( name ) + '.*?</title>(.+?)</item>' , re . DOTALL ) . findall ( i11I1IIiiIi ) [ 0 ]
 iconimage = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( Iii ) [ 0 ]
 eevev = [ ]
 if '<link>' in Iii :
  I1iiiiI1iI = re . compile ( '<link>(.+?)</link>' ) . findall ( Iii )
  for iIiiiii1i in I1iiiiI1iI :
   eevev . append ( iIiiiii1i )
 if '<sportsdevil>' in Iii :
  iiIi1IIiI = re . compile ( '<sportsdevil>(.+?)</sportsdevil>' ) . findall ( Iii )
  for i1eVevVVev in iiIi1IIiI :
   i1eVevVVev = 'plugin://plugin.video.SportsDevil/?mode=1&amp;item=catcher%3dstreams%26url=' + i1eVevVVev
   eevev . append ( i1eVevVVev )
 iIiIIIi = 1
 for i11I1IIiiIi in eevev :
  if '(' in i11I1IIiiIi :
   i11I1IIiiIi = i11I1IIiiIi . split ( '(' )
   iiiI1I1iIIIi1 = i11I1IIiiIi [ 1 ] . replace ( ')' , '' )
   i11I1IIiiIi = i11I1IIiiIi [ 0 ]
  IIi1IiiiI1Ii = VevevevVVeevevee ( i11I1IIiiIi )
  VevevVevVeeeeevev = i11I1IIiiIi . split ( '/' ) [ 2 ] . replace ( 'www.' , '' )
  if iiiI1I1iIIIi1 <> '' : name = "Link " + str ( iIiIIIi ) + ' | ' + iiiI1I1iIIIi1 + IIi1IiiiI1Ii
  else : name = "Link " + str ( iIiIIIi ) + ' | ' + VevevVevVeeeeevev + IIi1IiiiI1Ii
  iIiIIIi = iIiIIIi + 1
  i1Veevev ( name , i11I1IIiiIi , 2 , iconimage , 10 , '' , isFolder = False , description = VevVevVVevVevVev . getSetting ( 'tv' ) )
  if 82 - 82: i1iIIi1 - i1iIIi1 + Veveevev
def i1i1i11IIi ( name , url , iconimage , fanart , item ) :
 VeveeeeevVeevev = re . compile ( '<title>(.+?)</title>.+?folder>(.+?)</folder>.+?thumbnail>(.+?)</thumbnail>.+?fanart>(.+?)</fanart>' ) . findall ( item )
 for name , url , iconimage , fanart in VeveeeeevVeevev :
  if 'youtube.com/channel/' in url :
   VeveVVeeeVVevV = url . split ( 'channel/' ) [ 1 ]
   i1I111I ( name , url , iiI , iconimage , fanart , description = VeveVVeeeVVevV )
  elif 'youtube.com/user/' in url :
   VeveVVeeeVVevV = url . split ( 'user/' ) [ 1 ]
   i1I111I ( name , url , iiI , iconimage , fanart , description = VeveVVeeeVVevV )
  elif 'youtube.com/playlist?' in url :
   VeveVVeeeVVevV = url . split ( 'list=' ) [ 1 ]
   i1I111I ( name , url , iiI , iconimage , fanart , description = VeveVVeeeVVevV )
  elif 'plugin://' in url :
   II111Ii1i1 = HTMLParser ( )
   url = II111Ii1i1 . unescape ( url )
   i1I111I ( name , url , iiI , iconimage , fanart )
  else :
   i1I111I ( name , url , 1 , iconimage , fanart )
   if 98 - 98: VVeevevev . VVeevevev * I1ii * Veeve * IiIi1Iii1I1
def eVeeVev ( ) :
 eevVeevev = xbmc . Keyboard ( '' , '[B][COLOR cyan]What Would You Like Me To Find?[/COLOR][/B]' )
 eevVeevev . doModal ( )
 if ( eevVeevev . isConfirmed ( ) ) :
  VeveVVeeeVVevV = eevVeevev . getText ( )
  VeveVVeeeVVevV = VeveVVeeeVVevV . upper ( )
 else : quit ( )
 i11I1IIiiIi = IiIiIi ( 'http://matsbuilds.uk/Menus/anewEvolvemenu/search.xml' )
 ii1 = re . compile ( '<link>(.+?)</link>' ) . findall ( i11I1IIiiIi )
 for VeI1Ii11I1Ii1i in ii1 :
  try :
   i11I1IIiiIi = IiIiIi ( VeI1Ii11I1Ii1i )
   I1i11 = re . compile ( '<item>(.+?)</item>' ) . findall ( i11I1IIiiIi )
   for iI11iiiI1II in I1i11 :
    iI = re . compile ( '<title>(.+?)</title>' ) . findall ( iI11iiiI1II )
    for iI1iII1 in iI :
     iI1iII1 = iI1iII1 . upper ( )
     if VeveVVeeeVVevV in iI1iII1 :
      eeveV ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV , iI11iiiI1II )
  except : pass
  if 79 - 79: VVeevevev - iiI1i1 + i11IiIiiIIIII - IiIi1Iii1I1
def VeV ( url ) :
 eVeVev = "ShowPicture(%s)" % url
 xbmc . executebuiltin ( eVeVev )
 if 35 - 35: Veveevev + i11iIiiIii - Veeve
def Ii1ii111i1 ( name , url , iconimage , description ) :
 if description : name = description
 try :
  if 'plugin://plugin.video.SportsDevil/' in url :
   i1i1i1I ( name , url , iconimage )
  elif '.ts' in url :
   url = 'plugin://plugin.video.f4mTester/?streamtype=TSDOWNLOADER&amp;name=' + name + '&amp;url=' + url
   url = url . replace ( '|' , '' )
   i1i1i1I ( name , url , iconimage )
  elif urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
   url = urlresolver . HostedMediaFile ( url ) . resolve ( )
   eVeeevevev ( name , url , iconimage )
  elif liveresolver . isValid ( url ) == True :
   url = liveresolver . resolve ( url )
   eVeeevevev ( name , url , iconimage )
  else : eVeeevevev ( name , url , iconimage )
 except :
  VeeVeeveve ( IiI11i1IIiiI ( 'Picasso' ) , 'Stream Unavailable' , '3000' , Veveveeeeeevev )
  if 60 - 60: VVVevV * VevVVe
def VVVevVVVevevee ( url ) :
 if urlresolver . HostedMediaFile ( url ) . valid_url ( ) :
  url = urlresolver . HostedMediaFile ( url ) . resolve ( )
 xbmc . Player ( ) . play ( url )
 if 17 - 17: eVVVeeveevV % II1Iiii1111i / VVVevV . i1iIIi1 * eVVVeeveevV - Veeve
def eVeeevevev ( name , url , iconimage ) :
 VeeevVVeVeVev = True
 VeevVV = xbmcgui . ListItem ( name , iconImage = iconimage , thumbnailImage = iconimage ) ; VeevVV . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 VeeevVVeVeVev = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = VeevVV )
 VeevVV . setPath ( url )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , VeevVV )
 if 41 - 41: i11IiIiiIIIII
def i1i1i1I ( name , url , iconimage ) :
 xbmc . executebuiltin ( 'Dialog.Close(all,True)' )
 VeeevVVeVeVev = True
 VeevVV = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage ) ; VeevVV . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 VeeevVVeVeVev = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = url , listitem = VeevVV )
 xbmc . Player ( ) . play ( url , VeevVV , False )
 if 77 - 77: IiIi1Iii1I1
def VeeVVVVeVevevVeVV ( url ) :
 xbmc . executebuiltin ( "PlayMedia(%s)" % url )
 if 85 - 85: I1ii - iiI1i1 / Ii11111i
def IiIiIi ( url ) :
 VeeveveeevevevevVV = urllib2 . Request ( url )
 VeeveveeevevevevVV . add_header ( base64 . b64decode ( 'VXNlci1BZ2VudA==' ) , base64 . b64decode ( 'dTM0ODczZWpyZGU4dTkyM2pxdzlkaXUy' ) )
 VeveVVeevVe = urllib2 . urlopen ( VeeveveeevevevevVV )
 i11I1IIiiIi = VeveVVeevVe . read ( )
 VeveVVeevVe . close ( )
 if '{' in i11I1IIiiIi :
  eVeVev = i11I1IIiiIi [ : : - 1 ]
  eVeVev = eVeVev . replace ( '}' , '' ) . replace ( '{' , '' ) . replace ( ',' , '' ) . replace ( ']' , '' ) . replace ( '[' , '' )
  eVeVev = eVeVev + '=='
  i11I1IIiiIi = eVeVev . decode ( 'base64' )
 i11I1IIiiIi = i11I1IIiiIi . replace ( '<fanart></fanart>' , '<fanart>x</fanart>' ) . replace ( '<thumbnail></thumbnail>' , '<thumbnail>x</thumbnail>' ) . replace ( '<utube>' , '<link>https://www.youtube.com/watch?v=' ) . replace ( '</utube>' , '</link>' )
 if url <> IiI : i11I1IIiiIi = i11I1IIiiIi . replace ( '\n' , '' ) . replace ( '\r' , '' )
 print i11I1IIiiIi
 return i11I1IIiiIi
 if 73 - 73: i11IiIiiIIIII - IiIi1Iii1I1
def IiI1iiiIii ( url ) :
 VeeveveeevevevevVV = urllib2 . Request ( url )
 VeeveveeevevevevVV . add_header ( base64 . b64decode ( 'VXNlci1BZ2VudA==' ) , base64 . b64decode ( 'dTM0ODczZWpyZGU4dTkyM2pxdzlkaXUy' ) )
 VeveVVeevVe = urllib2 . urlopen ( VeeveveeevevevevVV )
 i11I1IIiiIi = VeveVVeevVe . read ( )
 VeveVVeevVe . close ( )
 return i11I1IIiiIi
 if 68 - 68: IiiIII111ii * VeeevVVeveVV * iiI1i1 . Veeve
def IIIIiI11I11 ( url ) :
 VeeveveeevevevevVV = urllib2 . Request ( url )
 VeeveveeevevevevVV . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3' )
 VeveVVeevVe = urllib2 . urlopen ( VeeveveeevevevevVV )
 i11I1IIiiIi = VeveVVeevVe . read ( )
 VeveVVeevVe . close ( )
 i11I1IIiiIi = i11I1IIiiIi . replace ( '\n' , '' ) . replace ( '\r' , '' )
 return i11I1IIiiIi
 if 81 - 81: eVVVeeveevV / Ii11111i + VVeVeeevevee + i11IiIiiIIIII / VevVVe
 if 27 - 27: Veveevev * i1iIIi1
def VevVeeevee ( ) :
 IIi11IIiIii1 = [ ]
 I1iIII1 = sys . argv [ 2 ]
 if len ( I1iIII1 ) >= 2 :
  VevVVVevVVeeeevev = sys . argv [ 2 ]
  iIii = VevVVVevVVeeeevev . replace ( '?' , '' )
  if ( VevVVVevVVeeeevev [ len ( VevVVVevVVeeeevev ) - 1 ] == '/' ) :
   VevVVVevVVeeeevev = VevVVVevVVeeeevev [ 0 : len ( VevVVVevVVeeeevev ) - 2 ]
  eVeevVeVVeev = iIii . split ( '&' )
  IIi11IIiIii1 = { }
  for iIiIIIi in range ( len ( eVeevVeVVeev ) ) :
   iII11I1Ii1 = { }
   iII11I1Ii1 = eVeevVeVVeev [ iIiIIIi ] . split ( '=' )
   if ( len ( iII11I1Ii1 ) ) == 2 :
    IIi11IIiIii1 [ iII11I1Ii1 [ 0 ] ] = iII11I1Ii1 [ 1 ]
 return IIi11IIiIii1
 if 92 - 92: VVeVeeevevee / VVeVeeevevee . VVVevV
def VeeVeeveve ( title , message , ms , nart ) :
 xbmc . executebuiltin ( "XBMC.notification(" + title + "," + message + "," + ms + "," + nart + ")" )
 if 17 - 17: i11iIiiIii - Veeve * eeveee
def i1 ( string ) :
 IIi1IIIIi = re . compile ( '(\[.+?\])' ) . findall ( string )
 for VVVeV in IIi1IIIIi : string = string . replace ( VVVeV , '' )
 return string
 if 14 - 14: VVeVeeevevee . iiI1i1 . VeeevVVeveVV . Veeve / eeveee
def IiI11i1IIiiI ( string ) :
 string = string . split ( ' ' )
 IiIi1 = ''
 for i111iiI1ii in string :
  IIiii = '[B][COLOR yellow]' + i111iiI1ii [ 0 ] . upper ( ) + '[/COLOR][COLOR white]' + i111iiI1ii [ 1 : ] + '[/COLOR][/B] '
  IiIi1 = IiIi1 + IIiii
 return IiIi1
 if 30 - 30: VVeVeeevevee / i11IiIiiIIIII . i1iIIi1 . VeeevVVeveVV - II1Iiii1111i
def i1Veevev ( name , url , mode , iconimage , itemcount , metatype , isFolder = False , description = '' ) :
 if isFolder == True : VevVevVVevVevVev . setSetting ( 'favtype' , 'folder' )
 else : VevVevVVevVevVev . setSetting ( 'favtype' , 'link' )
 if VVVeev == 'true' :
  Ii1iI1iI11I1 = name
  name = i1 ( name )
  I1 = ""
  i11iIIi11 = ""
  eeVeeeevevevVVevev = [ ]
  IiIiI1I1I1 = eval ( base64 . b64decode ( 'bWV0YWhhbmRsZXJzLk1ldGFEYXRhKHRtZGJfYXBpX2tleT0iZDk1NWQ4ZjAyYTNmMjQ4MGE1MTg4MWZlNGM5NmYxMGUiKQ==' ) )
  IIi = { }
  if metatype == 'movie' :
   eeeeeVeeeveee = name . partition ( '(' )
   if len ( eeeeeVeeeveee ) > 0 :
    I1 = eeeeeVeeeveee [ 0 ]
    i11iIIi11 = eeeeeVeeeveee [ 2 ] . partition ( ')' )
   if len ( i11iIIi11 ) > 0 :
    i11iIIi11 = i11iIIi11 [ 0 ]
   IIi = IiIiI1I1I1 . get_meta ( 'movie' , name = I1 , year = i11iIIi11 )
   if not IIi [ 'trailer' ] == '' : eeVeeeevevevVVevev . append ( ( IiI11i1IIiiI ( 'Play Trailer' ) , 'XBMC.RunPlugin(%s)' % VeevVee . build_plugin_url ( { 'mode' : 11 , 'url' : IIi [ 'trailer' ] } ) ) )
  elif metatype == 'tvep' :
   iI1iII1 = VevVevVVevVevVev . getSetting ( 'tv' )
   if '<>' in url :
    print url
    eeevevVeveveV = url . split ( '<>' ) [ 0 ]
    eeveveVVeve = url . split ( '<>' ) [ 1 ]
    VVVevevV = url . split ( '<>' ) [ 2 ]
    VVeVVeveeeveeV = url . split ( '<>' ) [ 3 ]
    VeveevVevevVeeveev = url . split ( '<>' ) [ 4 ]
    VevevVeveVVevevVevev = url . split ( '<>' ) [ 5 ]
    IIi = IiIiI1I1I1 . get_episode_meta ( eeveveVVeve , imdb_id = eeevevVeveveV , season = VVVevevV , episode = VVeVVeveeeveeV , air_date = '' , episode_title = '' , overlay = '' )
   else :
    I11 = re . compile ( 'Season (.+?) Episode (.+?)\)' ) . findall ( name )
    for eeeveeVV , iI1IiIIiIIi in I11 :
     IIi = IiIiI1I1I1 . get_episode_meta ( iI1iII1 , imdb_id = '' , season = eeeveeVV , episode = iI1IiIIiIIi , air_date = '' , episode_title = '' , overlay = '' )
  try :
   if IIi [ 'cover_url' ] == '' : iconimage = iconimage
   else : iconimage = IIi [ 'cover_url' ]
  except : pass
  iiI11ii1I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( eeeevVV ) + "&iconimage=" + urllib . quote_plus ( iconimage )
  VeeevVVeVeVev = True
  VeevVV = xbmcgui . ListItem ( Ii1iI1iI11I1 , iconImage = iconimage , thumbnailImage = iconimage )
  VeevVV . setInfo ( type = "Video" , infoLabels = IIi )
  VeevVV . setProperty ( "IsPlayable" , "true" )
  VeevVV . addContextMenuItems ( eeVeeeevevevVVevev , replaceItems = False )
  if not IIi . get ( 'backdrop_url' , '' ) == '' : VeevVV . setProperty ( 'fanart_image' , IIi [ 'backdrop_url' ] )
  else : VeevVV . setProperty ( 'fanart_image' , eeeevVV )
  IiIi11Iii = VevVevVVevVevVev . getSetting ( 'favlist' )
  III1i1iI1 = [ ]
  III1i1iI1 . append ( ( IiI11i1IIiiI ( 'Stream Information' ) , 'XBMC.Action(Info)' ) )
  if IiIi11Iii == 'yes' : III1i1iI1 . append ( ( '[COLOR cyan]Remove From Keep Safe? [/COLOR]' , 'XBMC.RunPlugin(%s?mode=21&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
  else : III1i1iI1 . append ( ( '[COLOR cyan]Add To Keep Safe?[/COLOR]' , 'XBMC.RunPlugin(%s?mode=20&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
  VeevVV . addContextMenuItems ( III1i1iI1 , replaceItems = False )
  VeeevVVeVeVev = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiI11ii1I1 , listitem = VeevVV , isFolder = isFolder , totalItems = itemcount )
  return VeeevVVeVeVev
 else :
  if isFolder :
   i1I111I ( name , url , mode , iconimage , eeeevVV , description = '' )
  else :
   eeevVVe ( name , url , mode , iconimage , eeeevVV , description = '' )
   if 97 - 97: VVeVeeevevee - i11iIiiIii
def i1I111I ( name , url , mode , iconimage , fanart , description = '' ) :
 VevVevVVevVevVev . setSetting ( 'favtype' , 'folder' )
 iiI11ii1I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 VeeevVVeVeVev = True
 VeevVV = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 VeevVV . setInfo ( type = "Video" , infoLabels = { "Title" : name , 'plot' : description } )
 VeevVV . setProperty ( 'fanart_image' , fanart )
 if 'youtube.com/channel/' in url :
  iiI11ii1I1 = 'plugin://plugin.video.youtube/channel/' + description + '/'
 if 'youtube.com/user/' in url :
  iiI11ii1I1 = 'plugin://plugin.video.youtube/user/' + description + '/'
 if 'youtube.com/playlist?' in url :
  iiI11ii1I1 = 'plugin://plugin.video.youtube/playlist/' + description + '/'
 if 'plugin://' in url :
  iiI11ii1I1 = url
 III1i1iI1 = [ ]
 IiIi11Iii = VevVevVVevVevVev . getSetting ( 'favlist' )
 if IiIi11Iii == 'yes' : III1i1iI1 . append ( ( '[COLOR cyan]Remove From Keep Safe?[/COLOR]' , 'XBMC.RunPlugin(%s?mode=21&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
 else : III1i1iI1 . append ( ( '[COLOR cyan]Add To Keep Safe?[/COLOR]' , 'XBMC.RunPlugin(%s?mode=20&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
 VeevVV . addContextMenuItems ( III1i1iI1 , replaceItems = False )
 VeeevVVeVeVev = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiI11ii1I1 , listitem = VeevVV , isFolder = True )
 return VeeevVVeVeVev
 if 17 - 17: VVeVeeevevee
def iII ( name , url , mode , iconimage , fanart , description = '' ) :
 VevVevVVevVevVev . setSetting ( 'favtype' , 'link' )
 iiI11ii1I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 VeeevVVeVeVev = True
 VeevVV = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 VeevVV . setProperty ( 'fanart_image' , fanart )
 III1i1iI1 = [ ]
 IiIi11Iii = VevVevVVevVevVev . getSetting ( 'favlist' )
 if IiIi11Iii == 'yes' : III1i1iI1 . append ( ( '[COLOR cyan]Remove from Keep Safe?[/COLOR]' , 'XBMC.RunPlugin(%s?mode=21&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
 else : III1i1iI1 . append ( ( '[COLOR cyan]Add to Keeo Safe[/COLOR]' , 'XBMC.RunPlugin(%s?mode=20&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
 VeevVV . addContextMenuItems ( III1i1iI1 , replaceItems = False )
 VeeevVVeVeVev = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiI11ii1I1 , listitem = VeevVV , isFolder = False )
 return VeeevVVeVeVev
 if 73 - 73: I1ii
def eeevVVe ( name , url , mode , iconimage , fanart , description = '' ) :
 VevVevVVevVevVev . setSetting ( 'favtype' , 'link' )
 iiI11ii1I1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&description=" + str ( description ) + "&fanart=" + urllib . quote_plus ( fanart ) + "&iconimage=" + urllib . quote_plus ( iconimage )
 VeeevVVeVeVev = True
 VeevVV = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 VeevVV . setProperty ( 'fanart_image' , fanart )
 VeevVV . setProperty ( "IsPlayable" , "true" )
 III1i1iI1 = [ ]
 IiIi11Iii = VevVevVVevVevVev . getSetting ( 'favlist' )
 if IiIi11Iii == 'yes' : III1i1iI1 . append ( ( '[COLOR cyan]Remove from Keep Safe?[/COLOR]' , 'XBMC.RunPlugin(%s?mode=21&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
 else : III1i1iI1 . append ( ( '[COLOR cyan]Add to Keep Safe?[/COLOR]' , 'XBMC.RunPlugin(%s?mode=20&name=%s&url=%s&iconimage=%s)' % ( sys . argv [ 0 ] , name , url , iconimage ) ) )
 VeevVV . addContextMenuItems ( III1i1iI1 , replaceItems = False )
 VeeevVVeVeVev = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iiI11ii1I1 , listitem = VeevVV , isFolder = False )
 return VeeevVVeVeVev
II = base64 . b64decode ( 'aHR0cDovL21hdHNidWlsZHMudWsvTWVudXMvYW5ld0V2b2x2ZW1lbnUvRXZvbHZlTWFpbk1lbnUueG1s' )
def iii11iII ( url , name ) :
 II11iI = IiI1iiiIii ( url )
 if len ( II11iI ) > 1 :
  Ii1iI = eeVe
  Iiiiii111i1ii = os . path . join ( os . path . join ( Ii1iI , '' ) , name + '.txt' )
  if not os . path . exists ( Iiiiii111i1ii ) :
   file ( Iiiiii111i1ii , 'w' ) . close ( )
  VevVVeveVVe = open ( Iiiiii111i1ii )
  VVeveVeve = VevVVeveVVe . read ( )
  if VVeveVeve == II11iI : pass
  else :
   VVe ( '[B][COLOR yellow]PICASSO INFO[/COLOR][/B]' , II11iI )
   i1i1iII1 = open ( Iiiiii111i1ii , "w" )
   i1i1iII1 . write ( II11iI )
   i1i1iII1 . close ( )
   if 39 - 39: eeveee * VevevVevVevVev + i11IiIiiIIIII * Veeve
def VVe ( heading , text ) :
 id = 10147
 xbmc . executebuiltin ( 'ActivateWindow(%d)' % id )
 xbmc . sleep ( 500 )
 VeVeveveev = xbmcgui . Window ( id )
 VVeVeVevevVevVeve = 50
 while ( VVeVeVevevVevVeve > 0 ) :
  try :
   xbmc . sleep ( 10 )
   VVeVeVevevVevVeve -= 1
   VeVeveveev . getControl ( 1 ) . setLabel ( heading )
   VeVeveveev . getControl ( 5 ) . setText ( text )
   return
  except :
   pass
   if 12 - 12: VVVevV + VVeevevev % VVeVeeevevee
def eevVeeeveeveeeev ( name ) :
 global Icon
 global Next
 global Previous
 global window
 global Quit
 global images
 Iiiiii111i1ii = os . path . join ( os . path . join ( eeVe , '' ) , name + '.txt' )
 VevVVeveVVe = open ( Iiiiii111i1ii )
 VVeveVeve = VevVVeveVVe . read ( )
 images = re . compile ( '<image>(.+?)</image>' ) . findall ( VVeveVeve )
 VevVevVVevVevVev . setSetting ( 'pos' , '0' )
 window = pyxbmct . AddonDialogWindow ( '' )
 eeeveevevevevVeev = '/resources/art'
 eevVeveveVee = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + VVeve + eeeveevevevevVeev , 'next_focus.png' ) )
 VevevevVevVVevevee = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + VVeve + eeeveevevevevVeev , 'next1.png' ) )
 eVVV = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + VVeve + eeeveevevevevVeev , 'previous_focus.png' ) )
 eeeeveeeeev = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + VVeve + eeeveevevevevVeev , 'previous.png' ) )
 VVVeveee = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + VVeve + eeeveevevevevVeev , 'close_focus.png' ) )
 IIiiii = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + VVeve + eeeveevevevevVeev , 'close.png' ) )
 iI111i1I1II = xbmc . translatePath ( os . path . join ( 'special://home/addons/' + VVeve + eeeveevevevevVeev , 'main-bg1.png' ) )
 window . setGeometry ( 1300 , 720 , 100 , 50 )
 VevevVV = pyxbmct . Image ( iI111i1I1II )
 window . placeControl ( VevevVV , - 10 , - 10 , 130 , 70 )
 ii11i11i1 = '0xFF000000'
 Previous = pyxbmct . Button ( '' , focusTexture = eVVV , noFocusTexture = eeeeveeeeev , textColor = ii11i11i1 , focusedColor = ii11i11i1 )
 Next = pyxbmct . Button ( '' , focusTexture = eevVeveveVee , noFocusTexture = VevevevVevVVevevee , textColor = ii11i11i1 , focusedColor = ii11i11i1 )
 Quit = pyxbmct . Button ( '' , focusTexture = VVVeveee , noFocusTexture = IIiiii , textColor = ii11i11i1 , focusedColor = ii11i11i1 )
 Icon = pyxbmct . Image ( images [ 0 ] , aspectRatio = 2 )
 window . placeControl ( Previous , 102 , 1 , 10 , 10 )
 window . placeControl ( Next , 102 , 40 , 10 , 10 )
 window . placeControl ( Quit , 102 , 21 , 10 , 10 )
 window . placeControl ( Icon , 0 , 0 , 100 , 50 )
 Previous . controlRight ( Next )
 Previous . controlUp ( Quit )
 window . connect ( Previous , II1Ii1iI1i1 )
 window . connect ( Next , eev )
 Previous . setVisible ( False )
 window . setFocus ( Quit )
 Previous . controlRight ( Quit )
 Quit . controlLeft ( Previous )
 Quit . controlRight ( Next )
 Next . controlLeft ( Quit )
 window . connect ( Quit , window . close )
 window . doModal ( )
 del window
 if 78 - 78: iiI1i1 + VVeVeeevevee - i11IiIiiIIIII * IiIi1Iii1I1 - VeeevVVeveVV % Veveevev
def eev ( ) :
 i1VeVV = int ( VevVevVVevVevVev . getSetting ( 'pos' ) )
 iIII1I1i1i = int ( i1VeVV ) + 1
 VevVevVVevVevVev . setSetting ( 'pos' , str ( iIII1I1i1i ) )
 eevVIIiI1I1 = len ( images )
 Icon . setImage ( images [ int ( iIII1I1i1i ) ] )
 Previous . setVisible ( True )
 if int ( iIII1I1i1i ) == int ( eevVIIiI1I1 ) - 1 :
  Next . setVisible ( False )
  if 15 - 15: i11IiIiiIIIII * II1Iiii1111i % VVVevV * iiI1i1 - i11iIiiIii
def II1Ii1iI1i1 ( ) :
 i1VeVV = int ( VevVevVVevVevVev . getSetting ( 'pos' ) )
 VeevevVVVVeeevee = int ( i1VeVV ) - 1
 VevVevVVevVevVev . setSetting ( 'pos' , str ( VeevevVVVVeeevee ) )
 Icon . setImage ( images [ int ( VeevevVVVVeeevee ) ] )
 Next . setVisible ( True )
 if int ( VeevevVVVVeeevee ) == 0 :
  Previous . setVisible ( False )
  if 80 - 80: IiIi1Iii1I1 * Veveevev * Veeve - Ii11111i . Veveevev % VevVVe
def II1iiIIIiIii ( url , fanart ) :
 VevVevVVevVevVev . setSetting ( 'favlist' , 'yes' )
 I1i11II = None
 file = open ( Ve , 'r' )
 I1i11II = file . read ( ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iI = re . compile ( "<item>(.+?)</item>" , re . DOTALL ) . findall ( I1i11II )
 for iI11iiiI1II in iI :
  eeveV ( Ii11iii11I , url , Veveveeeeeevev , fanart , iI11iiiI1II )
 VevVevVVevVevVev . setSetting ( 'favlist' , 'no' )
 if 31 - 31: I1ii / i1iIIi1 * eeveee . Veeve
def eeeVVevVVevV ( name , url , iconimage , fanart ) :
 eeveve = VevVevVVevVevVev . getSetting ( 'favtype' )
 url = url . replace ( ' ' , '%20' )
 iconimage = iconimage . replace ( ' ' , '%20' )
 if '<>' in url :
  eeevevVeveveV = url . split ( '<>' ) [ 0 ]
  VVVevevV = url . split ( '<>' ) [ 1 ]
  VVeVVeveeeveeV = url . split ( '<>' ) [ 2 ]
  VeveevVevevVeeveev = url . split ( '<>' ) [ 3 ]
  VevevVeveVVevevVevev = url . split ( '<>' ) [ 4 ]
  eVeVev = '<FAV><item>\n<title>' + name + '</title>\n<meta>tvep</meta>\n<nan>tvshow</nan>\n<showyear>' + VeveevVevevVeeveev + '</showyear>\n<imdb>' + eeevevVeveveV + '</imdb>\n<season>' + VVVevevV + '</season>\n<episode>' + VVeVVeveeeveeV + '</episode>\n<episodeyear>' + VevevVeveVVevevVevev + '</episodeyear>\n<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart></item></FAV>\n'
 elif len ( url ) == 9 :
  eVeVev = '<FAV><item>\n<title>' + name + '</title>\n<meta>movie</meta>\n<nan>movie</nan>\n<imdb>' + url + '</imdb>\n' + '<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart></item></FAV>\n'
 else :
  eVeVev = '<FAV><item>\n<title>' + name + '</title>\n<' + eeveve + '>' + url + '</' + eeveve + '>\n' + '<thumbnail>' + iconimage + '</thumbnail>\n<fanart>' + fanart + '</fanart></item></FAV>\n'
 IiII = open ( Ve , 'a' )
 IiII . write ( eVeVev )
 IiII . close ( )
 if 47 - 47: eeveee + IiiIII111ii - I1ii % VeeevVVeveVV
def eevVev ( name , url , iconimage ) :
 print name
 I1i11II = None
 file = open ( Ve , 'r' )
 I1i11II = file . read ( )
 eeVeVe = ''
 iI = re . compile ( '<item>(.+?)</item>' , re . DOTALL ) . findall ( I1i11II )
 for VeveeeeevVeevev in iI :
  eVeVev = '\n<FAV><item>\n' + VeveeeeevVeevev + '</item>\n'
  if name in VeveeeeevVeevev :
   print 'xxxxxxxxxxxxxxxxx'
   eVeVev = eVeVev . replace ( 'item' , ' ' )
  eeVeVe = eeVeVe + eVeVev
 file = open ( Ve , 'w' )
 file . truncate ( )
 file . write ( eeVeVe )
 file . close ( )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 21 - 21: Veveevev + i11iIiiIii + VevVVe * eeveee % IiiIII111ii % Veeve
def VevevevVVeevevee ( url ) :
 try :
  VevevVevVeeeeevev = url . split ( '/' ) [ 2 ] . replace ( 'www.' , '' )
  file = open ( IIi1IiiiI1Ii , 'r' )
  eVVevVVevVV = file . read ( )
  if VevevVevVeeeeevev in eVVevVVevVV : return '[COLOR cyan] (RD)[/COLOR]'
  else : return ''
 except : return ''
 if 87 - 87: I1ii + iiI1i1 - VeeevVVeveVV
def IiI1 ( ) :
 xbmcaddon . Addon ( ) . openSettings ( )
 if 12 - 12: VVeVeeevevee % Veveevev
def i1i ( ) :
 xbmcaddon . Addon ( 'script.module.universalscrapers' ) . openSettings ( )
 if 5 - 5: I1ii . VVVevV . Veeve . VeeevVVeveVV
def VeevVeeVev ( ) :
 xbmcaddon . Addon ( 'script.module.urlresolver' ) . openSettings ( )
 if 87 - 87: I1ii % i11IiIiiIIIII
def eeevVVVeVe ( ) :
 xbmcaddon . Addon ( 'script.module.metahandler' ) . openSettings ( )
 if 21 - 21: VVeevevev - Ii11111i . I1ii + i11IiIiiIIIII . iiI1i1 - Veveevev
def eVee ( link ) :
 try :
  I11IIIiIi11 = re . compile ( '<layouttype>(.+?)</layouttype>' ) . findall ( link ) [ 0 ]
  if I11IIIiIi11 == 'thumbnail' : xbmc . executebuiltin ( 'Container.SetViewMode(500)' )
  else : xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
 except : pass
 if 39 - 39: i11IiIiiIIIII % Ii11111i % Veveevev . Ii
 if 86 - 86: VVeevevev * VeeevVVeveVV
VevVVVevVVeeeevev = VevVeeevee ( ) ; VeI1Ii11I1Ii1i = None ; Ii11iii11I = None ; iiI = None ; VeeVeveVe = None ; eVeevevVeevevV = None ; eVVeevevVevVVVe = None
try : VeeVeveVe = urllib . unquote_plus ( VevVVVevVVeeeevev [ "site" ] )
except : pass
try : VeI1Ii11I1Ii1i = urllib . unquote_plus ( VevVVVevVVeeeevev [ "url" ] )
except : pass
try : Ii11iii11I = urllib . unquote_plus ( VevVVVevVVeeeevev [ "name" ] )
except : pass
try : iiI = int ( VevVVVevVVeeeevev [ "mode" ] )
except : pass
try : eVeevevVeevevV = urllib . unquote_plus ( VevVVVevVVeeeevev [ "iconimage" ] )
except : pass
try : eeeevVV = urllib . unquote_plus ( VevVVVevVVeeeevev [ "fanart" ] )
except : pass
try : eVVeevevVevVVVe = str ( VevVVVevVVeeeevev [ "description" ] )
except : pass
if 31 - 31: VVeVeeevevee % eVVVeeveevV * VVeVeeevevee
if iiI == None or VeI1Ii11I1Ii1i == None or len ( VeI1Ii11I1Ii1i ) < 1 : ee ( )
elif iiI == 1 : VeVVVeveveVVev ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 2 : Ii1ii111i1 ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eVVeevevVevVVVe )
elif iiI == 3 : eevVeveeev ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV )
elif iiI == 4 : eVeeevevev ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV )
elif iiI == 5 : eVeeVev ( )
elif iiI == 6 : i1iiIiI1Ii1i ( VeI1Ii11I1Ii1i , eVeevevVeevevV )
elif iiI == 7 : VeV ( VeI1Ii11I1Ii1i )
elif iiI == 8 : eevVeeeveeveeeev ( Ii11iii11I )
elif iiI == 9 : IIIII ( Ii11iii11I , VeI1Ii11I1Ii1i )
elif iiI == 10 : iI1I ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 11 : VeeVVVVeVevevVeVV ( VeI1Ii11I1Ii1i )
elif iiI == 12 : VeevVeeVev ( )
elif iiI == 13 : eeevVVVeVe ( )
elif iiI == 15 : SCRAPEMOVIE ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV )
elif iiI == 16 : i1i1i1I ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV )
elif iiI == 17 : iIiIIIIIii ( Ii11iii11I , VeI1Ii11I1Ii1i )
elif iiI == 18 : IiII111i1i11 ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 19 : eevevevVeve ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
if 45 - 45: Ii . VevVVe + eVVVeeveevV - VeeevVVeveVV % VevevVevVevVev
elif iiI == 20 : eeeVVevVVevV ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 21 : eevVev ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV )
elif iiI == 22 : II1iiIIIiIii ( VeI1Ii11I1Ii1i , eeeevVV )
elif iiI == 23 : DOIPLAYER ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 24 : eevVeve ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 25 : i1i ( )
if 1 - 1: iiI1i1
elif iiI == 26 : VevVeveveevVVVev ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 27 : i1iiI11I ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 28 : eVeeV ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 29 : II1iIi11 ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 30 : eevVevVVVVeVVev ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 31 : Iii1iI ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 32 : iII1i11IIi1i ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 33 : iII1i1 ( VeI1Ii11I1Ii1i )
elif iiI == 34 : eeveVevevevee ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 35 : II1I ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
if 93 - 93: Ii . i11iIiiIii . II1Iiii1111i
elif iiI == 36 : eevVeveve ( )
elif iiI == 37 : VVevVeeeev ( VeI1Ii11I1Ii1i )
elif iiI == 38 : i1ii1I1I1 ( VeI1Ii11I1Ii1i )
elif iiI == 39 : VVV ( VeI1Ii11I1Ii1i )
elif iiI == 40 : eevVIiI1i ( )
elif iiI == 41 : eeveveVVeeVVeeve ( VeI1Ii11I1Ii1i )
elif iiI == 42 : eVeevVeveeveve ( VeI1Ii11I1Ii1i )
if 99 - 99: VVeVeeevevee - IiIi1Iii1I1 - I1ii % VVeevevev
elif iiI == 43 : iIIII ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 44 : ii1iiIiIII1ii ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 45 : Veve ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 46 : eeVVeV ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
if 21 - 21: Veeve % VVVevV . Ii - VeeevVVeveVV
elif iiI == 47 : DODOCLOGMENU ( )
elif iiI == 48 : GET_DOCCONTENT ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , II1 )
elif iiI == 49 : DO_DOCCONTENT ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , II1 )
elif iiI == 50 : RESOLVE2 ( VeI1Ii11I1Ii1i )
elif iiI == 51 : iI1IiI11ii1I1 ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV , eeeevVV )
elif iiI == 52 : VeVeeVeV ( Ii11iii11I , VeI1Ii11I1Ii1i , eVeevevVeevevV )
elif iiI == 53 : IiI1 ( )
if 4 - 4: VeeevVVeveVV . VevevVevVevVev
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
