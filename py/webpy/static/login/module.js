define([
	'js/angular'
	],function(){
	var loginModule=angular.module('login', [
			'ui.router',
			'ngResource',
			'oc.lazyLoad']);
	loginModule.config(['$stateProvider',function($stateProvider){
		$stateProvider.state('login', {
			url: '/login',
			component: 'login',
			resolve: {
				data: ['loginService',function(loginService){
					return loginService.get().$promise.then(function(resp){
						return resp
					});
				}]
			},
			lazyLoad: function($transition$){
				return $transition$.injector().get('$ocLazyLoad').load(['login/component']);
			}
		});
	}]);
});
