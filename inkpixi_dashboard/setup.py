from cx_Freeze import setup, Executable

exe=Executable(
     script='dashboard_main.py',
     base="Win32Gui",
     icon="images/postcard.ico",
     targetName="Postcard Dashboard.exe",
     #shortcutName="Remove From Mailing List",
     #shortcutDir="ProgramMenuFolder",
     )

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Postcard Dashboard",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]Postcard Dashboard.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     ),
    ("ProgramShortcut",        # Shortcut
     "StartMenuFolder",          # Directory_
     "Postcard Dashboard",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]Postcard Dashboard.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

msi_data = {"Shortcut": shortcut_table}

build_exe_options = {'packages':['ui', 'database'], 'include_files':['C:\Python34\Lib\site-packages\PyQt5\libEGL.dll', 'resources_rc.py', 'images/'], 
                     'includes':['decimal', 'atexit'], 'excludes':['Tkinter'], 'include_msvcr': True}

bdist_msi_options = {
    #GUID -- use generator online for now.
    'upgrade_code': '{3207bded-264b-4b27-8535-afa36068a1fc}',
    'add_to_path': False,
    'data': msi_data,
    #'initial_target_dir': r'[Program Files] \%s\%s' % ('test', 'test'),
    }
setup(
     version = "1.0",
     description = "Visibility to post card campaign data.",
     author = "David Hoy",
     name = "Postcard Dashboard",
     options = {'build_exe': build_exe_options, 'bdist_msi': bdist_msi_options},
     executables = [exe]
     )