import { Template } from 'meteor/templating';
import { Emails } from '../api/emails.js';
import './body.html';

Template.body.onCreated(function bodyOnCreated() {
  Meteor.subscribe('emails');
});

Template.body.events({
  'submit .submit-email'(event) {
    // Prevent default browser form submit
    event.preventDefault();

    // Get value from form element
    const target = event.target;
    const text = target.text.value;

    // Insert a task into the collection
    Emails.insert({
      text,
      createdAt: new Date(), // current time
    });

    // Clear form
    target.text.value = '';

    // This is to view what's in the collections.
     console.log(Emails.find().fetch());

  },
});
