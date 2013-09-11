angular.module('meta', ['ui.bootstrap']);
function meta_info($scope,$http) {
$http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded;charset=utf-8";
$scope.alerts = [
    { type: 'success', msg: 'Url and meta info added successfully' }
  ];
  $scope.getInfo = function() {
	var url=$scope.url;
	$http({ 
		method: 'POST', 
		url: '/getinfo/', 
		data: "url="+url
	  }).success(function(response)
		  {
		    $scope.loaded=true;
		    $scope.title=response.title;
		    $scope.keywords=response.keywords;
		    $scope.desc=response.desc;
		  });
  };

  $scope.closeAlert = function(index) {
	$scope.alerts.splice(index, 1);
  };
 
}
