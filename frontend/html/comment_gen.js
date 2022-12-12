/* using: Vue, axios */

new Vue({
    el: '#app',
    data() {
        return {
			result_message: '',
            datas: [],
			url_input: "",
			url_now: "",
			is_button_disabled: true,
			is_input_disabled: false,
			is_loading: false,
			is_comment_show: false,
        }
    },

    methods: {
	sendURL: function(){
	    let self = this;

	    self.is_button_disabled = true;
	    self.is_input_disabled = true;
		self.url_now = self.url_input;
		self.datas = [];
		self.is_loading = true;
	    axios.post('/api/url', {
		url: self.url_input
	    }, {timeout: 3000}
	    ).then(function(response){
		self.is_input_disabled = false;
		self.result_message = "送信に成功しました！";
		self.url_input = ""; // リセ
		self.generate();
	    }).catch(function(error){
	    console.log("error post:" + error.message);	    
		self.is_input_disabled = false;
		self.is_button_disabled = false;
		self.result_message = "問題が発生しました。やりなおしてください。: " + error.message;
	    })
	},

	generate: function(){
		let self = this;
		axios.get('/api/generate', {
		params: {
			url: self.url_now
		},
		// timeout: 5000000,
		}).then(function(response){
		items = response.data;
		items.push(...self.datas);
		self.datas = items;
		self.is_loading = false;
		self.result_message = "生成に成功しました！";
		self.is_comment_show = true;
		}).catch(function(error){
			console.log("error get: " + error.message);	    
		})
	},

    },
    watch: {
	url_input: function(url_input) {
	    if(url_input.length > 0){
		this.is_button_disabled = false;
	    }else{
		this.is_button_disabled = true;
	    }
	},
    }
	
    
    
    
    
})
