angular.module('datetimepickerDatepicker', ['servoy']).directive('datetimepickerDatepicker', function() {
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
					$scope.picker = $('#' + $scope.model.svyMarkupId).datebox({
						mode: "flipbox",
						//Default options
						bootstrapDropdown: true,
						bootstrapModal: false,
						bootstrapDropdownRight: false,
						bootstrapResponsive: false,
						customData: false,
						//Custom Options
						useKinetic: $scope.model.useKinetic,
						useSetButton: $scope.model.useSetButton,
						useFocus: $scope.model.useFocus,
						lockInput: $scope.model.lockInput,
						beforeToday: $scope.model.beforeToday,
						afterToday: $scope.model.afterToday,
						overrideDateFieldOrder: $scope.model.dateFieldOrder.split(','),
						overrideDateFormat: $scope.model.dateFormat,
						maxDays: Number($scope.model.maxDays),
						overrideSetDateButtonLabel: $scope.model.setDateButtonLabel,
						overrideTitleDateDialogLabel: $scope.model.titleDateDialogLabel
					});
				});
			},
			templateUrl: 'datetimepicker/datepicker/datepicker.html'
		};
	})