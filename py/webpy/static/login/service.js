angular.module('login').factory('loginService',['$resource','basePath', function($resource,basePath){
	return $resource(basePath+'/list',{},{});
}]);