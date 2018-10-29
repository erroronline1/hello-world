'''
apply iconsets to windows start using visual elements manifests

first useful approach for pythonscripting by error on line 1

visualements documentation:
https://msdn.microsoft.com/en-us/library/windows/apps/dn393983.aspx#create_the_customization_xml_file
icon ressource:
https://dakirby309.deviantart.com/art/Metro-UI-Icon-Set-725-Icons-280724102


1. unpack icon ressources to harddrive and keep it there
2. define apps/programs in start, their directory and the desired image/icon
3. execute script in administrator mode
4. you may have to delete/change the program folder shortcuts
5. enjoy a unified start menu

be aware that existing manifests may be overwritten.
as long as i am not into ui one has still gather the information to fill the list, but at least the files write themselves
'''
#define apps in start
app_ly=[]
#append for readability
app_ly.append({'exe':'firefox', 'path':'C:\Program Files\Mozilla Firefox', 'img':'C:\metro_ui_icon_set\Web Browsers\Firefox.png', 'showname':'on', 'foreground': 'light', 'background':'#888888'})
#app_ly.append({'exe':'chrome', 'path':'C:\Program Files (x86)\Google\Chrome\Application', 'img':'C:\metro_ui_icon_set\Web Browsers\Google Chrome.png', 'showname':'on', 'foreground': 'light', 'background':'#888888'})
app_ly.append({'exe':'Mailbird', 'path':'C:\Program Files (x86)\Mailbird', 'img':'C:\metro_ui_icon_set\Other\Mail.png', 'showname':'on', 'foreground': 'light', 'background':'#888888'})
#app_ly.append({'exe':'filezilla', 'path':'C:\Program Files\FileZilla FTP Client', 'img':'C:\metro_ui_icon_set\Applications\Filezilla.png', 'showname':'on', 'foreground': 'light', 'background':'#888888'})
#app_ly.append({'exe':'inkscape', 'path':'C:\Program Files\Inkscape', 'img':'C:\metro_ui_icon_set\Applications\Inkscape.png', 'showname':'on', 'foreground': 'light', 'background':'#888888'})
#app_ly.append({'exe':'pythonw', 'path':'C:\python', 'img':'C:\metro_ui_icon_set\System Icons\Command Prompt.png', 'showname':'on', 'foreground': 'light', 'background':'#888888'})
#app_ly.append({'exe':'manager-windows', 'path':'C:\Bitnami\wampstack-7.1.12-0', 'img':'C:\metro_ui_icon_set\Other\Home.png', 'showname':'on', 'foreground': 'light', 'background':'#888888'})
#app_ly.append({'exe':'VirtualBox', 'path':'C:\Program Files\Oracle\VirtualBox', 'img':'C:\metro_ui_icon_set\Applications\VirtualBox.png', 'showname':'on', 'foreground': 'light', 'background':'#888888'})


import os
def run():
  for app in app_ly:
    filename='{0}.VisualElementsManifest.xml'.format(app['exe'])
    filecontent='''<Application xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'>
    <VisualElements
        ShowNameOnSquare150x150Logo='{0}'
        Square150x150Logo='{1}'
        Square70x70Logo='{1}'
        ForegroundText='{2}'
        BackgroundColor='{3}'/>
  </Application>
  '''.format(app['showname'],app['img'],app['foreground'],app['background'])
    """  try:
      os.chmod(app['path']+'\\'+filename, 0o777)
    except Exception as e:
      print('could not set file properties')
  """
    try:
      file=open("c:\\users\\getriebesand\\downloads\\"+filename,'w')
  #    file=open(app['path']+'\\'+filename,'w')
      file.write(filecontent)
      file.close()
      print(filename,'has been written to ',app['path'])
    except Exception as e:
      print(e)
      print(filename,'could not be written.')
    
file=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Mailbird\Mailbird.lnk"
f=open(file,'br')
print(f.readline())
f.close()

#print(file.readlines())
#with open('C:\\metro_ui_icon_set\\Web Browsers\\Firefox.png','rb') as f:
#  print(f.read())

#file.close()