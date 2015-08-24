from cx_Freeze import setup, Executable

exe=Executable(
     script='remove_mailing_list.py',
     base="Win32Gui",
     icon="ui/image/document_delete.ico",
     targetName="Remove From Mailing List.exe",
     shortcutName="Remove From Mailing List",
     shortcutDir="DesktopFolder",
     )
build_exe_options = {'packages':['ui', 'data'], 'include_files':['C:\Python34\Lib\site-packages\PyQt5\libEGL.dll', 'image_rc.py'], 
                     'includes':['decimal', 'atexit'], 'excludes':['Tkinter'], 'include_msvcr': True}

bdist_msi_options = {
    #GUID -- use generator online for now.
    'upgrade_code': '{45230F5B-2D1F-4E96-A432-22AC8DA78F9A}',
    'add_to_path': False,
    #'initial_target_dir': r'[Program Files] \%s\%s' % ('test', 'test'),
    }
setup(
     version = "0.1",
     description = "Search and remove addresses from the 5 Order Manager databases for returned post cards or customer requests.",
     author = "David Hoy",
     name = "Mailing List Removal Tool",
     options = {'build_exe': build_exe_options, 'bdist_msi': bdist_msi_options},
     executables = [exe]
     )