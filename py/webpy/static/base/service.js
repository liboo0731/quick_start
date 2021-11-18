angular.module('base').factory('baseService',['$resource','basePath', function($resource,basePath){
	return $resource(basePath+'/base',{},{});
}]);