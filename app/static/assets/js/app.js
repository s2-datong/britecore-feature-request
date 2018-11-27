/* Encapsulates frontend ui interactions */
class App{

	constructor(){
		this.api = new Api()
	}

	slideleft(id){
		let center = document.querySelector('.screen.center')
		let other = document.querySelector('#' + id)
		if(center == null || other == null){ return; }

		other.className = "screen right"
		setTimeout(function(){
			center.className = "screen transition left";
			other.className = "screen transition center";
		}, 100)
		
	}

	slideright(id){
		let center = document.querySelector('.screen.center')
		let other = document.querySelector('#' + id)
		if(center == null || other == null){ return; }

		other.className = "screen left"
		setTimeout(function(){
			center.className = "screen transition right";
			other.className = "screen transition center";
		}, 100)
	}

	async login(){
		try{
			await this.api.login(
				document.querySelector('#username').value, 
				document.querySelector('#password').value
			)

			this.slideleft('feature')
			this.init()

		}catch(e){
			alert(e.message)
			console.log(e)
		}
	}

	async init(){
		let req1 = this.lookUpClients()
		let req2 = this.lookUpProductAreas()
		await req1;
		await req2;

		await this.lookupPriority()
		await this.listFeatureRequests()
	}

	logout(){
		this.slideright('login')
	} 

	async listFeatureRequests(){
		try{
			let featureRequests = await this.api.getFeatureRequests()
			
			if(featureRequests.length > 0){
				let html = ""
				featureRequests.forEach((request) => {
					let entry = `
					<div class="col-md-3">
						<div class="card">
						  <div class="card-body">
						    <h5 class="card-title">${request.title}</h5>
						    <p class="card-text">${request.description}</p>
						    <ul class="list-group list-group-flush">
							    <li class="list-group-item">Client: ${request.client} </li>
							    <li class="list-group-item">Priority: ${request.priority} </li>
							    <li class="list-group-item">Target Date: ${request.target_date} </li>
							    <li class="list-group-item">Product Area: ${request.product_area} </li>
							</ul>
						    <a href="#" class="card-link" onclick="app.deleteFeatureRequest(${request.id}, '${request.title}')">
									Delete Request</a> </td>
						  </div>
						</div>
					</div>
					`
					html += entry
				})

				
				document.querySelector("#featureRequests").innerHTML = html
			}
		}catch(e){
			console.log(e)
		}
	}

	async addFeatureRequest(){
		try{
			let msg = await this.api.submitFeatureRequest(
				document.querySelector('#title').value, 
				document.querySelector('#description').value, 
				document.querySelector('#client').value,  
				document.querySelector('#priority').value,  
				document.querySelector('#date').value,  
				document.querySelector('#area').value
			)

			alert(msg)

			$('#feature-request-modal').modal('hide')
			await app.listFeatureRequests()
		}
		catch(e){
			console.log(e)
		}
	}

	async deleteFeatureRequest(id, title){
		let c = confirm('Are you sure you want to delete ' + title)
		if(!c){ return; }

		try{
			let resp = await this.api.deleteFeatureRequest(id)
			alert(resp)
			await app.listFeatureRequests()
		}catch(e){
			console.log(e)
		}
	}

	async lookUpClients(){
		try{
			let clients = await this.api.lookUpClients( )
			let html = ""
			clients.forEach((client) => {
				html += `<option>${client}</option>`
			})
			document.querySelector('#client').innerHTML = html
		}
		catch(e){
			console.log(e)
		}
	}

	async lookUpProductAreas(){
		try{
			let areas = await this.api.lookUpProductAreas()
			let html = ""
			areas.forEach((area) => {
				html += `<option>${area}</option>`
			})
			document.querySelector('#area').innerHTML = html
		}
		catch(e){
			console.log(e)
		}
	}

	async lookupPriority(){
		try{
			let priorities = await this.api.lookUpClientPriority( document.querySelector('#client').value )
			let html = ""
			priorities.forEach((p) => {
				html += `<option>${p}</option>`
			})
			document.querySelector('#priority').innerHTML = html
		}
		catch(e){
			console.log(e)
		}
	}


}