call pyuic4 -i 0 mag_search.ui -o mag_search_ui.py;
call pyrcc4 -o source_rc.py source.qrc;
call pyinstaller -F -i logo.ico main_search.py