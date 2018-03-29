/* This file creates a Meteor Mongo collection called 'emails' to store emails
 * for beta users.
 */
import { Mongo } from 'meteor/mongo';

export const Emails = new Mongo.Collection('emails');

// The code within this if statement only runs on the server
if (Meteor.isServer) {
  Meteor.publish('emails', function emailsPublication() {
    return Emails.find();
  });
}
