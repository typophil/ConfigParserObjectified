# ConfigParserObjectified
A (very) small wrapper around ConfigParser (as of Python 2.7) to allow dotted access to config values. See ReadMe for further details.

I like to access configuration values through dotted notation in a configuration object. As one would do with oslo.config, but without the whole overhead. This is far from perfect or from covering everything you need.

You create an instance of `ConfigParserObjectified.ConfigObject` providing the config file (path/file) as argument. `ConfigParser` then is used to parse the config file. After that, it cycles through the sections and options/values and dynamically creates attributes on itself.

This `module` was written based on `Python 2.7`.

It's as simple as this:

1. You import the module

		from ConfigParserObjectified import ConfigObject

2. Then you create your config Object:

		MyCFG = ConfigObject("$PathToConfigFile")

3. Now you can access your configuration file like so:

		MyCFG.SECTION.option
	
	Which will return the value.

----

###Sample:###

_sample.cfg_

	[URLS]
	github: https://github.com
	bitbucket: https://bitbucket.org
	
	[GitHubProjects]
	cpo: typophil/ConfigParserObjectified
	
	[FavoriteDishes]
	breakfast: Fried Egg
	lunch: Caesar Salad
	dinner: BBQ Burger with Potato Wedges

_use_sample_cfg.py_

	from ConfigParserObjectified import ConfigObject

	CFG = ConfigObject("sample.cfg")
	
	def get_cpo_project_url():
	    return "{0}/{1}".format(CFG.URLS.github, CFG.GitHubProjects.cpo)
	
	def get_current_fav_dinner():
	    return CFG.FavoriteDishes.dinner
	
	if __name__ == "__main__":
	    print(get_cpo_project_url())
	    print(get_current_fav_dinner())

Should output:

	~]$ python use_sample_cfg.py
	https://github.com/typophil/ConfigParserObjectified
	BBQ Burger with Potato Wedges