(function() {
  $(function() {
    var jsonUrl;
    jsonUrl = "http://illutron.johan.cc/api/";
    window.Person = Backbone.Model.extend({
      initialize: function() {
        return alert("asd");
      },
      defaults: function() {
        return {
          "username": "-"
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
      url: jsonUrl + "members/",
      sync: function(method, model, options) {
        options.timeout = 10000;
        options.dataType = "jsonp";
        return Backbone.sync(method, model, options);
      }
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
        }), 5000);
        return this;
      },
      render: function() {
        return this;
      },
      addAll: function() {
        alert("asd");
        return People.each(this.addPerson);
      },
      addPerson: function(person) {
        var view;
        alert(person.url());
        view = new PersonView({
          model: person
        });
        return this.$("#people-list").append(view.render().el);
      }
    });
    return window.App = new AppView;
  });
}).call(this);
