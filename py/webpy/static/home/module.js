define([
	'angular'
	],function(){
	var homeModule=angular.module('home', [
			'ui.router',
			'ngResource',
			'ui.bootstrap',
			'oc.lazyLoad']);
	homeModule.config(['$stateProvider',function($stateProvider){
		$stateProvider.state('home', {
			url: '/home',
			component: 'home',
			resolve: {
				data: ['homeService',function(homeService){
					return homeService.get().$promise.then(function(resp){
						return resp
					});
				}]
			},
			lazyLoad: function($transition$){
				return $transition$.injector().get('$ocLazyLoad').load(['home/component', 'home/modalDirective']);
			}
		});
	}]);
});
