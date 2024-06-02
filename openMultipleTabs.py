# Modules which need to be imported
import webbrowser

# Site which you want to Open in your
# Browser
url = "www.google.com"

# Below code is used to specify
# location of webbrowser which you
# want to use.
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# Below code will open your URL
for i in range(100):
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(url)
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
    webbrowser.get('edge').open_new_tab(url)
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
    webbrowser.get('firefox').open_new_tab(url)