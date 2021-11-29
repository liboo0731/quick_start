angular.module('home').directive('uibModal',['$uibModal','$ocLazyLoad',function($uibModal,$ocLazyLoad){
    return {
        restrict: 'A',
        scope: {
            uibModal: '='
        },
        link: function(scope,element,attr){
            element.on('click', function() {
                //动态加载组件,在组件加载完成后打开弹窗
                $ocLazyLoad
                    .load(scope.uibModal.path)
                    .then(function(){
                        //弹窗打开方法
                        $uibModal.open({
                            animation:false,
                            size:scope.uibModal.size?scope.uibModal.size:'',
                            backdrop:'static',
                            component: scope.uibModal.component,
                            resolve:{
                                //获取所点击元素内容作为标题
                                title:function(){
                                    return element.context.innerHTML;
                                },
                                //传入组件的数据
                                data:function(){
                                    return scope.uibModal.data;
                                }
                            }
                            }).rendered.then(function(){
                                //弹窗显示出来后，绑定拖拽功能
                                $('.modal-content').drag(function(ev,dd){
                                    $(this).css({
                                        top: dd.offsetY,
                                        left: dd.offsetX
                                    });
                                },{
                                    handle:'.modal-header',
                                    relative:true
                                });
                            });
                });
            });
        }
    }
}]);