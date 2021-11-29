angular.module('home').component('homeForm',{
    templateUrl:'static/home/form/template.html',
    controller:[function(){
        var $ctrl = this;
        $ctrl.$onInit = function(){
            console.log(this.resolve);
        };

        $ctrl.ok = function () {
          $ctrl.close({$value: $ctrl.resolve.title});
        };

        $ctrl.cancel = function () {
          $ctrl.dismiss({$value: 'cancel'});
        };
    }],
    //close 和dismiss 被绑定自$uibModalInstance
    bindings:{
        resolve:'<',
        close: '&',
        dismiss: '&'
    }
})