var slideroptions = {
	sliderID: "slider",
	slideTime: 3000
};

var ChSlider = {};

ChSlider.init = function (options){
	var mainItem = document.getElementById(options.sliderID);
	var items = mainItem.getElementsByTagName('li');
	this.slideCount = 1;
	if (items.length > 1){
		setInterval(function () { ChSlider.slide(items) }, options.slideTime);
	}	
};

ChSlider.slide = function(elements){
	if (this.slideCount >0) {
		elements[this.slideCount-1].className = '';
	}else{
		elements[elements.length-1].className = '';
	}

	elements[this.slideCount].className = 'active';

	if (elements.length-1 > this.slideCount){
		this.slideCount++;
	}else{
		this.slideCount = 0;
	}
};

ChSlider.init(slideroptions);