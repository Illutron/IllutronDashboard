(function() {
  $(function() {
    window.Person = Backbone.Model.extend({
      defaults: function() {
        return {
          "name": "-"
        };
      }
    });
    window.PeopleList = Backbone.Collection.extend({
      model: Person
    });
    window.People = new PeopleList;
    window.PersonView = Backbone.View.extend({
      tagName: "div",
      template: _.template($('#person-template').html()),
      initialize: function() {
        return this;
      },
      render: function() {
        $(this.el).html(this.template(this.model.toJSON()));
        return this;
      }
    });
    window.AppView = Backbone.View.extend({
      el: $("#app"),
      initialize: function() {
        return this;
      },
      render: function() {
        return this;
      },
      addPerson: function(person) {
        var view;
        view = new PersonView({
          model: person
        });
        return this.$("#people-list").append(view.render().el);
      }
    });
    window.App = new AppView;
    return window.App.addPerson(new Person({
      "name": "Benjamin"
    }));
  });
}).call(this);
