/* Encapulates making api calls to the server */
class Api{
	constructor(){
		this.api = "http://localhost:5000"
	}

	async login(username, password){
		let data = {username, password}
		let result = await fetch(`${this.api}/user`, {method: 'POST', body: JSON.stringify(data), 
			headers: new Headers({
			    'Content-Type': 'application/json'
			}) 
		})
		let response = await result.json()

		if(response.status == 200){
			localStorage.setItem( 'token', response.token )
			return response.token
		}
		else{
			throw new Error(response.message)
		}
	}

	async submitFeatureRequest(title, description, client, priority, date, area){
		let data = {title, description, client, priority, date, area}
		let token = localStorage.getItem('token')

		let result = await fetch(`${this.api}/feature`, {method: 'POST', body: JSON.stringify(data), 
			headers: new Headers({
			    'Content-Type': 'application/json',
			    token
			}) 
		})
		let response = await result.json()

		if(response.status == 200){
			return response.message
		}
		else{
			throw new Error(response.message)
		}
	}

	async updateFeatureRequest(id, data){
		let token = localStorage.getItem('token')

		let result = await fetch(`${this.api}/feature/${id}`, {method: 'PUT', body: JSON.stringify(data), 
			headers: new Headers({
			    'Content-Type': 'application/json',
			    token
			}) 
		})
		let response = await result.json()
		if(response.status == 200){
			return response.message
		}
		else{
			throw new Error(response.message)
		}
	}

	async getFeatureRequests(){
		let token = localStorage.getItem('token')

		let result = await fetch(`${this.api}/feature`, {method: 'GET', 
			headers: new Headers({
			    token
			}) 
		})
		let response = await result.json()
		return response
	}

	async deleteFeatureRequest(id){
		let token = localStorage.getItem('token')

		let result = await fetch(`${this.api}/feature/${id}`, {method: 'DELETE', 
			headers: new Headers({
			    token
			}) 
		})
		let response = await result.json()
		if(response.status == 200){
			return response.message
		}
		else{
			throw new Error(response.message)
		}
	}

	async lookUpClients(){
		let result = await fetch(`${this.api}/clients`, {method: 'GET'})
		let response = await result.json()
		return response
	}

	async lookUpProductAreas(){
		let result = await fetch(`${this.api}/product_areas`, {method: 'GET'})
		let response = await result.json()
		return response
	}

	async lookUpClientPriority(clientName){
		let result = await fetch(`${this.api}/priority/${clientName}`, {method: 'GET'})
		let response = await result.json()
		return response
	}
}