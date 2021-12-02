angular.module('app').factory('appService',['$resource','basePath', function($resource,basePath){
	return $resource(basePath+'/base',{},{});
}]);