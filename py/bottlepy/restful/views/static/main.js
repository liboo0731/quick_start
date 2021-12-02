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
    		deps:['plugins/bootstrap3/js/bootstrap', 'js/lodash'],
    		exports: 'angular'
    	},
    	'js/ocLazyLoad.require': {
    		deps: ['angular']
    	},
    	'js/angular-ui-router': {
    		deps: ['js/ocLazyLoad.require']
    	},
    	'js/angular-resource': {
    		deps: ['angular']
    	},
    	'js/drag': {
    	    deps: ['jquery']
    	},
    	'js/ui-bootstrap-tpls': {
    	    deps: ['angular', 'plugins/bootstrap3/js/bootstrap']
    	},
    	'home/service': {
    		deps: ['home/module']
    	}
    },
    urlArgs: resourcesVersion
});
require(['app']);

