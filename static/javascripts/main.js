(function() {
  $.ajaxSetup({
    cache: false
  });
  $(function() {
    var jsonUrl;
    jsonUrl = "api/";
    window.Person = Backbone.Model.extend({
      initialize: function() {
        return this;
      },
      defaults: function() {
        return {
          "username": "-",
          "on_illutron": false,
          "image": ""
        };
      },
      url: function() {
        var u;
        u = jsonUrl + '/members' + '/';
        u = u + this.get("id");
        return u;
      }
    });
    window.PeopleList = Backbone.Collection.extend({
      model: Person,
      url: jsonUrl + "members/list"
    });
    window.People = new PeopleList;
    window.PersonView = Backbone.View.extend({
      tagName: "div",
      template: _.template($('#person-template').html()),
      initialize: function() {
        this.model.bind('change', this.render, this);
        this.model.bind('destroy', this.remove, this);
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
        People.bind('add', this.addPerson, this);
        People.bind('reset', this.addAll, this);
        People.fetch();
        setInterval((function() {
          return window.People.each(function(person) {
            return person.fetch();
          });
        }), 3000);
        return this;
      },
      render: function() {
        return this;
      },
      addAll: function() {
        return People.each(this.addPerson);
      },
      addPerson: function(person) {
        var view;
        view = new PersonView({
          model: person
        });
        this.$("#people-list").append(view.render().el);
        return person.fetch();
      }
    });
    return window.App = new AppView;
  });
}).call(this);
