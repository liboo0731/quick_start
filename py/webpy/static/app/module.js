define([
	'js/angular'
	],function(){
	var homeModule=angular.module('app', [
			'ui.router',
			'ngResource',
			'ngTable',
			'oc.lazyLoad']);
	homeModule.config(['$stateProvider',function($stateProvider){
		$stateProvider.state({
			name:'app',
			url: '/app',
			redirectTo: 'app.list',
			lazyLoad: function($transition$){
				return $transition$.injector().get('$ocLazyLoad').load([
					'app/service'
				]);
			}
		});
		$stateProvider.state('app.list', {
			url: '/list',
			component: 'appList',
			resolve: {
				data: ['appService',function(appService){
					return appService.get().$promise.then(function(resp){
						return resp
					});
				}]
			},
			lazyLoad: function($transition$){
				return $transition$.injector().get('$ocLazyLoad').load(['app/list/component']);
			}
		});
		$stateProvider.state('app.form', {
			url: '/form',
			component: 'appForm',
			resolve: {
				data: ['appService',function(appService){
					return appService.get().$promise.then(function(resp){
						return resp
					});
				}]
			},
			lazyLoad: function($transition$){
				return $transition$.injector().get('$ocLazyLoad').load(['app/form/component']);
			}
		});
	}]);
});
