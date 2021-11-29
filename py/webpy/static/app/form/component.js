angular.module('app').component('appForm',{
	bindings:{
		data:'<'
	},
	templateUrl: 'static/app/form/template.html?'+resourcesVersion,
	controller: ['NgTableParams','$scope','$element',function(NgTableParams,$scope,$element){
		var self = this;
		
		self.$onInit = function(){

		}
	}]
});