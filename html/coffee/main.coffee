$ ()->
	jsonUrl = "http://illutron.johan.cc/"
	
	window.Person = Backbone.Model.extend({
		defaults: ->
			{
			"member": "-"
			}
			
		url: ->
			u = jsonUrl + '/members'+'/'
			u = u + this.get("id")
			u
	})

	window.PeopleList = Backbone.Collection.extend({
		model: Person
		#url: "http://jive.local:8000/api/latest/"
		url: jsonUrl+ "members/"
		
		sync: (method, model, options) -> 
			options.timeout = 10000
			options.dataType = "jsonp"
			Backbone.sync(method, model, options)
		
		# initialize: ->
		# 			this.bind("add", this.changed)
		# 		
	

	})

	window.People = new PeopleList

	window.PersonView = Backbone.View.extend({
		tagName: "div"
		template: _.template($('#person-template').html())
	
		initialize: ->
			this
	
		render: ->
			$(this.el).html(this.template(this.model.toJSON()))
			this
			    
	})

	window.AppView = Backbone.View.extend(	
		el: $("#app")

		initialize: ->
			People.bind('add',   this.addPerson, this);
			People.bind('reset',   this.addAll, this);
			
			People.fetch()
			
			
			setInterval( (-> window.People.each(  (person) -> person.fetch() )) , 5000);
			
			this

		render: -> this
		
		addAll: ->
			People.each(this.addPerson);
	      
		
		addPerson: (person) ->
			#alert person.url()
			view = new PersonView(model: person)
			@$("#people-list").append view.render().el

	)

	window.App = new AppView;
	
	#window.App.addPerson new Person({"name":"Benjamin"})
	
	

		