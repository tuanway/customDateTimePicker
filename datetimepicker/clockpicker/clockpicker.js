angular.module('datetimepickerClockpicker', ['servoy']).directive('datetimepickerClockpicker', function() {
		return {
			restrict: 'E',
			scope: {
				model: "=svyModel",
				api: "=svyApi",
				handlers: "=svyHandlers",
				svyServoyapi: '=svyServoyapi'
			},
			link: function($scope, $element, $attrs) {
				// wait till load event fires so all resources are available
				$(function() {
					$scope.picker = $('#' + $scope.model.svyMarkupId).clockpicker({
						default: $scope.model.default,
						placement: $scope.model.placement,
						align: $scope.model.align,
						donetext: $scope.model.donetext,
						autoclose: $scope.model.autoclose,
						vibrate: $scope.model.vibrate,
						init: $scope.handlers.init,
						beforeShow: $scope.handlers.beforeShow,
						afterShow: $scope.handlers.afterShow,
						beforeHide: $scope.handlers.beforeHide,
						afterHide: $scope.handlers.afterHide,
						beforeHourSelect: $scope.handlers.beforeHourSelect,
						afterHourSelect: $scope.handlers.afterHourSelect,
						beforeDone: $scope.handlers.beforeDone,
						afterDone: $scope.handlers.afterDone,
						twelvehour: $scope.handlers.twelvehour
					});
				});

				$scope.api.show = function() {
					$scope.picker.show();
				}

				$scope.api.hide = function() {
					$scope.picker.hide();
				}

				$scope.api.toggleView = function(type) {
					$scope.picker.toggleView(type);
				}
			},
			templateUrl: 'datetimepicker/clockpicker/clockpicker.html'
		};
	})