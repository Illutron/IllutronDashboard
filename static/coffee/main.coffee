$.ajaxSetup({ cache: false });

$ ()->
	jsonUrl = "api/"
	
	window.Person = Backbone.Model.extend({
		initialize: ->
			this
		defaults: ->
			{
			"username": "-"
			"on_illutron" : false
			"image" : ""
			}
			
		url: ->
			u = jsonUrl + '/members'+'/'
			u = u + this.get("id")
			u
	})

	window.PeopleList = Backbone.Collection.extend({
		model: Person
		#url: "http://jive.local:8000/api/latest/"
		url: jsonUrl+ "members"
		
		# sync: (method, model, options) -> 
		# 	options.timeout = 10000
		# 	options.dataType = "jsonp"
		# 	Backbone.sync(method, model, options)
		
		# initialize: ->
		# 			this.bind("add", this.changed)
		# 		
	

	})

	window.People = new PeopleList

	window.PersonView = Backbone.View.extend({
		tagName: "div"
		template: _.template($('#person-template').html())
	
		initialize: ->
			this.model.bind('change', this.render, this);
			this.model.bind('destroy', this.remove, this);
	      
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
			
			
			setInterval( (-> window.People.each(  (person) -> person.fetch() )) , 3000);
			
			this

		render: -> this
		
		addAll: ->
			People.each(this.addPerson);
	      
		
		addPerson: (person) ->
			view = new PersonView(model: person)
			@$("#people-list").append view.render().el
			person.fetch()
	)

	window.App = new AppView;
	
	#window.App.addPerson new Person({"name":"Benjamin"})
	
	

		