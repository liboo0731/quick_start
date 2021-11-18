var resourcesVersion = "bust=" +  (new Date()).getTime();
//var resourcesVersion = "=v1"
require.config({
	map: {
    	'*': {
    		'angular': 'js/angular'
    	}
    },
    paths: {
    	'jquery': 'js/jquery'
    },
	shim: {
		'plugins/bootstrap3/js/bootstrap':['jquery'],
		'js/angular': {
    		deps:['plugins/bootstrap3/js/bootstrap'],
    		exports: 'angular'
    	},
    	'js/ocLazyLoad.require': {
    		deps: ['js/angular']
    	},
    	'js/angular-ui-router': {
    		deps: ['js/ocLazyLoad.require']
    	},
    	'js/angular-resource': {
    		deps: ['js/angular']
    	},
    	'home/service': {
    		deps: ['home/module']
    	}
    },
    urlArgs: resourcesVersion
});
require(['app']);

