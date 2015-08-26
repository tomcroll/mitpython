# mitpython
MIT Python Course

First setup sublime:
wget http://c758482.r82.cf2.rackcdn.com/sublime-text_build-3083_amd64.deb
sudo dpkg -i sublime-text_build-3083_amd64.deb 

Install Package Control

To begin taking advantage of the various packages for extending Sublime’s functionality, you need to install the package manager called Package Control – which you must install manually. Once installed, you can use Package Control to install/remove/upgrade all other ST3 packages.

    To install, copy the Python code for Sublime Text 3 found below. Click View > Show Console to open the ST3 console. Paste the code into the console. Press enter. Reboot ST3.

Code:

import urllib.request,os,hashlib; h = 'eb2297e1a458f27d836c04bb0cbaf282' + 'd0e7a3098092775ccb37ca9d6b2e4b7d'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by) 


    You can now install packages by using the keyboard shortcut cmd+shift+P. Start typing install until Package Control: Install Package appears. Press enter and search for available packages.

    Some other relevant commands are:
        List Packages shows all your installed packages
        Remove Packages removes a specific package
        Upgrade Package upgrades a specific package
        Upgrade/Overwrite All Packages upgrades all your installed packages


    Check out the official documentation to view more commands.

Create a Custom Settings File

You can fully configure Sublime Text using JSON-based settings files, making it easy to transfer, or synchronize, your customized settings to another system. First, we need to create our customized settings. It’s best to create a base file for all environments as well as language-specific settings files.

To set up a base file click Sublime Text > Preferences > Settings – User. Add an empty JSON object to the file and add your settings like so:

{
  // base settings
  "auto_complete": false,
  "sublimelinter": false,
  "tab_size": 2,
  "word_wrap": true
}

    For language specific settings click Sublime Text > Preferences > Settings – More > Syntax Specific – User. Then save the file using the following format: LANGUAGE.sublime-settings. So, for Python-specific settings, save the file as Python.sublime-settings.

    You can obviously configure your settings to your liking; however, I highly recommend starting with my base and Python-specific settings – then making changes as you see fit.

Install Flatland Theme:

    Optional: You can use Dropbox to sync all your settings. Simply upload your settings files to Dropbox and load them from there to sync the Sublime environments on all your machines.

    A good reference for settings can be found at the Sublime Text Unofficial Documentation.

Themes

ST3 also gives you the option to change the overall theme to better suit your personality. Design your own. Or, if you’re not artistically inclined, you can download one of the various custom themes designed by the Sublime community through Package Control. Check out ColorSublime to preview themes before installing them.

The ever popular Soda Dark Theme and the minimal Flatland are two of my personal favorites.

After installing a theme, make sure to update your base settings, Sublime Text > Preferences > Settings – User:

{
  "theme": "Flatland Dark.sublime-theme",
  "color_scheme": "Packages/Theme - Flatland/Flatland Dark.tmTheme"
}

Packages

Besides the packaged themes, I take advantage of the following packages to speed up my workflow.
SideBarEnhancements

SideBarEnhancements extends the number of menu options in the sidebar, speeding up your overall workflow. Options such as “New file” and “Duplicate” are essential and should be part of ST3 out of the box. The “Delete” option alone makes it worth downloading. This feature simply sends files to the Trash, which may seem trivial but if you delete a file without it, it’s very difficult to recover unless you’re using a version control system.

Install Anaconda
Sublimelinter
Sublimelinter-pyflakes
	-pep8

https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/

