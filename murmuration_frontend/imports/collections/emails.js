/* This file creates a Meteor Mongo collection called 'emails' to store emails
 * of beta users.
 */
import { Mongo } from 'meteor/mongo';

/* To view what is in the database, open a new terminal tab in the client directory,
 * type "meteor mongo", and then type "db.emails.find().pretty()"
 *
 * To clear the database of all test inputs, type "db.emails.remove({})"
 */
export const Emails = new Mongo.Collection('emails');
