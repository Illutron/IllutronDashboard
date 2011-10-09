$ ()->
	window.Person = Backbone.Model.extend({
		defaults: ->
			{
			"name": "-"
			}
	})

	window.PeopleList = Backbone.Collection.extend({
		model: Person
	
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
			this

		render: -> this
	
		addPerson: (person) ->
			view = new PersonView(model: person)
			@$("#people-list").append view.render().el

	)

	window.App = new AppView;
	
	window.App.addPerson new Person({"name":"Benjamin"})
	