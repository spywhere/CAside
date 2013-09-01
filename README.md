## CAside

A source/header files synchronizer for Sublime Text 3

### Features
 * Header/Source files synchronization
 * Multiple extensions supported (via Regular Expression)
 
 
### Important Notes
You must open your workspace as a group you selected

For example: You select to open all files in group 1, then you must set your workspace to group 2 (View > Groups > Max Columns: 2)

### Commands

The following commands can be accessed via *Command Palette* (Control+Shift+P or Super+Shift+P) only

* Enable/Disable
	* Enable or disable CAside plugin
* Select
	* Select (a view in) currently focused group
* Synchronize
	* Synchronize the source and header

### How it's work
When you activate a view, CAside will looking for a file from current view and try to find a correspond target file (For example, when you open a .c file, CAside will looking for .h file) if a file is found, it will open on a new group as you assign in settings file.

### CAside in action

![Demo](http://spywhere.github.io/images/CAsideDemo.gif)


### Installation
You can install CAside via [Sublime Package Control](http://wbond.net/sublime_packages/package_control) or by clone this repository into your *Sublime Text 3 / Packages* folder

	cd PACKAGES_PATH
	git clone git://github.com/spywhere/CAside.git
	
PACKAGES_PATH is related to folder which can be accessed via the *Preference > Browse Packages...*

### Settings
Settings are accessed via the *Preferences > Package Settings > CAside* or via command palette by type *"Preference CAside"*

Default settings should not be modified. However, you can copy the relevant settings into CAside user settings file