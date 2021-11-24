angular.module('base').component('baseList',{
	bindings:{
		data:'<'
	},
	templateUrl: 'static/base/template.html?'+resourcesVersion,
	controller: ['NgTableParams','$scope','$element',function(NgTableParams,$scope,$element){
        var self = this;
        data = [{
            name: "123",
            age: 12,
            money: 23,
        }];
        var originalData = angular.copy(data);

        self.tableParams = new NgTableParams({}, {
          filterDelay: 0,
          dataset: angular.copy(data)
        });

        self.cancel = function (row, rowForm) {
          var originalRow = resetRow(row, rowForm);
          angular.extend(row, originalRow);
        }

        self.del = function (row) {
          _.remove(self.tableParams.settings().dataset, function(item) {
            return row === item;
          });
          self.tableParams.reload().then(function(data) {
            if (data.length === 0 && self.tableParams.total() > 0) {
              self.tableParams.page(self.tableParams.page() - 1);
              self.tableParams.reload();
            }
          });
        }

        function resetRow(row, rowForm){
          row.isEditing = false;
          rowForm.$setPristine();
          return _.findWhere(originalData, function(r){
            return r.id === row.id;
          });
        }

        self.save = function (row, rowForm) {
          var originalRow = resetRow(row, rowForm);
          angular.extend(originalRow, row);
        }

        self.add = function () {
          self.isEditing = true;
          self.isAdding = true;
          self.tableParams.settings().dataset.unshift({
            isEditing: true
          });
          // we need to ensure the user sees the new row we've just added.
          // it seems a poor but reliable choice to remove sorting and move them to the first page
          // where we know that our new item was added to
          self.tableParams.sorting({});
          self.tableParams.page(1);
          self.tableParams.reload();
        }

        self.applyGlobalSearch = function(){
            var term = self.globalSearchTerm;
            if (self.isInvertedSearch){
                term = "!" + term;
            };
            self.tableParams.filter({$:term});
        };
	}]
});
