import { Template } from 'meteor/templating';
import { Emails } from '../collections/emails.js';
import './body.html';

Template.body.events({
  'submit .submit-email'(event) {
    // Prevent default browser form submit.
    event.preventDefault();

    // Get value from form element.
    const target = event.target;
    const text = target.text.value;

    // Insert an email into the collection.
    Emails.insert({
      text,
      createdAt: new Date(),
    });

    // Clear form.
    target.text.value = '';
  },
});
