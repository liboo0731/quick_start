angular.module('home').component('home',{
	bindings:{
		data:'<'
	},
	templateUrl: 'static/home/template.html?'+resourcesVersion,
	controller: [function(){
		var self = this;
		
	}]
});